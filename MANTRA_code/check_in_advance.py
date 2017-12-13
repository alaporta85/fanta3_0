import random
import MANTRA_functions as ms
import pickle
import os

f = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/' +
         'fantaplayers/fantaplayers_13.pckl', 'rb')
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
            ('STRINIC', ['Ds', 'E'], 'SAMPDORIA', 'no'),
            ('DE VRIJ', ['Dc'], 'LAZIO', 'yes'),
            ('DAINELLI', ['Dc'], 'CHIEVO', 'no'),
            ('GAZZOLA', ['Dd', 'E'], 'SASSUOLO', 'yes'),
            ('PERISIC', ['W', 'A'], 'INTER', 'yes'),
            ('PRAET', ['C', 'T'], 'SAMPDORIA', 'no'),
            ("KESSIE'", ['M', 'C'], 'MILAN', 'yes'),
            ('CHIESA', ['W', 'A'], 'FIORENTINA', 'yes'),
            ('SIMEONE', ['Pc'], 'FIORENTINA', 'yes'),
            ('HIGUAIN', ['Pc'], 'JUVENTUS', 'yes'),
            ('FALCINELLI', ['Pc'], 'SASSUOLO', 'yes'),
            ('MAXI LOPEZ', ['Pc'], 'UDINESE', 'no'),
            ('CATALDI', ['M', 'C'], 'BENEVENTO', 'yes'),
            ('BARRETO E', ['M', 'C'], 'SAMPDORIA', 'yes'),
            ('LAXALT', ['E'], 'GENOA', 'yes'),
            ('BROZOVIC', ['C', 'T'], 'INTER', 'yes'),
            ('LAURINI', ['Dd', 'E'], 'FIORENTINA', 'yes'),
            ('ANDREOLLI', ['Dc'], 'CAGLIARI', 'yes'),
            ('FELIPE', ['Dc'], 'SPAL', 'yes'),
            ('HEURTAUX', ['Dc'], 'VERONA', 'yes'),
            ('ANTEI', ['Dd', 'Dc'], 'BENEVENTO', 'yes'),
            ('SZCZESNY', ['Por'], 'JUVENTUS', 'no'),
#            ('PINSOGLIO', ['Por'], 'JUVENTUS'),
#            ('BARRECA', ['Ds', 'E'], 'TORINO'),
#            ('ADJAPONG', ['Dd', 'E'], 'SASSUOLO'),
#            ('RANOCCHIA', ['Dc'], 'INTER'),
#            ('IZCO', ['E', 'M'], 'CROTONE'),
            ]

stress = [('REINA', ['Por'], 'NAPOLI', 'yes'),
          ('CHIELLINI', ['Ds', 'Dc'], 'JUVENTUS', 'yes'),
          ('BENATIA', ['Dc'], 'JUVENTUS', 'yes'),
          ('FERRARI G', ['Dc'], 'SAMPDORIA', 'yes'),
          ('LULIC', ['E', 'C', 'W'], 'LAZIO', 'yes'),
          ('FREULER', ['M', 'C'], 'ATALANTA', 'yes'),
          ('LUIS ALBERTO', ['C', 'T'], 'LAZIO', 'yes'),
          ('MARIO RUI', ['Ds', 'E'], 'NAPOLI', 'yes'),
          ('DYBALA', ['A'], 'JUVENTUS', 'yes'),
          ('MERTENS', ['Pc'], 'NAPOLI', 'yes'),
          ('LJAJIC', ['A'], 'TORINO', 'no'),
          ('CANDREVA', ['W'], 'INTER', 'yes'),
          ('POLITANO', ['A'], 'SASSUOLO', 'yes'),
          ('VERETOUT', ['C', 'T'], 'FIORENTINA', 'yes'),
          ('GONALONS', ['M', 'C'], 'ROMA', 'yes'),
          ('MAGGIO', ['Dd', 'E'], 'NAPOLI', 'no'),
          ('DE SCIGLIO', ['Dd', 'Ds', 'E'], 'JUVENTUS', 'yes'),
          ('NAGATOMO', ['Dd', 'Ds', 'E'], 'INTER', 'no'),
          ('SALAMON', ['Dc'], 'SPAL', 'yes'),
          ('ZUKANOVIC', ['Ds', 'Dc'], 'GENOA', 'yes'),
          ('IZZO', ['Dd', 'Dc'], 'GENOA', 'yes'),
          ('SEPE', ['Por'], 'NAPOLI', 'no'),
          ('RAFAEL CABRAL', ['Por'], 'NAPOLI', 'no'),
#          ('BARZAGLI', ['Dc'], 'JUVENTUS'),
#          ('CAPUANO', ['Ds', 'Dc'], 'CAGLIARI'),
#          ('DE ROSSI', ['M', 'C'], 'ROMA'),
#          ('DI FRANCESCO F', ['W', 'A'], 'BOLOGNA'),
#          ('NANI', ['A'], 'LAZIO'),
          ]

ciolle = [('ALISSON', ['Por'], 'ROMA', 'yes'),
          ('KOULIBALY', ['Dc'], 'NAPOLI', 'yes'),
          ('ZAPATA C', ['Dc'], 'MILAN', 'yes'),
          ('SKRINIAR', ['Dc'], 'INTER', 'yes'),
          ('KOLAROV', ['Ds', 'E'], 'ROMA', 'yes'),
          ('BENASSI', ['C'], 'FIORENTINA', 'yes'),
          ('MARCHISIO', ['M', 'C'], 'JUVENTUS', 'yes'),
          ('RODRIGUEZ R', ['Ds', 'E'], 'MILAN', 'yes'),
          ('ILICIC', ['T', 'A'], 'ATALANTA', 'no'),
          ('BELOTTI', ['Pc'], 'TORINO', 'yes'),
          ('CALLEJON', ['A'], 'NAPOLI', 'yes'),
          ('CORNELIUS', ['Pc'], 'ATALANTA', 'yes'),
          ('PERICA', ['Pc'], 'UDINESE', 'yes'),
          ('VERDI', ['T', 'A'], 'BOLOGNA', 'yes'),
          ('BARELLA', ['C', 'T'], 'CAGLIARI', 'yes'),
          ('JANKTO', ['E', 'C'], 'UDINESE', 'yes'),
          ('GAGLIARDINI', ['M', 'C'], 'INTER', 'yes'),
          ('HETEMAJ', ['E', 'M'], 'CHIEVO', 'yes'),
          ('HYSAJ', ['Dd', 'Ds', 'E'], 'NAPOLI', 'yes'),
          ('MUSACCHIO', ['Dc'], 'MILAN', 'no'),
          ('LYANCO', ['Dc'], 'TORINO', 'no'),
          ('SKORUPSKI', ['Por'], 'ROMA', 'no'),
          ('LOBONT', ['Por'], 'ROMA', 'no'),
#          ('NUYTINCK', ['Dc'], 'UDINESE'),
#          ('PADOIN', ['Dd', 'E', 'M'], 'CAGLIARI'),
#          ('RINCON', ['M', 'C'], 'TORINO'),
#          ('LINETTY', ['C'], 'SAMPDORIA'),
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
