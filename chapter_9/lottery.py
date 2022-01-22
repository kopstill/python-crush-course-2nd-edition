from random import randint

lottery_winning = (6, 17, 23, 32, 46, 59, 61, 78, 83, 95, 'L', 'F', 'G', 'N', 'P')


def generate_prize():
    string = ''
    for x in range(4):
        string += str(lottery_winning[randint(0, len(lottery_winning) - 1)])
    return string


win_str = generate_prize()


def is_win(user_character):
    if user_character in lottery_winning:
        print('Congratulations! You win!')
    else:
        print('Sorry, you missed the prize!')


print(f'Win string is: {win_str}')
is_win(randint(0, 100))
