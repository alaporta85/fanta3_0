# Spider to scrape the players of each fantateam day by day. They will be
# stored in a dict and saved inside a .pckl file. The keys of the dict are the
# names of the fantateams while the values are lists containing a tuple for
# each player. The tuple is:
#
#                       (name_of_the_player, roles)

import scrapy
from scrapy_splash import SplashRequest
import pickle
import os

path = '/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam'
os.chdir(path)


class Players_Roles(scrapy.Spider):

    name = 'all_players_per_fantateam'

    start_urls = ['http://leghe.fantagazzetta.com/fantascandalo/' +
                  'tutte-le-rose']

    players_dict = {}

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5})

    def parse(self, response):

        # Tables containing all the players, one table each fantateam
        all_tables = response.xpath('//table[contains(@class,"tbpink")]')

        # For each table
        for table in all_tables:

            # Extract the fantateam
            fantateam = table.xpath('.//h3/text()').extract_first()

            players_container = []

            # All the players of the fantateam
            players = table.xpath('.//tbody/tr')

            # For each player
            for player in players:

                # Extract the role
                roles = player.xpath('.//span[contains(@class,"role")]/' +
                                     'text()').extract()

                # Extract the name
                name = player.xpath('.//a/text()').extract_first()

                # Extract the team
                team = player.xpath('.//td[contains(@class,"aleft")]/' +
                                    'text()').extract_first()

                players_container.append((name, roles, team))

            # Store the result in the dict
            self.players_dict[fantateam] = players_container

        players_dir = path + '/fantaplayers'

        n_files_present = len([file for file in os.listdir(players_dir) if
                               file.endswith('.pckl')])

        next_file = n_files_present + 1

        filename = players_dir + '/fantaplayers_%d.pckl' % next_file

        # Save the file
        f = open(filename, 'wb')
        pickle.dump(self.players_dict, f)
        f.close()

        print('\n')
        print('Fantaplayers of day %d scraped correctly.' % next_file)
        print('\n')
