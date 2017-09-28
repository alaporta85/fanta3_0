from itertools import permutations, combinations
import copy
import random

teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#teams = ['A', 'B', 'C', 'D', 'E', 'F']
#teams = ['A', 'B', 'C', 'D']

def no_repeated_teams(day):
    
    '''Checks whether a team appears more than once in one day. If not, the day
       is a valid one and returns True, else False.'''
    
    res = [team for match in day for team in match]
    if len(set(res)) == len(teams):
        return True
    else:
        return False
    
def no_repeated_days(a_round):
    
    '''Checks whether a day appears more than once in one round. If not, the
       round is a valid one and returns True, else False.'''
       
    res = [match for day in a_round for match in day]
    
    if len(set(res)) == (len(teams)-1)*(len(teams)//2):
        return True
    else:
        return False
    
def available_days(day,all_days):
    
    '''Returns the list of the days which are available in the round where the
       day "day" is already present. This is to avoid that any match can be
       played more than once in one round.'''
       
    res = []
    for new_day in all_days:
        comb = day + new_day
        if len(set(comb)) == len(teams):
            res.append(new_day)
            
    return res

def leagues_generator(teams, n_rounds,rand='NO'):
    
    '''Returns a list of 'n_rounds' rounds between ALL the combinations which
       are possible with given set of teams.'''
    
    def recursive_rounds(a_round,all_valid_days):
        
        '''Creates recursively the rounds.'''
        
        nonlocal all_valid_rounds
        
        if rand == 'YES':
            all_valid_days = random.sample(all_valid_days, len(all_valid_days))
                
        for day in all_valid_days:
            a_round_copy = copy.copy(a_round)
            a_round_copy.append(day)
            
            if len(all_valid_rounds) == n_rounds:
                break
                    
            elif len(a_round_copy) == len(teams) - 1:
                all_valid_rounds.append(a_round_copy)

            else:
                new_list = available_days(day,all_valid_days)
                recursive_rounds(a_round_copy,new_list)
    
    # All the possible matches
    pairs = list(combinations(teams,2))
    
    n_matches_per_day = len(teams)//2
    
    # All the possible days    
    all_days = combinations(pairs,n_matches_per_day)
    
    all_valid_days = []
    
    # If there are NO repeated teams in all the matches forming a day, it means
    # it is a valid day
    for day in all_days:
        if no_repeated_teams(day):
            all_valid_days.append(day)
            
    all_valid_rounds = []
            
    a_round = []
    recursive_rounds(a_round,all_valid_days)
                
    return all_valid_rounds
                                
                                
        
    




    













    
        