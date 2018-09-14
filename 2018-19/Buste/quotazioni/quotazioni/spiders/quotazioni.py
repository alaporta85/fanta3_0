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

path = '/Users/andrea/Desktop/fanta3_0/Buste/quotazioni'
os.chdir(path)


class Quotazioni(scrapy.Spider):

    name = 'quotazioni'

    teams = ['giochici-giochici-stars/1102184', 'bucalina-fc/1101833',
             'ciolle-united/1113529', 'fc-pastaboy/1102066',
             'fc-roxy/1110987', 'ac-picchia/1112834', 'fc-stress/1108610',
             'fc-bombagallo/1108048']

    svincol = ['http://leghe.fantagazzetta.com/fantascandalo/lista-svincolati']

    rose = ['http://leghe.fantagazzetta.com/fantascandalo/' +
            'dettaglio-rosa/{}'.format(name) for name in teams]

    players_dict = {}
    teams_scraped = 0

    def start_requests(self):
        for url in self.rose:
            yield SplashRequest(url, self.parse_rose, args={'wait': 0.5})

    def parse_rose(self, response):

        team = response.xpath(
                             '//span[@class="titbig2"]/text()').extract_first()

        table = response.xpath('//table[@id="tbteamdet"]/tbody/tr')

        for row in table:

            player = row.xpath('.//td')[1].xpath(
                                            './/span/a/text()').extract_first()

            value = int(row.xpath('.//td')[4].xpath(
                                                  './/text()').extract_first())

            self.players_dict[player] = value

        print('\nQuotazioni from {} scraped correctly.\n'.format(team))

        self.teams_scraped += 1

        if self.teams_scraped == 8:
            f = open('quotazioni.pckl', 'wb')
            pickle.dump(self.players_dict, f)
            f.close()
