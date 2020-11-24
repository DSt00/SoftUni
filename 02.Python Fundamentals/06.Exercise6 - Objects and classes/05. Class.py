class Class:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.__students_count = 22

    def add_student(self, name, grade):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average = sum(self.grades) / len(self.grades)
        return f'{average:.2f}'

    def __repr__(self):
        avg = Class.get_average_grade(self)
        return f'The students in {self.name}: {", ".join(self.students)}. Average grade: {avg}'
