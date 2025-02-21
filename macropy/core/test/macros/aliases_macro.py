import ast

import macropy.core.macros
from macropy.core.quotes import macros, q
macros = macropy.core.macros.Macros()

@macros.expr
def e(tree, exact_src, **kw):
    return ast.Constant("omg")

@macros.expr
def f(tree, exact_src, **kw):
    return ast.Constant("wtf")

@macros.expr
def g(tree, exact_src, **kw):
    return ast.Constant("bbq")
