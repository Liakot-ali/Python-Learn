cnt = 1
while cnt <= 10:
    print("Hello")
    print("This is in loop")
    cnt += 1
print("End of while loop")

#--------guessing game----------
answer = 5
count = 0
print("Enter a integer number between 1-10")
while True:
    take = int(input("Guess : "))
    count += 1

    if take == answer:
        print("You are win")
        break
    if count == 3:
        print("You are fail")
        break
# car game

while True:
    cmd = input(">")
    if cmd.lower() == "start":
        print("Car started")
    elif cmd.lower() == "stop":
        print("Car stopped")
    elif cmd.lower() == "help":
        print('''
start - Start the Car
stop - Stop the Car
quit - Quit from the Game
help - To see details
''')
    elif cmd.lower() == "quit":
        print("Your quit the game")
        break
    else:
        print("Input not understand")
        print('''
        start - Start the Car
        stop - Stop the Car
        quit - Quit from the Game
        help - To see details
        ''')

for i in "Liakot":
    print(i)
