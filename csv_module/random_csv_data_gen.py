###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner 2 python                     #
#       CSV and random module                 #
#       Random CSV data generator             #
#                                             #
###############################################

# Two txt files one with first names and the other with last names
# The idea is to create random csv data file and contains the following header and data
# ID, FirstName, LastName, birthDate, Phone, Email


import csv
import random

# reading the last_names file and storing it to a list
with open('last_names.txt', 'r') as last_name_file:
    # empty list to house the last names
    last_names = []
    for line in last_name_file:
        # append add to the list
        # strip remove any whitespaces from the end and the beginning of the string
        last_names.append(line.strip())

# reading and storing the first names
with open('first_names.txt', 'r') as first_names_file:
    first_names = []
    for line in first_names_file:
        first_names.append(line.strip())

with open('new_data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # element_id --> ID in the CSV file
    element_id = 1

    # NOTE since we are using writer not DictWriter we can't use fieldsnames
    csv_writer.writerow(['ID', 'FirstName', 'LastName', 'birthDate', 'Phone', 'Email'])

    # for creating 100 data inputs
    for line in range(100):
        # SEE random module
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        # SEE formatting
        birth_date = "{}-{}-{}".format(random.randint(1970, 2006),
                                       random.randint(1, 12),
                                       random.randint(1, 28))

        phone = "{:03}-{:03}-{:04}".format(random.randint(1, 99),
                                           random.randint(1, 999),
                                           random.randint(1, 9999))

        email = "{}.{}@fakemail.at".format(first_name.lower(), last_name.lower())

        csv_writer.writerow([element_id, first_name, last_name, birth_date, phone, email])
        element_id += 1
