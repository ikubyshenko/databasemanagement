from Queries import *

def menu():
    while True:
        print("\n=== EVENT SYSTEM ===")
        print("1. Add Customer")
        print("2. Add Event")
        print("3. Buy Ticket")
        print("4. Add Review")
        print("5. Show Customers")
        print("6. Show Reviews")
        print("7. Update Event Status")
        print("8. Update Customer Phone")
        print("9. Delete Review")
        print("10. Delete Ticket")
        print("11. Exit")

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
            show_customers()

        elif choice == "6":
            show_reviews()

        elif choice == "7":
            update_event_status()

        elif choice == "8":
            update_customer_phone()

        elif choice == "9":
            delete_review()

        elif choice == "10":
            delete_ticket()

        elif choice == "11":
            break


menu()