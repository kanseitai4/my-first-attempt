import random

counter = 0
print("Hi! you want to sing in?\n")
sign_in = input("Write : yes or no\n").strip().lower()
if sign_in == "yes":
    print("Enter you nickname\n")
    nickname = input().strip().lower()
    print("What you want to do?")
    print("'guessing game', 'jojo stand information', 'calculator', 'russian roulette'")
    function = input().strip().lower()
    if function == "guessing game":
        while counter <= 3:
            guessing_number = random.randrange(10)
            print("i hide number, try to guess it!\n")
            guess_number = int(input())
            if guess_number == guessing_number:
                print("YES! you win this life")
                counter += 1
            elif guess_number < guessing_number:
                print("you number is too small")
                counter += 1
            elif guess_number > guessing_number:
                print("you number is too big!")
                counter += 1
    elif function == "jojo stand information":
        print("Which part stand you want to know? only from 3-5 parts")
        part = int(input())
        if part == 3:
            jojo_3_season_stands = {
                "Jotaro": "Star Platinum",
                "Joseph": "Hermit purple",
                "Polnareff": "Silver Chariot",
                "Abdul": "Magician Red",
                "Kakoyin": "Elephant Green",
                "Dio": "The World",
                }
            print("Enter character that stand you want to know(enter only famous character, plz)\n")
            character = input().strip().title()
            print(jojo_3_season_stand.get(character, "We dont know info about this character, sorry"))
        elif part == 4:
            jojo_4_season_stands = {
                "Josuke": "Crazy Diamond",
                "Jotaro": "Star Platinum",
                "Okyasu": "The Hand",
                "Koichi": "Echoes",
                "Rohan": "Heaven's Door",
                "Kira": "Killer Quin",
                }
            print("Enter character stand you want to know\n")
            character = input().strip().title()
            print(jojo_4_season_stands.get(character, "No info about this character"))
        elif part == 5:
            jojo_5_season_stands = {
                "Giorno": "Gold Experience Requiem",
                "Buchelatti": "Sticky fingers",
                "Narancia": "Aerosmith",
                "Abakkio": "Moody Blues",
                "Fugo": "Purple Haze",
                "Mista": "Sex Pistols",
                }
            print("What character stand info you want to know about?")
            character = input().strip().title()
            print(jojo_5_season_stands.get(character, "No such info about this stand and character, sorry"))
        elif part == 1 or 2 or part > 5:
            print("we dont know information about this part stands or this part without stands")    
    elif function == "russian roulette":
        unlucky_numbers = [1, 6, 3, 8, 2]
        lucky_numbers = [4, 5, 7, 9, 10]
        print("Welcome to the russian roulette! you should pick one number  from 1 to 10\n")
        roulette_number = int(input())
        if roulette_number in unlucky_numbers:
            print("YOU DIE!")
        elif roulette_number in lucky_numbers:
            print("You survive")
    elif function == "calculator":
        print("Hello! you in the calculator, choose one operation : '+', '-', '*', '/' ")
        operation = input().strip().lower()
        if operation == '+':
            print("Enter first number : ")
            num1 = int(input())
            print("Enter second number : ")
            num2 = int(input())
            sum = num1 + num2
            print(f"sum is {sum}")
        elif operation == '-':
            print("Enter first number : ")
            num1 = int(input())
            print("Enter second number : ")
            num2 = int(input())
            sum = num1 - num2
            print(f"sum is {sum}")
        elif operation == '*':
            print("Enter first number : ")
            num1 = float(input())
            print("Enter second number : ")
            num2 = float(input())
            sum = num1 * num2
            print(f"sum is {sum}")
        elif operation == '/':
            print("Enter first number : ")
            num1 = float(input())
            print("Enter second number : ")
            num2 = float(input())
            sum = num1 / num2
            print(f"sum is {sum}")