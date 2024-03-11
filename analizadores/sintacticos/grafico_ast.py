import ast
import pprint
from graphviz import Digraph

dot = Digraph()

code = '''
def suma(a,b):
    valor = a + b
    print("el resultado de la suma es, " + valor)

greet(2,5)
'''

code = "3 + 2 * 4"


def add_node(node, parent=None):
    node_name = str(node.__class__.__name__)
    dot.node(str(id(node)), node_name)
    if parent:
        dot.edge(str(id(parent)), str(id(node)))
    for child in ast.iter_child_nodes(node):
        add_node(child, node)

tree = ast.parse(code)
add_node(tree)

dot.format = 'png'
dot.render('ast', view=True)