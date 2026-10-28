from zad2.Book import Book
from zad2.Employee import Employee
from zad1 import Student


class Order:
    def __init__(self, employee: Employee, student: Student,
                 books: list[Book], order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        res = (f"Order placed on {self.order_date} by {self.student} "
               f"processed by {self.employee} containing")
        for book in self.books:
            res += f" [{book}]"
        return res
