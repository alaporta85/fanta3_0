import random
import mantra_functions_without_filters as ms
from schemes_allowed_changes import schemes, compatible_roles, malus_roles
import pickle
from itertools import combinations, permutations, product
import copy



acpicchia = [('STRAKOSHA', ['Por'], 'LAZIO','yes'),
             ('CALDARA', ['Dc'], 'ATALANTA','yes'),
             ('RUGANI', ['Dc'], 'JUVENTUS','no'),
             ('MANOLAS', ['Dc'], 'ROMA','yes'),
             ('FLORENZI', ['E', 'C', 'W'], 'ROMA','yes'),
             ('CASTRO', ['C', 'T'], 'CHIEVO','yes'),
             ('ZIELINSKI', ['C', 'T'], 'NAPOLI','yes'),
             ('LICHTSTEINER', ['Dd', 'E'], 'JUVENTUS','yes'),
             ('CALHANOGLU', ['T'], 'MILAN','no'),
             ('CUADRADO', ['W'], 'JUVENTUS','yes'),
             ("ANDRE' SILVA", ['Pc'], 'MILAN','no'),
             ('CUTRONE', ['Pc'], 'MILAN','no'),
             ('EL SHAARAWY', ['A'], 'ROMA','yes'),
             ('DEFREL', ['A'], 'ROMA','yes'),
             ('DOUGLAS COSTA', ['W', 'A'], 'JUVENTUS','yes'),
             ('STROOTMAN', ['M', 'C'], 'ROMA','yes'),
             ('JORGINHO', ['M', 'C'], 'NAPOLI','no'),
             ('ALLAN', ['M', 'C'], 'NAPOLI','yes'),
             ('BRUNO PERES', ['Dd', 'E'], 'ROMA','yes'),
             ('LETIZIA', ['Dd', 'Ds', 'E'], 'BENEVENTO','no'),
             ('GAMBERINI', ['Dc'], 'CHIEVO','yes'),
             ('SAMIR', ['Ds', 'Dc'], 'UDINESE','yes'),
             ('MIRANTE', ['Por'], 'BOLOGNA','no'),
# =============================================================================
#              ('VIVIANO', ['Por'], 'SAMPDORIA'),
#              ('HOWEDES', ['Dd', 'Dc'], 'JUVENTUS'),
#              ('KARSDORP', ['Dd', 'E'], 'ROMA'),
#              ('DE SCIGLIO', ['Dd', 'Ds', 'E'], 'JUVENTUS'),
#              ('GOBBI', ['Ds', 'E'], 'CHIEVO'),
#              ('DIAWARA', ['M', 'C'], 'NAPOLI'),
#              ('BASELLI', ['C'], 'TORINO'),
#              ('SCHICK', ['A'], 'ROMA'),
#              ('BORRIELLO', ['Pc'], 'SPAL')
# =============================================================================
             ]


def check_in_advance(module,fantateam):
    players_database = {player[0]:(99,'aaa',random.randint(1,10),random.randint(1,10))
                        for player in fantateam if player[3] == 'yes'}
    f=open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/Day_99.pckl','wb')
    pickle.dump(players_database,f)
    f.close()
    
    lineup = [('Day 99',player[0],player[1]) for player in fantateam]
    
    return ms.MANTRA_simulation(lineup,module)
    
#    return lineup
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
