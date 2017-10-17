import mantra_functions_without_filters as mfwf
import statistic_functions as sf
import pandas as pd
import os
import pickle

# Load the list with our round
g = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_our_round/' +
         'our_round.pckl', 'rb')
our_round = pickle.load(g)
g.close()

# Load the dict with all the lineups day by day
h = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/' +
         'lineups.pckl', 'rb')
lineups = pickle.load(h)
h.close()

# Load the dict with all the players of each fantateam. This dict if made of
# all the fantaplayers updated to the last played day
i = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/' +
         'all_players_per_fantateam.pckl', 'rb')
fantaplayers = pickle.load(i)
i.close()

# Load the dict with the names of the fantateams
p = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_our_round/' +
         'fantateams_names.pckl', 'rb')
fantanames = pickle.load(p)
p.close()

# Load the absolute points. Used to play fast leagues
m = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/' +
         'abs_points.pckl', 'rb')
abs_points = pickle.load(m)
m.close()

# Create a dict with the roles of the players. It will be used to select the
# best players role by role
all_roles = {player[0]: player[1] for team in fantaplayers
             for player in fantaplayers[team]}

# Votes are stored in different .pckl files for different days. Here we create
# a unique dict with all the votes. First we create the list with all the files
files = os.listdir('/Users/andrea/Desktop/fanta3_0/' +
                   'cday_lineups_votes/votes')[1:]

# Initialize the database
players_database = {}

# For each .pckl file we add to the database the data relative to each player
for file in files:
    f = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/' +
             '%s' % file, 'rb')
    day = pickle.load(f)
    f.close()
    for player in day:
        if player in players_database:
            players_database[player].append(day[player])
        else:
            players_database[player] = [day[player]]

# Finally we delete some variables we do not need anymore
del day, file, files, player


