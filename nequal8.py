from itertools import permutations, combinations
import random
import copy

teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#teams = ['A', 'B', 'C', 'D','E','F']
#teams = ['A', 'B', 'C', 'D']

def no_repeated_teams(day):
    res = [team for match in day for team in match]
    if len(set(res)) == len(teams):
        return True
    else:
        return False
    
def no_repeated_days(a_round):
    res = [match for day in a_round for match in day]
    
    if len(set(res)) == (len(teams)-1)*(len(teams)//2):
        return True
    else:
        return False
    
def available_days(day,all_days):
    res = []
    for new_day in all_days:
        comb = day + new_day
        if len(set(comb)) == len(teams):
            res.append(new_day)
            
    return res

def leagues_generator(teams, n_leagues):
    
    n_matches_per_day = len(teams)//2
    
    n_days_per_round = len(teams) - 1
    
    pairs = list(combinations(teams,2))
        
    all_days = combinations(pairs,n_matches_per_day)
    
    all_valid_days = []
    
    for day in all_days:
        if no_repeated_teams(day):
            all_valid_days.append(day)
            
    all_valid_rounds = []
    
    def recursive_rounds(a_round,all_valid_days):
        
        nonlocal all_valid_rounds
                
        for day in all_valid_days:
            while len(all_valid_rounds) < n_leagues:
                a_round_copy = copy.copy(a_round)
                a_round_copy.append(day)
                
                if len(a_round_copy) == len(teams) - 1:
                    all_valid_rounds.append(a_round_copy)
# =============================================================================
#                     count += 1
#                     if not count % 1000000:
#                         print(count)
#                     if count == 31449600:
#                         print('bingo')
#                     if count == 31449601:
#                         print('ops')
# =============================================================================
                    
                else:
                    new_list = available_days(day,all_valid_days)
                    recursive_rounds(a_round_copy,new_list)
            else:
                break
            
    a_round = []
    recursive_rounds(a_round,all_valid_days)
    
    
#    for day1 in all_valid_days:
#        a_round = []
#        list2 = available_days(day1,all_valid_days)
#        for day2 in list2:
#            list3 = available_days(day2,list2)
#            for day3 in list3:
#                all_valid_rounds.append((day1,day2,day3))
#                a_round = []
                
    return len(all_valid_rounds)

            
# =============================================================================
#     for day1 in all_valid_days:
#         a_round = []
# #        a_round.append(day1)
#         list2 = available_days(day1,all_valid_days)
#         for day2 in list2:
# #            a_round.append(day2)
#             list3 = available_days(day2,list2)
#             for day3 in list3:
# #                a_round.append(day3)
#                 list4 = available_days(day3,list3)
#                 for day4 in list4:
# #                    a_round.append(day4)
#                     list5 = available_days(day4,list4)
#                     for day5 in list5:
# #                        a_round.append(day5)
#                         list6 = available_days(day5,list5)
#                         for day6 in list6:
#                             count += 1
# #                            a_round.append(day6)
#                             if not count%1000000:
#                                 print(count)
#                             if count == 31449600:
#                                 print('bingo')
#                             if count == 31449601:
#                                 print('ops')
# =============================================================================
                                
                                
                                
                                
# =============================================================================
#     for day1 in all_valid_days:
#         a_round = []
# #        a_round.append(day1)
#         list2 = available_days(day1,all_valid_days)
#         for day2 in list2:
# #            a_round.append(day2)
#             list3 = available_days(day2,list2)
#             for day3 in list3:
# #                a_round.append(day3)
#                 list4 = available_days(day3,list3)
#                 for day4 in list4:
# #                    a_round.append(day4)
#                     list5 = available_days(day4,list4)
#                     for day5 in list5:
# #                        a_round.append(day5)
#                         count += 1
# #                            a_round.append(day6)
#                         if not count%100:
#                             print(count)
#                         if count == 720:
#                             print('bingo')
#                         if count == 721:
#                             print('ops')
# =============================================================================
                            

                                
                                
        
    




    













    
        