from zad1.Student import Student

stud1 = Student("Adam", [60, 33.3, 89, 100, 24])
stud2 = Student("Maciek", [12.4, 0, 56, 44.4, 60])

print(stud1.is_passed())
print(stud2.is_passed())