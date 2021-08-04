import os

def newFile():
    dir = input("What folder would you like the file to be saved in? ")
    file = input("What would you like the file to be named? ")
    name = input("What is your name? ")
    address = input("What is your address? ")
    phone = input("What is your phone number? ")

    if not os.path.exists(f"./{dir}"):
        os.makedirs(f"./{dir}")
    
    f = open(f"{dir}/{file}", "x")
    f.write(f"{name}, {address}, {phone}")
    f.close()

    f = open(f"{dir}/{file}", "r")
    print(f.read())
    f.close()

def openFile():
    dir = input("What folder is the file saved in? ")
    file = input("What is the file name? ")

    f = open(f"{dir}/{file}", "r")
    print(f.read())
    f.close()

def main():
    response = input("Would you like to [open] an existing file or create a [new] one? ")

    while response != "open" and response != "o" and response != "new" and response != "n":
        print("Error: invalid input")
        response = input("Would you like to [open] an existing file or create a [new] one? ")

    if response == "new" or response == "n":
        newFile()
    elif response == "open" or response == "o":
        openFile()
    else:
        print("Error: unknown error")

if __name__ == "__main__":
    main()