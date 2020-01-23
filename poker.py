import itertools

input_is_not_filled = True
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['C', 'D', 'H', 'S']
all_cards = [tup[0] + tup[1] for tup in itertools.product(ranks, suits)]
your_cards = []
while input_is_not_filled:
    first_card = input('INPUT YOUR FIRST CARD: ')
    if first_card in all_cards:
        all_cards.remove(first_card)
        your_cards.append(first_card)
        while input_is_not_filled:
            second_card = input('INPUT YOUR SECOND CARD: ')
            if second_card in all_cards and second_card not in your_cards:
                all_cards.remove(second_card)
                your_cards.append(second_card)
                while input_is_not_filled:
                    third_card = input('INPUT YOUR THIRD CARD: ')
                    if third_card in all_cards and third_card not in your_cards:
                        all_cards.remove(third_card)
                        your_cards.append(third_card)
                        while input_is_not_filled:
                            fourth_card = input('INPUT YOUR FOURTH CARD: ')
                            if fourth_card in all_cards and fourth_card not in your_cards:
                                all_cards.remove(fourth_card)
                                your_cards.append(fourth_card)
                                while input_is_not_filled:
                                    fifth_card = input('INPUT YOUR FIFTH CARD: ')
                                    if fifth_card in all_cards and fifth_card not in your_cards:
                                        all_cards.remove(fifth_card)
                                        your_cards.append(fifth_card)
                                        input_is_not_filled = False
suit_C = [tup[0] + tup[1] for tup in itertools.product(ranks, 'C')]
suit_D = [tup[0] + tup[1] for tup in itertools.product(ranks, 'D')]
suit_H = [tup[0] + tup[1] for tup in itertools.product(ranks, 'H')]
suit_S = [tup[0] + tup[1] for tup in itertools.product(ranks, 'S')]
def check_royal_flush():
    global royal_flush
    if 'AC' in your_cards and '2C' in your_cards and '3C' in your_cards and '4C' in your_cards and '5C' in your_cards:
        royal_flush = True
    if 'AD' in your_cards and '2D' in your_cards and '3D' in your_cards and '4D' in your_cards and '5D' in your_cards:
        royal_flush = True
    if 'AH' in your_cards and '2H' in your_cards and '3H' in your_cards and '4H' in your_cards and '5H' in your_cards:
        royal_flush = True
    if 'AS' in your_cards and '2S' in your_cards and '3S' in your_cards and '4S' in your_cards and '5S' in your_cards:
        royal_flush = True
