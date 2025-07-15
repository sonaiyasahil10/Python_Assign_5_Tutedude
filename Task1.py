SOM={"Alice": 85, "Bryon": 56 , "Crawley":80}

name = input("Enter the student's name: ")

if name in SOM:
    print(name + "'s " + "marks: " + str(SOM[name]))
else:
    print("Student not found")