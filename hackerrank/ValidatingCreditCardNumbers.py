import re

#https://www.hackerrank.com/challenges/validating-credit-card-number/problem


def validate(card_number):

    if not re.match(r'((4|5|6)\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d)|((4|5|6)\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d)',
                    card_number):
        return False

    # check if card number starting from 4,5 or 6
    if card_number[0] not in "456":
        return False

    # check if card number is greater than 16 and
    if not (len(card_number) == 16 or (len(card_number) == 19 and card_number[4] == '-' and card_number[9] == '-' and card_number[14] == '-')):
        return False

    card_number = card_number.replace("-","")

    for i in range(len(card_number) - 3):
        if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
            return False

    return True


def validate_credit_card(card_number):

    cc_number = []

    for ch in card_number:

        count = 0

        if ch.isdigit() or ch == '-':

            count += 1
            if ch.isdigit():
                cc_number.append(int(ch))
        else:
            return False

    if len(cc_number) == 0 or len(cc_number) > 16 or cc_number[0] not in range(4,7):
        return False

    return True


if __name__ == '__main__':

    cc = ['6133-3767-8944-4856','4123456789123456', '5123AS-4567-8912-3456', '61234-567-8912-3456', '1123356789123456A',
          '5123 - 3567 - 8912 - 3456', '5671qe' ]

    for card in cc:
        print(validate(card))

