import mantra_functions_without_filters as mfwf
import os
import pickle

# Load the dict with the schedule
g = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_schedule/'+
         'schedule.pckl', 'rb')
schedule = pickle.load(g)
g.close()

# Load the dict with all the lineups day by day
h = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/'+
         'lineups.pckl', 'rb')
lineups = pickle.load(h)
h.close()

# Load the dict with all the players of each fantateam
i = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/'+
         'all_players_per_fantateam.pckl', 'rb')
fantaplayers = pickle.load(i)
i.close()

# Load the dict with the names of the fantateams
l = open('/Users/andrea/Desktop/fanta3_0/serieA_fantateams_schedule/'+
         'fantateams_names.pckl', 'rb')
fantanames = pickle.load(l)
l.close()

# Votes are stored in different .pckl files for different days. Here we create
# a unique dict with all the votes. First we create the list with all the files
files = os.listdir('/Users/andrea/Desktop/fanta3_0/'+
                   'cday_lineups_votes/votes')[1:]

# Initialize the database
players_database = {}

# For each .pckl file we add to the database the data relative to each player
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

# Finally we delete some variables we do not need anymore            
del day,file,files,player


class Player(object):
    def __init__(self,name):
        self.name = name
        self.team = ''
        self.FGvotes = [(data[0],data[2]) for data in
                         players_database[self.name] if data[2] != 'n.e.']
        self.FGfantavotes = []
        self.FGavrg = 0
        self.FGfanta_avrg = 0
        self.STvotes = [(data[0],data[3]) for data in
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
                avrg_FG = (sum([vote[1] for vote in self.FGvotes])/
                                self.FG_matches_played)
                fanta_avrg_FG = (sum([vote[1] for vote in self.FGfantavotes])/
                                self.FG_matches_played)
                self.FGavrg = round(avrg_FG,2)
                self.FGfanta_avrg = round(fanta_avrg_FG,2)
            except ZeroDivisionError:
                self.FGavrg = 0
                self.FGfanta_avrg = 0
            
            try:
                avrg_ST = (sum([vote[1] for vote in self.STvotes])/
                                self.ST_matches_played)
                fanta_avrg_ST = (sum([vote[1] for vote in self.STfantavotes])/
                                self.ST_matches_played)
                self.STavrg = round(avrg_ST,2)
                self.STfanta_avrg = round(fanta_avrg_ST,2)
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
                    
                    self.FGfantavotes.append((day,FGfantavote))
                
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
                
                    self.STfantavotes.append((day,STfantavote))
            
                
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
        
    def vote(self,day,mode='ST'):
        
        '''Return the vote of the player in that day.'''
        
        if mode == 'FG':
            try:
                vote = [data[1] for data in self.FGvotes
                             if data[0]==day][0]
                return vote
            except IndexError:
                return 'n.e.'
        else:
            try:
                vote = [data[1] for data in self.STvotes
                             if data[0]==day][0]
                return vote
            except IndexError:
                return 'n.e.'
        
    def fantavote(self,day,mode='ST'):
        
        '''Return the vote of the player in that day.'''
        
        if mode == 'FG':
            try:
                fantavote = [data[1] for data in self.FGfantavotes
                             if data[0]==day][0]
                return fantavote
            except IndexError:
                return 'n.e.'
        else:
            try:
                fantavote = [data[1] for data in self.STfantavotes
                             if data[0]==day][0]
                return fantavote
            except IndexError:
                return 'n.e.'
    
class Fantateam(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.abs_points = 0
        self.victories = 0
        self.draws = 0
        self.defeats = 0
        self.malus = 0
        self.goals_scored = 0
        self.goals_taken = 0
        self.lineups = lineups[self.name]
        self.players = fantaplayers[self.name]
        
        
    def lineup(self, day):
        
        '''Returns the lineup of the fantateam in that day.'''
        
        return self.lineups[day-1]
                
    def players(self):
        
        '''Returns all the players of the fantateam.'''
        
        return self.players

class Match(object):
    def __init__(self,team1,team2,day,mode):
        self.team1 = team1
        self.team2 = team2
        self.day = day
        self.mode = mode
        self.lineup1 = fantanames[team1].lineup(day)
        self.lineup2 = fantanames[team2].lineup(day)
        
        self.play_match()
        
    def calculate_goals(self,a_number):
        
        '''Returns the number of goals scored by the fantateam in the match.
           The input 'a_number' represents the abs_points of the day, which is
           given by the sum of all fantavotes of the players taking part to the
           match.'''
           
        if a_number < 66:
            return 0
        else:
            return int((a_number-66)//6 + 1)
    
    def play_match(self):
        
        '''Plays the match and updates all the parameters realtive to each
           fantateam.'''
        
        # Separate module and player in two different variables and launch the
        # MANTRA simulation for both teams
        module1 = self.lineup1[0]
        lineup1 = self.lineup1[1]
        lineup_after_playing1,malus1 = mfwf.MANTRA_simulation(lineup1,
                                                            module1,
                                                            self.mode)
        
        module2 = self.lineup2[0]
        lineup2 = self.lineup2[1]
        lineup_after_playing2,malus2 = mfwf.MANTRA_simulation(lineup2,
                                                            module2,
                                                            self.mode)
        # Update the number of malus
        fantanames[self.team1].malus += malus1
        fantanames[self.team2].malus += malus2
        
        # Create a list of all players who will contribute to the final
        # fantavote calculation and finally calculate the abs_points for each
        # team, including eventual malus
        players_with_vote1 = [all_players[player[1]] for player
                              in lineup_after_playing1
                              if player[1]==player[1].upper()]
        abs_points1 = sum([player.fantavote(self.day,self.mode) for player
                           in players_with_vote1]) - 0.5*malus1
        
        players_with_vote2 = [all_players[player[1]] for player
                              in lineup_after_playing2
                              if player[1]==player[1].upper()]
        abs_points2 = sum([player.fantavote(self.day,self.mode) for player
                           in players_with_vote2]) - 0.5*malus2
        
        # Update the abs_points attribute of both fantateams
        fantanames[self.team1].abs_points += abs_points1
        fantanames[self.team2].abs_points += abs_points2
        
        # Calculate the goals scored by each fantateam in the match
        goals1 = self.calculate_goals(abs_points1)
        goals2 = self.calculate_goals(abs_points2)
        
        # Update goals_scored and goals_taken attributes for both teams
        fantanames[self.team1].goals_scored += goals1
        fantanames[self.team1].goals_taken += goals2
        fantanames[self.team2].goals_scored += goals2
        fantanames[self.team2].goals_taken += goals1
        
        # Update the rest of the attributes based on the number of goals scored
        # in the match by the fantateams
        if goals1 == goals2:
            fantanames[self.team1].draws += 1
            fantanames[self.team2].draws += 1
            fantanames[self.team1].points += 1
            fantanames[self.team2].points += 1
        elif goals1 > goals2:
            fantanames[self.team1].victories += 1
            fantanames[self.team2].defeats += 1
            fantanames[self.team1].points += 3
        else:
            fantanames[self.team1].defeats += 1
            fantanames[self.team2].victories += 1
            fantanames[self.team2].points += 3
            
            
class Day(object):
    def __init__(self,day,schedule,mode):
        self.day = day
        self.schedule = schedule
        self.mode = mode
        self.matches = self.schedule[str(day)]
        
    def play_day(self):
        
        '''Plays all the matches of the day.'''
        
        for match in self.matches:
            Match(match[0],match[1],self.day,self.mode)
            
            
class League(object):
    def __init__(self,n_days,schedule,mode):
        self.n_days = n_days
        self.schedule = schedule
        self.mode = mode
        
    def play_league(self):
        
        '''Plays n_days days in the schedule.'''
        
        for i in range(1,self.n_days+1):
            day = Day(i,self.schedule,self.mode)
            day.play_day()
        

        
fantanames = {team:Fantateam(team) for team in fantanames}
all_players = {player:Player(player) for player in players_database}

a = League(6,schedule,'ST')
a.play_league()

b = []

for team in fantanames:
    b.append((team,fantanames[team].abs_points))
    
print(sorted(b,key=lambda x:x[1],reverse=True))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    