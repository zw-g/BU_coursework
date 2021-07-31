import function
import  sys

class game:

    def __init__(self, name):
        self.turn_to_play = function.set_player(name)
        self.first_round = 0
        self.__name = name

    def start(self):
        __table = []

        # 洗牌
        card_list = function.shuffle()

        # 摸牌完毕 【0】= 庄家牌，【1】= 南， 【2】= 西， 【3】 = 北， 【4】=还没有抓的牌
        card_list = function.draw(card_list)
        deck = card_list.pop(4)

        #sort 牌
        card_list[0] = function.organize(card_list[0])
        card_list[1] = function.organize(card_list[1])
        card_list[2] = function.organize(card_list[2])
        card_list[3] = function.organize(card_list[3])
        #print(end='整理')
        #print(card_list)

        round_count = 0
        add = False
        skip = True
        while len(deck) != 0:
            action = []
            if (round_count)%4 == self.turn_to_play or round_count == self.turn_to_play:
                round_count += 1
                #human 人类
                if (self.turn_to_play != 0 or add) and skip:
                    #function.display(card_list[self.turn_to_play][0])
                    function.draw_one(card_list[self.turn_to_play][0], deck)
                else:
                    add = True
                    skip = True

                print(end='card in your hand：')
                function.display(card_list[self.turn_to_play][0])
                print('card you have Peng(杠), Gang(杠): ')

                try:
                    function.display(card_list[self.turn_to_play][1])
                except:
                    pass
                try:
                    function.display(card_list[self.turn_to_play][2])
                except:
                    pass
                try:
                    function.display(card_list[self.turn_to_play][3])
                except:
                    pass
                try:
                    function.display(card_list[self.turn_to_play][4])
                except:
                    pass

                # 摸牌杠 check
                #print(end='摸牌杠')
                if function.gang_check(card_list[self.turn_to_play][0], ''):
                    action.append(2)
                # 摸牌糊 check
                #print(end='摸牌糊')
                if function.hu_check(card_list[self.turn_to_play], ''):
                    action.append(3)
                # 七小对 check
                #print(end='七小对')
                if function.seven_pair(card_list[self.turn_to_play], ''):
                    action.append(3)

                print('action you could make: ')
                if 2 in action and 3 in action:
                    print('Gang(杠), Hu(糊)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'gang':
                        # move the gang card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop-1)
                        #becasue of gang they need to make sure +1 card
                        if len(deck) > 1:
                            card_list[self.turn_to_play][0].append(deck.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                    if user.lower() == 'hu':
                        # win!!!!
                        print('you win!!! with: ')
                        function.organize(card_list[self.turn_to_play])
                        function.display(card_list[self.turn_to_play][0])
                        print('card you have Peng(杠), Gang(杠): ')

                        try:
                            function.display(card_list[self.turn_to_play][1])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][2])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][3])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][4])
                        except:
                            pass
                        return False
                elif 2 in action:
                    print('Gang(杠)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'gang':
                        # move the gang card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop - 1)

                        # becasue of gang they need to make sure +1 card
                        if len(deck) > 1:
                            card_list[self.turn_to_play][0].append(deck.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                elif 3 in action:
                    print('Hu(糊)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'hu':
                        # win!!!!
                        print('you win!!! with: ')
                        function.organize(card_list[self.turn_to_play])
                        function.display(card_list[self.turn_to_play][0])
                        print('card you have Peng(杠), Gang(杠): ')

                        try:
                            function.display(card_list[self.turn_to_play][1])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][2])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][3])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][4])
                        except:
                            pass
                        return False
                else:
                    print('none')

                user = input('{} which card you like to play?'.format(self.__name))
                __table.append(function.play_one(card_list[self.turn_to_play][0], user.upper()))
                print('card played on the table(桌面): ')
                function.display(__table)

                print('')
            else:
                round_count += 1
                #robot 电脑

                # 庄家不摸一张牌
                if ((round_count)%4) != 0 or add:
                    function.draw_one(card_list[(round_count)%4][0], deck)
                else:
                    add = True
                #put draw card into user
                user = card_list[(round_count)%4][0][-1]
                #play the card
                __table.append(function.play_one(card_list[(round_count)%4][0], user))

                #print what computer played
                a = round_count%4
                if a == 0:
                    a = 4
                b = __table[-1]
                print ("computer {} played: {}".format(a, b))

                #shows whats on the table
                print('card played on the table(桌面): ')
                function.display(__table)

                # 碰 check
                #print(end='碰')
                if function.peng_check(card_list[self.turn_to_play][0], __table[-1]):
                    action.append(1)
                    #print(end='碰')

                # 打牌杠 check
                #print(end='打牌杠')
                if function.gang_check(card_list[self.turn_to_play][0], __table[-1]):
                    action.append(2)
                    #print(end='打牌杠')

                # 打牌糊 check
                #print(end='打牌糊')
                if function.hu_check(card_list[self.turn_to_play], __table[-1]):
                    action.append(3)
                    #print(end='打牌糊')

                # 点炮七小对 check
                #print(end='点炮七小对')
                if function.seven_pair(card_list[self.turn_to_play], __table[-1]):
                    action.append(3)
                    #print(end='点炮七小对')

                print('action you could make: ')
                if 1 in action and 2 in action and 3 in action:
                    print('Peng(碰), Gang(杠), Hu(糊)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'peng':
                        # move the peng card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        #recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                    if user.lower() == 'gang':
                        # move the gang card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # becasue of gang they need to make sure +1 card
                        if len(deck) > 1:
                            card_list[self.turn_to_play][0].append(deck.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                    if user.lower() == 'hu':
                        #win!!!!
                        print('you win!!! with: ')
                        card_list[self.turn_to_play][0].append(__table.pop(-1))
                        function.organize(card_list[self.turn_to_play])
                        function.display(card_list[self.turn_to_play][0])
                        print('card you have Peng(杠), Gang(杠): ')

                        try:
                            function.display(card_list[self.turn_to_play][1])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][2])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][3])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][4])
                        except:
                            pass
                        return False
                elif 1 in action and 2 in action:
                    print('Peng(碰), Gang(杠)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'peng':
                        # move the peng card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                    if user.lower() == 'gang':
                        # move the gang card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # becasue of gang they need to make sure +1 card
                        if len(deck) > 1:
                            card_list[self.turn_to_play][0].append(deck.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                elif 2 in action and 3 in action:
                    print('Gang(杠), Hu(糊)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'gang':
                        # move the gang card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # becasue of gang they need to make sure +1 card
                        if len(deck) > 1:
                            card_list[self.turn_to_play][0].append(deck.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                    if user.lower() == 'hu':
                        # win!!!!
                        print('you win!!! with: ')
                        card_list[self.turn_to_play][0].append(__table.pop(-1))
                        function.organize(card_list[self.turn_to_play])
                        function.display(card_list[self.turn_to_play][0])
                        print('card you have Peng(杠), Gang(杠): ')

                        try:
                            function.display(card_list[self.turn_to_play][1])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][2])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][3])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][4])
                        except:
                            pass
                        return False
                elif 1 in action and 3 in action:
                    print('Peng(碰), Hu(糊)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'peng':
                        # move the peng card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                    if user.lower() == 'hu':
                        # win!!!!
                        print('you win!!! with: ')
                        card_list[self.turn_to_play][0].append(__table.pop(-1))
                        function.organize(card_list[self.turn_to_play])
                        function.display(card_list[self.turn_to_play][0])
                        print('card you have Peng(杠), Gang(杠): ')

                        try:
                            function.display(card_list[self.turn_to_play][1])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][2])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][3])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][4])
                        except:
                            pass
                        return False
                elif 1 in action:
                    print('Peng(碰)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'peng':
                        # move the peng card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                elif 2 in action:
                    print('Gang(杠)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'gang':
                        # move the gang card to the list location
                        length = len(card_list[self.turn_to_play])
                        card_list[self.turn_to_play].append([])
                        for element in card_list[self.turn_to_play][0]:
                            if element == __table[-1]:
                                index = card_list[self.turn_to_play][0].index(element)
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                card_list[self.turn_to_play][length].append(card_list[self.turn_to_play][0].pop(index))
                                break
                        card_list[self.turn_to_play][length].append(__table.pop(-1))

                        # becasue of gang they need to make sure +1 card
                        if len(deck) > 1:
                            card_list[self.turn_to_play][0].append(deck.pop(-1))

                        # recurtion to the user to play a card
                        round_count = self.turn_to_play
                        skip = False
                elif 3 in action:
                    print('Hu(糊)')
                    print(end='card in your hand：')
                    function.display(card_list[self.turn_to_play][0])
                    user = input('{} would you like to perform any action?'.format(self.__name))
                    if user.lower() == 'hu':
                        # win!!!!
                        print('you win!!! with: ')
                        card_list[self.turn_to_play][0].append(__table.pop(-1))
                        function.organize(card_list[self.turn_to_play])
                        function.display(card_list[self.turn_to_play][0])
                        print('card you have Peng(杠), Gang(杠): ')

                        try:
                            function.display(card_list[self.turn_to_play][1])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][2])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][3])
                        except:
                            pass
                        try:
                            function.display(card_list[self.turn_to_play][4])
                        except:
                            pass
                        return False
                else:
                    print('none')
        if len(deck) == 0:
            print('tie no one win (平局)')
            return False
        '''
        #摸一张牌
        if self.turn_to_play != 0:
            function.draw_one(card_list[self.turn_to_play][0], deck)

        #摸牌杠 check
        print(end='摸牌杠')
        print(function.gang_check(card_list[self.turn_to_play][0], ''))


        #摸牌糊 check
        print(end='摸牌糊')
        print(function.hu_check(card_list[self.turn_to_play], ''))

        #七小对 check
        print(end='七小对')
        print(function.seven_pair(card_list[self.turn_to_play], ''))

        #打牌
        #user = input('which card to play: ')
        user = card_list[self.turn_to_play][0][-1]
        __table.append(function.play_one(card_list[self.turn_to_play][0], user))

        # 碰 check
        print(end='碰')
        print(function.peng_check(card_list[self.turn_to_play][0], __table[-1]))

        #打牌杠 check
        print(end='打牌杠')
        print(function.gang_check(card_list[self.turn_to_play][0], __table[-1]))

        #打牌糊 check
        print(end='打牌糊')
        print(function.hu_check(card_list[self.turn_to_play], __table[-1]))

        #点炮七小对 check
        print(end='点炮七小对')
        print(function.seven_pair(card_list[self.turn_to_play], __table[-1]))

        print(__table)
        function.display(card_list[self.turn_to_play][0])
        '''

    def ask(self):
        if (self.first_round != 0):
            user = input('\n{}, last game ends would you like to play another round?\n'.format(self.__name))
            if self.__check(user):
                return True
            else:
                return False
        else:
            self.first_round += 1
            return True

    def __check(self, user):
        user = user.lower()
        __yes_list = ['yes', 'sure', 'all right', 'alright', 'very well', 'of course', 'by all means', 'sure', 'certainly',
                  'absolutely', 'indeed', 'affirmative', 'in the affirmative', 'agreed', 'roger', 'aye', 'aye aye',
                  'yeah', 'yah', 'yep', 'yup', 'uh-huh', 'okay', 'ok', 'okey-dokey', 'okey-doke', 'achcha', 'righto',
                  'righty-ho', 'surely', 'k', 'y']
        __no_list = ['n', 'no', 'no indeed', 'absolutely not', 'most vertainly not', 'of course not',
                     'under no circumstances', 'by no means', 'not at all', 'negative', 'never', 'not really',
                     'no thanks', 'nae', 'nope', 'nah', 'not on your life', 'no way', 'no fear', 'not on your nelly',
                     'no siree', 'naw', 'nay']
        __yes_list = set(__yes_list)
        __no_list = set(__no_list)

        if user in __yes_list:
            return True
        elif user in __no_list:
            return False
        else:
            print('Wrong input ')
            print('if you want to play another game please enter:')
            for element in __yes_list:
                print(repr(element), end=', ')
            print('\nif you do not want to play another game please enter:')
            for element in __no_list:
                print(repr(element), end=', ')
            return self.ask()