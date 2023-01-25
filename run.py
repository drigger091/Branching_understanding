import substract as sb
import add as ad

def run():

    print("What woud you like to do?")
    while(True):
        print("1: Would you like to substract two numbers?")
        print("2: Would you like to add two numbers?")
        print("3: Would you like to multiply two numbers?")
        print("4:Exit")


        ch = int(input("Please enter your choice?"))

        if ch == 1:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number?"))
            sb.sub(x,y)
        
        if ch == 2:
            x = int(input("Please enter the first number"))
            y = int(input("Please enter the second number?"))
            ad.add(x,y)

        if ch == 3:
            pass

        if ch == 4:
            exit()