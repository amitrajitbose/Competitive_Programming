class GradeTooHighException(Exception):
	def __init__(self):
		Exception.__init__(self, "Grade Too High")

class GradeTooLowException(Exception):
	def __init__(self):
		Exception.__init__(self, "Grade Too Low")
