import ast
import sys

print("="*50)
param1 = sys.argv[1]
print('expresion a analizar ' + param1)
expa = ast.parse(param1, mode='eval')
print(ast.dump(expa))
print("="*50)