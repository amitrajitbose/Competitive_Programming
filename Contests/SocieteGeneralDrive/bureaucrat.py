import exception

class Bureaucrat:

	def __init__(self, name: str, grade: int):
		self.name = name
		self.grade = grade
		if self.grade < 1:
			raise exception.GradeTooHighException
		elif self.grade > 150:
			raise exception.GradeTooLowException

	def __str__(self):
		return self.name + " grade: " + str(self.grade)
