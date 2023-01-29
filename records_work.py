import csv
import os
from prettytable import PrettyTable
import logger


def csv_create():
    with open('ID.txt', 'r') as f:
        id = f.readline()

    if id == "":
        with open("Patients.csv", "a") as data:
            names = ["ID", "Surname", 'Name', 'Middle name', 'Birthday', 'Adress', 'Phone', 'Main diagnosis',
                     'Concomitant diagnosis1', 'Concomitant diagnosis 2']
            file_writer = csv.DictWriter(data, fieldnames=names)
            file_writer.writeheader()
    logger.logging.info("New record")


def record_to_add(dict):
    with open("Patients.csv", "a") as data:
        names = list(dict.keys())
        file_writer = csv.DictWriter(data, fieldnames=names)
        file_writer.writerow(dict)
        logger.logging.info("New record")


def delete_record():
    x = input("Enter word for search: ")
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
                    count += 1
    print(my_table)
    if count >= 2:
        y = input("Enter ID to confirm deletion or Enter to exit: ")
        with open('Patients.csv', 'r') as inp, open('Patients1.csv', 'w') as out:
            writer = csv.writer(out)
            count1 = 1
            for row in csv.reader(inp):
                count1 += 1
                if count1 % 2 == 0:
                    if row[0] != y:
                        writer.writerow(row)
            print("Record has updated.")

        os.remove('Patients.csv')
        os.rename('Patients1.csv', 'Patients.csv')
        logger.logging.info("Records update")
        return
    else:
        return


def edit_record():
    x = input("Enter word for search: ")
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
                    count += 1
                else:
                    print("Record not found")
    print(my_table)
    if count >= 2:
        y = input("Enter ID to continue edition or Enter to exit: ")

        with open('Patients.csv', 'r') as inp, open('Patients1.csv', 'w') as out:
            writer = csv.writer(out)
            count1 = 1
            for row in csv.reader(inp):
                count1 += 1
                if count1 % 2 == 0:
                    if row[0] != y:
                        writer.writerow(row)
                    else:
                        Surname = input("Surname: ")
                        Name = input("Name: ")
                        Middle_name = input("Middle_name: ")
                        Birthday = input("Birthday: ")
                        Adress = input("Adress: ")
                        Phone = input("Phone: ")
                        Main_diagnosis = input("Main_diagnosis: ")
                        Concomitant_diagnosis1 = input("Concomitant_diagnosis1: ")
                        Concomitant_diagnosis2 = input("Concomitant_diagnosis2: ")
                        new_value = [y, Surname, Name, Middle_name, Birthday, Adress, Phone,
                                     Main_diagnosis, Concomitant_diagnosis1, Concomitant_diagnosis2]
                        writer.writerow(new_value)
            print("Record has updated.")

        os.remove('Patients.csv')
        os.rename('Patients1.csv', 'Patients.csv')
        logger.logging.info("Records update")
    else:
        return
