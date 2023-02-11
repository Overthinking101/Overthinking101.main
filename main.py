print("Hello fellow soldier. Welcome to the stupidest "
      "program ever created.")
name = input("What is your name soldier? ")

print("That's an odd name. Anyways, lets move on.")
age = input("How old are you soldier? ")

AgeYesNo = "0"
AgeYesAnswer = "yes"
AgeNoAnswer = "no"

while AgeYesNo != AgeYesAnswer or AgeYesNo != AgeNoAnswer:
    print("Please answer yes or no. If you want to quit, type 'quit'.")
    AgeYesNo = str(input())

    if AgeYesNo == AgeYesAnswer:
        print("Ok, let's move on then")
        break

    if AgeYesNo == AgeNoAnswer:
        print("I don't trust you now")
        break
    else:
        if AgeYesNo == "quit":
            exit("Goodbye then")

