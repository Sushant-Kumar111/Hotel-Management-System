import RoomsManager
import CategoryManager
import HistoryManager


def init():
    print("Room Categories:")
    categoriesMap = CategoryManager.getCategories()
    categories = list(categoriesMap.keys())
    availableRooms = RoomsManager.getAvailableRooms(categories)

    for index in range(1, len(categories) + 1):
        category = categories[index - 1]
        print(str(index) + ". " + category + " - ₹" +
              categoriesMap[category], "(" + str(len(availableRooms[category])) + ")")

    choice = int(input("Enter your selection: "))
    print()

    if (choice not in range(1, len(categories) + 1)):
        print("Invalid choice. Checkin failed.\n")
    else:
        category = categories[choice-1]
        rate = int(categoriesMap[category])
        rooms = availableRooms[category]
        if (len(rooms) > 0):
            getDetailsAndCheckin(rate, category, rooms[0])
        else:
            print("No room available for the selected category.\n")


def getDetailsAndCheckin(rate, category, roomNo):
    name = input("Enter guest's name: ")
    address = input("Enter guest's address: ")
    phone = input("Enter guest's phone number: ")
    email = input("Enter guest's email address: ")
    identity = input("Enter guest's aadhar number: ")
    guestCount = int(input("Enter guest count: "))
    dayCount = int(input("Enter days of booking: "))
    date = input("Enter checkin date(yyyy-mm-dd): ")
    print()

    print("Total cost:", rate * guestCount * dayCount)
    choice = input("Confirm checkin? (Yes/No): ")
    if choice == "Yes":
        bookingId = HistoryManager.checkinUser(name, address, email, phone,
                               identity, guestCount, dayCount, date, roomNo, category)
        RoomsManager.updateRoomStatus(roomNo, bookingId)
        print("Checkin successful! Booked room:", roomNo)
        print()
    elif choice == "No":
        print("Checkin canceled.\n")
    else:
        print("Invalid choice. Checkin failed.\n")