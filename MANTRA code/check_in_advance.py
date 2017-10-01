import random
import mantra_functions_without_filters as ms
import pickle
import os


acpicchia = [('STRAKOSHA', ['Por'], 'LAZIO','yes'),
             ('CALDARA', ['Dc'], 'ATALANTA','yes'),
             ('RUGANI', ['Dc'], 'JUVENTUS','no'),
             ('MANOLAS', ['Dc'], 'ROMA','yes'),
             ('FLORENZI', ['E', 'C', 'W'], 'ROMA','yes'),
             ('CASTRO', ['C', 'T'], 'CHIEVO','yes'),
             ('ZIELINSKI', ['C', 'T'], 'NAPOLI','yes'),
             ('LICHTSTEINER', ['Dd', 'E'], 'JUVENTUS','yes'),
             ('CALHANOGLU', ['T'], 'MILAN','yes'),
             ('CUADRADO', ['W'], 'JUVENTUS','yes'),
             ("ANDRE' SILVA", ['Pc'], 'MILAN','no'),
             ('CUTRONE', ['Pc'], 'MILAN','yes'),
             ('EL SHAARAWY', ['A'], 'ROMA','yes'),
             ('DEFREL', ['A'], 'ROMA','yes'),
             ('DOUGLAS COSTA', ['W', 'A'], 'JUVENTUS','yes'),
             ('STROOTMAN', ['M', 'C'], 'ROMA','yes'),
             ('JORGINHO', ['M', 'C'], 'NAPOLI','no'),
             ('ALLAN', ['M', 'C'], 'NAPOLI','yes'),
             ('BRUNO PERES', ['Dd', 'E'], 'ROMA','yes'),
             ('LETIZIA', ['Dd', 'Ds', 'E'], 'BENEVENTO','yes'),
             ('GAMBERINI', ['Dc'], 'CHIEVO','yes'),
             ('SAMIR', ['Ds', 'Dc'], 'UDINESE','yes'),
             ('MIRANTE', ['Por'], 'BOLOGNA','no'),
#             ('VIVIANO', ['Por'], 'SAMPDORIA'),
#             ('HOWEDES', ['Dd', 'Dc'], 'JUVENTUS'),
#             ('KARSDORP', ['Dd', 'E'], 'ROMA'),
#             ('DE SCIGLIO', ['Dd', 'Ds', 'E'], 'JUVENTUS'),
#             ('GOBBI', ['Ds', 'E'], 'CHIEVO'),
#             ('DIAWARA', ['M', 'C'], 'NAPOLI'),
#             ('BASELLI', ['C'], 'TORINO'),
#             ('SCHICK', ['A'], 'ROMA'),
#             ('BORRIELLO', ['Pc'], 'SPAL')
             ]

bucalina = [('BUFFON', ['Por'], 'JUVENTUS','yes'),
            ('STRINIC', ['Ds', 'E'], 'SAMPDORIA','yes'),
            ('FELIPE', ['Dc'], 'SPAL','yes'),
            ('DE VRIJ', ['Dc'], 'LAZIO','yes'),
            ('MATTIELLO', ['Dd', 'Ds', 'E'], 'SPAL','no'),
            ('PERISIC', ['W', 'A'], 'INTER','yes'),
            ('BROZOVIC', ['C', 'T'], 'INTER','yes'),
            ('BARRETO E', ['M', 'C'], 'SAMPDORIA','yes'),
            ('CHIESA', ['W', 'A'], 'FIORENTINA','yes'),
            ('HIGUAIN', ['Pc'], 'JUVENTUS','yes'),
            ('VERDI', ['T', 'A'], 'BOLOGNA','yes'),
            ('MAXI LOPEZ', ['Pc'], 'UDINESE','yes'),
            ('FALCINELLI', ['Pc'], 'SASSUOLO','no'),
            ('PRAET', ['C', 'T'], 'SAMPDORIA','yes'),
            ("KESSIE'", ['M', 'C'], 'MILAN','yes'),
            ('CATALDI', ['M', 'C'], 'BENEVENTO','yes'),
            ('LAXALT', ['E'], 'GENOA','yes'),
            ('IZCO', ['E', 'M'], 'CROTONE','no'),
            ('RANOCCHIA', ['Dc'], 'INTER','no'),
            ('DE MAIO', ['Dc'], 'BOLOGNA','no'),
            ('HEURTAUX', ['Dc'], 'VERONA','yes'),
            ('ANDREOLLI', ['Dc'], 'CAGLIARI','yes'),
            ('SZCZESNY', ['Por'], 'JUVENTUS','no'),
#            ('PINSOGLIO', ['Por'], 'JUVENTUS'),
#            ('CANCELO', ['Dd', 'E'], 'INTER'),
#            ('BARRECA', ['Ds', 'E'], 'TORINO'),
#            ('VAN DER WIEL', ['Dd', 'E'], 'CAGLIARI'),
#            ('ANTEI', ['Dd', 'Dc'], 'BENEVENTO'),
            ]


def check_in_advance(module,fantateam):
    players_database = {player[0]:(99,'aaa',random.randint(1,10),random.randint(1,10))
                        for player in fantateam if player[3] == 'yes'}
    f=open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/Day_99.pckl','wb')
    pickle.dump(players_database,f)
    f.close()
    
    lineup = [('Day 99',player[0],player[1]) for player in fantateam]
    
    res = ms.MANTRA_simulation(lineup,module)
    
    os.remove('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/'+
              'Day_99.pckl')
    
    return res
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
