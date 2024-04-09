# Part of case-study #2: Last of us
# Developer: Kosheleva Ann
#            Rusakova Margarita
#
# Description: This program contains participation of three teams.
# Their task is not to lose all their resources and strengthen their power during the gameplay.
import random

import ru_local as ru


def main():
    # Here we show the main task.
    print(ru.CHOICE)
    # Here we ask the players which team they prefer to represent in the game.
    choice_1 = int(input(f'{ru.FIRST_TEAM}'))
    choice_2 = int(input(f'{ru.SECOND_TEAM}'))
    team_1 = [50] * 5
    team_2 = [100] * 5
    team_3 = [200] * 5

    def first_team():
        """
        The first team function
        :return: return list(zip(ru.STOCK, team_1))
        """
        a = [1, 2, 3, 4, 5]
        random_nmr_1 = random.choice(a)

        def event_1_1(answer):
            """
            The event_1_1 function
            :param answer: yes or no
            :return: return list(zip(ru.STOCK, team_1))
            """
            if answer == 'да':
                team_1[3] -= 5
                team_1[1] += 100
                # Here we show the result of actions happening after choosing yes as an answer.
                print(ru.EVENT_1_1_YES)
            else:
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_1_1_NO)

            return list(zip(ru.STOCK, team_1))

        def event_1_2(answer):
            """
            The event_1_2 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_1))
            """
            if answer == 'да':
                team_1[2] -= 10
                team_1[4] += 20
                # Here we show the result of actions happening after choosing yes as an answer.
                print(ru.EVENT_1_2_YES)
            else:
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_1_2_NO)

            return list(zip(ru.STOCK, team_1))

        def event_1_3(answer):
            """
            The event_1_3 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_1))
            """
            if answer == 'да':
                # Here we show the result of actions happening after choosing yes as an answer.
                print(ru.EVENT_1_3_YES)
            else:
                team_1[3] -= 20
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_1_3_NO)

            return list(zip(ru.STOCK, team_1))

        def event_1_4(answer):
            """
            The event_1_4 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_1))
            """
            if answer == 'да':
                team_2[3] -= 50
                team_1[4] -= 100
                # Here we show the result of actions happening after choosing yes as an answer.
                print(ru.EVENT_1_4_YES)
            else:
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_1_4_NO)

            return list(zip(ru.STOCK, team_1))

        match random_nmr_1:
            case 1:
                # Here we output an independent event when number one is selected by the random number generator.
                print(ru.EVENT_1_1)
                print(event_1_1(input()))
            case 2:
                # Here we output an independent event when number two is selected by the random number generator.
                print(ru.EVENT_1_2)
                print(event_1_2(input()))
            case 3:
                # Here we output an independent event when number three is selected by the random number generator.
                print(ru.EVENT_1_3)
                print(event_1_3(input()))
            case 4:
                # Here we output an independent event when number four is selected by the random number generator.
                print(ru.EVENT_1_4)
                print(event_1_4(input()))
            case _:
                # Here we output an independent event when number zero is selected by the random number generator.
                print(ru.EVENT_1_0)

        choice = [1, 2, 3, 4]
        # Here we show the list of citizens with complaints that can be resolved.
        print(ru.CITIZENS_COMPLAINTS)
        # Here we make a dictionary of citizens and their complaints, so the player can choose rather help them or not.
        print(list(zip(ru.CITIZENS_1, ru.COMPLAINTS)))

        complaints_list = []
        for k in range(len(ru.CITIZENS_1)):
            complaints = input(f'{ru.HELP} {ru.CITIZENS_1[k]}')
            complaints_list.append(complaints)

        new_citizens_list = []
        new_complaints_list = []

        for t in range(len(complaints_list)):
            if complaints_list[t] != 'да':
                new_citizens_list.append(ru.CITIZENS_1[t])
                new_complaints_list.append(ru.COMPLAINTS[t])

        for k in range(len(complaints_list)):
            if complaints_list[k] == 'да':
                complaints_list[k] = '1'
            else:
                complaints_list[k] = '0'
        for choice, complaints_list in zip(choice, complaints_list):
            match choice:
                case 1:
                    team_1[2] -= 10 * int(complaints_list)
                case 2:
                    team_1[2] -= 5 * int(complaints_list)
                case 3:
                    team_1[2] -= 20 * int(complaints_list)
                case 4:
                    team_1[0] -= 20 * int(complaints_list)

        a.pop(random_nmr_1 - 1)

        return list(zip(ru.STOCK, team_1))

    def second_team():
        """
        The second team function
        :return: return list(zip(ru.STOCK, team_2))
        """
        c = [1, 2, 3, 4, 5]
        b = [1, 2]
        d = [1, 2]
        random_nmr_2 = random.choice(c)

        def event_2_1(answer):
            """
            The event_2_1 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_2))
            """
            team_2[2] -= 20
            team_2[4] -= 10
            if answer == 'да':
                team_2[2] -= 10
                # Here we show the result of actions happening after choosing yes as an answer.
                print(ru.EVENT_2_1_YES)
            else:
                team_2[2] -= 25
                team_2[4] -= 5
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_2_1_NO)

            return list(zip(ru.STOCK, team_2))

        def event_2_2(answer):
            """
            The event_2_2 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_2))
            """
            if answer == 'да':
                random_nmr_3 = random.choice(b)
                if random_nmr_3 == 1:
                    team_2[0] -= 30
                    # Here we show the result of the first random event happening after choosing yes as an answer.
                    print(ru.EVENT_2_2_FIRST_YES)
                else:
                    team_2[0] -= 30
                    # Here we show the result of the second random event happening after choosing yes as an answer.
                    print(ru.EVENT_2_2_SECOND_YES)
            else:
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_2_2_NO)

            return list(zip(ru.STOCK, team_2))

        def event_2_3(answer):
            """
            The event_2_3 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_2))
            """
            if answer == 'да':
                random_nmr_4 = random.choice(d)
                if random_nmr_4 == 1:
                    team_2[3] -= 20
                    # Here we show the result of the first random event happening after choosing yes as an answer.
                    print(ru.EVENT_2_3_FIRST_YES)
                else:
                    team_2[2] += 40
                    team_2[0] += 60
                    # Here we show the result of the second random event happening after choosing yes as an answer.
                    print(ru.EVENT_2_3_SECOND_YES)
            else:
                team_2[2] -= 20
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_2_3_NO)

            return list(zip(ru.STOCK, team_2))

        match random_nmr_2:
            case 1:
                # Here we output an independent event when number one is selected by the random number generator.
                print(ru.EVENT_2_1)
                print(event_2_1(input()))
            case 2:
                # Here we output an independent event when number two is selected by the random number generator.
                print(ru.EVENT_1_2)
                print(event_2_2(input()))
            case 3:
                # Here we output an independent event when number three is selected by the random number generator.
                print(ru.EVENT_2_3)
                print(event_2_3(input()))
            case _:
                # Here we output an independent event when number zero is selected by the random number generator.
                print(ru.EVENT_2_0)

        # Here we show the variety of weapons that can be sold to earn some money.
        print(ru.AUCTION)
        auction_list = []
        act_choice = [1, 2, 3, 4, 5]
        for k in range(1, 6):
            people = int(input(f'{ru.AUCTION_1[k - 1]}'))
            auction_list.append(people)

        for act_choice, auction_list in zip(act_choice, auction_list):
            match act_choice:
                case 1 | 3:
                    team_2[0] += 13 * auction_list
                case 2:
                    team_2[0] += 40 * auction_list
                case 4:
                    team_2[0] += 50 * auction_list
                case 5:
                    team_2[0] += 29 * auction_list
        if int(team_2[0]) > 100000:
            team_2[0] = 100
            team_2[1] -= 10
            team_2[2] -= 10
            team_2[3] -= 10
            team_2[4] -= 10
            # Here we show the action happening as a consequence of trying to sell too much weapons to the potential
            # enemies.
            print(f'{ru.ADD_PROBLEM}')
        c.pop(random_nmr_2 - 1)
        return list(zip(ru.STOCK, team_2))

    def third_team():
        """
        The third team function
        :return: return list(zip(ru.STOCK, team_3))
        """
        e = [1, 2, 3, 4, 5]
        f = [1, 2]
        g = [1, 2]
        j = [1, 2]
        random_nmr_5 = random.choice(e)

        def event_3_1(answer):
            """
            The event_3_1 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_3))
            """
            team_3[2] -= 20
            team_3[4] -= 10
            if answer == 'да':
                random_nmr_6 = random.choice(j)
                if random_nmr_6 == 1:
                    team_3[2] -= 50
                    # Here we show the result of the first random event happening after choosing yes as an answer.
                    print(ru.EVENT_3_1_FIRST_YES)
                else:
                    team_3[2] -= 50
                    team_3[3] -= 20
                    # Here we show the result of the second random event happening after choosing yes as an answer.
                    print(ru.EVENT_3_1_SECOND_YES)
            else:
                random_nmr_6 = random.choice(j)
                if random_nmr_6 == 1:
                    team_3[2] -= 50
                    # Here we show the result of the first random event happening after choosing no as an answer.
                    print(ru.EVENT_3_1_FIRST_NO)
                else:
                    # Here we show the result of the second random event happening after choosing no as an answer.
                    print(ru.EVENT_3_1_SECOND_NO)

            return list(zip(ru.STOCK, team_3))

        def event_3_2(answer):
            """
            The event_3_2 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_3))
            """
            if answer == 'да':
                random_nmr_7 = random.choice(f)
                if random_nmr_7 == 1:
                    team_3[0] -= 50
                    # Here we show the result of the first random event happening after choosing yes as an answer.
                    print(ru.EVENT_3_2_FIRST_YES)
                else:
                    team_3[0] -= 50
                    team_3[3] -= 3
                    # Here we show the result of the second random event happening after choosing yes as an answer.
                    print(ru.EVENT_3_2_SECOND_YES)
            else:
                team_3[3] -= 400
                team_3[2] -= 450
                team_3[4] -= 300
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_3_2_NO)

            return list(zip(ru.STOCK, team_3))

        def event_3_3(answer):
            """
            The event_3_3 function
            :param answer: yes or no
            :return: list(zip(ru.STOCK, team_3))
            """
            if answer == 'да':
                random_nmr_4 = random.choice(g)
                if random_nmr_4 == 1:
                    team_3[1] += 30
                    team_3[2] -= 20
                    # Here we show the result of the first random event happening after choosing yes as an answer.
                    print(ru.EVENT_3_2_FIRST_YES)
                else:
                    team_3[1] += 40
                    team_3[2] -= 20
                    # Here we show the result of the second random event happening after choosing yes as an answer.
                    print(ru.EVENT_3_2_SECOND_YES)
            else:
                # Here we show the result of actions happening after choosing no as an answer.
                print(ru.EVENT_3_3_NO)

            return list(zip(ru.STOCK, team_3))

        match random_nmr_5:
            case 1:
                # Here we output an independent event when number one is selected by the random number generator.
                print(ru.EVENT_3_1)
                print(event_3_1(input()))
            case 2:
                # Here we output an independent event when number two is selected by the random number generator.
                print(ru.EVENT_3_2)
                print(event_3_2(input()))
            case 3:
                # Here we output an independent event when number three is selected by the random number generator.
                print(ru.EVENT_3_3)
                print(event_3_3(input()))
            case _:
                # Here we output an independent event when number zero is selected by the random number generator.
                print(ru.EVENT_3_0)

        # Here we suggest the ways by which the team can develop their village and spend resources to.
        print(ru.RESOURCES)
        resources_list = []
        choice_3 = [1, 2, 3, 4]
        for k in range(1, 5):
            resources = input(f'{ru.DIRECTIONS} {ru.RESOURCE_1[k - 1]}')
            resources_list.append(resources)
        for k in range(len(resources_list)):
            if resources_list[k] == 'да':
                resources_list.pop(k)
                resources_list.insert(k, 1)
            else:
                resources_list.pop(k)
                resources_list.insert(k, 0)

        for choice_3, resources_list in zip(choice_3, resources_list):
            match choice_3:
                case 1:
                    team_3[0] -= 60 * resources_list
                    team_3[2] += 60 * resources_list
                case 2:
                    team_3[2] -= 50 * resources_list
                case 3:
                    team_3[2] -= 20 * resources_list
                    team_3[0] -= 30 * resources_list
                case 4:
                    team_3[4] += 60 * resources_list
                    team_3[0] -= 50 * resources_list
                case 5:
                    team_3[0] -= 100 * resources_list
                    team_3[2] -= 50 * resources_list

        e.pop(random_nmr_5 - 1)
        return list(zip(ru.STOCK, team_3))

    # Here is the main loop, which uses a conditional operator to see which of the commands goes first and,
    # depending on this, it outputs the opening phrases. It also displays which move is being made.
    for i in range(5):
        print(f'{ru.NUMBER} {i}')
        if choice_1 == 1:
            print(ru.MOVE_1)
            print(ru.INTRODUCTION_1) if i == 0 else print()
            if choice_2 == 2:
                print(first_team()) if all(team_1[k] > 0 for k in range(len(team_1))) else print(ru.REMOVAL)
                print(ru.MOVE_2)
                print(ru.INTRODUCTION_2) if i == 0 else print()
                print(second_team()) if all(team_2[k] > 0 for k in range(len(team_2))) else print(ru.REMOVAL)
                print(ru.MOVE_3)
                print(ru.INTRODUCTION_3) if i == 0 else print()
                print(third_team()) if all(team_3[k] > 0 for k in range(len(team_3))) else print(ru.REMOVAL)

            else:
                print(first_team()) if all(team_1[k] > 0 for k in range(len(team_1))) else print(ru.REMOVAL)
                print(ru.MOVE_3)
                print(ru.INTRODUCTION_3) if i == 0 else print()
                print(third_team()) if all(team_3[k] > 0 for k in range(len(team_3))) else print(ru.REMOVAL)
                print(ru.MOVE_2)
                print(ru.INTRODUCTION_2) if i == 0 else print()
                print(second_team()) if all(team_2[k] > 0 for k in range(len(team_2))) else print(ru.REMOVAL)
        elif choice_1 == 2:
            if choice_2 == 1:
                print(ru.MOVE_2)
                print(ru.INTRODUCTION_2) if i == 0 else print()
                print(second_team()) if all(team_2[k] > 0 for k in range(len(team_2))) else print(ru.REMOVAL)
                print(ru.MOVE_1)
                print(ru.INTRODUCTION_1) if i == 0 else print()
                print(first_team()) if all(team_1[k] > 0 for k in range(len(team_1))) else print(ru.REMOVAL)
                print(ru.MOVE_3)
                print(ru.INTRODUCTION_3) if i == 0 else print()
                print(third_team()) if all(team_3[k] > 0 for k in range(len(team_3))) else print(ru.REMOVAL)
            else:
                print(ru.MOVE_3)
                print(ru.INTRODUCTION_3) if i == 0 else print()
                print(third_team()) if all(team_3[k] > 0 for k in range(len(team_3))) else print(ru.REMOVAL)
                print(ru.MOVE_1)
                print(ru.INTRODUCTION_1) if i == 0 else print()
                print(first_team()) if all(team_1[k] > 0 for k in range(len(team_1))) else print(ru.REMOVAL)
                print(ru.MOVE_2)
                print(ru.INTRODUCTION_2) if i == 0 else print()
                print(second_team()) if all(team_2[k] > 0 for k in range(len(team_2))) else print(ru.REMOVAL)
        else:
            if choice_2 == 2:
                print(ru.MOVE_3)
                print(ru.INTRODUCTION_3) if i == 0 else print()
                print(third_team()) if all(team_3[k] > 0 for k in range(len(team_3))) else print(ru.REMOVAL)
                print(ru.MOVE_2)
                print(ru.INTRODUCTION_2) if i == 0 else print()
                print(second_team()) if all(team_2[k] > 0 for k in range(len(team_2))) else print(ru.REMOVAL)
                print(ru.MOVE_1)
                print(ru.INTRODUCTION_1) if i == 0 else print()
                print(first_team()) if all(team_1[k] > 0 for k in range(len(team_1))) else print(ru.REMOVAL)
            elif choice_2 == 1:
                print(ru.MOVE_2)
                print(ru.INTRODUCTION_2) if i == 0 else print()
                print(second_team()) if all(team_2[k] > 0 for k in range(len(team_2))) else print(ru.REMOVAL)
                print(ru.MOVE_3)
                print(ru.INTRODUCTION_3) if i == 0 else print()
                print(third_team()) if all(team_3[k] > 0 for k in range(len(team_3))) else print(ru.REMOVAL)
                print(ru.MOVE_1)
                print(ru.INTRODUCTION_1) if i == 0 else print()
                print(first_team()) if all(team_1[k] > 0 for k in range(len(team_1))) else print(ru.REMOVAL)

    def winner():
        """
        The winner function that returns the team which made the greatest score depending on the sum of all resources.
        :return: print(winner())
        """
        max_result = max(sum(team_1), sum(team_2), sum(team_3))
        if max_result == sum(team_1) and all(team_1[k] > 0 for k in range(len(team_1))):
            print(f'{ru.VINNER_1}')
        elif max_result == sum(team_2) and all(team_2[k] > 0 for k in range(len(team_2))):
            print(f'{ru.VINNER_2}')
        elif max_result == sum(team_3) and all(team_3[k] > 0 for k in range(len(team_3))):
            print(f'{ru.VINNER_3}')

    print(winner())


if __name__ == '__main__':
    main()
