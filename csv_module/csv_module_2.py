###############################################
#                                             #
#       Created by Youssef Sully              #
#       Beginner 2 python                     #
#       CSV module                            #
#       Write CSV file                        #
#                                             #
###############################################

import csv

print("\n{} {} {}\n".format("-" * 9, "Writer", "-" * 9))

# newline='' to eliminate any unwanted \n in the csv file
with open('write_data.csv', 'w', newline='') as csv_write_file_1:
    # initializing writer
    csv_writer = csv.writer(csv_write_file_1)
    # the argument should be iterable like string, list and dictionary
    csv_writer.writerow(['1', 'Youssef', 'Sully', '6465-6546-6546', 'youssefsully80@fakeemail.at'])

print("Check write_data.csv file")

print("\n{} {} {}\n".format("-" * 9, "Writer", "-" * 9))

with open('dict_write_data.csv', 'w', newline='') as csv_write_file_2:
    # creating a HEADER list
    fieldnames = ['ID', 'FirstName', 'LastName', 'Phone', 'Email']

    # fieldnames=fieldnames using the list above as header
    # DictWriter writes dictionary (also check DictReader)
    csv_writer = csv.DictWriter(csv_write_file_2, fieldnames=fieldnames)

    # writes the header
    csv_writer.writeheader()
    csv_writer.writerow({'ID': '1',
                         'FirstName': 'Youssef',
                         'LastName': 'Sully',
                         'Phone': '6465-6546-6546',
                         'Email': 'youssefsully80@fakeemail.at'
                         })

print("Check dict_write_data.csv file")