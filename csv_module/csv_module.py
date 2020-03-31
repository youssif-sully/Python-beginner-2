###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner 2 python                     #
#       CSV module                            #
#       Read CSV file                         #
#                                             #
###############################################

import csv

print("\n{} {} {}\n".format("-" * 9, "Reader", "-" * 9))

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader, '\n')  # returns an object in some memory address

    # NOTE that the returned value is a list of string
    for element1 in csv_reader:
        print(element1)

print("\n{} {} {}\n".format("-" * 9, "Reader and list manipulation", "-" * 9))

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)    # move the csv_reader to the NEXT value and in other words the
    # first value (FirstName) is escaped by the csv_reader to the NEXT value (JULIE)

    # since the output is a list of string it can be specified which element to print using index
    for element in csv_reader:
        print(element[1])

print("\n{} {} {}\n".format("-" * 9, "DictReader", "-" * 9))

# DictReader returns dictionary where the Header (ID, FirstName, LastName,
# Phone, Email)elements are the Keys
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for element1 in csv_reader:
        print(element1)

print("\n{} {} {}\n".format("-" * 9, "DictReader and dictionary manipulation", "-" * 9))

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # since the output is a dictionary it can be specified which element to print using key
    for element2 in csv_reader:
        print(element2['Email'])
