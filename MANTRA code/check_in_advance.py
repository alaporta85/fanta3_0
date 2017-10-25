import random
import MANTRA_functions as ms
import pickle
import os

f = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/' +
         'fantaplayers/fantaplayers_9.pckl', 'rb')
rose = pickle.load(f)
f.close()

#%%

acpicchia = [('STRAKOSHA', ['Por'], 'LAZIO', 'yes'),
             ('CALDARA', ['Dc'], 'ATALANTA', 'yes'),
             ('RUGANI', ['Dc'], 'JUVENTUS', 'no'),
             ('MANOLAS', ['Dc'], 'ROMA', 'yes'),
             ('FLORENZI', ['E', 'C', 'W'], 'ROMA', 'yes'),
             ('CASTRO', ['C', 'T'], 'CHIEVO', 'yes'),
             ('ZIELINSKI', ['C', 'T'], 'NAPOLI', 'yes'),
             ('LICHTSTEINER', ['Dd', 'E'], 'JUVENTUS', 'yes'),
             ('CALHANOGLU', ['T'], 'MILAN', 'yes'),
             ('CUADRADO', ['W'], 'JUVENTUS', 'yes'),
             ("ANDRE' SILVA", ['Pc'], 'MILAN', 'no'),
             ('CUTRONE', ['Pc'], 'MILAN', 'yes'),
             ('EL SHAARAWY', ['A'], 'ROMA', 'yes'),
             ('DEFREL', ['A'], 'ROMA', 'yes'),
             ('DOUGLAS COSTA', ['W', 'A'], 'JUVENTUS', 'yes'),
             ('STROOTMAN', ['M', 'C'], 'ROMA', 'yes'),
             ('JORGINHO', ['M', 'C'], 'NAPOLI', 'no'),
             ('ALLAN', ['M', 'C'], 'NAPOLI', 'yes'),
             ('BRUNO PERES', ['Dd', 'E'], 'ROMA', 'yes'),
             ('LETIZIA', ['Dd', 'Ds', 'E'], 'BENEVENTO', 'yes'),
             ('GAMBERINI', ['Dc'], 'CHIEVO', 'yes'),
             ('SAMIR', ['Ds', 'Dc'], 'UDINESE', 'yes'),
             ('MIRANTE', ['Por'], 'BOLOGNA', 'no'),
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

bucalina = [('BUFFON', ['Por'], 'JUVENTUS', 'yes'),
            ('STRINIC', ['Ds', 'E'], 'SAMPDORIA', 'yes'),
            ('FELIPE', ['Dc'], 'SPAL', 'yes'),
            ('DE VRIJ', ['Dc'], 'LAZIO', 'yes'),
            ('MATTIELLO', ['Dd', 'Ds', 'E'], 'SPAL', 'no'),
            ('PERISIC', ['W', 'A'], 'INTER', 'yes'),
            ('BROZOVIC', ['C', 'T'], 'INTER', 'yes'),
            ('BARRETO E', ['M', 'C'], 'SAMPDORIA', 'yes'),
            ('CHIESA', ['W', 'A'], 'FIORENTINA', 'yes'),
            ('HIGUAIN', ['Pc'], 'JUVENTUS', 'yes'),
            ('VERDI', ['T', 'A'], 'BOLOGNA', 'yes'),
            ('MAXI LOPEZ', ['Pc'], 'UDINESE', 'yes'),
            ('FALCINELLI', ['Pc'], 'SASSUOLO', 'no'),
            ('PRAET', ['C', 'T'], 'SAMPDORIA', 'yes'),
            ("KESSIE'", ['M', 'C'], 'MILAN', 'yes'),
            ('CATALDI', ['M', 'C'], 'BENEVENTO', 'yes'),
            ('LAXALT', ['E'], 'GENOA', 'yes'),
            ('IZCO', ['E', 'M'], 'CROTONE', 'no'),
            ('RANOCCHIA', ['Dc'], 'INTER', 'no'),
            ('DE MAIO', ['Dc'], 'BOLOGNA', 'no'),
            ('HEURTAUX', ['Dc'], 'VERONA', 'yes'),
            ('ANDREOLLI', ['Dc'], 'CAGLIARI', 'yes'),
            ('SZCZESNY', ['Por'], 'JUVENTUS', 'no'),
#            ('PINSOGLIO', ['Por'], 'JUVENTUS'),
#            ('CANCELO', ['Dd', 'E'], 'INTER'),
#            ('BARRECA', ['Ds', 'E'], 'TORINO'),
#            ('VAN DER WIEL', ['Dd', 'E'], 'CAGLIARI'),
#            ('ANTEI', ['Dd', 'Dc'], 'BENEVENTO'),
            ]

stress = [('REINA', ['Por'], 'NAPOLI', 'yes'),
          ('BARZAGLI', ['Dc'], 'JUVENTUS', 'yes'),
          ('CAPUANO', ['Ds', 'Dc'], 'CAGLIARI', 'no'),
          ('CHIELLINI', ['Ds', 'Dc'], 'JUVENTUS', 'no'),
          ('GHOULAM', ['Ds', 'E'], 'NAPOLI', 'yes'),
          ('LUIS ALBERTO', ['C', 'T'], 'LAZIO', 'yes'),
          ('VERETOUT', ['C', 'T'], 'FIORENTINA', 'yes'),
          ('LULIC', ['E', 'C', 'W'], 'LAZIO', 'yes'),
          ('DYBALA', ['A'], 'JUVENTUS', 'yes'),
          ('MERTENS', ['Pc'], 'NAPOLI', 'yes'),
          ('LJAJIC', ['A'], 'TORINO', 'yes'),
          ('LOMBARDI', ['A'], 'BENEVENTO', 'no'),
          ('DI FRANCESCO F', ['W', 'A'], 'BOLOGNA', 'no'),
          ('CANDREVA', ['W'], 'INTER', 'yes'),
          ('BENTANCUR', ['C'], 'JUVENTUS', 'yes'),
          ('DE ROSSI', ['M', 'C'], 'ROMA', 'no'),
          ('POLI', ['M', 'C'], 'BOLOGNA', 'no'),
          ('CALABRIA', ['Dd', 'E'], 'MILAN', 'yes'),
          ('ABATE', ['Dd', 'E'], 'MILAN', 'no'),
          ('MARIO RUI', ['Ds', 'E'], 'NAPOLI', 'no'),
          ('REGINI', ['Ds', 'Dc'], 'SAMPDORIA', 'no'),
          ('IZZO', ['Dd', 'Dc'], 'GENOA', 'yes'),
          ('SEPE', ['Por'], 'NAPOLI', 'no'),
#          ('RAFAEL CABRAL', ['Por'], 'NAPOLI'),
#          ('SEPE', ['Por'], 'NAPOLI'),
#          ('BENATIA', ['Dc'], 'JUVENTUS'),
#          ('FREULER', ['M', 'C'], 'ATALANTA'),
#          ('GONALONS', ['M', 'C'], 'ROMA'),
#          ('MURGIA', ['M', 'C'], 'LAZIO'),
#          ('NANI', ['A'], 'LAZIO'),
#          ('RICCI', ['A'], 'GENOA'),
          ]


def check_in_advance(module, fantateam):
    players_database = {player[0]: (99, 'aaa', random.randint(1, 10),
                        random.randint(1, 10))
                        for player in fantateam if player[3] == 'yes'}
    f = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/' +
             'votes/Day_99.pckl', 'wb')
    pickle.dump(players_database, f)
    f.close()

    lineup = [('Day 99', player[0], player[1]) for player in fantateam]

    res = ms.MANTRA_simulation(lineup, module)

    os.remove('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/' +
              'Day_99.pckl')

    return res
