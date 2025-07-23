import RoomsManager
import CategoryManager
import HistoryManager
import Checkin
import Checkout
import History

print("HOTEL MANAGEMENT")
print("================\n")

RoomsManager.generateTable()
CategoryManager.generateTable()
HistoryManager.generateTable()

while True:
    print("1. Checkin")
    print("2. Checkout")
    print("3. History")
    print("4. Exit")
    choice = int(input("Enter your selection: "))
    print()

    if choice == 1:
        Checkin.init()
    elif choice == 2:
        Checkout.init()
    elif choice == 3:
        History.init()
    elif choice == 4:
        break
    else:
        print("Please choose from the given choices\n")
