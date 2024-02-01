#ask user what operation it wants to do
def operation():
    while True:
        print()
        op=input("What calculation do you want me to do: ")

        if op =='+' or op =='-' or op =='*' or op =='/':
            break
        else:
            print("I don't know what that is.")
            print("Try typing either '+','-','*' or '/'")
    return op

#check if numbers is a number
def num_check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#ask user for two numbers(make sure they are numbers)
def numbers(op):
    print()
    while True:
        num1=input("Enter the first Number: ").strip()
        if num_check(num1):
            num1=float(num1)
            break
        else:
            print("It is not a number\n")

    while True:
        num2=input("Enter the second Number: ").strip()
        if num_check(num2):
            num2=float(num2)
            if num2==0.0 and op=='/':
                print("You can't divide by 0\n")
            else:
                break
        else:
            print("It is not a number\n")

    return num1,num2

#Calculate it
def calculate(num1,num2,op):
    if op=='+':
        ans=num1+num2
    elif op=='-':
        ans=num1-num2
    elif op=='*':
        ans=num1*num2
    elif op=='/':
        ans=num1/num2

    print("%f%s%f=%f" %(num1,op,num2,ans))

#Ask user if they wanna use it more
def cont(yes):
    while True:
        print()
        x=input("Do u want to keep using me(y/n): ").lower()
        if x=='y':
            return True
        elif x=='n':
            return False
        else:
            print("Either type y for yes or n for no.\n")
    


#main
print("I am a Calculator")
yes=True

while yes: #repeat until they dont want to calculate anymore
    op=operation()
    num1,num2=numbers(op)
    calculate(num1,num2,op)
    yes=cont(yes)