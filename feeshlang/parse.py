from lark import Lark

grammar = """
    program: empty? expr (empty expr)* empty?

    expr: builtin | identifier | number | string

    builtin.1: PERIOD
        | COMMA
        | LSQUARE
        | RSQUARE
        | LPAREN
        | RPAREN
        | LCURLY
        | RCURLY
        | EXCLAIM
        | TILDE
        | PLUS
        | MINUS
        | DIV
        | MUL
        | VARDEAR
        | VARFALL
        | VESSEL
        | AM
        | AT
        | PERCENT
        | GREATER
        | LESSER

    
    
    PERIOD:  "."
    COMMA:   ","
    LSQUARE: "["
    RSQUARE: "]"
    LPAREN:  "("
    RPAREN:  ")"
    LCURLY:  "{"
    RCURLY:  "}"
    EXCLAIM: "!"
    TILDE:   "~"
    PLUS:    "+"
    MINUS:   "-"
    DIV:     "/"
    MUL:     "*"
    VARDEAR: "vardear"
    VARFALL: "varfall"
    VESSEL:  "vessel"
    AM:      "am?"
    AT:      "@"
    PERCENT: "%"
    GREATER: ">"
    LESSER:  "<"
    
    identifier: CNAME
    number: SIGNED_NUMBER
    string: "`" INNER_STRING "'"
    INNER_STRING: /[^']/+

    empty: WS

    %import common.WS
    %import common.SIGNED_NUMBER
    %import common.C_COMMENT
    %ignore C_COMMENT
    %import common.CNAME
"""

l = Lark(grammar, start='program')

def parse_program(program):
    p = l.parse(program)
    for expr in p.children:
        #print(expr)
        if (expr is not None) and (expr.data == 'expr'):
            for child in expr.children:
                d = child.data
                if d == 'number':
                    yield ('n', float(child.children[0]))
                elif d == 'string':
                    yield ('s', str(child.children[0]))
                elif d == 'identifier':
                    yield ('s', str(child.children[0]))
                elif d == 'builtin':
                    yield ('b', str(child.children[0]))