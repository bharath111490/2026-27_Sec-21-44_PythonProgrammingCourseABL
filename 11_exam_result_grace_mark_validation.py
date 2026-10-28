# Examination Result and Grace-Mark Validation

num_subjects = int(input("Enter number of subjects: "))

marks = []
max_marks = 100
pass_mark = 35
grace_limit = 5

failed_subjects = 0
total = 0

for i in range(num_subjects):
    mark = int(input(f"Enter marks for Subject {i + 1}: "))

    if mark < 0 or mark > max_marks:
        print("Invalid marks entered!")
        exit()

    # Apply grace marks if eligible
    if mark < pass_mark and (pass_mark - mark) <= grace_limit:
        grace = pass_mark - mark
        mark += grace
        print(f"Grace Marks Applied: {grace} (New Marks = {mark})")

    marks.append(mark)
    total += mark

    if mark < pass_mark:
        failed_subjects += 1

percentage = (total / (num_subjects * max_marks)) * 100

print("\n----- RESULT -----")
print("Final Marks:", marks)
print("Total Marks:", total)
print(f"Percentage: {percentage:.2f}%")

if failed_subjects > 0:
    print("Result: FAIL")
else:
    if percentage >= 75:
        print("Classification: DISTINCTION")
    elif percentage >= 60:
        print("Classification: FIRST CLASS")
    elif percentage >= 50:
        print("Classification: SECOND CLASS")
    else:
        print("Classification: PASS")