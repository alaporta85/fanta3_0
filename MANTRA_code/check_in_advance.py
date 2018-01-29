import random
import MANTRA_functions as ms
import pickle
import os

f = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/' +
         'fantaplayers/fantaplayers_18.pckl', 'rb')
rose = pickle.load(f)
f.close()

#%%

acpicchia = [('STRAKOSHA', ['Por'], 'LAZIO', (1, 'y')),
             ('VIVIANO', ['Por'], 'SAMPDORIA', (23, 'y')),
             ('MIRANTE', ['Por'], 'BOLOGNA'),
             ('CALDARA', ['Dc'], 'ATALANTA', (3, 'y')),
             ('MANOLAS', ['Dc'], 'ROMA', (4, 'n')),
             ('RUGANI', ['Dc'], 'JUVENTUS', (22, 'n')),
             ('GAMBERINI', ['Dc'], 'CHIEVO', (21, 'y')),
             ('BRUNO PERES', ['Dd', 'E'], 'ROMA', (19, 'y')),
             ('SAMIR', ['Ds', 'Dc'], 'UDINESE', (2, 'n')),
             ('LICHTSTEINER', ['Dd', 'E'], 'JUVENTUS'),
             ('LETIZIA', ['Dd', 'Ds', 'E'], 'BENEVENTO'),
             ('HOWEDES', ['Dd', 'Dc'], 'JUVENTUS'),
             ('GOBBI', ['Ds', 'E'], 'CHIEVO', (20, 'n')),
             ('ALLAN', ['M', 'C'], 'NAPOLI', (18, 'y')),
             ('STROOTMAN', ['M', 'C'], 'ROMA', (16, 'y')),
             ('JORGINHO', ['M', 'C'], 'NAPOLI', (17, 'y')),
             ('DIAWARA', ['M', 'C'], 'NAPOLI'),
             ('FLORENZI', ['E', 'C', 'W'], 'ROMA', (8, 'n')),
             ('SPINAZZOLA', ['E'], 'ATALANTA', (5, 'y')),
             ('ZIELINSKI', ['C', 'T'], 'NAPOLI', (7, 'y')),
             ('CASTRO', ['C', 'T'], 'CHIEVO'),
             ('GERSON', ['C', 'T'], 'ROMA', (6, 'y')),
             ('DOUGLAS COSTA', ['W', 'A'], 'JUVENTUS', (12, 'n')),
             ('CUADRADO', ['W'], 'JUVENTUS', (11, 'y')),
             ('CALHANOGLU', ['T'], 'MILAN'),
             ('MANDZUKIC', ['A'], 'JUVENTUS', (9, 'y')),
             ('EL SHAARAWY', ['A'], 'ROMA', (10, 'y')),
             ('SCHICK', ['A'], 'ROMA', (13, 'y')),
             ('DEFREL', ['A'], 'ROMA'),
             ('BORRIELLO', ['Pc'], 'SPAL'),
             ("ANDRE' SILVA", ['Pc'], 'MILAN', (14, 'y')),
             ('CUTRONE', ['Pc'], 'MILAN', (15, 'y'))]

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

stress = [('REINA', ['Por'], 'NAPOLI', (1, 'y')),
          ('CHIELLINI', ['Ds', 'Dc'], 'JUVENTUS', (2, 'y')),
          ('BENATIA', ['Dc'], 'JUVENTUS', (3, 'y')),
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
          ('BARZAGLI', ['Dc'], 'JUVENTUS', (4, 'n')),
          ('CAPUANO', ['Ds', 'Dc'], 'CAGLIARI'),
          ('DE ROSSI', ['M', 'C'], 'ROMA'),
          ('DI FRANCESCO F', ['W', 'A'], 'BOLOGNA'),
          ('NANI', ['A'], 'LAZIO')
          ]

