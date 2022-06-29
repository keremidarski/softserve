class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, paper, answers):
        grade = self.grade_test(paper, answers)
        self.add_grade(grade, paper)

    def add_grade(self, percentage, paper):
        if type(self.tests_taken) == str:
            self.tests_taken = {}

        if percentage >= int(paper.pass_mark[:-1]):
            status = "Passed!"
        else:
            status = "Failed!"

        self.tests_taken[paper.subject] = f"{status} ({percentage}%)"

    def grade_test(self, paper, answers):
        correct_answers = 0

        for i in range(len(paper.markscheme)):
            if answers[i] == paper.markscheme[i]:
                correct_answers += 1

        return round((correct_answers / len(answers)) * 100)


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()

print(student1.tests_taken)
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken)

print(student2.tests_taken)
student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(student2.tests_taken)
