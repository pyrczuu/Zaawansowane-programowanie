from zad2.Book import Book
from zad2.Employee import Employee
from zad2.Library import Library
from zad2.Order import Order
from zad1.Student import Student

ciniba = Library("Katowice", "Bankowa 11a", "40-007",
                 "8:00-20:00", "32 786 51 30")

miejska_biblioteka = Library("Katowice", "Uniczowska 36", "40-748",
                             "8:00-19:00", "322 067 193")


book1 = Book(ciniba, "2020-01-01", "Anna",
             "Kempa", 201)

book2 = Book(miejska_biblioteka, "1947-06-10", "Albert",
             "Camus", 294)

book3 = Book(ciniba, "2023-05-11", "Kamil",
             "Kovalenko", 999)

book4 = Book(miejska_biblioteka, "1998-10-28", "Adam",
             "Małysz", 123)

book5 = Book(miejska_biblioteka, "2000-12-31", "Damian",
             "Pyrcz", 10)


employee1 = Employee("Adam", "Kowalski", "2024-06-31", "2002-02-13",
                     "Katowice", "Kaskady", "40-748", "888-888-888")

employee2 = Employee("Hubert", "Nowak", "2026-09-01", "1998-09-31",
                     "Zabrze", "Roosevelta", "41-800", "199-448-888")

employee3 = Employee("Katarzyna", "Nowakowska", "2018-04-16", "1998-02-23",
                     "Katowice", "Fiołkowa", "40-123", "123-456-789")

stud1 = Student("Adam", [60, 33.3, 89, 100, 24])
stud2 = Student("Maciek", [12.4, 0, 56, 44.4, 60])
stud3 = Student("Błażej", [0, 80, 56.5, 67, 100])

order1 = Order(employee1, stud1, [book1, book2], "2026-10-21")
order2 = Order(employee2, stud2, [book3, book4], "2023-05-13")

print(order1)
print(order2)