def check_straight_flush():
    global straight_flush
    if '2C' in your_cards and '3C' in your_cards and '4C' in your_cards and '5C' in your_cards and '6C' in your_cards:
        straight_flush = True
    if '3C' in your_cards and '4C' in your_cards and '5C' in your_cards and '6C' in your_cards and '7C' in your_cards:
        straight_flush = True
    if '4C' in your_cards and '5C' in your_cards and '6C' in your_cards and '7C' in your_cards and '8C' in your_cards:
        straight_flush = True
    if '5C' in your_cards and '6C' in your_cards and '7C' in your_cards and '8C' in your_cards and '9C' in your_cards:
        straight_flush = True
    if '6C' in your_cards and '7C' in your_cards and '8C' in your_cards and '9C' in your_cards and '10C' in your_cards:
        straight_flush = True
    if '7C' in your_cards and '8C' in your_cards and '9C' in your_cards and '10C' in your_cards and 'JC' in your_cards:
        straight_flush = True
    if '8C' in your_cards and '9C' in your_cards and '10C' in your_cards and 'JC' in your_cards and 'QC' in your_cards:
        straight_flush = True
    if '9C' in your_cards and '10C' in your_cards and 'JC' in your_cards and 'QC' in your_cards and 'KC' in your_cards:
        straight_flush = True
    if '2D' in your_cards and '3D' in your_cards and '4D' in your_cards and '5D' in your_cards and '6D' in your_cards:
        straight_flush = True
    if '3D' in your_cards and '4D' in your_cards and '5D' in your_cards and '6D' in your_cards and '7D' in your_cards:
        straight_flush = True
    if '4D' in your_cards and '5D' in your_cards and '6D' in your_cards and '7D' in your_cards and '8D' in your_cards:
        straight_flush = True
    if '5D' in your_cards and '6D' in your_cards and '7D' in your_cards and '8D' in your_cards and '9D' in your_cards:
        straight_flush = True
    if '6D' in your_cards and '7D' in your_cards and '8D' in your_cards and '9D' in your_cards and '10D' in your_cards:
        straight_flush = True
    if '7D' in your_cards and '8D' in your_cards and '9D' in your_cards and '10D' in your_cards and 'JD' in your_cards:
        straight_flush = True
    if '8D' in your_cards and '9D' in your_cards and '10D' in your_cards and 'JD' in your_cards and 'QD' in your_cards:
        straight_flush = True
    if '9D' in your_cards and '10D' in your_cards and 'JD' in your_cards and 'QD' in your_cards and 'KD' in your_cards:
        straight_flush = True
    if '2H' in your_cards and '3H' in your_cards and '4H' in your_cards and '5H' in your_cards and '6H' in your_cards:
        straight_flush = True
    if '3H' in your_cards and '4H' in your_cards and '5H' in your_cards and '6H' in your_cards and '7H' in your_cards:
        straight_flush = True
    if '4H' in your_cards and '5H' in your_cards and '6H' in your_cards and '7H' in your_cards and '8H' in your_cards:
        straight_flush = True
    if '5H' in your_cards and '6H' in your_cards and '7H' in your_cards and '8H' in your_cards and '9H' in your_cards:
        straight_flush = True
    if '6H' in your_cards and '7H' in your_cards and '8H' in your_cards and '9H' in your_cards and '10H' in your_cards:
        straight_flush = True
    if '7H' in your_cards and '8H' in your_cards and '9H' in your_cards and '10H' in your_cards and 'JH' in your_cards:
        straight_flush = True
    if '8H' in your_cards and '9H' in your_cards and '10H' in your_cards and 'JH' in your_cards and 'QH' in your_cards:
        straight_flush = True
    if '9H' in your_cards and '10H' in your_cards and 'JH' in your_cards and 'QH' in your_cards and 'KH' in your_cards:
        straight_flush = True
    if '2S' in your_cards and '3S' in your_cards and '4S' in your_cards and '5S' in your_cards and '6S' in your_cards:
        straight_flush = True
    if '3S' in your_cards and '4S' in your_cards and '5S' in your_cards and '6S' in your_cards and '7S' in your_cards:
        straight_flush = True
    if '4S' in your_cards and '5S' in your_cards and '6S' in your_cards and '7S' in your_cards and '8S' in your_cards:
        straight_flush = True
    if '5S' in your_cards and '6S' in your_cards and '7S' in your_cards and '8S' in your_cards and '9S' in your_cards:
        straight_flush = True
    if '6S' in your_cards and '7S' in your_cards and '8S' in your_cards and '9S' in your_cards and '10S' in your_cards:
        straight_flush = True
    if '7S' in your_cards and '8S' in your_cards and '9S' in your_cards and '10S' in your_cards and 'JS' in your_cards:
        straight_flush = True
    if '8S' in your_cards and '9S' in your_cards and '10S' in your_cards and 'JS' in your_cards and 'QS' in your_cards:
        straight_flush = True
    if '9S' in your_cards and '10S' in your_cards and 'JS' in your_cards and 'QS' in your_cards and 'KS' in your_cards:
        straight_flush = True
