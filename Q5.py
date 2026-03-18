file = open("my_file.txt", "a")
running = True
while running == True:
    user_addition = input("What would you like to add? ")
    if user_addition.lower() == "quit":
        print("OK, bye!")
        running = False
    else:
        file.write(user_addition)
        continue

file.close()