ciolle = [('ALISSON', ['Por'], 'ROMA', (1, 'y')),
          ('KOLAROV', ['Ds', 'E'], 'ROMA', (2, 'y')),
          ('SKRINIAR', ['Dc'], 'INTER', (3, 'y')),
          ('KOULIBALY', ['Dc'], 'NAPOLI', (4, 'y')),
          ('HYSAJ', ['Dd', 'Ds', 'E'], 'NAPOLI', (5, 'y')),
          ('JANKTO', ['E', 'C'], 'UDINESE', (6, 'y')),
          ('HETEMAJ', ['E', 'M'], 'CHIEVO', (7, 'y')),
          ('BENASSI', ['C'], 'FIORENTINA', (8, 'y')),
          ('VERDI', ['T', 'A'], 'BOLOGNA', (9, 'y')),
          ('CALLEJON', ['A'], 'NAPOLI', (10, 'y')),
          ('ILICIC', ['T', 'A'], 'ATALANTA', (11, 'n')),
          ('KEAN', ['Pc'], 'VERONA', (12, 'y')),
          ('CORNELIUS', ['Pc'], 'ATALANTA', (13, 'y')),
          ('PERICA', ['Pc'], 'UDINESE', (14, 'y')),
          ('GAGLIARDINI', ['M', 'C'], 'INTER', (15, 'y')),
          ('BARELLA', ['C', 'T'], 'CAGLIARI', (16, 'y')),
          ('RINCON', ['M', 'C'], 'TORINO', (17, 'y')),
          ('LINETTY', ['C'], 'SAMPDORIA', (18, 'y')),
          ('RODRIGUEZ R', ['Ds', 'E'], 'MILAN', (19, 'y')),
          ('PADOIN', ['Dd', 'E', 'M'], 'CAGLIARI', (20, 'y')),
          ('NUYTINCK', ['Dc'], 'UDINESE', (21, 'y')),
          ('SKORUPSKI', ['Por'], 'ROMA', (22, 'y')),
          ('LOBONT', ['Por'], 'ROMA', (23, 'y')),
          ('LYANCO', ['Dc'], 'TORINO', 'no'),
          ('MARCHISIO', ['M', 'C'], 'JUVENTUS', 'yes'),
          ('MUSACCHIO', ['Dc'], 'MILAN', 'no'),
          ('ZAPATA C', ['Dc'], 'MILAN', 'yes'),
          ('BELOTTI', ['Pc'], 'TORINO', 'no')
          ]

pastaboy = [('CONSIGLI', ['Por'], 'SASSUOLO'),
            ('BERISHA', ['Por'], 'ATALANTA', (23, 'y')),
            ('SIRIGU', ['Por'], 'TORINO', (1, 'y')),
            ('ALEX SANDRO', ['Ds', 'E'], 'JUVENTUS', (2, 'n')),
            ('FAZIO', ['Dc'], 'ROMA', (4, 'n')),
            ('BONUCCI', ['Dc'], 'MILAN', (20, 'y')),
            ("D'AMBROSIO", ['Dd', 'Ds', 'E'], 'INTER', (22, 'y')),
            ('MIRANDA', ['Dc'], 'INTER', (3, 'y')),
            ('DE SILVESTRI', ['Dd', 'E'], 'TORINO', (5, 'y')),
            ('ANSALDI', ['Dd', 'Ds', 'E'], 'TORINO'),
            ('ASAMOAH', ['Ds', 'E'], 'JUVENTUS', (18, 'y')),
            ('CANNAVARO', ['Dc'], 'SASSUOLO'),
            ('TOMOVIC', ['Dd', 'Dc'], 'CHIEVO', (21, 'y')),
            ('JUAN JESUS', ['Ds', 'Dc'], 'ROMA', (19, 'y')),
            ('CESAR', ['Dc'], 'CHIEVO'),
            ('MATUIDI', ['M', 'C'], 'JUVENTUS', (17, 'n')),
            ('CRISTANTE', ['M', 'C'], 'ATALANTA', (16, 'y')),
            ('VECINO', ['M', 'C'], 'INTER', (7, 'y')),
            ('RADOVANOVIC', ['M', 'C'], 'CHIEVO'),
            ('HAMSIK', ['C', 'T'], 'NAPOLI', (8, 'y')),
            ('BONAVENTURA', ['C', 'W', 'T'], 'MILAN', (14, 'y')),
            ('BARAK', ['C', 'T'], 'UDINESE', (6, 'n')),
            ('BERNARDESCHI', ['W', 'A'], 'JUVENTUS', (9, 'y')),
            ('EYSSERIC', ['W', 'T'], 'FIORENTINA'),
            ('UNDER', ['W'], 'ROMA'),
            ('TAARABT', ['T', 'A'], 'GENOA', (13, 'y')),
            ('PALACIO', ['A'], 'BOLOGNA', (15, 'y')),
            ('FARIAS', ['A'], 'CAGLIARI', (11, 'y')),
            ('SAU', ['A'], 'CAGLIARI'),
            ('NIANG', ['A'], 'TORINO', (10, 'y')),
            ('IMMOBILE', ['Pc'], 'LAZIO'),
            ('ZAPATA D', ['Pc'], 'SAMPDORIA', (12, 'y'))]

