n =  int(input("Enter the number"))
for i in range(1,n):
    if i<=n:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3==0 or i % 5!=0:
            print("Fizz")
        elif i %3!=0 or i %5==0:
            print("Buzz")
    else:
        print("The number you entered is" ,i)



