import student

test = student.Student('Иванов', 'Иван', 'Иванович', 'Algebra', 5, 99)
print(test.get_avg())
test.add_subject('Biology',4,88)
print(test.get_avg())

