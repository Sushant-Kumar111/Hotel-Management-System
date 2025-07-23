import RoomsManager
import HistoryManager


def init():
    roomNo = input("Enter room number: ")
    print()
    roomInfo = RoomsManager.getRoomInfo(roomNo)
    if (len(roomInfo) == 0):
        print("Room not found.\n")
    else:
        bookingId = roomInfo[2]
        if (bookingId == ""):
            print("Room is not booked.\n")
        else:
            bookingInfo = HistoryManager.getBookingInfo(bookingId)
            print("Room was booked in the name of:", bookingInfo[1])
            choice = input("Confirm to checkout? (Yes/No): ")
            print()
            if choice == "Yes":
                date = input("Enter checkout date (yyyy-mm-dd): ")
                print()
                HistoryManager.checkoutUser(bookingId, date)
                RoomsManager.updateRoomStatus(roomNo, None)
                print("Checkout successful!")
                print()
                pass
            elif choice == "No":
                print("Checkout canceled.\n")
            else:
                print("Invalid choice. Checkout failed.\n")