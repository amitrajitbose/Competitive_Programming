import os
import sys

def step4():
    try:
        from concrete_forms import RobotomyRequestForm, ShrubberyCreationForm
        from intern import Intern
    except:
        return 0

    backup = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    rrf = Intern.make_form('robotomy request', 'Bender')
    scf = Intern.make_form('shrubbery creation', 'Zuul')
    no_form = Intern.make_form('fake name', 'fake target')

    if isinstance(scf, ShrubberyCreationForm) and isinstance(rrf, RobotomyRequestForm) and no_form is None:
        sys.stdout = backup
        return 100

    if isinstance(scf, ShrubberyCreationForm) and isinstance(rrf, RobotomyRequestForm) and no_form is not None:
        sys.stdout = backup
        return 75

    if isinstance(scf, ShrubberyCreationForm) or isinstance(rrf, RobotomyRequestForm):
        sys.stdout = backup
        return 25

    sys.stdout = backup
    return 0

