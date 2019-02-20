#ticket
#Figure out whether you deserve a ticket or not and for how much
#BY: Ifeatu Okaneme

def main():
    mph = float(input("Enter your mph: "))

    limit = float(input("Enter the speed limit: "))

    #fine is $50 plus $5 times the speed over the limit
    fine = 50 + 5 * (mph - limit)

    #for when the speed is over 90 ONLY
    penalty = 200 + fine

    if mph >= 90:

        print(mph, "Your fine is $", penalty)

    elif mph >= limit:

        print(mph, "Your fine is $", fine)

    else:

        print(mph)

main()
