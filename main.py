def show_balance(balance):
    print("********************")
    print(f"Your balance is NOK{ balance:.2f}")
    print("********************")

def deposit():
    print("********************")
    amount = float(input("Enter amount to deposit: "))
    print("********************")

    if amount < 0: 
        print("********************")
        print("You can't deposit a negative amount")
        print("********************")
        return 0
    else:
        return amount


def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to withdrawn: "))
    print("********************")

    if amount > balance:
        print("********************")
        print("You can't withdraw more than your balance")
        print("********************")
        return 0
    elif amount < 0:
        print("********************")
        print("Amount must be greater than 0")
        print("********************")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("********************")
        print ("     Banking program    ")
        print("********************")
        print ("1. Show balance")
        print ("2. Deposit")
        print ("3. Withdraw")   
        print ("4. Exit")  
        print("********************") 

        choice = input("Enter choice(1-4) : ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()   
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False  
        else: 
            print("********************")  
            print ("That is an invalid choice")
            print("********************")
    print("********************")
    print ("Thank you have a nice day!")
    print("********************")


is_running = True
balance = 0

while is_running:
    print ("Banking program")
    print ("1. Show balance")
    print ("2. Deposit")
    print ("3. Withdraw")   
    print ("4. Exit")   

    choice = input("Enter choice(1-4) : ")

    if choice == '1':
        show_balance(balance)
    elif choice == '2':
       balance += deposit()   
    elif choice == '3':
        balance -= withdraw(balance)
    elif choice == '4':
        is_running = False  
    else:   
        print ("That is an invalid choice")

print ("Thank you have a nice day!")

if __name__ == '__main__':  main()