# This Spider scrapes two sets of data:


#   1. All the lineups of the fantaplayers for each played day of the season.
#      The lineups will be saved inside a .pckl file and they will be stored
#      inside a dict. The keys of the dictionary are the fantateams. Each
#      fantateam has a value which is a list containing as many tuples as
#      the number of days of the season (already played). Each of these tuples
#      has 2 elements: a string and a list. The string represents the module
#      while the list contains 23 tuples representing the players in the lineup
#      for that specific day. Each tuple has the form:
#
#                      ('Day X', name_of_the_player, roles)


#   2. The absolute points per fantateam per day. The result will be stored
#      inside a dict where the keys are the names of the fantateams and the
#      values are lists containing tuples. Each tuple has two elements: the day
#      of the season and the absolute points made by the fantateam on that day


#   3. All the data of each player in Serie A from Fantagazzetta day by day.
#      The data will be saved in .pckl file called "Day_X" (X is the number of
#      the day) and they will be stored inside a dictionary. The keys of the
#      dictionary are the players' names. Each player has a value which is a
#      tuple. The tuple contains 14 values which are:
#
#               1. Day of the season                         (day)
#               2. Player's team name                        (name)
#               3. Vote from Fantagazzetta                   (FG_vote)
#               4. Alvin482 vote                             (ST_vote)
#               5. Yellow card                               (YC)
#               6. Red card                                  (RC)
#               7. Goals scored                              (Gs)
#               8. Goals scored on penalty                   (Gp)
#               9. Goals taken                               (Gt)
#              10. Penalty saved                             (Ps)
#              11. Penalty failed                            (Pf)
#              12. Owngoal                                   (Og)
#              13. Assist                                    (As)
#              14. Assist from free kick                     (Asf)
#
#      In case the player took part at the match but he has no vote because he
#      played not enough minutes to be evaluated, the value for FG_vote or
#      ST_vote will be 'n.e'.


import scrapy
from scrapy_splash import SplashRequest
import pickle
import os
import random
import copy

path = '/Users/andrea/Desktop/fanta3_0/cday_lineups_votes'
os.chdir(path)

# These will be used to assign default vote (6) to the players of the matches
# which are not played (bad weather for example)
f = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_our_round/' +
         'serieA_teams.pckl', 'rb')
serieA_teams = pickle.load(f)
f.close()

days_to_skip = [27]


