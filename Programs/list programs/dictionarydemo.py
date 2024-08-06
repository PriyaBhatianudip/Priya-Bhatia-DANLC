class DictionaryDemo:
    # single dictionary
    emp_list = {"id": 101, "Name": "Kiran Singh", "Age": 25}

    # set of dictionaries in a list
    emp_listx = [
                    {"id": 101, "Name": "Kiran Singh", "Age": 25},
                    {"id": 102, "Name": "K Singh", "Age": 23} #e
    ]

    # nested dictionary
    emp_list1 = {
        "1": {"id": 101, "Name": "Kiran Singh", "Age": 25},
        "2": {"id": 102, "Name": "K Singh", "Age": 23}
    }

    def printdictionary(self):
        print(self.emp_list)

    def addelements(self):
        key1 = input("Enter key value : ")
        value1 = input("Enter value : ")
        # self.emp_list.update({key1 : value1})

        self.emp_list[key1] = value1
        # how to call another function from one function when in same class
        self.printdictionary()



class Customer:
    dd = DictionaryDemo()

    def addnewemployee(self):
        emp ={}
        id = int(input("Enter id : "))
        name = input("Enter name : ")
        age = int(input("Enter Age : "))

        emp.update({"id": id, "name": name, "age": age})
        self.dd.emp_listx.append(emp)

        self.display()


    def display(self):
        print("Employee records")
        for e in self.dd.emp_listx:
            print(e)

    def menu(self):

        while True:
            print("1. Add New Employee")
            print("2. Update an Employee")
            print("3. Delete an Employee")
            print("4. Search an Employee Record")
            print("5. sort records according to Name")
            print("6. Exit")
            print("Enter your choice :")
            choice = int(input())

            if choice == 1:
                self.addnewemployee()
            elif choice == 2:
                print()
            elif choice == 3:
                print()
            elif choice == 4:
                print()
            elif choice == 5:
                print()
            elif choice == 6:
                print("Good Bye!!")
                break
            else:
                print("Wrong choice!!")


cc = Customer()
cc.menu()