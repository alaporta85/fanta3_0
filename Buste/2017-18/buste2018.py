import os
import copy
import pandas as pd
from tabulate import tabulate
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def number_of_falses():

    """Count the number of False in the dict containing all the data.
       Every time a player is assigned, the corresponding spot is replaced by
       a False.
       The process ends when all the spot are False. Ex: suppose the mail
       from Ciolle United is

       - MESSI, 80
       - RONALDO, 70
       - NEYMAR, 60

       If Ciolle United acquires MESSI, then the mail changes into

       - False
       - RONALDO, 70
       - NEYMAR, 60

       If MESSI is acquired from another team, than the mail from Ciolle United
       changes into

       - RONALDO, 70
       - NEYMAR, 60
       - False

       because Ciolle lost their priority so all the rest shifts up.
    """

    return len([el for team in all_data for el in all_data[team] if not el])


def final_sum(astring):

    """Return a tuple containing the money the team wants to use to pay the
       player.
       The input is a STRING like

           [VERDI(22), IMMOBILE(23), 13]

       Output is a TUPLE like

           (13, 45)

       where 13 is the cash and 45 is the money coming from selling players, in
       this case 22 + 23.
    """

    astring = astring.replace('[', '')
    astring = astring.replace(']', '')
    alist = astring.split(',')
    char = '0123456789'
    own_money = 0
    players_money = 0

    for el in alist:
        try:
            own_money += int(el)
        except ValueError:
            new = copy.copy(el)
            for letter in el:
                if letter not in char:
                    new = new.replace(letter, '')
            players_money += int(new)

    return own_money, players_money


def players_offered_to_pay(adict, team, astring):

    """Used to fill the dict players_used_to_pay. It contains all the players
       included in the offers as available to sell. If mail from Ciolle United
       is

           MESSI/40/[IMMOBILE(23), ZAPATA(5), 12]
           RONALDO/30/[IMMOBILE(23), 7]
           NEYMAR/25/[VERDI(13), 12]

       the dict will be

           players_used_to_pay = {Ciolle United: [IMMOBILE, ZAPATA, VERDI]}

       IMPORTANT: Each players appears only ONCE in the dict even if he is
       included in more offers, like IMMOBILE.

       This is used to check whether the team is able to buy the player or not.
    """

    char = '0123456789()'
    the_list = astring[1:-1].split(',')
    for el in the_list:
        new_el = copy.copy(el)
        for letter in el:
            if letter in char:
                new_el = new_el.replace(letter, '')

        temp = new_el.replace(' ', '').upper()
        if temp and team in adict and temp not in adict[team]:
            adict[team].append(temp)
        elif temp and team not in adict:
            adict[team] = [temp]


def create_data_dict():

    """Create the dict 'all_data' and for each team call the function
       'players_offered_to_pay' to fill the dict 'players_used_to_pay'.

       The dict 'all_data' contains all the offers, team by team, in order of
       priority.

       It also fill the dict 'mails_to_print' with the original offers.
    """

    all_data = {}
    players_used_to_pay = {}
    for filename in all_files:
        busta = []
        team = filename.split('_')[0]
        f = open(filename)
        content = f.readlines()
        f.close()
        for line in content:
            line = line.replace('\n', '')
            mails_to_print[team].append(line)
            nome = line.split('/')[0].upper()
            soldi = int(line.split('/')[1])
            players_offered_to_pay(players_used_to_pay, team,
                                   line.split('/')[2])
            payment = final_sum(line.split('/')[2])
            busta.append((nome, soldi, payment))
        all_data[team] = busta

    # In case the mail has less than 'max_players_per_mail' offers, it will be
    # completed by adding as many False as needed.
    for team in all_data:
        while len(all_data[team]) < max_players_per_mail:
            all_data[team].append(False)

    return all_data, players_used_to_pay


def are_players_available(team, player):

    """Check whether players included in the offer to pay the price are still
       available or not.
       This is to handle the cases where same players are used in more than one
       offer to avoid using them more than once.
       Return True is offer is valid, False otherwise.
    """

    char = '0123456789()'
    fin_list = []
    f = open('{}_{}.txt'.format(team, times[team]))
    content = f.readlines()
    f.close()

    for line in content:
        line = line.replace('\n', '')
        nome = line.split('/')[0].upper()
        if nome == player:
            the_list = line.split('/')[2][1:-1].split(',')
            break

    for el in the_list:
        new_el = copy.copy(el)
        for letter in el:
            if letter in char:
                new_el = new_el.replace(letter, '')
        temp = new_el.replace(' ', '')
        if temp:
            fin_list.append(temp.upper())

    check = set(fin_list).intersection(players_used_to_pay[team])
    if len(check) == len(fin_list):
        for player in fin_list:
            players_used_to_pay[team].remove(player)
        return True
    else:
        return False


