import csv
import os.path
import random

# File Format(Room No, Room Category, Booked Status)
ROOM_FILE = "room_data.csv"


def generateTable():
    if not os.path.isfile(ROOM_FILE):
        file = open(ROOM_FILE, 'w', newline="")
        enterSampleData(file)
        file.close()


def updateRoomStatus(roomNo, newStatus):
    with open(ROOM_FILE, 'r', newline="") as rFile, open("temp.csv", 'w', newline="") as wFile:
        reader = csv.reader(rFile)
        writer = csv.writer(wFile)
        for row in reader:
            if (row[0] == roomNo):
                row[2] = newStatus
            writer.writerow(row)

    os.remove(ROOM_FILE)
    os.rename("temp.csv", ROOM_FILE)


def getAvailableRooms(categories):
    rooms = dict()

    for category in categories:
        rooms[category] = []

    with open(ROOM_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            if (row[2] == ""):
                rooms[category].append(row[0])

    return rooms


def getRoomInfo(roomNo):
    with open(ROOM_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (row[0] == roomNo):
                return row
    return []


def enterSampleData(file):

    categories = ["Economy", "Deluxe", "Luxury", "Royal"]
    writer = csv.writer(file)
    data = []
    for x in range(1, 61):
        data.append(
            [x, categories[random.randint(0, 3)], None])
    writer.writerows(data)