class Player(object):
    def __init__(self, name):
        self.name = name
        self.team = ''
        self.FGvotes = [(data[0], data[2]) for data in
                        players_database[self.name] if data[2] != 'n.e.']
        self.FGfantavotes = []
        self.FGavrg = 0
        self.FGfanta_avrg = 0
        self.STvotes = [(data[0], data[3]) for data in
                        players_database[self.name] if data[3] != 'n.e.']
        self.STfantavotes = []
        self.STavrg = 0
        self.STfanta_avrg = 0
        self.YC = 0
        self.RC = 0
        self.Gs = 0
        self.Gp = 0
        self.Gt = 0
        self.Ps = 0
        self.Pf = 0
        self.Og = 0
        self.As = 0
        self.Asf = 0
        self.FG_matches_played = len(self.FGvotes)
        self.ST_matches_played = len(self.STvotes)

        def calculate_avrg(self):

            '''Set both the average based on the votes only and the one based
               on the fantavotes (votes +- bonus/malus).'''

            try:
                avrg_FG = (sum([vote[1] for vote in self.FGvotes]) /
                           self.FG_matches_played)
                fanta_avrg_FG = (sum([vote[1] for vote in self.FGfantavotes]) /
                                 self.FG_matches_played)
                self.FGavrg = round(avrg_FG, 2)
                self.FGfanta_avrg = round(fanta_avrg_FG, 2)
            except ZeroDivisionError:
                self.FGavrg = 0
                self.FGfanta_avrg = 0

            try:
                avrg_ST = (sum([vote[1] for vote in self.STvotes]) /
                           self.ST_matches_played)
                fanta_avrg_ST = (sum([vote[1] for vote in self.STfantavotes]) /
                                 self.ST_matches_played)
                self.STavrg = round(avrg_ST, 2)
                self.STfanta_avrg = round(fanta_avrg_ST, 2)
            except ZeroDivisionError:
                self.STavrg = 0
                self.STfanta_avrg = 0

        def calculate_fantavotes(day):

            '''Calculate the fantavote of the player in the specified day.
               'IndexError' appears when the player received no vote on that
               day. In fact we exclude all the votes == 'n.e.' when we define
               the attributes self.FGvotes or self.STvotes.'''

            try:
                FGvote = [data[1] for data in self.FGvotes
                          if data[0] == day][0]
            except IndexError:
                FGvote = 0

            try:
                STvote = [data[1] for data in self.STvotes
                          if data[0] == day][0]
            except IndexError:
                STvote = 0

            # If any of the two is != 0 we create the tuple containing only the
            # data we need. We do it by taking the tuple relative to the player
            # on that day from the database, which has the form:
            #
            #   (day,team_name,FGvote,STvote,YC,RC,Gs,Gp,Gt,Ps,Pf,Og,As,Asf)
            #
            # and removing the first four inputs. Final tuple has the form:
            #
            #               (YC,RC,Gs,Gp,Gt,Ps,Pf,Og,As,Asf)
            if FGvote or STvote:
                all_player_data_in_day = [data[4:] for data in
                                          players_database[self.name]
                                          if data[0] == day][0]

                # If we did NOT receive an IndexError before we calculate the
                # FGvote and append it to the attribute of the player
                if FGvote:
                    FGfantavote = (FGvote
                                   - 0.5*all_player_data_in_day[0]
                                   - all_player_data_in_day[1]
                                   + 3*all_player_data_in_day[2]
                                   + 3*all_player_data_in_day[3]
                                   - all_player_data_in_day[4]
                                   + 3*all_player_data_in_day[5]
                                   - 3*all_player_data_in_day[6]
                                   - 2*all_player_data_in_day[7]
                                   + all_player_data_in_day[8])

                    self.FGfantavotes.append((day, FGfantavote))

                # The same for STvote
                if STvote:
                    STfantavote = (STvote
                                   - 0.5*all_player_data_in_day[0]
                                   - all_player_data_in_day[1]
                                   + 3*all_player_data_in_day[2]
                                   + 3*all_player_data_in_day[3]
                                   - all_player_data_in_day[4]
                                   + 3*all_player_data_in_day[5]
                                   - 3*all_player_data_in_day[6]
                                   - 2*all_player_data_in_day[7]
                                   + all_player_data_in_day[8])

                    self.STfantavotes.append((day, STfantavote))

        def update_player(self):

            '''Updates all the attributes of the player.'''

            for day in players_database[self.name]:
                self.team = day[1]
                self.YC += day[4]
                self.RC += day[5]
                self.Gs += day[6] + day[7]
                self.Gp += day[7]
                self.Gt += day[8]
                self.Ps += day[9]
                self.Pf += day[10]
                self.Og += day[11]
                self.As += day[12]
                self.Asf += day[13]
                calculate_fantavotes(day[0])
            calculate_avrg(self)

        update_player(self)

    def all_bonus(self, day, mode='ST'):

        '''Return all the bonus points given by the Player on that day.'''

        data = [atuple for atuple in players_database[self.name]
                if atuple[0] == day]

        if data:
            goals = data[0][6] + data[0][7]
            assists = data[0][12]
            penalties_saved = data[0][9]
            return 3*goals+assists+3*penalties_saved
        else:
            return 0

    def all_malus(self, day, mode='ST'):

        '''Return all the malus points given by the Player on that day.'''

        data = [atuple for atuple in players_database[self.name]
                if atuple[0] == day]

        if data:
            YC = data[0][4]
            RC = data[0][5]
            Gt = data[0][8]
            Pf = data[0][10]
            Og = data[0][11]
            return 0.5*YC+RC+Gt+3*Pf+2*Og
        else:
            return 0

    def vote(self, day, mode='ST'):

        '''Return the vote of the player in that day.'''

        if mode == 'FG':
            try:
                vote = [data[1] for data in self.FGvotes
                        if data[0] == day][0]
                return vote
            except IndexError:
                return 'n.e.'
        else:
            try:
                vote = [data[1] for data in self.STvotes
                        if data[0] == day][0]
                return vote
            except IndexError:
                return 'n.e.'

    def fantavote(self, day, mode='ST'):

        '''Return the vote of the player in that day.'''

        if mode == 'FG':
            try:
                fantavote = [data[1] for data in self.FGfantavotes
                             if data[0] == day][0]
                return fantavote
            except IndexError:
                return 'n.e.'
        else:
            try:
                fantavote = [data[1] for data in self.STfantavotes
                             if data[0] == day][0]
                return fantavote
            except IndexError:
                return 'n.e.'


