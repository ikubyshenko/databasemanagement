from Queries import *

def menu():
    while True:
        print("\n=== EVENT SYSTEM ===")
        print("1. Add Customer")
        print("2. Add Event")
        print("3. Buy Ticket")
        print("4. Add Review")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            add_event()

        elif choice == "3":
            buy_ticket()
        
        elif choice == "4":
            add_review()
    
        elif choice == "5":
            break


menu()