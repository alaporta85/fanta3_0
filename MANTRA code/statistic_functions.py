from itertools import permutations, combinations
import copy
import random

#teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#teams = ['A', 'B', 'C', 'D', 'E', 'F']
#teams = ['A', 'B', 'C', 'D']

def no_repeated_teams(day,teams):
    
    '''Checks whether a team appears more than once in one day. If not, the day
       is a valid one and returns True, else False.'''
    
    res = [team for match in day for team in match]
    if len(set(res)) == len(teams):
        return True
    else:
        return False
    
def available_days(day,all_days,teams):
    
    '''Returns the list of the days which are available in the round where the
       day "day" is already present. This is to avoid that any match can be
       played more than once in one round.'''
       
    res = []
    for new_day in all_days:
        comb = day + new_day
        if len(set(comb)) == len(teams):
            res.append(new_day)
            
    return res

def leagues_generator(teams, n_rounds,rand):
    
    '''Returns a list of 'n_rounds' rounds between ALL the combinations which
       are possible with given set of teams. If rand=='YES' they will be
       generated randomly.'''
    
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
                new_list = available_days(day,all_valid_days,teams)
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
        if no_repeated_teams(day,teams):
            all_valid_days.append(day)
            
    all_valid_rounds = []
            
    a_round = []
    recursive_rounds(a_round,all_valid_days)
                
    return all_valid_rounds


def generate_schedule(a_round,total_days):
    
    '''Returns a dict which represents the complete schedule, created by the
       input a_round and containing 'total_days' days.'''
       
    if not total_days%len(a_round):
        number = total_days//len(a_round)
        fin_list = a_round*number
        return {i:fin_list[i-1] for i in range(1,total_days+1)}
    else:
        n_complete_rounds = total_days//len(a_round)
        n_days_left = total_days%len(a_round)
        last_days = [a_round[i] for i in range(n_days_left)]
        fin_list = (a_round*n_complete_rounds) + last_days
        
    return {i:fin_list[i-1] for i in range(1,total_days+1)}
        
                                
                                
        
    




    













    
        