import random
import MANTRA_functions as ms
import pickle
import os

f = open('/Users/andrea/Desktop/fanta3_0/all_players_per_fantateam/' +
         'fantaplayers/fantaplayers_27.pckl', 'rb')
rose = pickle.load(f)
f.close()


bombagall = [('DONNARUMMA G', ['Por'], 'MILAN', (1, 'y')),
             ('DONNARUMMA A', ['Por'], 'MILAN', (23, 'y')),
             ('STORARI', ['Por'], 'MILAN', (22, 'y')),
             ('MASIELLO A', ['Dd', 'Dc'], 'ATALANTA', (4, 'n')),
             ("N'KOULOU", ['Dc'], 'TORINO', (3, 'y')),
             ('CACERES', ['Dd', 'Dc'], 'LAZIO', (19, 'n')),
             ('PELUSO', ['Ds', 'Dc'], 'SASSUOLO', (2, 'y')),
             ('MASINA', ['Ds', 'E'], 'BOLOGNA'),
             ('BASTA', ['Dd', 'E'], 'LAZIO', (18, 'n')),
             ('CALABRIA', ['Dd', 'E'], 'MILAN', (5, 'y')),
             ('WALLACE', ['Dc'], 'LAZIO', (20, 'n')),
             ('BADELJ', ['M', 'C'], 'FIORENTINA', (7, 'y')),
             ('DUNCAN', ['M', 'C'], 'SASSUOLO', (17, 'y')),
             ('LOCATELLI M', ['M', 'C'], 'MILAN'), (16, 'n'),
             ('PJANIC', ['C', 'T'], 'JUVENTUS', (6, 'y')),
             ('MILINKOVIC-SAVIC', ['C', 'T'], 'LAZIO', (8, 'y')),
             ('BORJA VALERO', ['C', 'T'], 'INTER', (9, 'y')),
             ('BASELLI', ['C'], 'TORINO', (15, 'y')),
             ('PELLEGRINI', ['C'], 'ROMA'),
             ('FELIPE ANDERSON', ['W', 'A'], 'LAZIO', (12, 'y')),
             ('SUSO', ['T', 'A'], 'MILAN', (11, 'y')),
             ('GOMEZ A', ['A'], 'ATALANTA', (10, 'y')),
             ('THEREAU', ['A'], 'FIORENTINA', (14, 'n')),
             ('CERCI', ['A'], 'VERONA', (21, 'n')),
             ('KALINIC', ['Pc'], 'MILAN', (13, 'n')),
             ('LASAGNA', ['Pc'], 'UDINESE')]

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
 ('SKORUPSKI', ['Por'], 'ROMA', (22, 'y')),
 ('LOBONT', ['Por'], 'ROMA', (23, 'y')),
 ('KOULIBALY', ['Dc'], 'NAPOLI', (3, 'y')),
 ('SKRINIAR', ['Dc'], 'INTER', (4, 'y')),
 ('KOLAROV', ['Ds', 'E'], 'ROMA', (17, 'y')),
 ('HYSAJ', ['Dd', 'Ds', 'E'], 'NAPOLI', (18, 'y')),
 ('PADOIN', ['Dd', 'E', 'M'], 'CAGLIARI', (19, 'y')),
 ('CANCELO', ['Dd', 'E'], 'INTER', (5, 'y')),
 ('BURDISSO', ['Dc'], 'TORINO'),
 ('CONTI', ['Dd', 'E'], 'MILAN'),
 ('RANOCCHIA', ['Dc'], 'INTER', (20, 'n')),
 ('CASTAN', ['Dc'], 'CAGLIARI', (2, 'y')),
 ('LYANCO', ['Dc'], 'TORINO'),
 ('CHIRICHES', ['Dc'], 'NAPOLI'),
 ('TONELLI', ['Dc'], 'NAPOLI', (21, 'n')),
 ('RINCON', ['M', 'C'], 'TORINO'),
 ('MARCHISIO', ['M', 'C'], 'JUVENTUS', (16, 'n')),
 ('JANKTO', ['E', 'C'], 'UDINESE', (8, 'y')),
 ('HETEMAJ', ['E', 'M'], 'CHIEVO', (15, 'y')),
 ('MILINKOVIC-SAVIC', ['C', 'T'], 'LAZIO', (7, 'y')),
 ('DZEMAILI', ['C', 'T'], 'BOLOGNA', (6, 'y')),
 ('LINETTY', ['C'], 'SAMPDORIA', (14, 'n')),
 ('GIACCHERINI', ['W', 'T'], 'CHIEVO'),
 ('VERDI', ['T', 'A'], 'BOLOGNA', (9, 'y')),
 ('ILICIC', ['T', 'A'], 'ATALANTA', (13, 'n')),
 ('BELOTTI', ['Pc'], 'TORINO', (11, 'y')),
 ('CORNELIUS', ['Pc'], 'ATALANTA', (12, 'n')),
 ('KEAN', ['Pc'], 'VERONA', (10, 'n'))]

