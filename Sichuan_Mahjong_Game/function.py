import random

chinese_dic = {
    'A1': '一萬',
    'A2': '二萬',
    'A3': '三萬',
    'A4': '四萬',
    'A5': '五萬',
    'A6': '六萬',
    'A7': '七萬',
    'A8': '八萬',
    'A9': '九萬',
    'B1': '一索',
    'B2': '二索',
    'B3': '三索',
    'B4': '四索',
    'B5': '五索',
    'B6': '六索',
    'B7': '七索',
    'B8': '八索',
    'B9': '九索',
    'C1': '一筒',
    'C2': '二筒',
    'C3': '三筒',
    'C4': '四筒',
    'C5': '五筒',
    'C6': '六筒',
    'C7': '七筒',
    'C8': '八筒',
    'C9': '九筒'
}

def roll():
    two_dice = []
    two_dice.append(random.randint(1, 6))
    two_dice.append(random.randint(1, 6))
    #(dice one , dice two)
    return two_dice

def set_player(name):
    print("rolling the dice to decided who is the 东, (player who plays first)")

    thisdict = {
        name : 0,
        "computer_one": 0,
        "computer_two": 0,
        "computer_three": 0
    }

    user = roll()
    computer_one = roll()
    computer_two = roll()
    computer_three = roll()

    print(
        'your dice result is: {}\ncomputer one result is: {}\ncomputer two result is: {}\ncomputer three result is: {}\n'.format(
            user, computer_one, computer_two, computer_three))

    thisdict[name] = (user[0] + user[1])
    thisdict["computer_one"] = (computer_one[0] + computer_one[1])
    thisdict["computer_two"] = (computer_two[0] + computer_two[1])
    thisdict["computer_three"] = (computer_three[0] + computer_three[1])
    thisdict = dict(sorted(thisdict.items(), key=lambda item: item[1], reverse=True))

    temp = list(thisdict.items())
    count = int(str([idx for idx, key in enumerate(temp) if key[0] == name]).strip('[]'))


    print('{} will be the {} player to play\n'.format(name, count+1))

    return count

def shuffle():
    list_cards = ['A1', 'A1', 'A1', 'A1', 'A2', 'A2', 'A2', 'A2', 'A3', 'A3', 'A3', 'A3', 'A4', 'A4', 'A4', 'A4', 'A5',
                  'A5', 'A5', 'A5', 'A6', 'A6', 'A6', 'A6', 'A7', 'A7', 'A7', 'A7', 'A8', 'A8', 'A8', 'A8', 'A9', 'A9',
                  'A9', 'A9', 'B1', 'B1', 'B1', 'B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3', 'B3', 'B4', 'B4', 'B4',
                  'B4', 'B5', 'B5', 'B5', 'B5', 'B6', 'B6', 'B6', 'B6', 'B7', 'B7', 'B7', 'B7', 'B8', 'B8', 'B8', 'B8',
                  'B9', 'B9', 'B9', 'B9', 'C1', 'C1', 'C1', 'C1', 'C2', 'C2', 'C2', 'C2', 'C3', 'C3', 'C3', 'C3', 'C4',
                  'C4', 'C4', 'C4', 'C5', 'C5', 'C5', 'C5', 'C6', 'C6', 'C6', 'C6', 'C7', 'C7', 'C7', 'C7', 'C8', 'C8',
                  'C8', 'C8', 'C9', 'C9', 'C9', 'C9']
    random.shuffle(list_cards)
    return list_cards

def draw(card_list):
    draw_list = [[[]] for _ in range(4)]
    #print(draw_list)

    #甩色子：由庄家掷两枚骰子以确定端牌的起始位置。
    dice = roll()
    if dice[0] < dice[1]:
        dice = dice[0]
    else:
        dice = dice[1]
    for _ in range(dice*2):
        card_list.append(card_list.pop(0))

    #发牌
    for n in range (3):
        for x in range (4):
            if x == 0:
                for y in range (4):
                    draw_list[0][0].append(card_list.pop(0))
            if x == 1:
                for y in range (4):
                    draw_list[1][0].append(card_list.pop(0))
            if x == 2:
                for y in range (4):
                    draw_list[2][0].append(card_list.pop(0))
            if x == 3:
                for y in range (4):
                    draw_list[3][0].append(card_list.pop(0))
    draw_list[0][0].append(card_list.pop(0))
    draw_list[0][0].append(card_list.pop(3))
    draw_list[1][0].append(card_list.pop(0))
    draw_list[2][0].append(card_list.pop(0))
    draw_list[3][0].append(card_list.pop(0))
    draw_list.append(card_list)

    #print(draw_list)
    #print(draw_list[1])
    #print(draw_list[2])
    #print(draw_list[3])
    #发牌完毕， 【0】= 庄家牌，【1】= 南， 【2】= 西， 【3】 = 北， 【4】=还没有抓的牌
    return draw_list

