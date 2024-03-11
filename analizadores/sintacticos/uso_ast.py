import ast
import sys

print("="*50)
param1 = sys.argv[1]
print('expresion a analizar ' + param1)
#expa = ast.parse(param1, mode='eval')
expa = ast.parse(param1, mode='exec')
print(ast.dump(expa))
print("="*50)