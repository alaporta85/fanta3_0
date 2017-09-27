import mantra_functions_without_filters as mswf
import os
import pickle
import copy
import random

g = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_schedule/'+
         'schedule.pckl', 'rb')
schedule = pickle.load(g)
g.close()


h = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/'+
         'lineups.pckl', 'rb')
lineups = pickle.load(h)
h.close()


i = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/'+
         'all_players_per_fantateam.pckl', 'rb')
fantaplayers = pickle.load(i)
i.close()


l = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_schedule/'+
         'fantateams_names.pckl', 'rb')
fantanames = pickle.load(l)
l.close()


files = os.listdir('/Users/andrea/Desktop/fanta3_0/'+
                   'cday_lineups_votes/votes')[1:]
players_database = {}
for file in files:
    f = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/'+
             '%s' % file, 'rb')
    day = pickle.load(f)
    f.close()
    for player in day:
        if player in players_database:
            players_database[player].append(day[player])
        else:
            players_database[player] = [day[player]]
            
del day,file,files,player


class Player(object):
    def __init__(self,name):
        self.name = name
        self.team = ''
#        self.role = []
        self.FG_votes = [(data[0],data[2]) for data in
                         players_database[self.name] if data[2] != 'n.e.']
        self.FGfantavotes = []
        self.FG_avrg = 0
        self.FG_fanta_avrg = 0
        self.ST_votes = [(data[0],data[3]) for data in
                         players_database[self.name] if data[3] != 'n.e.']
        self.STfantavotes = []
        self.ST_avrg = 0
        self.ST_fanta_avrg = 0
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
        self.FG_matches_played = len(self.FG_votes)
        self.ST_matches_played = len(self.ST_votes)
        
        def calculate_avrg(self):            
            try:
                avrg_FG = (sum([vote[1] for vote in self.FG_votes])/
                                self.FG_matches_played)
                self.FG_avrg = round(avrg_FG,2)
            except ZeroDivisionError:
                self.FG_avrg = 0
            
            try:
                avrg_ST = (sum([vote[1] for vote in self.ST_votes])/
                                self.ST_matches_played)
                self.ST_avrg = round(avrg_ST,2)
            except ZeroDivisionError:
                self.ST_avrg = 0
                
                
        def calculate_fantavotes(day):
            FG_vote = [data[1] for data in self.FG_votes if data[0] == day][0]
            ST_vote = [data[1] for data in self.ST_votes if data[0] == day][0]
                        
            all_player_data_in_day = [data[4:] for data in
                                      players_database[self.name]
                                      if data[0] == day][0]
            
            FG_fantavote = (FG_vote
                            - 0.5*all_player_data_in_day[0]
                            - all_player_data_in_day[1]
                            + 3*all_player_data_in_day[2]
                            + 3*all_player_data_in_day[3]
                            - all_player_data_in_day[4]
                            + 3*all_player_data_in_day[5]
                            - 3*all_player_data_in_day[6]
                            - 2*all_player_data_in_day[7]
                            + all_player_data_in_day[8])
            ST_fantavote = (ST_vote
                            - 0.5*all_player_data_in_day[0]
                            - all_player_data_in_day[1]
                            + 3*all_player_data_in_day[2]
                            + 3*all_player_data_in_day[3]
                            - all_player_data_in_day[4]
                            + 3*all_player_data_in_day[5]
                            - 3*all_player_data_in_day[6]
                            - 2*all_player_data_in_day[7]
                            + all_player_data_in_day[8])
        
            
            self.FGfantavotes.append(FG_fantavote)
            self.STfantavotes.append(ST_fantavote)
            
                
        def update_player(self):
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
#            if self.name in all_players[self.team]:
#                self.role = all_roles[self.name]
            
        update_player(self)
        
# =============================================================================
#     def fantavote(self,day,mode='ST'):
#         for data in players_database[self.name]:
#             if data[0] == day:
#                 return
# =============================================================================
    
class Fantateam(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.victories = 0
        self.draws = 0
        self.defeats = 0
        self.malus = 0
        self.players = []
        
        self.lineups = lineups[self.name]
        self.players = fantaplayers[self.name]
        
        
    def lineup(self, day):
        return self.lineups[day-1]
                
    def players(self):
        return self.players

class Match(object):
    def __init__(self,team1,team2,day):
        self.team1 = team1
        self.team2 = team2
        self.day = day
        self.abs_points1 = 0
        self.abs_points2 = 0
        self.goals1 = 0
        self.goals2 = 0
        self.lineup1 = fantanames[team1].lineup(day)
        self.lineup2 = fantanames[team2].lineup(day)
        
        
fantanames = {team:Fantateam(team) for team in fantanames}
#all_players = {player:Player(player) for player in players_database}
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    