def display(deck):
    for x in range (len(deck)):
        print(end='|{}({})'.format(chinese_dic[deck[x]], deck[x]))
    print ('|')

def organize(cards):
    for element in cards:
        element.sort()
    return cards

def draw_one(player,deck):
    player.append(deck.pop(0))

def play_one(player,play):
    for element in player:
        if element == play:
            return player.pop(player.index(element))

def peng_check(player, card):
    count = 0
    for element in player:
        if element == card:
            count += 1
    if count > 1:
        return True
    else:
        return False

def gang_check(player, card):
    count = 0
    if card != '':
        for element in player:
            if element == card:
                count += 1
        #print(count)
        if count > 2:
            return True
        else:
            return False
    else:
        for element in player:
            if element == player[-1]:
                count += 1
        if count > 3:
            return True
        else:
            return False

def hu_check(player, card):
    temp = []
    if card == '':
        card_temp = str(player[0][-1])
        if len(player) == 1:
            if len(player[0]) == 14:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        #print('1')
                                        #print(str(temp[0]))
                                        #print(card_temp)
                                        #print(str(temp[0]) == card_temp)
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                return False
        elif len(player) == 2:
            if len(player[0]) == 11:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                return False
        elif len(player) == 3:
            if len(player[0]) == 8:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                return False
        elif len(player) == 4:
            if len(player[0]) == 5:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                return False
        #对对胡剩两张
        elif len(player) == 5:
            if len(player[0]) == 2:
                if player[0][0] == player[0][1]:
                    return True
        else:
            return False
    else:
        player[0].append(card)
        card_temp = str(player[0][-1])
        if len(player) == 1:
            if len(player[0]) == 14:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                    player[0].pop(-1)
                return False
        elif len(player) == 2:
            if len(player[0]) == 11:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                    player[0].pop(-1)
                return False
        elif len(player) == 3:
            if len(player[0]) == 8:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                    player[0].pop(-1)
                return False
        elif len(player) == 4:
            if len(player[0]) == 5:
                # 检查对子
                j = 1
                player = organize(player)
                while j < len(player[0]):
                    # check pair
                    if player[0][j - 1] == player[0][j]:
                        temp.append(player[0].pop(j - 1))
                        temp.append(player[0].pop(j - 1))
                        x = 0
                        while x < (len(player[0]) / 3):
                            # 检查连牌
                            if player[0][0][0] == player[0][1][0] and player[0][1][0] == player[0][2][0] and int(
                                    player[0][0][1]) + 1 == int(player[0][1][1]) and int(player[0][1][1]) + 1 == int(
                                player[0][2][1]):
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            elif player[0][0] == player[0][1] and player[0][1] == player[0][2]:
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                temp.append(player[0].pop(0))
                                if len(player[0]) == 0:
                                    while (len(temp)) > 1:
                                        if str(temp[0]) == card_temp:
                                            player[0].append(temp.pop(1))
                                        else:
                                            player[0].append(temp.pop(0))
                                    player = organize(player)
                                    player[0].append(temp.pop(0))
                                    player[0].pop(-1)
                                    return True
                            else:
                                for x in range(len(temp) - 2):
                                    player[0].append(temp.pop(0))
                                player = organize(player)
                                j += 1
                                x += 1
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                    else:
                        for x in range(len(temp)):
                            player[0].append(temp.pop(0))
                        player = organize(player)
                        j += 1
                if len(temp) != 0:
                    check = False
                    for element in temp:
                        if str(element) == card_temp:
                            check = True
                    if check:
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                    else:
                        index = player[0].index(card_temp)
                        temp.append(player[0].pop(index))
                        while (len(temp)) > 1:
                            if str(temp[0]) == card_temp:
                                player[0].append(temp.pop(1))
                            else:
                                player[0].append(temp.pop(0))
                        player = organize(player)
                        player[0].append(temp.pop(0))
                        player[0].pop(-1)
                else:
                    index = player[0].index(card_temp)
                    temp.append(player[0].pop(index))
                    player = organize(player)
                    player[0].append(temp.pop(0))
                    player[0].pop(-1)
                return False
        # 对对胡剩两张
        elif len(player) == 5:
            if len(player[0]) == 2:
                if player[0][0] == player[0][1]:
                    return True
        else:
            return False

def seven_pair(player, card):
    temp = []
    if card == '':
        if len(player) == 1:
            if len(player[0]) == 14:
                count = 0
                x = 0
                while x < (13):
                    if player[0][x] == player[0][x+1]:
                        count += 1
                        x += 2
                    elif player[0][x] == player[0][-1]:
                        count += 1
                        x += 1
                    else:
                        return False
                if count == 7:
                    return True
    else:
        if len(player) == 1:
            if len(player[0]) == 13:
                count = 0
                x = 0
                while x < (12):
                    if player[0][x] == player[0][x + 1]:
                        count += 1
                        x += 2
                    elif player[0][x] == card[0]:
                        count += 1
                        x += 1
                    else:
                        return False
                if count == 7:
                    return True
    return False