class Cday_lineups_votes(scrapy.Spider):

    def __init__(self):
        self.all_scraped_days = sorted([int(file.split('_')[1][:-5]) for
                                        file in os.listdir('votes') if
                                        file.endswith('.pckl')])
        self.missing_days = [x for x in range(1, 39) if
                             x not in self.all_scraped_days and
                             x not in days_to_skip]

        try:
            self.last_scraped_day = self.all_scraped_days[-1]
        except IndexError:
            self.last_scraped_day = 0

        self.cday = 0              # Days of Serie A already played
        self.count = 0             # Counter (see below inside parse_cday)
        self.start_urls = ['https://www.fantagazzetta.com/voti-fantacalcio' +
                           '-serie-a']
        self.lineups_urls = ['http://leghe.fantagazzetta.com/fantascandalo/' +
                             'formazioni?g={}'.format(x) for x in
                             self.missing_days]
        self.votes_urls = ['https://www.fantagazzetta.com/voti-' +
                           'fantacalcio-serie-a/2017-18/{}'.format(x) for x in
                           self.missing_days]

        # Load the names of the fanta-teams
        f = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_our_round' +
                 '/fantateams_names.pckl', 'rb')
        self.teams_names = pickle.load(f)
        f.close()

    # To handle some 302 Redirecting issues
    handle_httpstatus_list = [302]

    name = 'cday_lineups_votes'

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_cday, args={'wait': 0.5})

    def lineups_scraping(self, splash_response, url_day, teams_names):

        # Initialize the lineups dict
        lineups = {team: [] for team in teams_names}
        abs_points = {team: [] for team in teams_names}

        # All the tables containing the lineups
        tables = splash_response.xpath('//div[contains(@class, "col-lg-12")]' +
                                       '/div[contains(@class, "row itemBox")]')

        for table in tables:

            # This is a counter we need because each table contains the lineups
            # of two fanta-teams. The counter is used to assign the correct
            # lineup to the correct fanta-team
            table_count = 0

            # Names of the fanta-teams
            team1 = table.xpath('.//h3/text()').extract()[0]
            team2 = table.xpath('.//h3/text()').extract()[2]

            # Modules chosen
            module1 = table.xpath('.//h4/text()').extract()[0].split()[1]
            module2 = table.xpath('.//h4/text()').extract()[4].split()[1]

            # Scrape absolute points of the day and store them
            abs_points1 = table.xpath('.//span[contains' +
                                      '(@class,"pull-right")]/' +
                                      'text()').extract()[0]
            abs_points1 = float(abs_points1.replace(',', '.'))

            abs_points2 = table.xpath('.//span[contains' +
                                      '(@class,"pull-right")]/' +
                                      'text()').extract()[3]
            abs_points2 = float(abs_points2.replace(',', '.'))

            abs_points[team1].append((url_day, abs_points1))
            abs_points[team2].append((url_day, abs_points2))

            # This element contains the two lineups
            lineups_container = table.xpath('.//tbody')

            for lineup in lineups_container:

                # Inside this list we will append the 23 tuples of the lineup
                fin_list = []

                # This element contains all the 23 players
                players_container = lineup.xpath('.//tr[contains(@class,' +
                                                 '"playerrow")]')

                for player in players_container:

                    # Player's name
                    name = player.xpath('.//a/text()').extract_first()

                    # Player's roles
                    roles = player.xpath(
                            './/td/span[contains(@class,"role")]/text()')\
                        .extract()

                    fin_tuple = ('Day {}'.format(url_day), name, roles)

                    fin_list.append(fin_tuple)

                # Depending on the value of the counter we assign the lineup
                # to the correct team
                if table_count == 0:
                    lineups[team1].append((module1, fin_list))
                else:
                    lineups[team2].append((module2, fin_list))

                # Increase the counter for the second team
                table_count += 1

        return lineups, abs_points

    def votes_scraping(self, splash_response, url_day):

        """
           This function scrapes all the data for each player in Serie A,
           creates the final tuple and store all the data in a .pckl file.
        """

        # 20 tables containing the data of the players for a specific day of
        # the season
        tables = splash_response.xpath('//table[contains(@class,"no-footer")]')

        # Dict containing all the data for that day
        players_database = {}

        # Every time we scrape the votes of one team (Atalanta, Benevento etc)
        # we delete the team from this list. In this way we are able to check
        # whether we scraped all the teams or there are some of them missing.
        # In this case, it means that 1 or more matches have not been played.
        copy_serieA_teams = copy.copy(serieA_teams)

        for table in tables:

            # Name of the team (Atalanta, Benevento, etc.)
            team_name = table.xpath('.//span[contains(@class,"txtbig")]/' +
                                    'text()').extract_first()

            # Remove the team
            copy_serieA_teams.remove(team_name)

            # All players who have vote in that specific day
            players = table.xpath('.//tbody/tr')

            for player in players:

                # Extract the role of the player to make sure we don't
                # scrape data related to the coach
                role = player.xpath('.//span[contains(@class,"role")]/text()')\
                                    .extract_first()

                # So for every role which is different from 'ALL' (coach)
                # we start the scraping
                if role != 'ALL':

                    data = player.xpath('.//td')

                    name = player.xpath('.//a/text()').extract_first()

                    # These two labels tell us if a player has been evaluated
                    # or not. The word 'grey' inside the label means 'n.e.'
                    labelFG = data[2].xpath('.//span/@class').extract_first()\
                        .split(' ')[1]

                    labelST = data[4].xpath('.//span/@class').extract_first()\
                        .split(' ')[1]

                    try:
                        # If the vote is integer we don't have any problem
                        FG_vote = float(data[2].xpath('.//span/text()')
                                        .extract_first())
                        if 'grey' in labelFG:
                            FG_vote = 'n.e.'
                    except ValueError:
                        # If it is a decimal number we have to replace the
                        # ',' with a '.' before converting to float,
                        # otherwise we get a ValueError
                        FG_vote = data[2].xpath('.//span/text()')\
                                        .extract_first()

                        if FG_vote == '-' or 'grey' in labelFG:
                            FG_vote = 'n.e.'
                        else:
                            FG_vote = float(FG_vote.replace(',', '.'))

                    try:
                        ST_vote = float(data[4].xpath('.//span/text()')
                                        .extract_first())
                        if 'grey' in labelST:
                            ST_vote = 'n.e.'
                    except ValueError:
                        ST_vote = data[4].xpath('.//span/text()')\
                                        .extract_first()

                        if ST_vote == '-' or 'grey' in labelST:
                            ST_vote = 'n.e.'
                        else:
                            ST_vote = float(ST_vote.replace(',', '.'))

                    # If in the element data[4] we have only one span
                    # element that means that the player didn't receive
                    # any card (yellow or red)
                    if len(data[4].xpath('.//span')) == 1:
                        YC = 0
                        RC = 0

                    # On the other hand, two span elements inside data[4]
                    # mean that the player DID receive a card. To know
                    # which card we extract the class attribute of the
                    # second span element
                    else:
                        card = data[4].xpath('.//span')[1].xpath('@class')\
                               .extract_first()

                        if 'trn-ry' in card:
                            YC = 1
                            RC = 0
                        elif 'trn-rr' in card:
                            YC = 0
                            RC = 1

                    # This element and the following ones have a span
                    # element associated only in the case the value is
                    # != 0. In this case (goals scored), if the player
                    # scored any goal we extract the number from the
                    # span element
                    if len(data[8].xpath('.//span')) == 0:
                        Gs = 0
                    else:
                        Gs = int(data[8].xpath('.//span/text()')
                                 .extract_first())

                    if len(data[9].xpath('.//span')) == 0:
                        Gp = 0
                    else:
                        Gp = int(data[9].xpath('.//span/text()')
                                 .extract_first())

                    if len(data[10].xpath('.//span')) == 0:
                        Gt = 0
                    else:
                        Gt = int(data[10].xpath('.//span/text()')
                                 .extract_first())

                    if len(data[11].xpath('.//span')) == 0:
                        Ps = 0
                    else:
                        Ps = int(data[11].xpath('.//span/text()')
                                 .extract_first())

                    if len(data[12].xpath('.//span')) == 0:
                        Pf = 0
                    else:
                        Pf = int(data[12].xpath('.//span/text()')
                                 .extract_first())

                    if len(data[13].xpath('.//span')) == 0:
                        Og = 0
                    else:
                        Og = int(data[13].xpath('.//span/text()')
                                 .extract_first())

                    # This element can have zero, one or two span elements
                    # associated. Zero means no assist of any kind
                    if len(data[14].xpath('.//span')) == 0:
                        As = 0
                        Asf = 0

                    # One means the player did a certain number of normal
                    # assists (not from free kick) and we extract that
                    # number
                    elif len(data[14].xpath('.//span')) == 1:
                        As = int(data[14].xpath('.//span')[0]
                                 .xpath('.//text()').extract_first())
                        Asf = 0

                    # Two means the player did a certain number of assists
                    # and some or all of them are from free kick. In this
                    # case we extract both numbers
                    else:
                        As = int(data[14].xpath('.//span')[0]
                                 .xpath('.//text()').extract_first())
                        Asf = int(data[14].xpath('.//span')[1]
                                  .xpath('.//text()').extract_first())

                    # Create the final tuple
                    fin_tuple = (url_day, team_name, FG_vote, ST_vote,
                                 YC, RC, Gs, Gp, Gt, Ps, Pf, Og, As, Asf)

                    # Store the result inside the dict
                    players_database[name] = fin_tuple

        # Now we check if all the teams have been scraped (copy_serieA_teams
        # should be empty). If not empty
        if copy_serieA_teams:

            filename = ('/Users/andrea/Desktop/fanta3_0/all_players_per_team' +
                        '/players/players_{}.pckl'.format(url_day))

            f = open(filename, 'rb')
            all_players_per_team = pickle.load(f)
            f.close()

            # For each team left we create the default tuple
            for team in copy_serieA_teams:
                fin_tuple = (url_day, team, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

                # And we assign it to every player of that team
                for player in all_players_per_team[team]:
                    players_database[player] = fin_tuple

        # Save the database
        filename = ('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes' +
                    '/Day_{}.pckl'.format(url_day))
        f = open(filename, 'wb')
        pickle.dump(players_database, f)
        f.close()

    def parse_cday(self, response):

        # From the first link scraped (inside start_urls) we extract the
        # number of days of Serie A already played
        self.cday = int(response.xpath(
                '//h3[contains(@class,"visible-sm-block")]/span/text()')
                .extract()[1])

        self.lineups_urls = [url for url in self.lineups_urls if
                             int(url.split('=')[1]) <= self.cday]

        if not self.lineups_urls:
            print("\nNo data to be scraped.\nDays skipped: {}.\n".format(
                    days_to_skip))
            return

        # Print to check in Terminal that everything is fine
        print('\nMatches played in Serie A: {}.\n'.format(self.cday))

        # Now we can start scraping the links inside lineups_urls. After some
        # work on the link we remove it from the list. The process will be
        # finished when lineups_urls is empy
        while self.lineups_urls:
            url = self.lineups_urls[0]
            self.lineups_urls.remove(url)
            yield SplashRequest(url, self.parse_lineups, args={'wait': 0.5})

        # Same as for self.lineups_urls but in this case we do it for
        # self.votes_urls
        while self.votes_urls:
            url = self.votes_urls[0]
            self.votes_urls.remove(url)
            yield SplashRequest(url, self.parse_votes, args={'wait': 0.5})

    def parse_lineups(self, response):

        # Here we need to extract the url_day from the html we are scraping.
        url_day = int(response.xpath(
                '//span[contains(@id,"LabelGiornata")]/text()')
                .extract_first().split()[0])

        new_lineups, new_abs_points = self.lineups_scraping(response, url_day,
                                                            self.teams_names)

        # If there is no file created yet, we scrape and then store the result
        if not os.path.isfile('lineups.pckl'):

            f = open('lineups.pckl', 'wb')
            pickle.dump(new_lineups, f)
            f.close()

            f = open('abs_points.pckl', 'wb')
            pickle.dump(new_abs_points, f)
            f.close()

        # else we open it, load the content and append the new results to the
        # loaded variable, sort the by day and overwrite the old file with the
        # updated one.
        else:
            f = open('lineups.pckl', 'rb')
            lineups = pickle.load(f)
            f.close()

            f = open('abs_points.pckl', 'rb')
            abs_points = pickle.load(f)
            f.close()

            for fantateam in lineups:
                lineups[fantateam].append(new_lineups[fantateam][0])
                lineups[fantateam].sort(
                        key=lambda x: int(x[1][0][0].split(' ')[1]))

                abs_points[fantateam].append(new_abs_points[fantateam][0])
                abs_points[fantateam] = sorted(abs_points[fantateam],
                                               key=lambda x: x[0])

            f = open('lineups.pckl', 'wb')
            pickle.dump(lineups, f)
            f.close()

            f = open('abs_points.pckl', 'wb')
            pickle.dump(abs_points, f)
            f.close()

        # Print to check in Terminal that everything is fine
        print('\nLineups and abs_points from day ' +
              '{} scraped successfully.\n'.format(url_day))

    def parse_votes(self, response):

        # Define again the day for the same reasons as for parse_lineups
        url_day = int(response.xpath(
                '//input[contains(@id,"hGiornata")]/@value').extract_first())

        # Scraping of the database
        self.votes_scraping(response, url_day)

        # Print to check in Terminal that everything is fine
        print("\nPlayers' data from day ' +"
              "{} scraped successfully.\n".format(url_day))
