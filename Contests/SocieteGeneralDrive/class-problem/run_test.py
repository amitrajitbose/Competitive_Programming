import sys

from step1 import step1
from step2 import step2
from step3 import step3
from step4 import step4

score = []
weight = [1, 2, 2, 1]
stdout_backup = sys.stdout

try:
    score.append(step1())
except Exception as e:
    sys.stdout = stdout_backup
    print(e)
    score.append(0)

try:
    score.append(step2())
except Exception as e:
    sys.stdout = stdout_backup
    print(e)
    score.append(0)

try:
    score.append(step3())
except Exception as e:
    sys.stdout = stdout_backup
    print(e)
    score.append(0)
try:
    score.append(step4())
except Exception as e:
    sys.stdout = stdout_backup
    print(e)
    score.append(0)

final_score = 0
for s, w in zip(score, weight):
    final_score += (s * w)
final_score = final_score // sum(weight)

print(f'Scores:\nStep 1: {score[0]}\nStep 2: {score[1]}\nStep 3: {score[2]}\nStep 4: {score[3]}\nTotal: {final_score}')
