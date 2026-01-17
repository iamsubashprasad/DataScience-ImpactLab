Correctpass = "OpenAI123"
j=2;


for i in range (3):
    Pass_str = input("Enter your password ")
    if(Correctpass==Pass_str):
        print("Login Successfull")
        break
    elif(i!=3 or i==3):
        print("Wrong Password, You have left", j , "attempt")
        j=j-1
    else:
        print("Account Locked")


