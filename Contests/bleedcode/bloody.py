import itertools as it 
  
def utilityfunc(num_str): 
    num_iter = it.permutations(num_str, len(num_str)) 
    for num_list in num_iter: 
        
        v = ''.join(num_list) 
        x, y = v[:int(len(v)/2)], v[int(len(v)/2):] 
  
        if x[-1] == '0' and y[-1] == '0': 
            continue
  
        if int(x) * int(y) == int(num_str): 
            return x,y 
    return False
  

def isVampire(m_int): 
  
    n_str = str(m_int) 
  
    if len(n_str) % 2 == 1: 
        return False
  
    fangs = utilityfunc(n_str) 
    if not fangs: 
        return False
    return True
  
for _ in range(int(input())):
    n = int(input())
    if isVampire(n): 
        print ("Bloody")
    else:
        print("Not Bloody")