mento = [('SPORTIELLO', ['Por'], 'FIORENTINA'),
         ('SORRENTINO', ['Por'], 'CHIEVO'),
         ('GOMIS A', ['Por'], 'SPAL'),
         ('ROMULO', ['Dd', 'E', 'M'], 'VERONA'),
         ('ACERBI', ['Dc'], 'SASSUOLO'),
         ('PEZZELLA GER', ['Dc'], 'FIORENTINA'),
         ('ALBIOL', ['Dc'], 'NAPOLI'),
         ('SILVESTRE', ['Dc'], 'SAMPDORIA'),
         ('BIRAGHI', ['Ds', 'E'], 'FIORENTINA'),
         ('PISACANE', ['Dd', 'Ds', 'Dc'], 'CAGLIARI'),
         ('HATEBOER', ['Dd', 'E'], 'ATALANTA'),
         ('ROSSETTINI', ['Dd', 'Dc'], 'GENOA'),
         ('SANTON', ['Dd', 'Ds', 'E'], 'INTER'),
         ('KHEDIRA', ['M', 'C'], 'JUVENTUS'),
         ('TORREIRA', ['M', 'C'], 'SAMPDORIA'),
         ('FOFANA', ['M', 'C'], 'UDINESE'),
         ('VIVIANI', ['M', 'C'], 'SPAL'),
         ('MANDRAGORA', ['M', 'C'], 'CROTONE'),
         ('RAMIREZ', ['W', 'T'], 'SAMPDORIA'),
         ('DE PAUL', ['W', 'T'], 'UDINESE'),
         ('GIL DIAS', ['W', 'A'], 'FIORENTINA'),
         ('NALINI', ['W', 'A'], 'CROTONE'),
         ('BIRSA', ['T'], 'CHIEVO'),
         ('JOAO PEDRO', ['T'], 'CAGLIARI'),
         ('INSIGNE', ['A'], 'NAPOLI'),
         ('ICARDI', ['Pc'], 'INTER'),
         ('LAPADULA', ['Pc'], 'GENOA'),
         ('PAVOLETTI', ['Pc'], 'CAGLIARI')]


def print_res(original, final_field, malus, efficient_module, adapted_module):
    # This is for printing the result. We initialize the final list. In this
    # list, only players with vote will be printed uppercase
    printed_lineup = []
    final_bench = []

    for player in original:
        if player[1] in [data[1] for data in final_field]:
            player_single_role = [new_player for new_player in final_field
                                  if new_player[1] == player[1]][0]
            printed_lineup.append((player[0], player[1],
                                   player_single_role[2]))
        else:
            new_tuple = (player[0], player[1].title(), player[2])
            printed_lineup.append(new_tuple)
            new_tuple = (player[0], player[1].upper(), player[2])
            final_bench.append(new_tuple)

    separator = '- - - - - - - - - - - - - -'
    printed_lineup.insert(11, separator)

    if not efficient_module and not adapted_module:
        print()
        print('Optimal solution found: module is {}'.format(module))
    elif efficient_module:
        print()
        print('Efficient solution found: module changed ' +
              'from {} to {}'.format(module, efficient_module))
    else:
        print()
        print('Adapted solution found: module changed ' +
              'from {} to {}'.format(module, adapted_module))
        print('Players with malus: {}'.format(malus))

    print()
    for element in printed_lineup:
        print(element)


def check_in_advance(module, fantateam):

    players_database = {player[0]: (99, 'no_team', random.randint(1, 10),
                        random.randint(1, 10))
                        for player in fantateam if (len(player) == 4 and
                                                    player[3][1] == 'y')}

    f = open('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/' +
             'votes/Day_99.pckl', 'wb')
    pickle.dump(players_database, f)
    f.close()

    fin_lineup = []
    for i in range(1, 24):
        for player in fantateam:
            try:
                if player[3][0] == i:
                    new_tuple = ('Day 99', player[0], player[1])
                    fin_lineup.append(new_tuple)
                    break
            except IndexError:
                continue

    try:
        (final_field, final_bench, malus, efficient_module,
         adapted_module) = ms.MANTRA_simulation(fin_lineup, module)
    except ValueError:
        final_field, final_bench, malus = ms.MANTRA_simulation(
                                                            fin_lineup, module)
        efficient_module = 0
        adapted_module = 0

    os.remove('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/' +
              'Day_99.pckl')

    print_res(fin_lineup, final_field, malus, efficient_module, adapted_module)


module = '433'
fantateam = pastaboy

check_in_advance(module, fantateam)
