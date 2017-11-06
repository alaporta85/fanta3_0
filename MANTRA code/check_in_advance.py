import random
import MANTRA_functions as ms
import pickle
import os

#%%
f = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/' +
         'fantaplayers/fantaplayers_11.pckl', 'rb')
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

stress = [('REINA', ['Por'], 'NAPOLI', 'no'),
          ('IZZO', ['Dd', 'Dc'], 'GENOA', 'yes'),
          ('CHIELLINI', ['Ds', 'Dc'], 'JUVENTUS', 'yes'),
          ('BARZAGLI', ['Dc'], 'JUVENTUS', 'no'),
          ('LULIC', ['E', 'C', 'W'], 'LAZIO', 'yes'),
          ('LUIS ALBERTO', ['C', 'T'], 'LAZIO', 'yes'),
          ('FREULER', ['M', 'C'], 'ATALANTA', 'yes'),
          ('POLI', ['M', 'C'], 'BOLOGNA', 'yes'),
          ('DI FRANCESCO F', ['W', 'A'], 'BOLOGNA', 'yes'),
          ('DYBALA', ['A'], 'JUVENTUS', 'yes'),
          ('MERTENS', ['Pc'], 'NAPOLI', 'yes'),
          ('LJAJIC', ['A'], 'TORINO', 'yes'),
          ('NANI', ['A'], 'LAZIO', 'no'),
          ('CANDREVA', ['W'], 'INTER', 'yes'),
          ('BENTANCUR', ['C'], 'JUVENTUS', 'no'),
          ('GONALONS', ['M', 'C'], 'ROMA', 'yes'),
          ('DE ROSSI', ['M', 'C'], 'ROMA', 'no'),
          ('VERETOUT', ['C', 'T'], 'FIORENTINA', 'yes'),
          ('MARIO RUI', ['Ds', 'E'], 'NAPOLI', 'yes'),
          ('ABATE', ['Dd', 'E'], 'MILAN', 'yes'),
          ('CALABRIA', ['Dd', 'E'], 'MILAN', 'no'),
          ('REGINI', ['Ds', 'Dc'], 'SAMPDORIA', 'no'),
          ('SEPE', ['Por'], 'NAPOLI', 'yes'),
#          ('LOMBARDI', ['A'], 'BENEVENTO', 'no'),
#          ('RAFAEL CABRAL', ['Por'], 'NAPOLI'),
#          ('CAPUANO', ['Ds', 'Dc'], 'CAGLIARI', 'no'),
#          ('SEPE', ['Por'], 'NAPOLI'),
#          ('BENATIA', ['Dc'], 'JUVENTUS'),
#          ('MURGIA', ['M', 'C'], 'LAZIO'),
#          ('RICCI', ['A'], 'GENOA'),
#          ('GHOULAM', ['Ds', 'E'], 'NAPOLI', 'yes'),
          ]

