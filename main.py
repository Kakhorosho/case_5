import random
import ru_local as ru

print(ru.CHOICE)
choice_1 = int(input('Первая команда: '))
choice_2 = int(input('Вторая команда: '))
team_1 = [50] * 5
team_2 = [100] * 5
team_3 = [200] * 5


def first_team():
    a = [1, 2, 3, 4, 5]
    random_nmr_1 = random.choice(a)

    def event_1_1(answer):
        if answer == 'да':
            team_1[3] -= 5
            team_1[1] += 100
            print(ru.EVENT_1_1_YES)
            print(list(zip(ru.STOCK, team_1)))
        else:
            print(ru.EVENT_1_1_NO)
            print(list(zip(ru.STOCK, team_1)))

    def event_1_2(answer):
        if answer == 'да':
            team_1[2] -= 10
            team_1[4] += 20
            print(list(zip(ru.STOCK, team_1)))
        else:
            print(ru.EVENT_1_2_NO)
            print(list(zip(ru.STOCK, team_1)))

    def event_1_3(answer):
        if answer == 'да':
            print(ru.EVENT_1_3_YES)
            print(list(zip(ru.STOCK, team_1)))
        else:
            team_1[3] -= 20
            print(ru.EVENT_1_3_NO)
            print(list(zip(ru.STOCK, team_1)))

    match random_nmr_1:
        case 1:
            print(ru.EVENT_1_1)
            print(event_1_1(input()))
        case 2:
            print(ru.EVENT_1_2)
            print(event_1_2(input()))
        case 3:
            print(ru.EVENT_1_3)
            print(event_1_3(input()))
        case _:
            print(ru.EVENT_1_0)

    print(ru.CITIZENS_COMPLAINTS)
    complaints_list = []
    choice = [1, 2, 3, 4]
    for k in range(1, 5):
        complaints = input(f'{ru.CITIZENS_1[k - 1]}')
        complaints_list.append(complaints)
    for k in range(len(complaints_list)):
        if complaints_list[k] == 'да':
            complaints_list.pop(k)
            complaints_list.insert(k, 1)
        else:
            complaints_list.pop(k)
            complaints_list.insert(k, 0)

    for choice, complaints_list in zip(choice, complaints_list):
        match choice:
            case 1:
                team_1[2] -= 50 * complaints_list
            case 2:
                team_1[2] -= 5 * complaints_list
            case 3:
                team_1[2] -= 20 * complaints_list
            case 4:
                team_1[0] -= 50 * complaints_list

    a.pop(random_nmr_1 - 1)
    print(list(zip(ru.STOCK, team_1)))


def second_team():
    c = [1, 2, 3, 4, 5]
    b = [1, 2]
    d = [1, 2]
    random_nmr_2 = random.choice(c)

    def event_2_1(answer):
        team_2[2] -= 20
        team_2[4] -= 10
        if answer == 'да':
            team_2[2] -= 10
            print(list(zip(ru.STOCK, team_2)))
        else:
            team_2[2] -= 25
            team_2[4] -= 5
            print(ru.EVENT_2_1_NO)
            print(list(zip(ru.STOCK, team_2)))

    def event_2_2(answer):
        if answer == 'да':
            random_nmr_3 = random.choice(b)
            if random_nmr_3 == 1:
                team_2[0] -= 30
                print(ru.EVENT_2_2_FIRST_YES)
                print(list(zip(ru.STOCK, team_2)))
            else:
                team_2[0] -= 30
                print(ru.EVENT_2_2_SECOND_YES)
                print(list(zip(ru.STOCK, team_2)))
        else:
            print(ru.EVENT_2_2_NO)
            print(list(zip(ru.STOCK, team_2)))

    def event_2_3(answer):
        if answer == 'да':
            random_nmr_4 = random.choice(d)
            if random_nmr_4 == 1:
                print(ru.EVENT_2_3_FIRST_YES)
                print(list(zip(ru.STOCK, team_2)))
            else:
                team_2[2] += 40
                team_2[0] += 60
                print(ru.EVENT_2_3_SECOND_YES)
                print(list(zip(ru.STOCK, team_2)))
        else:
            team_2[2] -= 20
            print(ru.EVENT_2_3_NO)
            print(list(zip(ru.STOCK, team_2)))

    match random_nmr_2:
        case 1:
            print(ru.EVENT_2_1)
            print(event_2_1(input()))
        case 2:
            print(ru.EVENT_1_2)
            print(event_2_2(input()))
        case 3:
            print(ru.EVENT_2_3)
            print(event_2_3(input()))
        case _:
            print(ru.EVENT_2_0)

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

    c.pop(random_nmr_2 - 1)
    print(list(zip(ru.STOCK, team_2)))