pastaboy = [('SIRIGU', ['Por'], 'TORINO', (1, 'y')),
            ('CONSIGLI', ['Por'], 'SASSUOLO'),
 ('BERISHA', ['Por'], 'ATALANTA', (24, 'y')),
 ('ALEX SANDRO', ['Ds', 'E'], 'JUVENTUS', (5, 'y')),
 ('BONUCCI', ['Dc'], 'MILAN', (4, 'y')),
 ('DE SILVESTRI', ['Dd', 'E'], 'TORINO', (23, 'y')),
 ('FAZIO', ['Dc'], 'ROMA', (3, 'y')),
 ("D'AMBROSIO", ['Dd', 'Ds', 'E'], 'INTER', (21, 'y')),
 ('MIRANDA', ['Dc'], 'INTER', (2, 'y')),
 ('ANSALDI', ['Dd', 'Ds', 'E'], 'TORINO'),
 ('DE MAIO', ['Dc'], 'BOLOGNA'),
 ('TOMOVIC', ['Dd', 'Dc'], 'CHIEVO', (20, 'y')),
 ('ASAMOAH', ['Ds', 'E'], 'JUVENTUS'),
 ('LISANDRO LOPEZ', ['Dc'], 'INTER'),
 ('JUAN JESUS', ['Ds', 'Dc'], 'ROMA'),
 ('MATUIDI', ['M', 'C'], 'JUVENTUS', (18, 'y')),
 ('CRISTANTE', ['M', 'C'], 'ATALANTA', (7, 'y')),
 ('VECINO', ['M', 'C'], 'INTER', (17, 'n')),
 ('RADOVANOVIC', ['M', 'C'], 'CHIEVO', (16, 'y')),
 ('HAMSIK', ['C', 'T'], 'NAPOLI', (6, 'y')),
 ('BONAVENTURA', ['C', 'W', 'T'], 'MILAN', (8, 'y')),
 ('BARAK', ['C', 'T'], 'UDINESE', (15, 'y')),
 ('BENASSI', ['C'], 'FIORENTINA', (19, 'y')),
 ('BERNARDESCHI', ['W', 'A'], 'JUVENTUS'),
 ('UNDER', ['W'], 'ROMA', (9, 'n')),
 ('TAARABT', ['T', 'A'], 'GENOA'),
 ('PALACIO', ['A'], 'BOLOGNA'),
 ('NIANG', ['A'], 'TORINO', (14, 'y')),
 ('IMMOBILE', ['Pc'], 'LAZIO', (10, 'y')),
 ('ZAPATA D', ['Pc'], 'SAMPDORIA', (12, 'y')),
 ('BABACAR', ['Pc'], 'SASSUOLO', (13, 'y')),
 ('CODA M', ['Pc'], 'BENEVENTO', (11, 'y'))]

mento = [('PERIN', ['Por'], 'GENOA', (1, 'y')),
 ('SPORTIELLO', ['Por'], 'FIORENTINA'),
 ('SORRENTINO', ['Por'], 'CHIEVO', (12, 'y')),
 ('SILVESTRE', ['Dc'], 'SAMPDORIA', (20, 'n')),
 ('ROMULO', ['Dd', 'E', 'M'], 'VERONA', (19, 'y')),
 ('ALBIOL', ['Dc'], 'NAPOLI', (3, 'y')),
 ('PEZZELLA GER', ['Dc'], 'FIORENTINA'),
 ('RODRIGUEZ R', ['Ds', 'E'], 'MILAN', (8, 'y')),
 ('ACERBI', ['Dc'], 'SASSUOLO', (4, 'y')),
 ('BIRAGHI', ['Ds', 'E'], 'FIORENTINA', (21, 'n')),
 ('HATEBOER', ['Dd', 'E'], 'ATALANTA', (22, 'y')),
 ('SPOLLI', ['Dc'], 'GENOA'),
 ('ADNAN', ['Ds', 'E'], 'UDINESE', (5, 'y')),
 ('PISACANE', ['Dd', 'Ds', 'Dc'], 'CAGLIARI', (2, 'y')),
 ('KHEDIRA', ['M', 'C'], 'JUVENTUS', (6, 'y')),
 ('TORREIRA', ['M', 'C'], 'SAMPDORIA', (17, 'y')),
 ('PULGAR', ['M', 'C'], 'BOLOGNA'),
 ('VIVIANI', ['M', 'C'], 'SPAL', (7, 'n')),
 ('BARBERIS', ['M', 'C'], 'CROTONE', (18, 'y')),
 ('RAMIREZ', ['W', 'T'], 'SAMPDORIA'),
 ('DE PAUL', ['W', 'T'], 'UDINESE', (9, 'n')),
 ('NALINI', ['W', 'A'], 'CROTONE', (16, 'y')),
 ('GIL DIAS', ['W', 'A'], 'FIORENTINA', (15, 'y')),
 ('BIRSA', ['T'], 'CHIEVO', (23, 'y')),
 ('JOAO PEDRO', ['T'], 'CAGLIARI'),
 ('INSIGNE', ['A'], 'NAPOLI', (14, 'y')),
 ('PANDEV', ['A'], 'GENOA', (10, 'y')),
 ('ICARDI', ['Pc'], 'INTER', (11, 'y')),
 ('PAVOLETTI', ['Pc'], 'CAGLIARI', (13, 'y'))]


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
         adapted_module) = ms.mantra_simulation(fin_lineup, module)
    except ValueError:
        final_field, final_bench, malus = ms.mantra_simulation(
                                                            fin_lineup, module)
        efficient_module = 0
        adapted_module = 0

    os.remove('/Users/andrea/Desktop/fanta3_0/cday_lineups_votes/votes/' +
              'Day_99.pckl')

    print_res(fin_lineup, final_field, malus, efficient_module, adapted_module)


module = '3412'
fantateam = mento

check_in_advance(module, fantateam)
