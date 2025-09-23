Students={    
        "Alice":85,
        "Mark":55
    }

name=input("Enter the Students' name: ")
if Students.get(name) is None:
    print("Student not found.")
else:
    print(f"{name}'s marks: {Students.get(name)}")