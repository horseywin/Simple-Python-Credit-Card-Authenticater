def verify_card_number(raw_card_number):
    raw_card_number = str(raw_card_number)
    print(f'RAW CARD NUMBER: {raw_card_number}')

    card_format = str.maketrans(
        {
            ' ': '',
            '-': ''
        }
    )
    print(f'CARD_FORMAT: {card_format}')

    card_number = raw_card_number.translate(card_format)
    print(f'CARD NUMBER: {card_number}')

    card_number_reversed = card_number[::-1]
    print(f'CARD NUMBER REVERSED: {card_number_reversed}')

    sum_odd = 0
    sum_even = 0

    for digit in card_number_reversed[::2]:
        print(f'ADDING {digit}')
        sum_odd += int(digit)

    print(f'SUM OF ODD DIGITS: {sum_odd}')

    for digit in card_number_reversed[1::2]:
        digit = int(digit) * 2
        print(f'DOUBLED {digit // 2} TO MAKE IT {digit}')
        if int(digit) >= 10:
            print(f'{digit} IS >= THAN 10')
            print(f'{digit // 10} + {digit % 10} is {(digit // 10) + (digit % 10)}')
            digit = (digit // 10) + (digit % 10)
            print(f'ADDING {digit}...')
        else:
            print(f"LOOK'S LIKE {digit} IS LESS THAN 10")
            print(f'ADDING {digit}...')
        sum_even += int(digit)

    print(f'SUM OF EVEN DIGITS: {sum_even}')
    sum_digits = int(sum_even) + int(sum_odd)
    print(f'SUM OF ALL DIGITS IS {sum_digits}')
    print('VERIFYING...')

    if (sum_digits % 10) == 0:
        print(f'{sum_digits % 10} is equal to 0')
        print('CARD IS VALID')
    else:
        print(f'{sum_digits % 10} is not equal to 0')
        print('CARD IS INVALID')


# verify_card_number(input('ENTER CARD NUMBER'))
verify_card_number('377111445311026')