class Fantateam(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.victories = 0
        self.draws = 0
        self.defeats = 0
        self.goals_scored = 0
        self.goals_taken = 0
        self.goals_diff = 0
        self.abs_points = 0
        self.malus = 0
        self.lucky_points = 0
        self.lineups = lineups[self.name]
        self.fields = []   # All the players playing after MANTRA evaluation
        self.players = fantaplayers[self.name]
        self.bonus_from_field = 0
        self.bonus_from_bench = 0
        self.malus_from_field = 0
        self.malus_from_bench = 0
        self.gkeeper_contribute = 0
        self.defense_contribute = 0
        self.midfield_contribute = 0
        self.attack_contribute = 0

    def lineup(self, day):

        '''Returns the lineup of the fantateam in that day.'''

        return self.lineups[day-1]

    def players(self):

        '''Returns all the players of the fantateam.'''

        return self.players


class Match(object):
    def __init__(self, team1, team2, day, fantateams, mode):
        self.team1 = team1
        self.team2 = team2
        self.final_field1 = 0
        self.final_field2 = 0
        self.final_bench1 = 0
        self.final_bench2 = 0
        self.day = day
        self.mode = mode
        self.fantateams = fantateams
        self.lineup1 = self.fantateams[team1].lineup(day)
        self.lineup2 = self.fantateams[team2].lineup(day)

    def calculate_goals(self, a_number):

        '''Returns the number of goals scored by the fantateam in the match.
           The input 'a_number' represents the abs_points of the day, which is
           given by the sum of all fantavotes of the players taking part to the
           match.'''

        if a_number < 66:
            return 0
        else:
            return int((a_number-66)//6 + 1)

    def play_match(self):

        '''Plays the match by applying the MANTRA algorithm. We extract the
           final field and the final bench in order to be able to create later
           statistics on the bonus coming either from field and bench.'''

        # Separate module and player in two different variables and launch the
        # MANTRA simulation for both teams
        module1 = self.lineup1[0]
        lineup1 = self.lineup1[1]
        self.final_field1, self.final_bench1, malus1 = mfwf.MANTRA_simulation(
                                                                lineup1,
                                                                module1,
                                                                self.mode)[:3]

        module2 = self.lineup2[0]
        lineup2 = self.lineup2[1]
        self.final_field2, self.final_bench2, malus2 = mfwf.MANTRA_simulation(
                                                                lineup2,
                                                                module2,
                                                                self.mode)[:3]

        # In the following block of code we add to the final_bench lists (both
        # 1 and 2) all the players that do NOT appear in the lineup of each
        # fantateam. We do this step in order to be able to calculate the ratio
        # between bonus in the final_field and total bonus. Same for malus
        filename = ('/Users/andrea/Desktop/fanta3_0/all_players_per_' +
                    'fantateam/fantaplayers/fantaplayers_%d.pckl' % self.day)

        f = open(filename, 'rb')
        daily_players = pickle.load(f)
        f.close()

        for player1 in daily_players[self.team1]:
            if (player1[0] not in [element[1] for element in self.final_field1]
                and player1[0] not in [element[1] for element in
                                       self.final_bench1]):
                first_tuple_element = self.final_field1[0][0]
                new_tuple = (first_tuple_element, player1[0], player1[1])
                self.final_bench1.append(new_tuple)

        for player2 in daily_players[self.team2]:
            if (player2[0] not in [element[1] for element in self.final_field2]
                and player2[0] not in [element[1] for element in
                                       self.final_bench2]):
                first_tuple_element = self.final_field2[0][0]
                new_tuple = (first_tuple_element, player2[0], player2[1])
                self.final_bench2.append(new_tuple)

        # Update the number of malus
        self.fantateams[self.team1].malus += malus1
        self.fantateams[self.team2].malus += malus2

        # Update the final lineup after the match
        self.fantateams[self.team1].fields.append(self.final_field1)
        self.fantateams[self.team2].fields.append(self.final_field2)

        # Create a list of all players who will contribute to the final
        # fantavote calculation and finally calculate the abs_points for each
        # team, including eventual malus
        players_with_vote1 = [all_players[player[1]] for player
                              in self.final_field1]
        abs_points1 = sum([player.fantavote(self.day, self.mode) for player
                           in players_with_vote1]) - 0.5*malus1

        players_with_vote2 = [all_players[player[1]] for player
                              in self.final_field2]
        abs_points2 = sum([player.fantavote(self.day, self.mode) for player
                           in players_with_vote2]) - 0.5*malus2

        return abs_points1, abs_points2

    def play_fast_match(self):

        '''Play the match by taking directly the absolute points from the dict.
           This can be used only in 'ST' mode because it is the one we are
           using on the website. To be able to use it in 'FG', a dict with all
           the FG absolute points must be created first. It is used when we
           want to generate statistics by playing thousand of leagues because
           it is much faster than playing the match by applying the MANTRA
           algorithm.'''

        abs_points1 = [x[1] for x in abs_points[self.team1]
                       if x[0] == self.day][0]
        abs_points2 = [x[1] for x in abs_points[self.team2]
                       if x[0] == self.day][0]

        return abs_points1, abs_points2

    def update_lucky_points(self, abs_points1, abs_points2, goals1, goals2):

        '''Updates the attribute half_point of each fantateam. This attributes
           represents the number of points in the ranking which have been
           gained by the fantateam when just 0.5 in the total score made the
           difference.'''

        reference_list = [(self.team1, abs_points1), (self.team2, abs_points2)]

        # If the result is 0-0 we need to check whether any of the teams made
        # 65.5 as final score
        if goals1 == 0 and goals2 == 0:

            # In this case we sort the list in decreasing order. In fact we
            # will check always the first element of this list, depending on
            # the case. Now we want to check tho one with the highest score
            # between the two so we sort it decreasingly
            reference_list.sort(key=lambda x: x[1], reverse=True)
            if reference_list[0][1] == 65.5:
                self.fantateams[reference_list[0][0]].lucky_points -= 2
                self.fantateams[reference_list[1][0]].lucky_points += 1

        # In case of any draw different from 0-0
        elif goals1 == goals2:

            reference_list.sort(key=lambda x: x[1], reverse=True)

            if (reference_list[0][1]-66) % 6 == 5.5:
                self.fantateams[reference_list[0][0]].lucky_points -= 2
                self.fantateams[reference_list[1][0]].lucky_points += 1

        # In case it is not a draw we have two cases: one of the teams scored 0
        # goals or both teams scored at least 1 goal. In both cases we need to
        # to add two extra conditions to the loop. First we check that the
        # difference between the teams is just one goal (otherwise it makes no
        # sense) and then we check if the difference in the score is lower than
        # 6, so 5.5 as a maximum. This is to avoid cases like 71.5-77.5 whose
        # effect cancel out each other.
        elif ((goals1 == 0 or goals2 == 0) and (abs(goals1-goals2) == 1
              and abs(abs_points1-abs_points2) < 6)):

            # Now we sort it in increasing order because we want to check the
            # element with the lowest score
            reference_list.sort(key=lambda x: x[1])

            if reference_list[0][1] == 65.5:
                self.fantateams[reference_list[0][0]].lucky_points -= 1
                self.fantateams[reference_list[1][0]].lucky_points += 2

        # If both teams scored
        elif abs(goals1-goals2) == 1 and abs(abs_points1-abs_points2) < 6:

            reference_list.sort(key=lambda x: x[1])

            if (reference_list[0][1]-66) % 6 == 5.5:
                self.fantateams[reference_list[0][0]].lucky_points -= 1
                self.fantateams[reference_list[1][0]].lucky_points += 2

    def update_bonus_malus(self, the_team, the_final_field,
                           the_final_bench):

        '''Update the four attributes of each fantateam relative to the bonus
           and malus points coming from field and bench, separately. In the
           calculation votes are NOT included, only the bonus points.'''

        for player in the_final_field:
            if player[1] in all_players:
                total_bonus = all_players[player[1]].all_bonus(self.day,
                                                               self.mode)
                self.fantateams[the_team].bonus_from_field += total_bonus
                total_malus = all_players[player[1]].all_malus(self.day,
                                                               self.mode)
                self.fantateams[the_team].malus_from_field += total_malus

        for player in the_final_bench:
            if player[1] in all_players:
                total_bonus = all_players[player[1]].all_bonus(self.day,
                                                               self.mode)
                self.fantateams[the_team].bonus_from_bench += total_bonus
                total_malus = all_players[player[1]].all_malus(self.day,
                                                               self.mode)
                self.fantateams[the_team].malus_from_bench += total_malus

    def update_contributes(self, the_team, the_final_lineup):

        '''Updates the 4 attributes of each fantateam.'''

        roles_defense = ['Dc', 'Dd', 'Ds']
        roles_midfield = ['E', 'M', 'C', 'W', 'T']
        roles_attack = ['Pc', 'A']

        def count_players(the_final_lineup):

            '''Counts the players in each area according to their role.'''

            count_def = 0
            count_mid = 0
            count_for = 0

            for player in the_final_lineup:
                role = player[2]
                if role in roles_defense:
                    count_def += 1
                elif role in roles_midfield:
                    count_mid += 1
                elif role in roles_attack:
                    count_for += 1

            return count_def, count_mid, count_for

        # Define the n. of players playing in each area of the field
        n_def, n_mid, n_for = count_players(the_final_lineup)

        # For each player extract the role and update the corresponding
        # attribute of the fantateam weighted by the n. of players in that area
        for player in the_final_lineup:
            role = player[2]
            contrib = all_players[player[1]].fantavote(self.day, self.mode)

            if role == 'Por':
                self.fantateams[the_team].gkeeper_contribute += contrib
            elif role in roles_defense:
                self.fantateams[the_team].defense_contribute += contrib/n_def
            elif role in roles_midfield:
                self.fantateams[the_team].midfield_contribute += contrib/n_mid
            elif role in roles_attack:
                self.fantateams[the_team].attack_contribute += contrib/n_for

    def update_fantateams(self, abs_points1, abs_points2):

        '''Updates all the parameters realtive to each fantateam.'''

        # Update the abs_points attribute of both fantateams
        self.fantateams[self.team1].abs_points += abs_points1
        self.fantateams[self.team2].abs_points += abs_points2

        # Calculate the goals scored by each fantateam in the match
        goals1 = self.calculate_goals(abs_points1)
        goals2 = self.calculate_goals(abs_points2)

        # Update goals_scored and goals_taken attributes for both teams
        self.fantateams[self.team1].goals_scored += goals1
        self.fantateams[self.team1].goals_taken += goals2
        self.fantateams[self.team2].goals_scored += goals2
        self.fantateams[self.team2].goals_taken += goals1
        self.fantateams[self.team1].goals_diff += goals1 - goals2
        self.fantateams[self.team2].goals_diff += goals2 - goals1

        # Update the rest of the attributes based on the number of goals scored
        # in the match by the fantateams
        if goals1 == goals2:
            self.fantateams[self.team1].draws += 1
            self.fantateams[self.team2].draws += 1
            self.fantateams[self.team1].points += 1
            self.fantateams[self.team2].points += 1
        elif goals1 > goals2:
            self.fantateams[self.team1].victories += 1
            self.fantateams[self.team2].defeats += 1
            self.fantateams[self.team1].points += 3
        else:
            self.fantateams[self.team1].defeats += 1
            self.fantateams[self.team2].victories += 1
            self.fantateams[self.team2].points += 3

        # Update bonus and malus. The 'try' method is used to avoid errors
        # during Statistics calculation, where this update is not needed. In
        # that case, in fact, we do NOT have any final_field or final_bench
        # because we use directly the abs_points. So those two attributes will
        # have their default value which is 0. Calling the function
        # 'update_bonus_malus' with those attribute as inputs will cause a
        # TypeError because in this case they are 'int', so not iterable
        try:
            self.update_bonus_malus(self.team1,
                                    self.final_field1,
                                    self.final_bench1)
            self.update_bonus_malus(self.team2,
                                    self.final_field2,
                                    self.final_bench2)

            self.update_contributes(self.team1, self.final_field1)
            self.update_contributes(self.team2, self.final_field2)
            self.update_lucky_points(abs_points1, abs_points2, goals1, goals2)
        except TypeError:
            pass


class Day(object):
    def __init__(self, day, schedule, fantateams, mode):
        self.day = day
        self.schedule = schedule
        self.mode = mode
        self.matches = self.schedule[day]
        self.fantateams = fantateams

    def play_day(self):

        '''Plays all the matches of the day.'''

        for match in self.matches:
            the_match = Match(match[0], match[1], self.day, self.fantateams,
                              self.mode)
            abs_points1, abs_points2 = the_match.play_match()
            the_match.update_fantateams(abs_points1, abs_points2)

    def play_fast_day(self):

        '''Plays fast all the matches of the day.'''

        for match in self.matches:
            the_match = Match(match[0], match[1], self.day, self.fantateams,
                              self.mode)
            abs_points1, abs_points2 = the_match.play_fast_match()
            the_match.update_fantateams(abs_points1, abs_points2)


class League(object):
    def __init__(self, a_round, n_days, mode):
        self.a_round = a_round
        self.n_days = n_days
        self.mode = mode
        self.schedule = sf.generate_schedule(self.a_round, self.n_days)
        self.fantateams = {team: Fantateam(team) for team in fantanames}

    def play_league(self):

        '''Plays all the matches in the schedule.'''

        for i in self.schedule:
            day = Day(i, self.schedule, self.fantateams, self.mode)
            day.play_day()

    def play_fast_league(self):

        '''Plays fast all the matches in the schedule.'''

        for i in self.schedule:
            day = Day(i, self.schedule, self.fantateams, self.mode)
            day.play_fast_day()

    def create_final_data(self):

        '''Returns a list with only the names of the fantateams in order of
           ranking and another list containing all the data of the league per
           fantateam.'''

        all_data = [(self.fantateams[team].name,
                     self.fantateams[team].points,
                     self.fantateams[team].victories,
                     self.fantateams[team].draws,
                     self.fantateams[team].defeats,
                     self.fantateams[team].goals_scored,
                     self.fantateams[team].goals_taken,
                     self.fantateams[team].goals_diff,
                     self.fantateams[team].malus,
                     self.fantateams[team].abs_points) for team in fantanames]

        # Sort the data according to
        all_data.sort(key=lambda x: x[3], reverse=True)        # Draws
        all_data.sort(key=lambda x: x[2], reverse=True)        # Victories
        all_data.sort(key=lambda x: x[7], reverse=True)        # Diff goals
        all_data.sort(key=lambda x: x[5], reverse=True)        # Goals scored
        all_data.sort(key=lambda x: x[9], reverse=True)        # Abs points
        all_data.sort(key=lambda x: x[1], reverse=True)        # Points

        only_names = [team[0] for team in all_data]

        return only_names, all_data

    def final_ranking(self):

        '''Returns the names in order of ranking.'''

        return self.create_final_data()[0]

    def best_players(self, pos, mode):

        '''Prints the table of the best players divided per role according to
           the vote and fantavote average, separately. Each table will show a
           number of players which is equal to 'pos'.'''

        roles_defense = ['Dc', 'Dd', 'Ds']
        roles_midfield = ['E', 'M', 'C', 'W', 'T']
        roles_attack = ['Pc', 'A']
        gkeepers_vote = []
        gkeepers_fantavote = []
        defenders_vote = []
        defenders_fantavote = []
        midfielders_vote = []
        midfielders_fantavote = []
        forwards_vote = []
        forwards_fantavote = []

        # For each player in the database we TRY to extract the role. We use
        # 'try' because not all the players present in the database are in the
        # roles dict. In that case we will have a KeyError and we pass.
        for player in players_database:
            try:
                roles = all_roles[player]

                # Extract the averages depending on the mode
                if mode == 'FG':
                    avrg = all_players[player].FGavrg
                    fanta_avrg = all_players[player].FGfanta_avrg
                else:
                    avrg = all_players[player].STavrg
                    fanta_avrg = all_players[player].STfanta_avrg

                # For each role, we append the tuple (player_name,avrg) to the
                # corresponding list, sort it in order to have it always in
                # decreasing order and cut it to the first 'pos' positions
                if roles == ['Por']:
                    gkeepers_vote.append((player, avrg))
                    gkeepers_fantavote.append((player, fanta_avrg))
                    gkeepers_vote.sort(key=lambda x: x[1], reverse=True)
                    gkeepers_fantavote.sort(key=lambda x: x[1], reverse=True)
                    gkeepers_vote = gkeepers_vote[:pos]
                    gkeepers_fantavote = gkeepers_fantavote[:pos]

                if set(roles).intersection(roles_defense):
                    defenders_vote.append((player, avrg))
                    defenders_fantavote.append((player, fanta_avrg))
                    defenders_vote.sort(key=lambda x: x[1], reverse=True)
                    defenders_fantavote.sort(key=lambda x: x[1], reverse=True)
                    defenders_vote = defenders_vote[:pos]
                    defenders_fantavote = defenders_fantavote[:pos]

                if set(roles).intersection(roles_midfield):
                    midfielders_vote.append((player, avrg))
                    midfielders_fantavote.append((player, fanta_avrg))
                    midfielders_vote.sort(key=lambda x: x[1], reverse=True)
                    midfielders_fantavote.sort(key=lambda x: x[1],
                                               reverse=True)
                    midfielders_vote = midfielders_vote[:pos]
                    midfielders_fantavote = midfielders_fantavote[:pos]

                if set(roles).intersection(roles_attack):
                    forwards_vote.append((player, avrg))
                    forwards_fantavote.append((player, fanta_avrg))
                    forwards_vote.sort(key=lambda x: x[1], reverse=True)
                    forwards_fantavote.sort(key=lambda x: x[1], reverse=True)
                    forwards_vote = forwards_vote[:pos]
                    forwards_fantavote = forwards_fantavote[:pos]
            except KeyError:
                pass

        # Sum element-wise the two lists in each role. We do this because it is
        # easier to print the result later
        gkeeper = [a+b for a, b in zip(gkeepers_vote, gkeepers_fantavote)]
        defense = [a+b for a, b in zip(defenders_vote, defenders_fantavote)]
        midfield = [a+b for a, b in zip(midfielders_vote,
                                        midfielders_fantavote)]
        attack = [a+b for a, b in zip(forwards_vote, forwards_fantavote)]

        # Insert a spacer for clarity in the final printing
        spacer = [('', '', '', '')]
        fin_list = gkeeper+spacer+defense+spacer+midfield+spacer+attack

        # Create an empty first coloumn (we do not want any label) and a header
        first_col = ['' for i in range(len(fin_list))]
        header = ['', 'Vote average', '', 'Fantavote average']

        table = pd.DataFrame(fin_list, first_col, header)

        print(table)
        print('\n')

    def print_league(self):

        '''Returns a table showing all the data of the league per fantateam.'''

        only_names, all_data = self.create_final_data()
        short_data = [team[1:] for team in all_data]
        header = ['Points', 'V', 'N', 'P', 'Gs', 'Gt', 'Dr', 'Malus',
                  'Abs Points']

        table = pd.DataFrame(short_data, only_names, header)

        if self.mode == 'ST':
            print('Alvin482')
        else:
            print('Fantagazzetta')

        print(table)
        print('\n')

    def print_lucky_points(self):

        '''Print the ranking based on the points gained for a difference of 0.5
           in the absolute points of the two teams during each match of the
           league.'''

        fin_list = [(team, self.fantateams[team].lucky_points)
                    for team in fantanames]

        fin_list.sort(key=lambda x: x[1], reverse=True)

        first_col = [x[0] for x in fin_list]
        data = [x[1] for x in fin_list]

        table = pd.DataFrame(data, first_col, ['Lucky Points'])

        print(table)
        print('\n')

    def print_contributes(self):

        '''Print a table where all the contributes by area in the field.
           The 4 areas are: goal-keeper, defense, midfield, attack.
           The contribute is defined as the average fantavote of the players of
           a specific area. Example:


                      Day1              Day2                Day3

                    Bonucci(6)        Bonucci(7)          Bonucci(5)
                   Koulibaly(5)      Koulibaly(7)        Koulibaly(8)
                   Chiellini(7)      Chiellini(7)        Chiellini(7)
                  Musacchio (6)


           Sum of all the defense votes is 65, Since the total n. of players is
           10, the contribute will be 6.5.'''

        ranking = self.final_ranking()

        ref_list = [(team,
                     round(self.fantateams[team].
                           gkeeper_contribute/n_days, 1),
                     round(self.fantateams[team].
                           defense_contribute/n_days, 1),
                     round(self.fantateams[team].
                           midfield_contribute/n_days, 1),
                     round(self.fantateams[team].
                           attack_contribute/n_days, 1))
                    for team in ranking]

        names = [element[0] for element in ref_list]
        data = [element[1:] for element in ref_list]
        header = ['Por', 'Dc,Dd,Ds', 'E,M,C,W,T', 'A,Pc']

        table = pd.DataFrame(data, names, header)

        print("Average player's fantavote according to the role.")
        print(table)
        print('\n')

    def print_rates_bonus_malus(self):

        '''Prints a table with three columns:

            - First column represents the % of bonus points used, which is
              defined as the bonus points counted divided the total bonus
              points (counted + bench/tribune).

            - Second column is the same as first one but with malus.

            - Third column represents the lucky points.'''

        ranking = self.final_ranking()

        ref_list = []

        for team in ranking:
            bonus_field = self.fantateams[team].bonus_from_field
            bonus_bench = self.fantateams[team].bonus_from_bench
            malus_field = self.fantateams[team].malus_from_field
            malus_bench = self.fantateams[team].malus_from_bench

            bonus_rate = round((bonus_field/(bonus_field+bonus_bench))*100, 1)
            malus_rate = round((malus_field/(malus_field+malus_bench))*100, 1)

            ref_list.append((team, bonus_rate, malus_rate,
                             self.fantateams[team].lucky_points))

        names = [element[0] for element in ref_list]
        data = [element[1:] for element in ref_list]
        header = ['Bonus(%)', 'Malus(%)', 'Lucky Points']

        table = pd.DataFrame(data, names, header)

        print('% of bonus/malus points used and points obtained thanks to ' +
              '0.5.')
        print(table)
        print('\n')


class Statistic(object):
    def __init__(self, leagues, n_days, mode):
        self.leagues = leagues
        self.n_days = n_days
        self.mode = mode
        self.place1 = {team: 0 for team in fantanames}
        self.place2 = {team: 0 for team in fantanames}
        self.place3 = {team: 0 for team in fantanames}
        self.place4 = {team: 0 for team in fantanames}
        self.place5 = {team: 0 for team in fantanames}
        self.place6 = {team: 0 for team in fantanames}
        self.place7 = {team: 0 for team in fantanames}
        self.place8 = {team: 0 for team in fantanames}
        self.all_positions = [self.place1, self.place2, self.place3,
                              self.place4, self.place5, self.place6,
                              self.place7, self.place8]
        self.list_of_rounds = sf.random_rounds(self.leagues)

        self.create_statistic()

    def create_statistic(self):

        '''Creates the data which are relative to all the leagues played.'''

        # For each round we create the league and play it
        for a_round in self.list_of_rounds:
            new_league = League(a_round, self.n_days, self.mode)
            new_league.play_fast_league()

            # Extract the ranking
            ranking = new_league.final_ranking()

            # Increase the position counters for each fantateam according to
            # their positions in the ranking
            for fantaname in ranking:
                for position in self.all_positions:
                    if (ranking.index(fantaname)
                       == self.all_positions.index(position)):
                        position[fantaname] += 1
                        break

    def positions8_rate(self):

        '''Prints the statistics for all the positions.'''

        n_leagues = self.leagues

        # Create the rates for each position for each fantateam
        rates = [(fantaname,
                  round((self.place1[fantaname]*100)/n_leagues, 1),
                  round((self.place2[fantaname]*100)/n_leagues, 1),
                  round((self.place3[fantaname]*100)/n_leagues, 1),
                  round((self.place4[fantaname]*100)/n_leagues, 1),
                  round((self.place5[fantaname]*100)/n_leagues, 1),
                  round((self.place6[fantaname]*100)/n_leagues, 1),
                  round((self.place7[fantaname]*100)/n_leagues, 1),
                  round((self.place8[fantaname]*100)/n_leagues, 1))
                 for fantaname in fantanames]

        # Sort the list
        rates.sort(key=lambda x: x[1], reverse=True)

        # Create the lists to print the table
        only_names = [element[0] for element in rates]
        short_data = [element[1:] for element in rates]
        header = ['1st(%)', '2nd(%)', '3rd(%)', '4th(%)',
                  '5th(%)', '6th(%)', '7th(%)', '8th(%)']

        table = pd.DataFrame(short_data, only_names, header)

        print(table)

    def positions4_rate(self):

        '''Short version of the previous function. It prints the statistics
           relative to the first three positions in the ranking and the last
           one.'''

        n_leagues = self.leagues

        rates = [(fantaname,
                  round((self.place1[fantaname]*100)/n_leagues, 1),
                  round((self.place2[fantaname]*100)/n_leagues, 1),
                  round((self.place3[fantaname]*100)/n_leagues, 1),
                  round((self.place8[fantaname]*100)/n_leagues, 1))
                 for fantaname in fantanames]

        rates.sort(key=lambda x: x[1], reverse=True)

        only_names = [element[0] for element in rates]
        short_data = [element[1:] for element in rates]
        header = ['1st(%)', '2nd(%)', '3rd(%)', '8th(%)']

        table = pd.DataFrame(short_data, only_names, header)

        print('Statistics on %d random leagues:' % self.leagues)
        print(table)

    def round_team_position(self, a_team_name, position):

        '''Look for all the rounds where a team ends in position 'position' at
           the end of the league. Between  all the rounds found, it returns the
           one whit more points.'''

        all_rounds = []

        for a_round in self.list_of_rounds:
            new_league = League(a_round, self.n_days, self.mode)
            new_league.play_fast_league()
            ranking = new_league.final_ranking()
            if ranking[position-1] == a_team_name:
                points = new_league.fantateams[a_team_name].points
                all_rounds.append((points, a_round))

        all_rounds.sort(key=lambda x: x[0], reverse=True)

        print('\n')
        if all_rounds:
            print('Number of rounds found where %s ends in position %d in the'
                  ' final ranking: %d' % (a_team_name, position,
                                          len(all_rounds)))
            print('In the best case %s ends with %d points. The round is:\n'
                  % (a_team_name, all_rounds[0][0]))
            return all_rounds[0][1]
        else:
            print('No rounds found.')


teams = [name for name in fantanames]
all_players = {player: Player(player) for player in players_database}
n_days = len(lineups['Ciolle United'])


print('\n')
a = League(our_round, n_days, 'ST')
a.play_league()
a.print_league()
#b = League(our_round,n_days,'FG')
#b.play_league()
#b.print_league()
a.print_contributes()
a.print_rates_bonus_malus()
#a.best_players(2,'ST')
c = Statistic(10000, n_days, 'ST')
c.positions4_rate()
