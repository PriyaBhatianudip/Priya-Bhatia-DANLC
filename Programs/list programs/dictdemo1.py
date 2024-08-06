class DictDemo1:
    emp_list =[
        {"id": 101, "Name": "Kiran Singh", "Age": 25},
        {"id": 102, "Name": "K Singh", "Age": 23}
    ]

    def add_new_employee(self):
        # first create a dictionary with new record
        id = int(input("Enter Employee Id : "))
        name = input("Enter Employee Name : ")
        age = int(input("Enter Employee age"))

        emp = {"id": id, "name": name, "age": age}
        self.emp_list.append(emp)
        print("Record added Successfully!!")
        self.display()

    def display(self):
        print("------------------------------------")
        print("Employee Records")
        for e in self.emp_list:
            print(e)
        print("------------------------------------")

    def searchrecord(self):
        id = int(input("Enter Employee Id : "))
        flag = False
        for r in self.emp_list:
            print(r)
            if r["id"] == id:
                print("Record Found")
                print(r)
                flag = True
                break
        if not flag:
            print("Record does not Exist!!")

    def delete_record(self):
        id = int(input("Enter Employee Id : "))
        # self.emp_list = [r for r in self.emp_list if r["id"]!= id]
        list1 = []
        flag = True
        listlength1 = len(self.emp_list)
        for r in self.emp_list:
            if r["id"] != id:
                list1.append(r)

        self.emp_list = list1
        listlength2 = len(self.emp_list)
        if listlength1 == listlength2:
            print("Id not found!!!")
        elif listlength2 == 0:
            print("List is empty!!")
        else:
            print("Record deleted successfully!!")
        self.display()

# self is an inbuilt object of the same class where it is getting used
# it is used to access the members of a class
    def menu(self):

        while True:
            print("==========================================")
            print("1. Add New Employee")
            print("2. Update an Employee")
            print("3. Delete an Employee")
            print("4. Search an Employee Record")
            print("5. sort records according to Name")
            print("6. Exit")
            print("Enter your choice :")
            choice = int(input())

            if choice == 1:
                self.add_new_employee()
            elif choice == 2:
                print()
            elif choice == 3:
                self.delete_record()
            elif choice == 4:
                self.searchrecord()
            elif choice == 5:
                print()
            elif choice == 6:
                print("Good Bye!!")
                break
            else:
                print("Wrong choice!!")


dd = DictDemo1()
dd.menu()