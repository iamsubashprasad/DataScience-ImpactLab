amount = int(input("Enter the amount you wish to withdraw"))
if amount%100==0:
    print(f"(you have Dispense {amount} rupees from the account)")
else:
    print("you have entered invalid amount")
    