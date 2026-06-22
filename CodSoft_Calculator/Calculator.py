print("=====SIMPLE CALCULATOR=====")
while True:
    print("\nArthimetic operation: ")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.division(/)")
    print("4.Multiplication(*)")
    print("5.Modulus(%)")
    choice=input("\nchoose an operation(1-5): ")
    if choice in ["1","2","3","4","5"]:
        first_number=float(input("Enter first number: "))
        second_number=float(input("Enter second number: "))
        if choice=="1":
            result=first_number+second_number
            print("\nresult:",result)
        elif choice=="2":
            result=first_number-second_number
            print("\nresult:",result)
        elif choice=="3":
            if second_number==0:
                print("\nError:Division by zero is not allowed.")
            else:
                result=first_number/second_number
                print("\nresult:",result)
        elif choice=="4":
            result=first_number*second_number
            print("\nresult:",result)
        elif choice=="5":
            if second_number==0:
                print("\nError:Modulus by zero is not allowed")
            else:
                result=first_number%second_number
                print("\nresult:",result)
    else:
        print("\nInvalid operation selected.")