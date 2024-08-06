class demo:
    empdata ={}
    x = 1
    def add(self,a,b):
        print("Sum : ",a+b)

    def addnewemployee(self):
        id = int(input("Enter id : "))
        name = input("Enter name : ")
        city = input("Enter city : ")
        e = {"id":id, "name":name, "city":city}
        self.empdata.update({"key "+str(self.x): e})
        # key 1 :
        self.x += 1
    def display(self):
        print("Employee Data : ")
        key = input("Enter key : ")
        print(self.empdata.get(key, "Not Found!!"))

    def main(self):
        n = int(input("Enter number of employees : "))
        i = 0
        while i<n:
            self.addnewemployee()
            i += 1

        # self.display()
        # print(self.empdata)
        self.getallrecords()

        # empdata
        # key 2: {'id': 12, 'name': 'ff', 'city': 'gurgaon'}   ->  first row
    def getallrecords(self):
        queue = [(self.empdata, 0)]  # queue will get all the records of empdata
        #           dictionary, starting point
        while queue:  # this loop will run until there are values in the queue
            e, depth =queue.pop(0)   # it will store first row into e =key 1: {'id': 11, 'name': 'dd', 'city': 'delhi'}
            for key, value in e.items():  #  key = key1  value = record
                print("Depth : ",depth,key," : ",end=" ")
                print(value)


ob = demo()
ob.main()