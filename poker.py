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


    def progressbar(value, endvalue):
        percent = float(value) / endvalue
        sys.stdout.write("\r{0}% is done… Wait…".format(int(round(percent))))
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
            case_royal_flush[win_index] += 1
            case_win[win_index] += 1
        else:
            straight_flush = False
            check_straight_flush()
            if straight_flush:
                probability_to_win += 1
                case_straight_flush[win_index] += 1
                case_win[win_index] += 1
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
                    case_four_of_a_kind[win_index] += 1
                    case_win[win_index] += 1
                else:
                    full_house = False
                    check_full_house()
                    if full_house:
                        probability_to_win += 1
                        case_full_house[win_index] += 1
                        case_win[win_index] += 1
                    else:
                        flush = False
                        check_flush()
                        if flush:
                            probability_to_win += 1
                            case_flush[win_index] += 1
                            case_win[win_index] += 1
                        else:
                            straight = False
                            check_straight()
                            if straight:
                                probability_to_win += 1
                                case_straight[win_index] += 1
                                case_win[win_index] += 1
                            else:
                                three_of_a_kind = False
                                check_three_of_a_kind()
                                if three_of_a_kind:
                                    probability_to_win += 1
                                    case_three_of_a_kind[win_index] += 1
                                    case_win[win_index] += 1
                                else:
                                    two_pairs = False
                                    check_two_pairs()
                                    if two_pairs:
                                        probability_to_win += 1
                                        case_two_pairs[win_index] += 1
                                        case_win[win_index] += 1
                                    else:
                                        jacks_or_better = False
                                        check_jacks_or_better()
                                        if jacks_or_better:
                                            probability_to_win += 1
                                            case_jacks_or_better[win_index] += 1
                                            case_win[win_index] += 1


    def parser(hold_1st_card, hold_2nd_card, hold_3rd_card, hold_4th_card, hold_5th_card):
        global your_cards
        global number_of_non_held_cards
        global end_iteration
        global current_iteration
        global probability_to_win
        global win_index
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
            end_iteration = 0.1
        elif number_of_non_held_cards == 1:
            end_iteration = 4.7
        elif number_of_non_held_cards == 2:
            end_iteration = 216.2
        elif number_of_non_held_cards == 3:
            end_iteration = 9729
        elif number_of_non_held_cards == 4:
            end_iteration = 428076
        elif number_of_non_held_cards == 5:
            end_iteration = 18407268
        probability_to_win = 0
        win_index += 1
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
        if number_of_non_held_cards == 0:
            probability_to_win = (probability_to_win / 1) * 100
        elif number_of_non_held_cards == 1:
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


    def interpreter():
        print('')
        print('These are the best options, as you can see:')
        results = []
        results.append(checked_TTTTT)
        results.append(checked_TTTTF)
        results.append(checked_TTTFT)
        results.append(checked_TTFTT)
        results.append(checked_TFTTT)
        results.append(checked_FTTTT)
        try:
            results.append(checked_TTTFF)
        except NameError:
            pass
        try:
            results.append(checked_TTFTF)
        except NameError:
            pass
        try:
            results.append(checked_TTFFT)
        except NameError:
            pass
        try:
            results.append(checked_TFTTF)
        except NameError:
            pass
        try:
            results.append(checked_TFTFT)
        except NameError:
            pass
        try:
            results.append(checked_TFFTT)
        except NameError:
            pass
        try:
            results.append(checked_FTTTF)
        except NameError:
            pass
        try:
            results.append(checked_FTTFT)
        except NameError:
            pass
        try:
            results.append(checked_FTFTT)
        except NameError:
            pass
        try:
            results.append(checked_FFTTT)
        except NameError:
            pass
        try:
            results.append(checked_TTFFF)
        except NameError:
            pass
        try:
            results.append(checked_TFTFF)
        except NameError:
            pass
        try:
            results.append(checked_TFFTF)
        except NameError:
            pass
        try:
            results.append(checked_TFFFT)
        except NameError:
            pass
        try:
            results.append(checked_FTTFF)
        except NameError:
            pass
        try:
            results.append(checked_FTFTF)
        except NameError:
            pass
        try:
            results.append(checked_FTFFT)
        except NameError:
            pass
        try:
            results.append(checked_FFTTF)
        except NameError:
            pass
        try:
            results.append(checked_FFTFT)
        except NameError:
            pass
        try:
            results.append(checked_FFFTT)
        except NameError:
            pass
        try:
            results.append(checked_TFFFF)
        except NameError:
            pass
        try:
            results.append(checked_FTFFF)
        except NameError:
            pass
        try:
            results.append(checked_FFTFF)
        except NameError:
            pass
        try:
            results.append(checked_FFFTF)
        except NameError:
            pass
        try:
            results.append(checked_FFFFT)
        except NameError:
            pass
        try:
            results.append(checked_FFFFF)
        except NameError:
            pass
        best_option = 0
        for num1 in results:
            for num2 in results:
                if num1 <= num2 and best_option <= num2:
                    best_option = num2
        index = -1
        for result in results:
            index += 1
            if result == best_option:
                print('')
                print(dialogue[index], result)
                print('If you do that, it is going to be a …:')
                non_prepared_wins = []
                non_prepared_wins.append(case_royal_flush[index])
                non_prepared_wins.append(case_straight_flush[index])
                non_prepared_wins.append(case_four_of_a_kind[index])
                non_prepared_wins.append(case_full_house[index])
                non_prepared_wins.append(case_flush[index])
                non_prepared_wins.append(case_straight[index])
                non_prepared_wins.append(case_three_of_a_kind[index])
                non_prepared_wins.append(case_two_pairs[index])
                non_prepared_wins.append(case_jacks_or_better[index])
                hand_names = [' royal flush', ' straight flush', ' four of a kind', ' full house', ' flush',
                              ' straight', ' three of a kind', ' two pairs', ' jacks or better']
                wins = []
                try:
                    while True:
                        biggest_number = 0
                        for num1 in non_prepared_wins:
                            for num2 in non_prepared_wins:
                                if num1 <= num2 and biggest_number <= num2:
                                    biggest_number = num2
                                    non_prepared_wins_index = non_prepared_wins.index(biggest_number)
                        hand_percent = (biggest_number / case_win[index]) * 100
                        hand_chance = str(hand_percent) + hand_names[non_prepared_wins_index]
                        if hand_percent != 0:
                            wins.append(hand_chance)
                        del non_prepared_wins[non_prepared_wins_index]
                        del hand_names[non_prepared_wins_index]
                except IndexError:
                    pass
                for hand in wins:
                    print(hand)


    def outputer():
        global dialogue
        print('')
        print('Actually, output of the calculations.')
        print('Your cards are:')
        all_possible_cards = [tup[0] + tup[1] for tup in itertools.product(ranks, suits)]
        actual_card_icons = {}
        unicode_list = ['🃑 ', '🃁 ', '🂱 ', '🂡 ', '🃒 ', '🃂 ', '🂲 ', '🂢 ', '🃓 ', '🃃 ', '🂳 ', '🂣 ',
                        '🃔 ', '🃄 ', '🂴 ', '🂤 ', '🃕 ', '🃅 ', '🂵 ', '🂥 ', '🃖 ', '🃆 ', '🂶 ', '🂦 ',
                        '🃗 ', '🃇 ', '🂷 ', '🂧 ', '🃘 ', '🃈 ', '🂸 ', '🂨 ', '🃙 ', '🃉 ', '🂹 ', '🂩 ',
                        '🃚 ', '🃊 ', '🂺 ', '🂪 ', '🃛 ', '🃋 ', '🂻 ', '🂫 ', '🃝 ', '🃍 ', '🂽 ', '🂭 ',
                        '🃞 ', '🃎 ', '🂾 ', '🂮 ']
        unicode_index = -1
        for card in all_possible_cards:
            unicode_index += 1
            actual_card_icons[card] = unicode_list[unicode_index]
        first_card_icon = actual_card_icons.get(first_card)
        second_card_icon = actual_card_icons.get(second_card)
        third_card_icon = actual_card_icons.get(third_card)
        fourth_card_icon = actual_card_icons.get(fourth_card)
        fifth_card_icon = actual_card_icons.get(fifth_card)
        actual_card_names = {}
        for card in all_possible_cards:
            temp_data = list(card)
            current_card_meanings = []
            for meaning in temp_data:
                current_card_meanings.append(meaning)
            if current_card_meanings.count('A') == 1:
                rankname = 'Ace of '
            elif current_card_meanings.count('2') == 1:
                rankname = 'Two of '
            elif current_card_meanings.count('3') == 1:
                rankname = 'Three of '
            elif current_card_meanings.count('4') == 1:
                rankname = 'Four of '
            elif current_card_meanings.count('5') == 1:
                rankname = 'Five of '
            elif current_card_meanings.count('6') == 1:
                rankname = 'Six of '
            elif current_card_meanings.count('7') == 1:
                rankname = 'Seven of '
            elif current_card_meanings.count('8') == 1:
                rankname = 'Eight of '
            elif current_card_meanings.count('9') == 1:
                rankname = 'Nine of '
            elif current_card_meanings.count('0') == 1:
                rankname = 'Ten of '
            elif current_card_meanings.count('J') == 1:
                rankname = 'Jack of '
            elif current_card_meanings.count('Q') == 1:
                rankname = 'Queen of '
            elif current_card_meanings.count('K') == 1:
                rankname = 'King of '
            if current_card_meanings.count('C') == 1:
                suitname = 'clubs'
            elif current_card_meanings.count('D') == 1:
                suitname = 'diamonds'
            elif current_card_meanings.count('H') == 1:
                suitname = 'hearts'
            elif current_card_meanings.count('S') == 1:
                suitname = 'spades'
            actual_card_names[card] = rankname + suitname
        unicode_index = -1
        for every_card, name in actual_card_names.items():
            unicode_index += 1
            actual_card_names[every_card] = unicode_list[unicode_index] + name
        your_first_card = actual_card_names.get(first_card)
        your_second_card = actual_card_names.get(second_card)
        your_third_card = actual_card_names.get(third_card)
        your_fourth_card = actual_card_names.get(fourth_card)
        your_fifth_card = actual_card_names.get(fifth_card)
        print(first_card_icon + second_card_icon + third_card_icon + fourth_card_icon + fifth_card_icon)
        print('')
        print(your_first_card)
        print(your_second_card)
        print(your_third_card)
        print(your_fourth_card)
        print(your_fifth_card)
        print('Possibilities to win (percent):')
        dialogue = ['       If you do not change cards',
                    'If you change ___ ___ ___ ___ 5TH',
                    'If you change ___ ___ ___ 4TH ___',
                    'If you change ___ ___ 3RD ___ ___',
                    'If you change ___ 2ND ___ ___ ___',
                    'If you change 1ST ___ ___ ___ ___',
                    'If you change ___ ___ ___ 4TH 5TH',
                    'If you change ___ ___ 3RD ___ 5TH',
                    'If you change ___ ___ 3RD 4TH ___',
                    'If you change ___ 2ND ___ ___ 5TH',
                    'If you change ___ 2ND ___ 4TH ___',
                    'If you change ___ 2ND 3RD ___ ___',
                    'If you change 1ST ___ ___ ___ 5TH',
                    'If you change 1ST ___ ___ 4TH ___',
                    'If you change 1ST ___ 3RD ___ ___',
                    'If you change 1ST 2ND ___ ___ ___',
                    'If you change ___ ___ 3RD 4TH 5TH',
                    'If you change ___ 2ND ___ 4TH 5TH',
                    'If you change ___ 2ND 3RD ___ 5TH',
                    'If you change ___ 2ND 3RD 4TH ___',
                    'If you change 1ST ___ ___ 4TH 5TH',
                    'If you change 1ST ___ 3RD ___ 5TH',
                    'If you change 1ST ___ 3RD 4TH ___',
                    'If you change 1ST 2ND ___ ___ 5TH',
                    'If you change 1ST 2ND ___ 4TH ___',
                    'If you change 1ST 2ND 3RD ___ ___',
                    'If you change ___ 2ND 3RD 4TH 5TH',
                    'If you change 1ST ___ 3RD 4TH 5TH',
                    'If you change 1ST 2ND ___ 4TH 5TH',
                    'If you change 1ST 2ND 3RD ___ 5TH',
                    'If you change 1ST 2ND 3RD 4TH ___',
                    '      If you change all the cards']
        print(dialogue[0], checked_TTTTT)
        print(dialogue[1], checked_TTTTF)
        print(dialogue[2], checked_TTTFT)
        print(dialogue[3], checked_TTFTT)
        print(dialogue[4], checked_TFTTT)
        print(dialogue[5], checked_FTTTT)
        if number_of_non_held_cards == 2 or number_of_non_held_cards == 3 or number_of_non_held_cards == 4 or number_of_non_held_cards == 5:
            print(dialogue[6], checked_TTTFF)
            print(dialogue[7], checked_TTFTF)
            print(dialogue[8], checked_TTFFT)
            print(dialogue[9], checked_TFTTF)
            print(dialogue[10], checked_TFTFT)
            print(dialogue[11], checked_TFFTT)
            print(dialogue[12], checked_FTTTF)
            print(dialogue[13], checked_FTTFT)
            print(dialogue[14], checked_FTFTT)
            print(dialogue[15], checked_FFTTT)
        if number_of_non_held_cards == 3 or number_of_non_held_cards == 4 or number_of_non_held_cards == 5:
            print(dialogue[16], checked_TTFFF)
            print(dialogue[17], checked_TFTFF)
            print(dialogue[18], checked_TFFTF)
            print(dialogue[19], checked_TFFFT)
            print(dialogue[20], checked_FTTFF)
            print(dialogue[21], checked_FTFTF)
            print(dialogue[22], checked_FTFFT)
            print(dialogue[23], checked_FFTTF)
            print(dialogue[24], checked_FFTFT)
            print(dialogue[25], checked_FFFTT)
        if number_of_non_held_cards == 4 or number_of_non_held_cards == 5:
            print(dialogue[26], checked_TFFFF)
            print(dialogue[27], checked_FTFFF)
            print(dialogue[28], checked_FFTFF)
            print(dialogue[29], checked_FFFTF)
            print(dialogue[30], checked_FFFFT)
        if number_of_non_held_cards == 5:
            print(dialogue[31], checked_FFFFF)
        interpreter()


    case_royal_flush = []
    case_win = []
    case_straight_flush = []
    case_four_of_a_kind = []
    case_full_house = []
    case_flush = []
    case_straight = []
    case_three_of_a_kind = []
    case_two_pairs = []
    case_jacks_or_better = []
    for i in range(1, 33):
        case_royal_flush.append(int())
        case_win.append(int())
        case_straight_flush.append(int())
        case_four_of_a_kind.append(int())
        case_full_house.append(int())
        case_flush.append(int())
        case_straight.append(int())
        case_three_of_a_kind.append(int())
        case_two_pairs.append(int())
        case_jacks_or_better.append(int())
    win_index = -1
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
        outputer()
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
        outputer()
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
        outputer()
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
        outputer()
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
        outputer()
