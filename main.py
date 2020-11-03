print("Hi there, my name is Alexis and I was created to help you convert kilometers into miles.")

while True:
    route = int(input("Enter kilometers: "))

    print("This corresponds to " + str(int(route) / 1.61) + " miles.")

    another_conversion = input("Do you want to do another conversion? (yes/no) ")

    if another_conversion == "no":
        print("Ok, that's it for today. Have a good night.")
        break
    else:
        print("Great, let's do another one!")

