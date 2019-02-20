#credits.py
#Calculates a college student's standing based on their credits
#BY: Ifeatu Okaneme

def main():
    credit = float(input("Enter your amount of credits: "))

    if credit >= 26:
        print("You are a Senior")
    elif credit >= 16:
        print("You are a Junior")
    elif credit >= 7:
        print("You are a Sophmore")
    #elif credit >= 0:
    #    print("You are a Freshman")
    else:
        print("You are a Freshman")

main()
