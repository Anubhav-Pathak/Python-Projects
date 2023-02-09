import os;
from tabulate import tabulate
file = os.path.join(os.path.dirname(__file__),"Employee.txt")
print("-"*30,"  Employee Management System","-"*30,"Press 1 to Add an Employee","Press 2 to Display all Records","Press 3 to Check record on the basis of ID","Press 4 to Check record on the basis of Name","Press 5 to Update a Record","Press 6 to Delete a Record","Press 7 to Exit","-"*30,sep="\n")
Employees = {}
try:
    File = open(file,"r+")
    for Employee in File.readlines():
        items = Employee.split(", ")
        Employees[int(items[0])] = items[1:-1]
    File.close()
except FileNotFoundError: print("Employee.txt is missing")
def Input(id):
    name = input("Enter Employee's name: ")
    dob = input("Enter Employee's DOB: ")
    salary = int(input("Enter Employee's Salary: "))
    department = input("Enter Employee's Department: ")
    Employees[id] = [name,dob,salary,department]
def Display(n=0,id=0,name=""):
    heading = ("ID", "Name", "DOB", "Salary", "Department")
def Pass(n):
    if n == 4: 
        Input = input("Enter the Name: ")
        for list in Employees.values():
            if Input in list[0]: return (Input,True)
        else: print("Name is not present")
    else: 
        Input= int(input("Enter the ID: "))
        if Input in Employees.keys(): 
            if n == 1: print("ID is already present")
            return (Input,True)
        else: 
            if n == 1: return (Input, False)
            print("ID is not present")
    return (Input,False)
while True:
    try:
        n = int(input("Choose: "))
        if n < 1 or n > 7: print("Wrong Input")
        elif n == 2: Display()                                                      # Display Records
        elif n == 7:                                                                # Exit
            File = open(file,"w+")
            for id,info in Employees.items():
                File.write(f"{id}, {info[0]}, {info[1]}, {info[2]}, {info[3]}, \n")
            File.close()
            break
        else: 
            Result = Pass(n)
            if n == 1 and Result[1] == False: Input(Result[0])                      # Feed new Record
            elif Result[1] == True: 
                if n == 3: Display(3,id=Result[0])                                  # Check Record on the basis of ID
                elif n == 4: Display(4,name=Result[0])                              # Check Record on the basis of Name
                elif n == 5: Input(Result[0])                                       # Update Record
                else: Employees.pop(Result[0])                                      # Delete Record
    except ValueError:
        print("Wrong Input")
        continue
    except KeyboardInterrupt:
        print("Keyboard Interruption occured")
        continue