ciolle = [('ALISSON', ['Por'], 'ROMA', 'yes'),
          ('KOLAROV', ['Ds', 'E'], 'ROMA', 'yes'),
          ('SKRINIAR', ['Dc'], 'INTER', 'yes'),
          ('KOULIBALY', ['Dc'], 'NAPOLI', 'yes'),
          ('HYSAJ', ['Dd', 'Ds', 'E'], 'NAPOLI', 'yes'),
          ('GAGLIARDINI', ['M', 'C'], 'INTER', 'yes'),
          ('MARCHISIO', ['M', 'C'], 'JUVENTUS', 'yes'),
          ('BENASSI', ['C'], 'FIORENTINA', 'yes'),
          ('ILICIC', ['T', 'A'], 'ATALANTA', 'no'),
          ('CALLEJON', ['A'], 'NAPOLI', 'yes'),
          ('BELOTTI', ['Pc'], 'TORINO', 'yes'),
          ('SIMEONE', ['Pc'], 'FIORENTINA', 'yes'),
          ('CORNELIUS', ['Pc'], 'ATALANTA', 'no'),
          ('JOAO MARIO', ['C', 'T'], 'INTER', 'no'),
          ('JANKTO', ['E', 'C'], 'UDINESE', 'yes'),
          ('RODRIGUEZ R', ['Ds', 'E'], 'MILAN', 'yes'),
          ('PADOIN', ['Dd', 'E', 'M'], 'CAGLIARI', 'yes'),
          ('RINCON', ['M', 'C'], 'TORINO', 'yes'),
          ('BESSA', ['C', 'T'], 'VERONA', 'no'),
          ('LIROLA', ['Dd', 'E'], 'SASSUOLO', 'no'),
          ('NUYTINCK', ['Dc'], 'UDINESE', 'yes'),
          ('MUSACCHIO', ['Dc'], 'MILAN', 'no'),
          ('SKORUPSKI', ['Por'], 'ROMA', 'no'),
#          ('GRAVILLON', ['Dd', 'Dc'], 'BENEVENTO', 'no'),
#          ('SENSI', ['M', 'C'], 'SASSUOLO', 'yes'),
#          ('LOBONT', ['Por'], 'ROMA'),
#          ('DALBERT', ['Ds', 'E'], 'INTER'),
#          ('FERRARI A', ['Dd', 'Dc'], 'VERONA'),
#          ('KARAMOH', ['A'], 'INTER'),
#          ('KEAN', ['Pc'], 'VERONA')
          ]

pastaboy = [('BERISHA', ['Por'], 'ATALANTA', 'yes'),
            ('CANNAVARO', ['Dc'], 'SASSUOLO', 'yes'),
            ('BONUCCI', ['Dc'], 'MILAN', 'yes'),
            ('FAZIO', ['Dc'], 'ROMA', 'yes'),
            ('ASAMOAH', ['Ds', 'E'], 'JUVENTUS', 'no'),
            ('HAMSIK', ['C', 'T'], 'NAPOLI', 'yes'),
            ('MATUIDI', ['M', 'C'], 'JUVENTUS', 'yes'),
            ('VECINO', ['M', 'C'], 'INTER', 'yes'),
            ('BERNARDESCHI', ['W', 'A'], 'JUVENTUS', 'no'),
            ('IMMOBILE', ['Pc'], 'LAZIO', 'yes'),
            ('FARIAS', ['A'], 'CAGLIARI', 'yes'),
            ('ZAPATA D', ['Pc'], 'SAMPDORIA', 'yes'),
            ('SAU', ['A'], 'CAGLIARI', 'yes'),
            ('BONAVENTURA', ['C', 'W', 'T'], 'MILAN', 'no'),
            ('UNDER', ['W'], 'ROMA', 'no'),
            ('CRISTANTE', ['M', 'C'], 'ATALANTA', 'yes'),
            ('HALLFREDSSON', ['M', 'C'], 'UDINESE', 'no'),
            ('MIRANDA', ['Dc'], 'INTER', 'yes'),
            ('ALEX SANDRO', ['Ds', 'E'], 'JUVENTUS', 'yes'),
            ("D'AMBROSIO", ['Dd', 'Ds', 'E'], 'INTER', 'yes'),
            ('TOMOVIC', ['Dd', 'Dc'], 'CHIEVO', 'yes'),
            ('CIGARINI', ['M', 'C'], 'CAGLIARI', 'yes'),
            ('CONSIGLI', ['Por'], 'SASSUOLO', 'no'),
#            ('SIRIGU', ['Por'], 'TORINO'),
#            ('DE SILVESTRI', ['Dd', 'E'], 'TORINO'),
#            ('ANSALDI', ['Dd', 'Ds', 'E'], 'TORINO'),
#            ('JUAN JESUS', ['Ds', 'Dc'], 'ROMA'),
#            ('CESAR', ['Dc'], 'CHIEVO'),
#            ('EYSSERIC', ['W', 'T'], 'FIORENTINA'),
#            ('BERENGUER', ['W'], 'TORINO'),
#            ('NIANG', ['A'], 'TORINO'),
#            ('DESTRO', ['Pc'], 'BOLOGNA')
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

#%%
#fantateam = ciolle
#module = '4312'
#check_in_advance(module, fantateam)
