import exception
class Form:
    def __init__(self, name: str, grade_sign: int, grade_exec: int):
        self.name = name
        self.is_signed = False
        self.grade_sign = grade_sign
        self.grade_exec = grade_exec
        if self.grade_sign < 1 or self.grade_exec < 1:
            raise exception.GradeTooHighException
        if self.grade_sign > 150 or self.grade_exec > 150:
            raise exception.GradeTooLowException

    def __str__(self):
        return "{0} sign grade: {1}, exec grade: {2}, is signed: {3}".format(self.name, self.grade_sign, self.grade_exec, self.is_signed)

    def be_signed(self, bureaucrat):
        self.is_signed = True