def check_four_of_a_kind():
    if your_cards[0] in suit_C and your_cards[1] in suit_C and your_cards[2] in suit_C and your_cards[3] in suit_C:
        four_of_a_kind = True
    if your_cards[0] in suit_C and your_cards[1] in suit_C and your_cards[2] in suit_C and your_cards[4] in suit_C:
        four_of_a_kind = True
    if your_cards[0] in suit_C and your_cards[1] in suit_C and your_cards[3] in suit_C and your_cards[4] in suit_C:
        four_of_a_kind = True
    if your_cards[0] in suit_C and your_cards[2] in suit_C and your_cards[3] in suit_C and your_cards[4] in suit_C:
        four_of_a_kind = True
    if your_cards[1] in suit_C and your_cards[2] in suit_C and your_cards[3] in suit_C and your_cards[4] in suit_C:
        four_of_a_kind = True
    if your_cards[0] in suit_D and your_cards[1] in suit_D and your_cards[2] in suit_D and your_cards[3] in suit_D:
        four_of_a_kind = True
    if your_cards[0] in suit_D and your_cards[1] in suit_D and your_cards[2] in suit_D and your_cards[4] in suit_D:
        four_of_a_kind = True
    if your_cards[0] in suit_D and your_cards[1] in suit_D and your_cards[3] in suit_D and your_cards[4] in suit_D:
        four_of_a_kind = True
    if your_cards[0] in suit_D and your_cards[2] in suit_D and your_cards[3] in suit_D and your_cards[4] in suit_D:
        four_of_a_kind = True
    if your_cards[1] in suit_D and your_cards[2] in suit_D and your_cards[3] in suit_D and your_cards[4] in suit_D:
        four_of_a_kind = True
    if your_cards[0] in suit_H and your_cards[1] in suit_H and your_cards[2] in suit_H and your_cards[3] in suit_H:
        four_of_a_kind = True
    if your_cards[0] in suit_H and your_cards[1] in suit_H and your_cards[2] in suit_H and your_cards[4] in suit_H:
        four_of_a_kind = True
    if your_cards[0] in suit_H and your_cards[1] in suit_H and your_cards[3] in suit_H and your_cards[4] in suit_H:
        four_of_a_kind = True
    if your_cards[0] in suit_H and your_cards[2] in suit_H and your_cards[3] in suit_H and your_cards[4] in suit_H:
        four_of_a_kind = True
    if your_cards[1] in suit_H and your_cards[2] in suit_H and your_cards[3] in suit_H and your_cards[4] in suit_H:
        four_of_a_kind = True
    if your_cards[0] in suit_S and your_cards[1] in suit_S and your_cards[2] in suit_S and your_cards[3] in suit_S:
        four_of_a_kind = True
    if your_cards[0] in suit_S and your_cards[1] in suit_S and your_cards[2] in suit_S and your_cards[4] in suit_S:
        four_of_a_kind = True
    if your_cards[0] in suit_S and your_cards[1] in suit_S and your_cards[3] in suit_S and your_cards[4] in suit_S:
        four_of_a_kind = True
    if your_cards[0] in suit_S and your_cards[2] in suit_S and your_cards[3] in suit_S and your_cards[4] in suit_S:
        four_of_a_kind = True
    if your_cards[1] in suit_S and your_cards[2] in suit_S and your_cards[3] in suit_S and your_cards[4] in suit_S:
        four_of_a_kind = True
def count_probability():
    global probability_to_win
    print(probability_to_win)
def check():
    global royal_flush
    global probability_to_win
    global straight_flush
    global four_of_a_kind
    global full_house
    global flush
    global straight
    global three_of_a_kind
    global two_pairs
    global jacks_or_better
    royal_flush = False
    check_royal_flush()
    if royal_flush:
        probability_to_win += 250
    else:
        straight_flush = False
        check_straight_flush()
        if straight_flush:
            probability_to_win += 50
        else:
            four_of_a_kind = False
            check_four_of_a_kind()
            if four_of_a_kind:
                probability_to_win += 25
            else:
                full_house = False
                #check_full_house()

    #check_flush()
    #check_straight()
    #check_three_of_a_kind()
    #check_two_pairs()
    #check_jacks_or_better()
    count_probability()
