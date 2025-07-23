import csv
import os.path

# File Format(Id, Name, Address, Email, Phone, Identity, GuestCount, DayCount, CheckinDate, CheckoutDate, RoomNo, Category)
HISTORY_FILE = "history_data.csv"
HEADER = ["BookingId", "Name", "Address", "Email", "Phone", "Identity",
          "GuestCount", "DayCount", "CheckinDate", "CheckoutDate", "RoomNo", "Category"]


def generateTable():
    if not os.path.isfile(HISTORY_FILE):
        file = open(HISTORY_FILE, 'w', newline="")
        file.close()


def checkinUser(name, address, email, phone, identity, guestCount, dayCount, date, roomNo, category):
    id = getId()
    with open(HISTORY_FILE, 'a', newline="") as file:
        writer = csv.writer(file)
        data = [id, name, address, email, phone, identity,
                guestCount, dayCount, date, None, roomNo, category]
        writer.writerow(data)
    return id


def getBookingInfo(bookingId):
    with open(HISTORY_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if (row[0] == bookingId):
                return row


def checkoutUser(bookingId, checkoutDate):
    with open(HISTORY_FILE, 'r', newline="") as rFile, open("temp.csv", "w", newline="") as wFile:
        reader = csv.reader(rFile)
        writer = csv.writer(wFile)
        for row in reader:
            if (row[0] == bookingId):
                row[9] = checkoutDate
            writer.writerow(row)
    os.remove(HISTORY_FILE)
    os.rename("temp.csv", HISTORY_FILE)


def viewRecords():
    list = [HEADER]
    with open(HISTORY_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(row)
    return list


def searchRecordsForCheckin(start, end):
    list = [HEADER]
    with open(HISTORY_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if (start != ""):
                if (row[8] < start):
                    continue
            if (end != ""):
                if (row[8] > end):
                    continue
            list.append(row)
    return list


def searchRecordsForCheckout(start, end):
    list = [HEADER]
    with open(HISTORY_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if (start != ""):
                if (row[9] < start):
                    continue
            if (end != ""):
                if (row[9] > end):
                    continue
            list.append(row)
    return list


def getId():
    with open(HISTORY_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        lastRow = []
        for row in reader:
            lastRow = row

        if (len(lastRow) == 0):
            return 1
        else:
            lastRow[0] + 1
