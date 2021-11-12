def greet(bot_name, birth_year):
    print(" BOT :Hello! My name is {0}.".format(bot_name))
    print(" BOT :I was created in {0}.".format(birth_year))


def remind_name():
    print(' BOT :Please, remind me your name.')
    name = input()
    print(" BOT :What a great name you have, {0}!".format(name))

def guess_collagename():
   print(' BOT :in which college you are studying.')
   collagename= input()
   print(" BOT : WOW KIET clg which supperb supporytive faculty with plent of job offers and co-operate collage with Hi-Tech faclities")


def remind_birthday():
    print(' BOT :Please, remind me your birthday')
    birthday = input()
    print(" BOT :what a great day you had born,{0}!".format(birthday))

    input()

def guess_age():
    print(' BOT :Let me guess your age.')
    print(' BOT :Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(" BOT :Your age is {0}; that's a good time to start programming!".format(age))


def count():
    print(' BOT : Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print(" BOT :{0} !".format(counter))
        counter += 1


def test():
    print(" BOT : Let's test your programming knowledge.")
    print(" BOT : Why do we use methods?")
    print(" BOT : 1. To repeat a statement multiple times.")
    print(" BOT : 2. To decompose a program into several small subroutines.")
    print(" BOT : 3. To determine the execution time of a program.")
    print(" BOT : 4. To interrupt the execution of a program.")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, TRY AGAIN  the option which you have picked is WRONG.")
        guess = int(input())

    print('BOT :YEAH you had picked the right answer, have a nice day!')
    print('     .................................')
    print('     .................................')
    print('     .................................')


def end():
    print('BOT : CONGRATULATIONS, have a nice day!')
    print('     .................................')
    print('     .................................')
    print('     .................................')
    input()
    
greet('BOT KARUN', '2021')  # change it as you need
remind_name()
guess_collagename()
remind_birthday()
guess_age()
count()
test()
end()