# Spider to scrape the players of each Serie A team day by day. They will be
# stored in a dict and saved inside a .pckl file. The keys of the dict are the
# names of the teams in Serie A (Atalanta, Benevento etc etc) while the values
# are lists containing all the players of that team.


import scrapy
from scrapy_splash import SplashRequest
import pickle
import os

path = '/Users/andrea/Desktop/fanta3_0/all_players_per_team'
os.chdir(path)

class Players(scrapy.Spider):
    
    name = 'all_players_per_team'

    f = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_schedule/'+
             'serieA_teams.pckl', 'rb')
    serieA_teams = pickle.load(f)
    f.close()
    
    start_urls = ['https://www.fantagazzetta.com/squadre/%s#rosa'
                  % team for team in serieA_teams]
    
    players_dict = {}
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5})

    def parse(self, response):
                    
        # Name of Serie A team
        team_name = response.xpath('//h1/text()').extract_first()
        team_name = team_name.upper()
        
        # Table containing all the players of that team
        table = response.xpath('//table[contains(@id,"DataTables_Table_0")]'+
                               '/tbody/tr')
        
        players_container = []
        
        # For each player
        for player in table:
            
            # Extract the name                        
            name = player.xpath('.//a/text()').extract_first()
            players_container.append(name)
            
        # Store the name in the dict
        self.players_dict[team_name] = players_container
        
        # When we have all the 20 teams we save the result
        if len(self.players_dict) == 20:
            
            players_dir = ('/Users/andrea/Desktop/fanta3_0/'+
                           'all_players_per_team/players')
            
            n_files_present = len([file for file in os.listdir(players_dir) if
                                           file.endswith('.pckl')])
            
            next_file = n_files_present + 1
            
            filename = ('/Users/andrea/Desktop/fanta3_0/all_players_per_team/'+
                        'players/players_%d.pckl' % next_file)
            # Save the file
            f = open(filename, 'wb')
            pickle.dump(self.players_dict, f)
            f.close()
                

            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
                
    
    