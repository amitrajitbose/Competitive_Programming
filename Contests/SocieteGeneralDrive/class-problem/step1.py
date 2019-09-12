def step1():
    try:
        from bureaucrat import Bureaucrat
        from exception import GradeTooLowException, GradeTooHighException
    except:
        return 0

    score = 0
    bureaucrat1 = Bureaucrat('Michel', 15)
    if bureaucrat1.name != 'Michel' or bureaucrat1.grade != 15:
        return score
    score = 33

    if not (bureaucrat1.__str__() == 'Michel grade: 15' or bureaucrat1.__repr__() == 'Michel grade: 15'):
        return score

    score = 66

    try:
        Bureaucrat('fail', 0)
    except GradeTooHighException:
        pass
    except Exception:
       return score

    try:
        Bureaucrat('fail', 151)
    except GradeTooLowException:
        pass
    except Exception:
        return score

    return 100