def shiftup_and_complete(team, player):

    """Shift all the priorities up deleting the offers for the player 'player'
       and add False entries to complete the data relative to the team 'team'.
    """

    all_data[team] = [el for el in all_data[team] if not el or
                      el[0] != player]
    while len(all_data[team]) < max_players_per_mail:
        all_data[team].append(False)


def assign_player(candidates):

    """Assign the players to the right team according to the rules."""

    players_in_priority = [(name, all_data[name][priority], times[name]) for
                           name in candidates if all_data[name][priority]]
    try:
        player_to_call = sorted(sorted(players_in_priority,
                                       key=lambda x: x[2]),
                                key=lambda x: x[1][1], reverse=True)[0]
    except IndexError:
        return

    team_calling = player_to_call[0]
    player_name = player_to_call[1][0]
    price = player_to_call[1][1]
    money_available = money_left[team_calling] + player_to_call[1][2][1]
    players_to_sell = are_players_available(team_calling, player_name)

    if price <= money_available and players_to_sell:
        res[team_calling].append((player_name, price))
        all_data[team_calling][priority] = False
        money_left[team_calling] = money_available - price
        for name in all_data:
            shiftup_and_complete(name, player_name)
    else:
        shiftup_and_complete(team_calling, player_name)
        return assign_player(candidates)


priority = 0
max_players_per_mail = 5
last_name = ''
money_left = {'Giochici Giochici Stars': 20, 'Bucalina FC': 21,
              'Ciolle United': 23, 'FC Pastaboy': 48, 'FC ROXY': 20,
              'AC PICCHIA': 156, 'Fc Stress': 20, 'FC BOMBAGALLO': 29}

all_files = sorted([filename for filename in os.listdir() if
                    filename.endswith('.txt')],
                   key=lambda x: x.split('_')[1][:-4])

times = {filename.split('_')[0]: filename.split('_')[1][:-4] for filename in
         all_files}

ordered_by_time = [filename.split('_')[0] for filename in all_files]
res = {name: [] for name in ordered_by_time}

mails_to_print = {name: [] for name in money_left}
all_data, players_used_to_pay = create_data_dict()
for name in mails_to_print:
    while len(mails_to_print[name]) < max_players_per_mail:
        mails_to_print[name].append('')

n_falses = number_of_falses()

spots_to_fill = len(ordered_by_time) * max_players_per_mail

while n_falses < spots_to_fill:

    candidates = [name for name in ordered_by_time if all_data[name][priority]]

    if not candidates:
        priority += 1
        continue

    assign_player(candidates)
    n_falses = number_of_falses()

# To print the results
max_players_acquired = max([len(res[name]) for name in res])
four_names = ['Ciolle United', 'FC Pastaboy', 'FC ROXY', 'AC PICCHIA']
dict1 = {name: mails_to_print[name] for name in four_names}
dict2 = {name: mails_to_print[name] for name in res if name not in four_names}

for team in res:
    while len(res[team]) < max_players_acquired:
        res[team].append('')


table1 = tabulate(pd.DataFrame(dict1), showindex=False, headers='keys',
                  tablefmt="orgtbl", stralign='center')
table2 = tabulate(pd.DataFrame(dict2), showindex=False, headers='keys',
                  tablefmt="orgtbl", stralign='center')
table3 = tabulate(pd.DataFrame(res), showindex=False, headers='keys',
                  tablefmt="orgtbl", stralign='center')
table4 = tabulate(pd.DataFrame(money_left, index=[0]), showindex=False,
                  headers='keys', tablefmt="orgtbl", numalign='center')

print('\n\n\nBUSTE ORIGINALI:\n')
print(table1)
print('\n\n')
print(table2)
print('\n\n\nESITO BUSTE:\n')
print(table3)
print('\n\n\nSOLDI RIMANENTI:\n')
print(table4)
