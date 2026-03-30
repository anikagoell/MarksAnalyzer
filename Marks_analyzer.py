def make_list():
    d = {}
    n = int(input("Enter total number of students: "))
    for i in range(1, n + 1):
        while True:
            try:
                val = int(input(f"Enter marks of roll number {i}: "))
                if 0 <= val <= 100:
                    d[i] = val
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")  
    return d


def max_marks(d):
    d = encode(d)
    if len(d) > 0:
        values = []  
        for roll,l in d.items():
            values.append(l[0])
        print(f"Maximum marks are {max(values)}")
    else:
        print("The list is empty. (Choose 1 to enter data)")


def min_marks(d):
    d = encode(d)
    if len(d) > 0:
        values = []  
        for roll,l in d.items():
            values.append(l[0])
        print(f"Minimum marks are {min(values)}")
    else:
        print("The list is empty. (Choose 1 to enter data)")


def avg_marks(d):
    d = encode(d)
    if len(d) > 0:
        values = []  
        for roll,l in d.items():
            values.append(l[0])
        avg=sum(values)/len(values)
        print(f"Average marks are {avg}")
    else:
        print("The list is empty. (Choose 1 to enter data)")


def encode(d):
    result = {}
    
    for roll, marks in d.items():
        if 90 <= marks <= 100:
            result[roll] = [marks, 'A', 'Pass']
        elif 70 <= marks < 90:
            result[roll] = [marks, 'B', 'Pass']
        elif 40 <= marks < 70:
            result[roll] = [marks, 'C', 'Pass']
        else:
            result[roll] = [marks, 'D', 'Fail']   
    return result


def display(d):
    print(d)


def students_above_90(d):
    result = []
    
    for roll, marks in d.items():
        if isinstance(marks, list):
            if marks[0] >= 90:
                result.append(roll)
        else:
            if marks >= 90:
                result.append(roll)
    return result


def get_by_status(d, status):
    d=encode(d)
    result = []
    for roll, data in d.items():
        if data[2] == status:
            result.append(roll) 
    return result



student_dict = {}

while True:
    try:
        ch = int(input("""
Enter your choice:
1. Make list
2. Find maximum marks
3. Find minimum marks
4. Find average marks
5. Students scoring 90 and above
6. Grade students
7. Show failed students
8. Display list
9. Exit
Choice: """))
        
        if ch == 1:
            student_dict = make_list()
        
        elif ch == 2:
            max_marks(student_dict)
        
        elif ch == 3:
            min_marks(student_dict)
        
        elif ch == 4:
            avg_marks(student_dict)
        
        elif ch == 5:
            top_students = students_above_90(student_dict)
            print("Students scoring 90 and above:", top_students)
        
        elif ch == 6:
            newDict = encode(student_dict)
            display(newDict)
        
        elif ch == 7:
            failed = get_by_status(student_dict, "Fail")
            print("Roll Number of Failed students:", failed)
        
        elif ch == 8:
            display(student_dict)
        
        elif ch == 9:
            print("Exiting program")
            break
        
        else:
            print("Invalid choice. Try again.")
    
    except ValueError:
        print("Please enter a valid number.")