import RoomsManager
import HistoryManager


def init():
    while True:
        print("1. View Records")
        print("2. Search by Room No")
        print("3. Search by Checkin Date")
        print("4. Search by Checkout Date")
        print("5. Return")
        choice = int(input("Enter your selection: "))
        print()

        if choice == 1:
            records = HistoryManager.viewRecords()
            for record in records:
                print(record)
            print()
        elif choice == 2:
            roomNo = input("Enter room no: ")
            roomInfo = RoomsManager.getRoomInfo(roomNo)
            bookingId = roomInfo[2]
            if (bookingId == ""):
                print("Room is not booked.\n")
            else:
                bookingInfo = HistoryManager.getBookingInfo(bookingId)
                print(HistoryManager.HEADER)
                print(bookingInfo)
            print()
        elif choice == 3:
            start = input("Enter start date(yyyy-mm-dd): ")
            end = input("Enter end date(yyyy-mm-dd): ")
            records = HistoryManager.searchRecordsForCheckin(start, end)
            for record in records:
                print(record)
            print()
        elif choice == 4:
            start = input("Enter start date(yyyy-mm-dd): ")
            end = input("Enter end date(yyyy-mm-dd): ")
            records = HistoryManager.searchRecordsForCheckout(start, end)
            for record in records:
                print(record)
            print()
        elif choice == 5:
            break
        else:
            print("Please choose from the given choices\n")