def parser(hold_1st_card, hold_2nd_card, hold_3rd_card, hold_4th_card, hold_5th_card):
    global probability_to_win
    your_cards = []
    probability_to_win = 0
    if hold_1st_card:
        your_cards.append(first_card)
        if hold_2nd_card:
            your_cards.append(second_card)
            if hold_3rd_card:
                your_cards.append(third_card)
                if hold_4th_card:
                    your_cards.append(fourth_card)
                    if hold_5th_card:
                        your_cards.append(fifth_card)
                        check()
                        your_cards.remove(fifth_card)
                    else:
                        for new_card5 in all_cards:
                            if new_card5 not in your_cards:
                                your_cards.append(new_card5)
                                check()
                                your_cards.remove(new_card5)
                    your_cards.remove(fourth_card)
                else:
                    for new_card4 in all_cards:
                        if new_card4 not in your_cards:
                            your_cards.append(new_card4)
                            if hold_5th_card:
                                your_cards.append(fifth_card)
                                check()
                                your_cards.remove(fifth_card)
                            else:
                                for new_card5 in all_cards:
                                    if new_card5 not in your_cards:
                                        your_cards.append(new_card5)
                                        check()
                                        your_cards.remove(new_card5)
                            your_cards.remove(new_card4)
                your_cards.remove(third_card)
            else:
                for new_card3 in all_cards:
                    if new_card3 not in your_cards:
                        your_cards.append(new_card3)
                        if hold_4th_card:
                            your_cards.append(fourth_card)
                            if hold_5th_card:
                                your_cards.append(fifth_card)
                                check()
                                your_cards.remove(fifth_card)
                            else:
                                for new_card5 in all_cards:
                                    if new_card5 not in your_cards:
                                        your_cards.append(new_card5)
                                        check()
                                        your_cards.remove(new_card5)
                            your_cards.remove(fourth_card)
                        else:
                            for new_card4 in all_cards:
                                if new_card4 not in your_cards:
                                    your_cards.append(new_card4)
                                    if hold_5th_card:
                                        your_cards.append(fifth_card)
                                        check()
                                        your_cards.remove(fifth_card)
                                    else:
                                        for new_card5 in all_cards:
                                            if new_card5 not in your_cards:
                                                your_cards.append(new_card5)
                                                check()
                                                your_cards.remove(new_card5)
                                    your_cards.remove(new_card4)
                        your_cards.remove(new_card3)
            your_cards.remove(second_card)
        else:
            for new_card2 in all_cards:
                if new_card2 not in your_cards:
                    your_cards.append(new_card2)
                    if hold_3rd_card:
                        your_cards.append(third_card)
                        if hold_4th_card:
                            your_cards.append(fourth_card)
                            if hold_5th_card:
                                your_cards.append(fifth_card)
                                check()
                                your_cards.remove(fifth_card)
                            else:
                                for new_card5 in all_cards:
                                    if new_card5 not in your_cards:
                                        your_cards.append(new_card5)
                                        check()
                                        your_cards.remove(new_card5)
                            your_cards.remove(fourth_card)
                        else:
                            for new_card4 in all_cards:
                                if new_card4 not in your_cards:
                                    your_cards.append(new_card4)
                                    if hold_5th_card:
                                        your_cards.append(fifth_card)
                                        check()
                                        your_cards.remove(fifth_card)
                                    else:
                                        for new_card5 in all_cards:
                                            if new_card5 not in your_cards:
                                                your_cards.append(new_card5)
                                                check()
                                                your_cards.remove(new_card5)
                                    your_cards.remove(new_card4)
                        your_cards.remove(third_card)
                    else:
                        for new_card3 in all_cards:
                            if new_card3 not in your_cards:
                                your_cards.append(new_card3)
                                if hold_4th_card:
                                    your_cards.append(fourth_card)
                                    if hold_5th_card:
                                        your_cards.append(fifth_card)
                                        check()
                                        your_cards.remove(fifth_card)
                                    else:
                                        for new_card5 in all_cards:
                                            if new_card5 not in your_cards:
                                                your_cards.append(new_card5)
                                                check()
                                                your_cards.remove(new_card5)
                                    your_cards.remove(fourth_card)
                                else:
                                    for new_card4 in all_cards:
                                        if new_card4 not in your_cards:
                                            your_cards.append(new_card4)
                                            if hold_5th_card:
                                                your_cards.append(fifth_card)
                                                check()
                                                your_cards.remove(fifth_card)
                                            else:
                                                for new_card5 in all_cards:
                                                    if new_card5 not in your_cards:
                                                        your_cards.append(new_card5)
                                                        check()
                                                        your_cards.remove(new_card5)
                                            your_cards.remove(new_card4)
                                your_cards.remove(new_card3)
                    your_cards.remove(new_card2)
        your_cards.remove(first_card)
    else:
        for new_card1 in all_cards:
            if new_card1 not in your_cards:
                your_cards.append(new_card1)
                if hold_2nd_card:
                    your_cards.append(second_card)
                    if hold_3rd_card:
                        your_cards.append(third_card)
                        if hold_4th_card:
                            your_cards.append(fourth_card)
                            if hold_5th_card:
                                your_cards.append(fifth_card)
                                check()
                                your_cards.remove(fifth_card)
                            else:
                                for new_card5 in all_cards:
                                    if new_card5 not in your_cards:
                                        your_cards.append(new_card5)
                                        check()
                                        your_cards.remove(new_card5)
                            your_cards.remove(fourth_card)
                        else:
                            for new_card4 in all_cards:
                                if new_card4 not in your_cards:
                                    your_cards.append(new_card4)
                                    if hold_5th_card:
                                        your_cards.append(fifth_card)
                                        check()
                                        your_cards.remove(fifth_card)
                                    else:
                                        for new_card5 in all_cards:
                                            if new_card5 not in your_cards:
                                                your_cards.append(new_card5)
                                                check()
                                                your_cards.remove(new_card5)
                                    your_cards.remove(new_card4)
                        your_cards.remove(third_card)
                    else:
                        for new_card3 in all_cards:
                            if new_card3 not in your_cards:
                                your_cards.append(new_card3)
                                if hold_4th_card:
                                    your_cards.append(fourth_card)
                                    if hold_5th_card:
                                        your_cards.append(fifth_card)
                                        check()
                                        your_cards.remove(fifth_card)
                                    else:
                                        for new_card5 in all_cards:
                                            if new_card5 not in your_cards:
                                                your_cards.append(new_card5)
                                                check()
                                                your_cards.remove(new_card5)
                                    your_cards.remove(fourth_card)
                                else:
                                    for new_card4 in all_cards:
                                        if new_card4 not in your_cards:
                                            your_cards.append(new_card4)
                                            if hold_5th_card:
                                                your_cards.append(fifth_card)
                                                check()
                                                your_cards.remove(fifth_card)
                                            else:
                                                for new_card5 in all_cards:
                                                    if new_card5 not in your_cards:
                                                        your_cards.append(new_card5)
                                                        check()
                                                        your_cards.remove(new_card5)
                                            your_cards.remove(new_card4)
                                your_cards.remove(new_card3)
                    your_cards.remove(second_card)
                else:
                    for new_card2 in all_cards:
                        if new_card2 not in your_cards:
                            your_cards.append(new_card2)
                            if hold_3rd_card:
                                your_cards.append(third_card)
                                if hold_4th_card:
                                    your_cards.append(fourth_card)
                                    if hold_5th_card:
                                        your_cards.append(fifth_card)
                                        check()
                                        your_cards.remove(fifth_card)
                                    else:
                                        for new_card5 in all_cards:
                                            if new_card5 not in your_cards:
                                                your_cards.append(new_card5)
                                                check()
                                                your_cards.remove(new_card5)
                                    your_cards.remove(fourth_card)
                                else:
                                    for new_card4 in all_cards:
                                        if new_card4 not in your_cards:
                                            your_cards.append(new_card4)
                                            if hold_5th_card:
                                                your_cards.append(fifth_card)
                                                check()
                                                your_cards.remove(fifth_card)
                                            else:
                                                for new_card5 in all_cards:
                                                    if new_card5 not in your_cards:
                                                        your_cards.append(new_card5)
                                                        check()
                                                        your_cards.remove(new_card5)
                                            your_cards.remove(new_card4)
                                your_cards.remove(third_card)
                            else:
                                for new_card3 in all_cards:
                                    if new_card3 not in your_cards:
                                        your_cards.append(new_card3)
                                        if hold_4th_card:
                                            your_cards.append(fourth_card)
                                            if hold_5th_card:
                                                your_cards.append(fifth_card)
                                                check()
                                                your_cards.remove(fifth_card)
                                            else:
                                                for new_card5 in all_cards:
                                                    if new_card5 not in your_cards:
                                                        your_cards.append(new_card5)
                                                        check()
                                                        your_cards.remove(new_card5)
                                            your_cards.remove(fourth_card)
                                        else:
                                            for new_card4 in all_cards:
                                                if new_card4 not in your_cards:
                                                    your_cards.append(new_card4)
                                                    if hold_5th_card:
                                                        your_cards.append(fifth_card)
                                                        check()
                                                        your_cards.remove(fifth_card)
                                                    else:
                                                        for new_card5 in all_cards:
                                                            if new_card5 not in your_cards:
                                                                your_cards.append(new_card5)
                                                                check()
                                                                your_cards.remove(new_card5)
                                                    your_cards.remove(new_card4)
                                        your_cards.remove(new_card3)
                            your_cards.remove(new_card2)
                your_cards.remove(new_card1)
