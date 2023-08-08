import descriptor as desc
from statistics import mean


class Student:
    first_name = desc.CheckName()
    last_name = desc.CheckName()
    middle_name = desc.CheckName()
    subject = desc.CheckSubject('subjects.csv')
    subject_score = desc.CheckScoreRange()
    test_score = desc.CheckTestScoreRange()
    subjects = []

    def __init__(self, last_name, first_name, middle_name, subject, subject_score, test_score):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def add_subject(self, subject, subject_score, test_score):
        """Метод добавления нового предмета студенту"""
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def _update_subjects(self):
        """Метод добавления предмета в список предметов"""
        self.subjects.append({
            "subject": self.subject,
            "subject_score": self.subject_score,
            "test_score": self.test_score,
        })

    def get_avg(self):
        """Метод, возвращающий информацию по среднему балу за оценки и тесты"""
        avg_sub_score = mean(score['subject_score'] for score in self.subjects)
        avg_test_score = mean(score['test_score'] for score in self.subjects)
        return f'ФИО: {self.last_name} {self.first_name} {self.middle_name} \n' \
               f'   Предметы студента: {", ".join([sub["subject"].title() for sub in self.subjects])} \n' \
               f'       Средний бал по урокам: {avg_sub_score}\n' \
               f'       Средний бал по тестам: {avg_test_score}'
