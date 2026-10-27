# University Scholarship Allocation (One Student)

name = input("Enter student name: ")

aggregate = float(input("Enter aggregate marks: "))
sub1 = float(input("Enter Subject 1 marks: "))
sub2 = float(input("Enter Subject 2 marks: "))
sub3 = float(input("Enter Subject 3 marks: "))

attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

if (aggregate >= 75 and
    sub1 >= 50 and
    sub2 >= 50 and
    sub3 >= 50 and
    attendance >= 80 and
    income <= 300000):

    print("\nScholarship Approved")
    print("Name:", name)

else:
    print("\nScholarship Not Approved")