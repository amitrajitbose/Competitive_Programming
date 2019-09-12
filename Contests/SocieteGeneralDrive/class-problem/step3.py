import sys

def step3():
    try:
        from concrete_forms import ShrubberyCreationForm, RobotomyRequestForm
        from bureaucrat import Bureaucrat
        from exception import GradeTooLowException
    except:
        return 0

    backup = sys.stdout
    sys.stdout = open('step3_output', 'w')

    score = 0

    julien = Bureaucrat('Julien', 100)
    matt = Bureaucrat('Matt', 40)
    scf = ShrubberyCreationForm('Gregory house')
    rrf = RobotomyRequestForm('Zuluu')

    scf.be_signed(matt)
    rrf.be_signed(matt)

    exception = False
    try:
        scf.execute(julien)
    except:
        pass
    try:
        rrf.execute(julien)
    except GradeTooLowException:
        exception = True
    except:
        pass
    if not exception:
        sys.stdout.close()
        sys.stdout = backup
        return score

    score = 10

    rrf.execute(matt)

    julien.execute_form(scf)
    matt.execute_form(rrf)

    sys.stdout.close()
    sys.stdout = backup

    with open('./step3_output') as f:
        output = f.readlines()
        if output[0] and output[0] != 'Shrubbery has been planted at Gregory house\n':
            return score
        score = 25
        if output[1] and output[1] != 'Zuluu has been robotomied\n':
            return score
        score = 40
        if output[2] and output[2] != 'Shrubbery has been planted at Gregory house\n':
            return score
        score = 55
        if output[3] and output[3] != 'Julien executes ShrubberyCreationForm\n':
            return score
        score = 70
        if output[4] and output[4] != 'Zuluu has been robotomied\n':
            return score
        score = 85
        if output[5] and output[5] != 'Matt executes RobotomyRequestForm\n':
            return score
        score = 100
    return score