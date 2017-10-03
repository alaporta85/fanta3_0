from itertools import permutations, combinations
import copy
import random
import os


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

def leagues_generator(teams, n_rounds):
    
    '''Returns a list of 'n_rounds' rounds between ALL the combinations which
       are possible with given set of teams.'''
    
    def recursive_rounds(a_round,all_valid_days):
        
        '''Creates recursively the rounds.'''
        
        nonlocal all_valid_rounds
                
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


def clean_round(a_round):
    
    '''Takes a string as input which has the form:
        
        [(('A','B'),('C','D'),('E','F'),('G','H')),(('A','C'),.......]
        
       and returns it clean as:
           
        ABCDEFGHAC..........
    
       Such string will be then written in the .txt file inside the function
       all_leagues_generator_txt(teams).'''
       
    res = str(a_round).replace("'",'').replace('[','')\
                      .replace(']','').replace(',','')\
                      .replace(' ','').replace('(','').replace(')','')
    
    return res


def all_leagues_generator_txt(teams):
    
    '''Generates a .txt file containing all the possible rounds considering
       the input 'teams'. Each line in the file is a complete round. In our
       case we generate it by using letters as team names. Since there are 8
       teams, each round has:
           
           - 7 days
           
           - 4 matches per day
           
           - 2 teams per match
           
       So each line in our file will have 56 letters, each letter representing
       one of the real fantateams. The transformation from letters to real team
       will be done later by using the function real_round_from_line.'''
    
    def recursive_rounds(a_round,all_valid_days):
        
        '''Writes recursively the rounds in the file.'''
                        
        for day in all_valid_days:
            a_round_copy = copy.copy(a_round)
            a_round_copy.append(day)
            
            if len(a_round_copy) == len(teams) - 1:
                cleaned_round = str(clean_round(a_round_copy))
                myfile.write(cleaned_round+'\n')
            else:
                new_list = available_days(day,all_valid_days,teams)
                recursive_rounds(a_round_copy,new_list)
    
    teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
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
                        
    a_round = []
    myfile = open('All_Leagues_%dteams.txt' % len(teams),'w')
    recursive_rounds(a_round,all_valid_days)
    myfile.close()
    
    
def reduced_leagues_txt(filename,number):
    
    '''Creates another .txt file with 'number' random leagues. This is done to
       avoid opening the original big file when producing the statistics of the
       fantaleague. Since it is clear that 8-10 thousands leagues in the
       simulation are enough to have statistically reliable results, a good
       value for the input 'number' is around 50000.'''
       
    myfile = open('/Users/andrea/Desktop/fanta3_0/MANTRA code/'+
                  'Reduced_Leagues_8teams.txt','w')
    for i in range(number):
        line = get_random_line(filename)
        myfile.write(line+'\n')
        
    myfile.close()
    
    
def get_random_line(filename):
    
    '''Returns the content of a random line inside a .txt file.'''
    
    # First extract the number of bytes of the file
    total_bytes = os.stat(filename).st_size
    
    # Then we select a random point in the file by selecting a random byte
    random_point = random.randint(0, total_bytes)
    
    # Open the file
    myfile = open(filename)
    
    # Go to the randomly selected point
    myfile.seek(random_point)
    
    # Skip this line to clear the partial line
    myfile.readline()
    
    # Assing the content of the next complete line to a variable and close the
    # file
    line = myfile.readline()
    myfile.close()
    
    # Returns everything except the last carachter of the string which is '\n'
    return line[:-1]

def real_round_from_line(line):
    
    '''Takes the input which is a random line from the .txt file and has the
       form:
           
           ABCDEFGHAC..........
           
       and transforms it into a complete round with the real names of the
       fantateams by using the dict 'letters'.'''
    
    letters = {'A':'Ciolle United',
               'B':'FC Pastaboy',
               'C':'FC ROXY',
               'D':'Bucalina FC',
               'E':'Fc Stress',
               'F':'AC PICCHIA',
               'G':'FC BOMBAGALLO',
               'H':'Giochici Giochici Stars'}
    
    final_round = []
    res = []
    
    # Create the matches
    for i in range(0,len(line),2):
        res.append((letters[line[i]],letters[line[i+1]]))
        
        # When the number of matches is the one required to form a day we
        # append it to the final list and empy the day
        if len(res)==len(letters)//2:
            final_round.append(tuple(res))
            res = []
        
    return final_round

def random_rounds(number):
    
    '''Returns a list of 'number' random rounds ready to be used in the
       simulation. Each of these rounds will be used later to generate a
       complete schedule by using the function generate_schedule(a_round,
       total_days).'''
    
    myfile = ('/Users/andrea/Desktop/All_Leagues_8teams.txt')
    
    res = []
    for x in range(number):
        line = get_random_line(myfile)
        real_round = real_round_from_line(line)
        res.append(real_round)
        
    return res
                

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
                                
                                
        
    




    













    
        