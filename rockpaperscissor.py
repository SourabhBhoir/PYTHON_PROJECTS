import random

user_win = 0
com_win =0

while True:
    user_input = int("type r/p/s for play").lower()
    if user_input == 'q':
        quit()

    if user_input not in [r,p,s]:
        continue

    random_number = random.randint(0,1)
    print(random_number)

    if random_number == 0 and user_input == p:
        print("user_win")
        if random_number == 1 and user_input == s:
            print('user win')
    else:
     print(match tie!)           
print("good byee!")