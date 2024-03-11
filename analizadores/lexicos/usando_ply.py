import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ASSIGN',
    'SEMI',
)

# Reglas de expresiones regulares para tokens simples
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'\='
t_SEMI = r'\;'
t_ignore  = ' \t'

# Regla de expresiones regulares con acciones
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla de manejo de errores
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
yacc.yacc()
# Prueba de datos
data = '''
3 + 4 * 10
  + -20 *2
'''

# Darle al analizador léxico algún dato
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No más entrada
    print(tok)

# Salida esperada:
# ('NUMBER', 3)
# ('PLUS', '+')
# ('NUMBER', 4)
# ('TIMES', '*')
# ('NUMBER', 10)

# ('PLUS', '+')
# ('MINUS', '-')
# ('NUMBER', 20)
# ('TIMES', '*')
# ('NUMBER', 2)

# Path: analizadores/lexicos/usando_ply.py