def third_team():
    e = [1, 2, 3, 4, 5]
    f = [1, 2]
    g = [1, 2]
    j = [1, 2]
    random_nmr_5 = random.choice(e)

    def event_3_1(answer):
        team_3[2] -= 20
        team_3[4] -= 10
        if answer == 'да':
            random_nmr_6 = random.choice(j)
            if random_nmr_6 == 1:
                team_3[2] -= 50
                print(ru.EVENT_3_1_FIRST_YES)
                print(list(zip(ru.STOCK, team_3)))
            else:
                team_3[2] -= 50
                team_3[3] -= 20
                print(ru.EVENT_3_1_SECOND_YES)
                print(list(zip(ru.STOCK, team_3)))
        else:
            random_nmr_6 = random.choice(j)
            if random_nmr_6 == 1:
                team_3[2] -= 50
                print(ru.EVENT_3_1_FIRST_NO)
                print(list(zip(ru.STOCK, team_3)))
            else:
                print(ru.EVENT_3_1_SECOND_NO)
                print(list(zip(ru.STOCK, team_3)))

    def event_3_2(answer):
        if answer == 'да':
            random_nmr_7 = random.choice(f)
            if random_nmr_7 == 1:
                team_3[0] -= 50
                print(ru.EVENT_3_2_FIRST_YES)
                print(list(zip(ru.STOCK, team_3)))
            else:
                team_3[0] -= 50
                team_3[3] -= 3
                print(ru.EVENT_3_2_SECOND_YES)
                print(list(zip(ru.STOCK, team_3)))
        else:
            team_3[3] -= 400
            team_3[2] -= 450
            team_3[4] -= 300
            print(ru.EVENT_3_2_NO)
            print(list(zip(ru.STOCK, team_3)))

    def event_3_3(answer):
        if answer == 'да':
            random_nmr_4 = random.choice(g)
            if random_nmr_4 == 1:
                team_3[1] += 30
                team_3[2] += 20
                print(ru.EVENT_3_2_FIRST_YES)
                print(list(zip(ru.STOCK, team_3)))
            else:
                team_3[1] += 40
                print(ru.EVENT_3_2_SECOND_YES)
                print(list(zip(ru.STOCK, team_3)))
        else:
            team_3[2] -= 20
            print(ru.EVENT_3_3_NO)
            print(list(zip(ru.STOCK, team_3)))

    match random_nmr_5:
        case 1:
            print(ru.EVENT_3_1)
            print(event_3_1(input()))
        case 2:
            print(ru.EVENT_3_2)
            print(event_3_2(input()))
        case 3:
            print(ru.EVENT_3_3)
            print(event_3_3(input()))
        case _:
            print(ru.EVENT_3_0)

    print(ru.RESOURCES)
    resources_list = []
    choice_3 = [1, 2, 3, 4]
    for k in range(1, 5):
        resources = input(f'{ru.DIRECTIONS}. {ru.RESOURCE_1[k - 1]}')
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
    print(list(zip(ru.STOCK, team_3)))


for i in range(2):
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
