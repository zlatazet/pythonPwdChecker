import string
import getpass


def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very Bad Password!"
    elif strength == 2:
        remarks = "Not a good password"
    elif strength == 3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a strong password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    print('Your password has: ')
    print(f'{lower_count} lowercase characters')
    print(f'{upper_count} uppercase characrets')
    print(f'{num_count} numeric characters')
    print(f'{wspace_count}vwhitespace characters')
    print(f'{special_count} special characters')

    print(f'Password strength: {strength}')
    print(f'Hint: {remarks}')


def ask_pwd(another_pwd=False):
    valid = False
    if another_pwd:
        choice = input('Do you want to enter another pwd (y/n): ')
    else:
        choice = input("Do you want to change pwd strength (y/n): ")

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, try again')


if __name__ == '__main__':
    print('+++ welcome to PWD checker +++')
    ask_pwd = ask_pwd()
    while check_pwd:
        check_pwd()
        ask_pwd = ask_pwd(True)
