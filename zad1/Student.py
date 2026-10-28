class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self):
        total = 0
        for mark in self.marks:
            total += mark
        return (total / len(self.marks)) > 50

    def __str__(self):
        return f"{self.name}: {self.marks}"
