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

bucalina = [('SZCZESNY', ['Por'], 'JUVENTUS', 'yes'),
            ('STRINIC', ['Ds', 'E'], 'SAMPDORIA', 'no'),
            ('DE VRIJ', ['Dc'], 'LAZIO', 'yes'),
            ('RANOCCHIA', ['Dc'], 'INTER', 'yes'),
            ('LAURINI', ['Dd', 'E'], 'FIORENTINA', 'yes'),
            ('PERISIC', ['W', 'A'], 'INTER', 'yes'),
            ('PRAET', ['C', 'T'], 'SAMPDORIA', 'yes'),
            ("KESSIE'", ['M', 'C'], 'MILAN', 'yes'),
            ('CHIESA', ['W', 'A'], 'FIORENTINA', 'yes'),
            ('SIMEONE', ['Pc'], 'FIORENTINA', 'yes'),
            ('HIGUAIN', ['Pc'], 'JUVENTUS', 'yes'),
            ('FALCINELLI', ['Pc'], 'SASSUOLO', 'yes'),
            ('MAXI LOPEZ', ['Pc'], 'UDINESE', 'no'),
            ('BROZOVIC', ['C', 'T'], 'INTER', 'no'),
            ('CATALDI', ['M', 'C'], 'BENEVENTO', 'no'),
            ('BARRETO E', ['M', 'C'], 'SAMPDORIA', 'yes'),
            ('DAINELLI', ['Dc'], 'CHIEVO', 'no'),
            ('FELIPE', ['Dc'], 'SPAL', 'yes'),
            ('ANDREOLLI', ['Dc'], 'CAGLIARI', 'no'),
            ('LAXALT', ['E'], 'GENOA', 'yes'),
            ('GAZZOLA', ['Dd', 'E'], 'SASSUOLO', 'no'),
            ('ANTEI', ['Dd', 'Dc'], 'BENEVENTO', 'no'),
            ('PINSOGLIO', ['Por'], 'JUVENTUS', 'no')
#            ('BARRECA', ['Ds', 'E'], 'TORINO'),
#            ('ADJAPONG', ['Dd', 'E'], 'SASSUOLO'),
#            ('HEURTAUX', ['Dc'], 'VERONA', 'yes'),
#            ('IZCO', ['E', 'M'], 'CROTONE'),
#            ('BUFFON', ['Por'], 'JUVENTUS', 'yes'),
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
          ('KOLAROV', ['Ds', 'E'], 'ROMA', 'yes'),
          ('SKRINIAR', ['Dc'], 'INTER', 'yes'),
          ('KOULIBALY', ['Dc'], 'NAPOLI', 'yes'),
          ('HYSAJ', ['Dd', 'Ds', 'E'], 'NAPOLI', 'yes'),
          ('JANKTO', ['E', 'C'], 'UDINESE', 'yes'),
          ('HETEMAJ', ['E', 'M'], 'CHIEVO', 'yes'),
          ('BENASSI', ['C'], 'FIORENTINA', 'yes'),
          ('VERDI', ['T', 'A'], 'BOLOGNA', 'no'),
          ('CALLEJON', ['A'], 'NAPOLI', 'yes'),
          ('ILICIC', ['T', 'A'], 'ATALANTA', 'yes'),
          ('KEAN', ['Pc'], 'VERONA', 'yes'),
          ('CORNELIUS', ['Pc'], 'ATALANTA', 'yes'),
          ('PERICA', ['Pc'], 'UDINESE', 'yes'),
          ('GAGLIARDINI', ['M', 'C'], 'INTER', 'yes'),
          ('BARELLA', ['C', 'T'], 'CAGLIARI', 'yes'),
          ('RINCON', ['M', 'C'], 'TORINO', 'yes'),
          ('LINETTY', ['C'], 'SAMPDORIA', 'yes'),
          ('RODRIGUEZ R', ['Ds', 'E'], 'MILAN', 'yes'),
          ('PADOIN', ['Dd', 'E', 'M'], 'CAGLIARI', 'yes'),
          ('NUYTINCK', ['Dc'], 'UDINESE', 'yes'),
          ('SKORUPSKI', ['Por'], 'ROMA', 'yes'),
          ('LOBONT', ['Por'], 'ROMA', 'yes'),
#          ('LYANCO', ['Dc'], 'TORINO', 'no'),
#          ('MARCHISIO', ['M', 'C'], 'JUVENTUS', 'yes'),
#          ('MUSACCHIO', ['Dc'], 'MILAN', 'no'),
#          ('ZAPATA C', ['Dc'], 'MILAN', 'yes'),
#          ('BELOTTI', ['Pc'], 'TORINO', 'no')
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

mento = [('SORRENTINO', ['Por'], 'CHIEVO', 'yes'),
         ('BIRAGHI', ['Ds', 'E'], 'FIORENTINA', 'yes'),
         ('PEZZELLA GER', ['Dc'], 'FIORENTINA', 'no'),
         ('ROSSETTINI', ['Dd', 'Dc'], 'GENOA', 'no'),
         ('ROMULO', ['Dd', 'E', 'M'], 'VERONA', 'yes'),
         ('VIVIANI', ['M', 'C'], 'SPAL', 'yes'),
         ('KHEDIRA', ['M', 'C'], 'JUVENTUS', 'yes'),
         ('JOAO PEDRO', ['T'], 'CAGLIARI', 'yes'),
         ('DE PAUL', ['W', 'T'], 'UDINESE', 'no'),
         ('INSIGNE', ['A'], 'NAPOLI', 'yes'),
         ('ICARDI', ['Pc'], 'INTER', 'yes'),
         ('PAVOLETTI', ['Pc'], 'CAGLIARI', 'yes'),
         ('LAPADULA', ['Pc'], 'GENOA', 'yes'),
         ('BIRSA', ['T'], 'CHIEVO', 'yes'),
         ('RAMIREZ', ['W', 'T'], 'SAMPDORIA', 'yes'),
         ('TORREIRA', ['M', 'C'], 'SAMPDORIA', 'yes'),
         ('MANDRAGORA', ['M', 'C'], 'CROTONE', 'yes'),
         ('HATEBOER', ['Dd', 'E'], 'ATALANTA', 'yes'),
         ('PISACANE', ['Dd', 'Ds', 'Dc'], 'CAGLIARI', 'yes'),
         ('ALBIOL', ['Dc'], 'NAPOLI', 'yes'),
         ('ACERBI', ['Dc'], 'SASSUOLO', 'yes'),
         ('SILVESTRE', ['Dc'], 'SAMPDORIA', 'yes'),
         ('SPORTIELLO', ['Por'], 'FIORENTINA', 'yes'),
#         ('GOMIS A', ['Por'], 'SPAL'),
#         ('LAZAAR', ['Ds', 'E'], 'BENEVENTO'),
#         ('FOFANA', ['M', 'C'], 'UDINESE'),
#         ('GIL DIAS', ['W', 'A'], 'FIORENTINA'),
#         ('NALINI', ['W', 'A'], 'CROTONE'),
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
