import sys



def step2():
    try:
        from bureaucrat import Bureaucrat
        from exception import GradeTooLowException
        from form import Form
    except:
        return 0
    
    backup = sys.stdout
    sys.stdout = open('step2_output', 'w')
    score = 0

    form = Form('Amazing Form', 100, 50)
    if form.name != 'Amazing Form' or form.grade_sign != 100 or form.grade_exec != 50:
        sys.stdout.close()
        sys.stdout = backup
        return score

    score = 20

    if not (form.__str__() == 'Amazing Form sign grade: 100, exec grade: 50, is signed: False' or
            form.__repr__() == 'Amazing Form sign grade: 100, exec grade: 50, is signed: False'):
        sys.stdout.close()
        sys.stdout = backup
        return score

    julien = Bureaucrat('Julien', 140)
    matt = Bureaucrat('Matt', 60)
    exception = False

    score = 30

    try:
        form.be_signed(julien)
    except GradeTooLowException:
        exception = True
    if not exception:
        sys.stdout.close()
        sys.stdout = backup
        return score

    score = 50

    form.be_signed(matt)
    if not form.is_signed:
        return score

    form.is_signed = False
    julien.sign_form(form)
    form.is_signed = False
    matt.sign_form(form)

    sys.stdout.close()
    sys.stdout = backup

    with open('./step2_output') as f:
        output = f.readlines()

        score = 60
        if output[0] and output[0] != 'Julien cannot sign Amazing Form\n':
            return score

        score = 80
        if output[1] and output[1] != 'Matt signs Amazing Form\n':
            return score

    return 100