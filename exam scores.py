#exam scores.py
#calculate the letter grade

def main():
    grade = float(input("Enter a number grade: "))

    if grade >= 90:
        print("Your grade is A")
    elif grade >= 80:
        print("Your grade is B")
    elif grade >= 70:
        print("Your grade is C")
    elif grade >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")

main()
