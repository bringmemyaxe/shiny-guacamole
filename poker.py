import itertools
import sys

while True:
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


    def progressbar(value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length) - 1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent))))
        sys.stdout.flush()


    def check_royal_flush():
        global royal_flush
        if 'AC' in your_cards and '2C' in your_cards and '3C' in your_cards and '4C' in your_cards and '5C' in your_cards:
            royal_flush = True
        elif 'AD' in your_cards and '2D' in your_cards and '3D' in your_cards and '4D' in your_cards and '5D' in your_cards:
            royal_flush = True
        elif 'AH' in your_cards and '2H' in your_cards and '3H' in your_cards and '4H' in your_cards and '5H' in your_cards:
            royal_flush = True
        elif 'AS' in your_cards and '2S' in your_cards and '3S' in your_cards and '4S' in your_cards and '5S' in your_cards:
            royal_flush = True


    def check_straight_flush():
        global straight_flush
        if '2C' in your_cards and '3C' in your_cards and '4C' in your_cards and '5C' in your_cards and '6C' in your_cards:
            straight_flush = True
        elif '3C' in your_cards and '4C' in your_cards and '5C' in your_cards and '6C' in your_cards and '7C' in your_cards:
            straight_flush = True
        elif '4C' in your_cards and '5C' in your_cards and '6C' in your_cards and '7C' in your_cards and '8C' in your_cards:
            straight_flush = True
        elif '5C' in your_cards and '6C' in your_cards and '7C' in your_cards and '8C' in your_cards and '9C' in your_cards:
            straight_flush = True
        elif '6C' in your_cards and '7C' in your_cards and '8C' in your_cards and '9C' in your_cards and '10C' in your_cards:
            straight_flush = True
        elif '7C' in your_cards and '8C' in your_cards and '9C' in your_cards and '10C' in your_cards and 'JC' in your_cards:
            straight_flush = True
        elif '8C' in your_cards and '9C' in your_cards and '10C' in your_cards and 'JC' in your_cards and 'QC' in your_cards:
            straight_flush = True
        elif '9C' in your_cards and '10C' in your_cards and 'JC' in your_cards and 'QC' in your_cards and 'KC' in your_cards:
            straight_flush = True
        elif '2D' in your_cards and '3D' in your_cards and '4D' in your_cards and '5D' in your_cards and '6D' in your_cards:
            straight_flush = True
        elif '3D' in your_cards and '4D' in your_cards and '5D' in your_cards and '6D' in your_cards and '7D' in your_cards:
            straight_flush = True
        elif '4D' in your_cards and '5D' in your_cards and '6D' in your_cards and '7D' in your_cards and '8D' in your_cards:
            straight_flush = True
        elif '5D' in your_cards and '6D' in your_cards and '7D' in your_cards and '8D' in your_cards and '9D' in your_cards:
            straight_flush = True
        elif '6D' in your_cards and '7D' in your_cards and '8D' in your_cards and '9D' in your_cards and '10D' in your_cards:
            straight_flush = True
        elif '7D' in your_cards and '8D' in your_cards and '9D' in your_cards and '10D' in your_cards and 'JD' in your_cards:
            straight_flush = True
        elif '8D' in your_cards and '9D' in your_cards and '10D' in your_cards and 'JD' in your_cards and 'QD' in your_cards:
            straight_flush = True
        elif '9D' in your_cards and '10D' in your_cards and 'JD' in your_cards and 'QD' in your_cards and 'KD' in your_cards:
            straight_flush = True
        elif '2H' in your_cards and '3H' in your_cards and '4H' in your_cards and '5H' in your_cards and '6H' in your_cards:
            straight_flush = True
        elif '3H' in your_cards and '4H' in your_cards and '5H' in your_cards and '6H' in your_cards and '7H' in your_cards:
            straight_flush = True
        elif '4H' in your_cards and '5H' in your_cards and '6H' in your_cards and '7H' in your_cards and '8H' in your_cards:
            straight_flush = True
        elif '5H' in your_cards and '6H' in your_cards and '7H' in your_cards and '8H' in your_cards and '9H' in your_cards:
            straight_flush = True
        elif '6H' in your_cards and '7H' in your_cards and '8H' in your_cards and '9H' in your_cards and '10H' in your_cards:
            straight_flush = True
        elif '7H' in your_cards and '8H' in your_cards and '9H' in your_cards and '10H' in your_cards and 'JH' in your_cards:
            straight_flush = True
        elif '8H' in your_cards and '9H' in your_cards and '10H' in your_cards and 'JH' in your_cards and 'QH' in your_cards:
            straight_flush = True
        elif '9H' in your_cards and '10H' in your_cards and 'JH' in your_cards and 'QH' in your_cards and 'KH' in your_cards:
            straight_flush = True
        elif '2S' in your_cards and '3S' in your_cards and '4S' in your_cards and '5S' in your_cards and '6S' in your_cards:
            straight_flush = True
        elif '3S' in your_cards and '4S' in your_cards and '5S' in your_cards and '6S' in your_cards and '7S' in your_cards:
            straight_flush = True
        elif '4S' in your_cards and '5S' in your_cards and '6S' in your_cards and '7S' in your_cards and '8S' in your_cards:
            straight_flush = True
        elif '5S' in your_cards and '6S' in your_cards and '7S' in your_cards and '8S' in your_cards and '9S' in your_cards:
            straight_flush = True
        elif '6S' in your_cards and '7S' in your_cards and '8S' in your_cards and '9S' in your_cards and '10S' in your_cards:
            straight_flush = True
        elif '7S' in your_cards and '8S' in your_cards and '9S' in your_cards and '10S' in your_cards and 'JS' in your_cards:
            straight_flush = True
        elif '8S' in your_cards and '9S' in your_cards and '10S' in your_cards and 'JS' in your_cards and 'QS' in your_cards:
            straight_flush = True
        elif '9S' in your_cards and '10S' in your_cards and 'JS' in your_cards and 'QS' in your_cards and 'KS' in your_cards:
            straight_flush = True


    def check_four_of_a_kind():
        global four_of_a_kind
        if current_card_meanings.count('A') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('2') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('3') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('4') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('5') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('6') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('7') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('8') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('9') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('0') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('J') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('Q') == 4:
            four_of_a_kind = True
        elif current_card_meanings.count('K') == 4:
            four_of_a_kind = True


    def check_full_house():
        global full_house
        for three in ranks:
            for two in ranks:
                if current_card_meanings.count(three) == 3 and current_card_meanings.count(two) == 2:
                    full_house = True


    def check_flush():
        global flush
        for suit in suits:
            if current_card_meanings.count(suit) == 5:
                flush = True


    def check_straight():
        global straight
        if current_card_meanings.count('A') == 1:
            if current_card_meanings.count('2') == 1:
                if current_card_meanings.count('3') == 1:
                    if current_card_meanings.count('4') == 1:
                        if current_card_meanings.count('5') == 1:
                            straight = True
        elif current_card_meanings.count('2') == 1:
            if current_card_meanings.count('3') == 1:
                if current_card_meanings.count('4') == 1:
                    if current_card_meanings.count('5') == 1:
                        if current_card_meanings.count('6') == 1:
                            straight = True
        elif current_card_meanings.count('3') == 1:
            if current_card_meanings.count('4') == 1:
                if current_card_meanings.count('5') == 1:
                    if current_card_meanings.count('6') == 1:
                        if current_card_meanings.count('7') == 1:
                            straight = True
        elif current_card_meanings.count('4') == 1:
            if current_card_meanings.count('5') == 1:
                if current_card_meanings.count('6') == 1:
                    if current_card_meanings.count('7') == 1:
                        if current_card_meanings.count('8') == 1:
                            straight = True
        elif current_card_meanings.count('5') == 1:
            if current_card_meanings.count('6') == 1:
                if current_card_meanings.count('7') == 1:
                    if current_card_meanings.count('8') == 1:
                        if current_card_meanings.count('9') == 1:
                            straight = True
        elif current_card_meanings.count('6') == 1:
            if current_card_meanings.count('7') == 1:
                if current_card_meanings.count('8') == 1:
                    if current_card_meanings.count('9') == 1:
                        if current_card_meanings.count('0') == 1:
                            straight = True
        elif current_card_meanings.count('7') == 1:
            if current_card_meanings.count('8') == 1:
                if current_card_meanings.count('9') == 1:
                    if current_card_meanings.count('0') == 1:
                        if current_card_meanings.count('J') == 1:
                            straight = True
        elif current_card_meanings.count('8') == 1:
            if current_card_meanings.count('9') == 1:
                if current_card_meanings.count('0') == 1:
                    if current_card_meanings.count('J') == 1:
                        if current_card_meanings.count('Q') == 1:
                            straight = True
        elif current_card_meanings.count('9') == 1:
            if current_card_meanings.count('0') == 1:
                if current_card_meanings.count('J') == 1:
                    if current_card_meanings.count('Q') == 1:
                        if current_card_meanings.count('K') == 1:
                            straight = True


    def check_three_of_a_kind():
        global three_of_a_kind
        if current_card_meanings.count('A') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('2') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('3') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('4') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('5') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('6') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('7') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('8') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('9') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('0') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('J') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('Q') == 3:
            three_of_a_kind = True
        elif current_card_meanings.count('K') == 3:
            three_of_a_kind = True


    def check_two_pairs():
        global two_pairs
        for first_pair in ranks:
            for second_pair in ranks:
                if current_card_meanings.count(first_pair) == 2 and current_card_meanings.count(second_pair) == 2:
                    if first_pair != second_pair:
                        two_pairs = True


    def check_jacks_or_better():
        global jacks_or_better
        if current_card_meanings.count('J') == 2:
            jacks_or_better = True
        elif current_card_meanings.count('Q') == 2:
            jacks_or_better = True
        elif current_card_meanings.count('K') == 2:
            jacks_or_better = True


    def check():
        global current_iteration
        global end_iteration
        global royal_flush
        global probability_to_win
        global straight_flush
        global four_of_a_kind
        global current_card_meanings
        global full_house
        global flush
        global straight
        global three_of_a_kind
        global two_pairs
        global jacks_or_better
        current_iteration += 1
        progressbar(current_iteration, end_iteration)
        royal_flush = False
        check_royal_flush()
        if royal_flush:
            probability_to_win += 1
        else:
            straight_flush = False
            check_straight_flush()
            if straight_flush:
                probability_to_win += 1
            else:
                four_of_a_kind = False
                current_card_meanings = []
                for card in your_cards:
                    temp_data = list(card)
                    for meaning in temp_data:
                        current_card_meanings.append(meaning)
                check_four_of_a_kind()
                if four_of_a_kind:
                    probability_to_win += 1
                else:
                    full_house = False
                    check_full_house()
                    if full_house:
                        probability_to_win += 1
                    else:
                        flush = False
                        check_flush()
                        if flush:
                            probability_to_win += 1
                        else:
                            straight = False
                            check_straight()
                            if straight:
                                probability_to_win += 1
                            else:
                                three_of_a_kind = False
                                check_three_of_a_kind()
                                if three_of_a_kind:
                                    probability_to_win += 1
                                else:
                                    two_pairs = False
                                    check_two_pairs()
                                    if two_pairs:
                                        probability_to_win += 1
                                    else:
                                        jacks_or_better = False
                                        check_jacks_or_better()
                                        if jacks_or_better:
                                            probability_to_win += 1


    def parser(hold_1st_card, hold_2nd_card, hold_3rd_card, hold_4th_card, hold_5th_card):
        global your_cards
        global number_of_non_held_cards
        global end_iteration
        global current_iteration
        global probability_to_win
        global checked_TTTTT
        global checked_TTTTF
        global checked_TTTFT
        global checked_TTFTT
        global checked_TFTTT
        global checked_FTTTT
        global checked_TTTFF
        global checked_TTFTF
        global checked_TTFFT
        global checked_TFTTF
        global checked_TFTFT
        global checked_TFFTT
        global checked_FTTTF
        global checked_FTTFT
        global checked_FTFTT
        global checked_FFTTT
        global checked_TTFFF
        global checked_TFTFF
        global checked_TFFTF
        global checked_TFFFT
        global checked_FTTFF
        global checked_FTFTF
        global checked_FTFFT
        global checked_FFTTF
        global checked_FFTFT
        global checked_FFFTT
        global checked_TFFFF
        global checked_FTFFF
        global checked_FFTFF
        global checked_FFFTF
        global checked_FFFFT
        global checked_FFFFF
        your_cards = []
        if number_of_non_held_cards == 0:
            end_iteration = 1
        elif number_of_non_held_cards == 1:
            end_iteration = 47
        elif number_of_non_held_cards == 2:
            end_iteration = 2162
        elif number_of_non_held_cards == 3:
            end_iteration = 97290
        elif number_of_non_held_cards == 4:
            end_iteration = 4280760
        elif number_of_non_held_cards == 5:
            end_iteration = 184072680
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
        if number_of_non_held_cards == 1:
            probability_to_win = (probability_to_win / 47) * 100
        elif number_of_non_held_cards == 2:
            probability_to_win = (probability_to_win / 2162) * 100
        elif number_of_non_held_cards == 3:
            probability_to_win = (probability_to_win / 97290) * 100
        elif number_of_non_held_cards == 4:
            probability_to_win = (probability_to_win / 4280760) * 100
        elif number_of_non_held_cards == 5:
            probability_to_win = (probability_to_win / 184072680) * 100
        if hold_1st_card:
            if hold_2nd_card:
                if hold_3rd_card:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_TTTTT = probability_to_win
                        else:
                            checked_TTTTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_TTTFT = probability_to_win
                        else:
                            checked_TTTFF = probability_to_win
                else:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_TTFTT = probability_to_win
                        else:
                            checked_TTFTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_TTFFT = probability_to_win
                        else:
                            checked_TTFFF = probability_to_win
            else:
                if hold_3rd_card:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_TFTTT = probability_to_win
                        else:
                            checked_TFTTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_TFTFT = probability_to_win
                        else:
                            checked_TFTFF = probability_to_win
                else:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_TFFTT = probability_to_win
                        else:
                            checked_TFFTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_TFFFT = probability_to_win
                        else:
                            checked_TFFFF = probability_to_win
        else:
            if hold_2nd_card:
                if hold_3rd_card:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_FTTTT = probability_to_win
                        else:
                            checked_FTTTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_FTTFT = probability_to_win
                        else:
                            checked_FTTFF = probability_to_win
                else:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_FTFTT = probability_to_win
                        else:
                            checked_FTFTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_FTFFT = probability_to_win
                        else:
                            checked_FTFFF = probability_to_win
            else:
                if hold_3rd_card:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_FFTTT = probability_to_win
                        else:
                            checked_FFTTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_FFTFT = probability_to_win
                        else:
                            checked_FFTFF = probability_to_win
                else:
                    if hold_4th_card:
                        if hold_5th_card:
                            checked_FFFTT = probability_to_win
                        else:
                            checked_FFFTF = probability_to_win
                    else:
                        if hold_5th_card:
                            checked_FFFFT = probability_to_win
                        else:
                            checked_FFFFF = probability_to_win


    mode = input('CHOOSE MODE: ')
    if mode == '1':
        number_of_non_held_cards = 0
        current_iteration = 0
        parser(True, True, True, True, True)  # TTTTT  # 0
        number_of_non_held_cards = 1
        current_iteration = 0
        parser(True, True, True, True, False)  # TTTTF  # 1
        parser(True, True, True, False, True)  # TTTFT  # 1
        parser(True, True, False, True, True)  # TTFTT  # 1
        parser(True, False, True, True, True)  # TFTTT  # 1
        parser(False, True, True, True, True)  # FTTTT  # 1
        print(checked_TTTTT)
        print(checked_TTTTF)
        print(checked_TTTFT)
        print(checked_TTFTT)
        print(checked_TFTTT)
        print(checked_FTTTT)
    elif mode == '2':
        number_of_non_held_cards = 0
        current_iteration = 0
        parser(True, True, True, True, True)  # TTTTT  # 0
        number_of_non_held_cards = 1
        current_iteration = 0
        parser(True, True, True, True, False)  # TTTTF  # 1
        parser(True, True, True, False, True)  # TTTFT  # 1
        parser(True, True, False, True, True)  # TTFTT  # 1
        parser(True, False, True, True, True)  # TFTTT  # 1
        parser(False, True, True, True, True)  # FTTTT  # 1
        number_of_non_held_cards = 2
        current_iteration = 0
        parser(True, True, True, False, False)  # TTTFF  # 2
        parser(True, True, False, True, False)  # TTFTF  # 2
        parser(True, True, False, False, True)  # TTFFT  # 2
        parser(True, False, True, True, False)  # TFTTF  # 2
        parser(True, False, True, False, True)  # TFTFT  # 2
        parser(True, False, False, True, True)  # TFFTT  # 2
        parser(False, True, True, True, False)  # FTTTF  # 2
        parser(False, True, True, False, True)  # FTTFT  # 2
        parser(False, True, False, True, True)  # FTFTT  # 2
        parser(False, False, True, True, True)  # FFTTT  # 2
        print(checked_TTTTT)
        print(checked_TTTTF)
        print(checked_TTTFT)
        print(checked_TTFTT)
        print(checked_TFTTT)
        print(checked_FTTTT)
        print(checked_TTTFF)
        print(checked_TTFTF)
        print(checked_TTFFT)
        print(checked_TFTTF)
        print(checked_TFTFT)
        print(checked_TFFTT)
        print(checked_FTTTF)
        print(checked_FTTFT)
        print(checked_FTFTT)
        print(checked_FFTTT)
    elif mode == '3':
        number_of_non_held_cards = 0
        current_iteration = 0
        parser(True, True, True, True, True)  # TTTTT  # 0
        number_of_non_held_cards = 1
        current_iteration = 0
        parser(True, True, True, True, False)  # TTTTF  # 1
        parser(True, True, True, False, True)  # TTTFT  # 1
        parser(True, True, False, True, True)  # TTFTT  # 1
        parser(True, False, True, True, True)  # TFTTT  # 1
        parser(False, True, True, True, True)  # FTTTT  # 1
        number_of_non_held_cards = 2
        current_iteration = 0
        parser(True, True, True, False, False)  # TTTFF  # 2
        parser(True, True, False, True, False)  # TTFTF  # 2
        parser(True, True, False, False, True)  # TTFFT  # 2
        parser(True, False, True, True, False)  # TFTTF  # 2
        parser(True, False, True, False, True)  # TFTFT  # 2
        parser(True, False, False, True, True)  # TFFTT  # 2
        parser(False, True, True, True, False)  # FTTTF  # 2
        parser(False, True, True, False, True)  # FTTFT  # 2
        parser(False, True, False, True, True)  # FTFTT  # 2
        parser(False, False, True, True, True)  # FFTTT  # 2
        number_of_non_held_cards = 3
        current_iteration = 0
        parser(True, True, False, False, False)  # TTFFF  # 3
        parser(True, False, True, False, False)  # TFTFF  # 3
        parser(True, False, False, True, False)  # TFFTF  # 3
        parser(True, False, False, False, True)  # TFFFT  # 3
        parser(False, True, True, False, False)  # FTTFF  # 3
        parser(False, True, False, True, False)  # FTFTF  # 3
        parser(False, True, False, False, True)  # FTFFT  # 3
        parser(False, False, True, True, False)  # FFTTF  # 3
        parser(False, False, True, False, True)  # FFTFT  # 3
        parser(False, False, False, True, True)  # FFFTT  # 3
        print('Possibilities to win:')
        print('       Do not change cards', checked_TTTTT)
        print('Change ___ ___ ___ ___ 5TH', checked_TTTTF)
        print('Change ___ ___ ___ 4TH ___', checked_TTTFT)
        print('Change ___ ___ 3RD ___ ___', checked_TTFTT)
        print('Change ___ 2ND ___ ___ ___', checked_TFTTT)
        print('Change 1ST ___ ___ ___ ___', checked_FTTTT)
        print('Change ___ ___ ___ 4TH 5TH', checked_TTTFF)
        print('Change ___ ___ 3RD ___ 5TH', checked_TTFTF)
        print('Change ___ ___ 3RD 4TH ___', checked_TTFFT)
        print('Change ___ 2ND ___ ___ 5TH', checked_TFTTF)
        print('Change ___ 2ND ___ 4TH ___', checked_TFTFT)
        print('Change ___ 2ND 3RD ___ ___', checked_TFFTT)
        print('Change 1ST ___ ___ ___ 5TH', checked_FTTTF)
        print('Change 1ST ___ ___ 4TH ___', checked_FTTFT)
        print('Change 1ST ___ 3RD ___ ___', checked_FTFTT)
        print('Change 1ST 2ND ___ ___ ___', checked_FFTTT)
        print('Change ___ ___ 3RD 4TH 5TH', checked_TTFFF)
        print('Change ___ 2ND ___ 4TH 5TH', checked_TFTFF)
        print('Change ___ 2ND 3RD ___ 5TH', checked_TFFTF)
        print('Change ___ 2ND 3RD 4TH ___', checked_TFFFT)
        print('Change 1ST ___ ___ 4TH 5TH', checked_FTTFF)
        print('Change 1ST ___ 3RD ___ 5TH', checked_FTFTF)
        print('Change 1ST ___ 3RD 4TH ___', checked_FTFFT)
        print('Change 1ST 2ND ___ ___ 5TH', checked_FFTTF)
        print('Change 1ST 2ND ___ 4TH ___', checked_FFTFT)
        print('Change 1ST 2ND 3RD ___ ___', checked_FFFTT)
    elif mode == '4':
        number_of_non_held_cards = 0
        current_iteration = 0
        parser(True, True, True, True, True)  # TTTTT  # 0
        number_of_non_held_cards = 1
        current_iteration = 0
        parser(True, True, True, True, False)  # TTTTF  # 1
        parser(True, True, True, False, True)  # TTTFT  # 1
        parser(True, True, False, True, True)  # TTFTT  # 1
        parser(True, False, True, True, True)  # TFTTT  # 1
        parser(False, True, True, True, True)  # FTTTT  # 1
        number_of_non_held_cards = 2
        current_iteration = 0
        parser(True, True, True, False, False)  # TTTFF  # 2
        parser(True, True, False, True, False)  # TTFTF  # 2
        parser(True, True, False, False, True)  # TTFFT  # 2
        parser(True, False, True, True, False)  # TFTTF  # 2
        parser(True, False, True, False, True)  # TFTFT  # 2
        parser(True, False, False, True, True)  # TFFTT  # 2
        parser(False, True, True, True, False)  # FTTTF  # 2
        parser(False, True, True, False, True)  # FTTFT  # 2
        parser(False, True, False, True, True)  # FTFTT  # 2
        parser(False, False, True, True, True)  # FFTTT  # 2
        number_of_non_held_cards = 3
        current_iteration = 0
        parser(True, True, False, False, False)  # TTFFF  # 3
        parser(True, False, True, False, False)  # TFTFF  # 3
        parser(True, False, False, True, False)  # TFFTF  # 3
        parser(True, False, False, False, True)  # TFFFT  # 3
        parser(False, True, True, False, False)  # FTTFF  # 3
        parser(False, True, False, True, False)  # FTFTF  # 3
        parser(False, True, False, False, True)  # FTFFT  # 3
        parser(False, False, True, True, False)  # FFTTF  # 3
        parser(False, False, True, False, True)  # FFTFT  # 3
        parser(False, False, False, True, True)  # FFFTT  # 3
        number_of_non_held_cards = 4
        current_iteration = 0
        parser(True, False, False, False, False)  # TFFFF  # 4
        parser(False, True, False, False, False)  # FTFFF  # 4
        parser(False, False, True, False, False)  # FFTFF  # 4
        parser(False, False, False, True, False)  # FFFTF  # 4
        parser(False, False, False, False, True)  # FFFFT  # 4
        print(checked_TTTTT)
        print(checked_TTTTF)
        print(checked_TTTFT)
        print(checked_TTFTT)
        print(checked_TFTTT)
        print(checked_FTTTT)
        print(checked_TTTFF)
        print(checked_TTFTF)
        print(checked_TTFFT)
        print(checked_TFTTF)
        print(checked_TFTFT)
        print(checked_TFFTT)
        print(checked_FTTTF)
        print(checked_FTTFT)
        print(checked_FTFTT)
        print(checked_FFTTT)
        print(checked_TTFFF)
        print(checked_TFTFF)
        print(checked_TFFTF)
        print(checked_TFFFT)
        print(checked_FTTFF)
        print(checked_FTFTF)
        print(checked_FTFFT)
        print(checked_FFTTF)
        print(checked_FFTFT)
        print(checked_FFFTT)
        print(checked_TFFFF)
        print(checked_FTFFF)
        print(checked_FFTFF)
        print(checked_FFFTF)
        print(checked_FFFFT)
    elif mode == '5':
        number_of_non_held_cards = 0
        current_iteration = 0
        parser(True, True, True, True, True)  # TTTTT  # 0
        number_of_non_held_cards = 1
        current_iteration = 0
        parser(True, True, True, True, False)  # TTTTF  # 1
        parser(True, True, True, False, True)  # TTTFT  # 1
        parser(True, True, False, True, True)  # TTFTT  # 1
        parser(True, False, True, True, True)  # TFTTT  # 1
        parser(False, True, True, True, True)  # FTTTT  # 1
        number_of_non_held_cards = 2
        current_iteration = 0
        parser(True, True, True, False, False)  # TTTFF  # 2
        parser(True, True, False, True, False)  # TTFTF  # 2
        parser(True, True, False, False, True)  # TTFFT  # 2
        parser(True, False, True, True, False)  # TFTTF  # 2
        parser(True, False, True, False, True)  # TFTFT  # 2
        parser(True, False, False, True, True)  # TFFTT  # 2
        parser(False, True, True, True, False)  # FTTTF  # 2
        parser(False, True, True, False, True)  # FTTFT  # 2
        parser(False, True, False, True, True)  # FTFTT  # 2
        parser(False, False, True, True, True)  # FFTTT  # 2
        number_of_non_held_cards = 3
        current_iteration = 0
        parser(True, True, False, False, False)  # TTFFF  # 3
        parser(True, False, True, False, False)  # TFTFF  # 3
        parser(True, False, False, True, False)  # TFFTF  # 3
        parser(True, False, False, False, True)  # TFFFT  # 3
        parser(False, True, True, False, False)  # FTTFF  # 3
        parser(False, True, False, True, False)  # FTFTF  # 3
        parser(False, True, False, False, True)  # FTFFT  # 3
        parser(False, False, True, True, False)  # FFTTF  # 3
        parser(False, False, True, False, True)  # FFTFT  # 3
        parser(False, False, False, True, True)  # FFFTT  # 3
        number_of_non_held_cards = 4
        current_iteration = 0
        parser(True, False, False, False, False)  # TFFFF  # 4
        parser(False, True, False, False, False)  # FTFFF  # 4
        parser(False, False, True, False, False)  # FFTFF  # 4
        parser(False, False, False, True, False)  # FFFTF  # 4
        parser(False, False, False, False, True)  # FFFFT  # 4
        number_of_non_held_cards = 5
        current_iteration = 0
        parser(False, False, False, False, False)  # FFFFF  # 5
        print(checked_TTTTT)
        print(checked_TTTTF)
        print(checked_TTTFT)
        print(checked_TTFTT)
        print(checked_TFTTT)
        print(checked_FTTTT)
        print(checked_TTTFF)
        print(checked_TTFTF)
        print(checked_TTFFT)
        print(checked_TFTTF)
        print(checked_TFTFT)
        print(checked_TFFTT)
        print(checked_FTTTF)
        print(checked_FTTFT)
        print(checked_FTFTT)
        print(checked_FFTTT)
        print(checked_TTFFF)
        print(checked_TFTFF)
        print(checked_TFFTF)
        print(checked_TFFFT)
        print(checked_FTTFF)
        print(checked_FTFTF)
        print(checked_FTFFT)
        print(checked_FFTTF)
        print(checked_FFTFT)
        print(checked_FFFTT)
        print(checked_TFFFF)
        print(checked_FTFFF)
        print(checked_FFTFF)
        print(checked_FFFTF)
        print(checked_FFFFT)
        print(checked_FFFFF)