while True:
    mode = input('''
FIRST MODE WILL COUNT WHICH ONE CARD IS THE BEST CHOICE TO CHANGE HOLDING THE OTHERS
SECOND MODE WILL DO THE SAME BUT CHANGING TWO CARDS
THIRD MODE -- CHANGING THREE CARDS
FOURTH MODE...
FIFTH...
BE CAREFUL: THE MORE CARDS YOU CHOOSE TO CHANGE, THE MORE TIME YOU WILL HAVE TO WAIT

CHOOSE MODE: ''')
    if mode == '1':
        parser(True, True, True, True, True)
        parser(True, True, True, True, False)
        parser(True, True, True, False, True)
        parser(True, True, False, True, True)
        parser(True, False, True, True, True)
        parser(False, True, True, True, True)
    elif mode == '2':
        parser(True, True, True, True, True)
        parser(True, True, True, True, False)
        parser(True, True, True, False, True)
        parser(True, True, False, True, True)
        parser(True, False, True, True, True)
        parser(False, True, True, True, True)
        parser(True, True, True, False, False)
        parser(True, True, False, True, False)
        parser(True, True, False, False, True)
        parser(True, False, True, True, False)
        parser(True, False, True, False, True)
        parser(True, False, False, True, True)
        parser(False, True, True, True, False)
        parser(False, True, True, False, True)
        parser(False, True, False, True, True)
        parser(False, False, True, True, True)
    elif mode == '3':
        parser(True, True, True, True, True)
        parser(True, True, True, True, False)
        parser(True, True, True, False, True)
        parser(True, True, False, True, True)
        parser(True, False, True, True, True)
        parser(False, True, True, True, True)
        parser(True, True, True, False, False)
        parser(True, True, False, True, False)
        parser(True, True, False, False, True)
        parser(True, False, True, True, False)
        parser(True, False, True, False, True)
        parser(True, False, False, True, True)
        parser(False, True, True, True, False)
        parser(False, True, True, False, True)
        parser(False, True, False, True, True)
        parser(False, False, True, True, True)
        parser(True, True, False, False, False)
        parser(True, False, True, False, False)
        parser(True, False, False, True, False)
        parser(True, False, False, False, True)
        parser(False, True, True, False, False)
        parser(False, True, False, True, False)
        parser(False, True, False, False, True)
        parser(False, False, True, True, False)
        parser(False, False, True, False, True)
        parser(False, False, False, True, True)
    elif mode == '4':
        parser(True, True, True, True, True)
        parser(True, True, True, True, False)
        parser(True, True, True, False, True)
        parser(True, True, False, True, True)
        parser(True, False, True, True, True)
        parser(False, True, True, True, True)
        parser(True, True, True, False, False)
        parser(True, True, False, True, False)
        parser(True, True, False, False, True)
        parser(True, False, True, True, False)
        parser(True, False, True, False, True)
        parser(True, False, False, True, True)
        parser(False, True, True, True, False)
        parser(False, True, True, False, True)
        parser(False, True, False, True, True)
        parser(False, False, True, True, True)
        parser(True, True, False, False, False)
        parser(True, False, True, False, False)
        parser(True, False, False, True, False)
        parser(True, False, False, False, True)
        parser(False, True, True, False, False)
        parser(False, True, False, True, False)
        parser(False, True, False, False, True)
        parser(False, False, True, True, False)
        parser(False, False, True, False, True)
        parser(False, False, False, True, True)
        parser(True, False, False, False, False)
        parser(False, True, False, False, False)
        parser(False, False, True, False, False)
        parser(False, False, False, True, False)
        parser(False, False, False, False, True)
    elif mode == '5':
        parser(True, True, True, True, True)
        parser(True, True, True, True, False)
        parser(True, True, True, False, True)
        parser(True, True, False, True, True)
        parser(True, False, True, True, True)
        parser(False, True, True, True, True)
        parser(True, True, True, False, False)
        parser(True, True, False, True, False)
        parser(True, True, False, False, True)
        parser(True, False, True, True, False)
        parser(True, False, True, False, True)
        parser(True, False, False, True, True)
        parser(False, True, True, True, False)
        parser(False, True, True, False, True)
        parser(False, True, False, True, True)
        parser(False, False, True, True, True)
        parser(True, True, False, False, False)
        parser(True, False, True, False, False)
        parser(True, False, False, True, False)
        parser(True, False, False, False, True)
        parser(False, True, True, False, False)
        parser(False, True, False, True, False)
        parser(False, True, False, False, True)
        parser(False, False, True, True, False)
        parser(False, False, True, False, True)
        parser(False, False, False, True, True)
        parser(True, False, False, False, False)
        parser(False, True, False, False, False)
        parser(False, False, True, False, False)
        parser(False, False, False, True, False)
        parser(False, False, False, False, True)
        parser(False, False, False, False, False)
