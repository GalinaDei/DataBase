patients_list = [{'ID': "", 'Surname': "", 'Name': "", 'Middle name': "", 'Birthday': "",
            'Adress': "",'Phone': "",'Main diagnosis': "",
            'Concomitant diagnosis1': "", 'Concomitant diagnosis 2': ""}]
def data_receive():
    print("New record")
    with open('ID.txt', 'r+') as f:
        id0 = f.readline()
    if id0 == "":
        id = 1
    else:
        id = int(id0) + 1
    with open('ID.txt', 'w') as f:
        f.write(str(id))
    Surname = input("Surname: ")
    Name = input("Name: ")
    Middle_name = input("Middle_name: ")
    Birthday = input("Birthday: ")
    Adress = input("Adress: ")
    Phone = input("Phone: ")
    Main_diagnosis = input("Main_diagnosis: ")
    Concomitant_diagnosis1 = input("Concomitant_diagnosis1: ")
    Concomitant_diagnosis2 = input("Concomitant_diagnosis2: ")

    patients = {'ID': id, 'Surname': Surname, 'Name': Name, 'Middle name': Middle_name, 'Birthday': Birthday,
            'Adress': Adress,'Phone': Phone,'Main diagnosis': Main_diagnosis,
            'Concomitant diagnosis1': Concomitant_diagnosis1, 'Concomitant diagnosis 2': Concomitant_diagnosis2}

    return patients
