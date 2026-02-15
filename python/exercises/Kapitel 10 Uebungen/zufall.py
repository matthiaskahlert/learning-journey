# zufall.py
import sys, random

if len(sys.argv) == 1:
    print(random.randint(0, 1000))
elif len(sys.argv) > 2:
    print('Aufrufformat: python zufall.py n')
else:
    try:
        n = int(sys.argv[1])
        print(random.randint(0, n))
    except:
        print('Argument muss eine natürliche Zahl sein.')
