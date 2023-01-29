import csv

from prettytable import PrettyTable

import logger


def show_all():

    my_table = PrettyTable()
    with open('Patients.csv', 'r', newline='\n') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if count == 0:
                my_table.field_names = row
                count += 1
            else:
                my_table.add_row(row)
    print(my_table)
    logger.logging.info("Search has done")


def find_record():
    x = input("Enter word for search: ")
    if x != "":
        my_table = PrettyTable()
        with open('Patients.csv', 'r', newline='\n') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if count == 0:
                    my_table.field_names = row
                    count += 1
                else:
                    if x in row:
                        my_table.add_row(row)
        print(my_table)
    else:
        return

    logger.logging.info("Search has done")
