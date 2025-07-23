import csv
import os.path

# File Format(Room Category, Room Price)
CATEGORY_FILE = "category_data.csv"


def generateTable():
    if not os.path.isfile(CATEGORY_FILE):
        file = open(CATEGORY_FILE, 'w', newline="")
        enterSampleData(file)
        file.close()


def getCategories():
    catergories = dict()

    with open(CATEGORY_FILE, 'r', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            catergories[row[0]] = row[1]

    return catergories


def enterSampleData(file):
    writer = csv.writer(file)
    data = [
        ["Economy", 850],
        ["Deluxe", 1500],
        ["Luxury", 5000],
        ["Royal", 8000],
    ]
    writer.writerows(data)
