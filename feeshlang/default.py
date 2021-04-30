from .ftypes import singletons, Function, FFunction
from .utils import list_rindex

def scan_forwards(context, needle):
    j = 1
    index = context.ip
    other_needle = context.code[index]
    for i in range(index + 1, len(context.code)):
        if context.code[i] == needle:
            j -= 1
        elif context.code[i] == other_needle:
            j += 1
        if j == 0:
            return i
    raise ValueError('could not find needle')

def convert(context, needle, transform):
    where = scan_forwards(context, needle)
    result = transform(context.code[context.ip+1:where])
    del context.code[context.ip+1:where+1]
    context.code[context.ip] = table[',']
    context.data.append(result)

def varfall(c):
    del c.world[c.data.pop()]

def vardear(c):
    a = c.data.pop()
    b = c.data.pop()
    c.world[a] = b

def vessel(c):
    n = c.data.pop()
    c.data.append(c.world[n])

def if_statement(c):
    i = c.data.pop()
    f = c.data.pop()
    e = c.data.pop()
    if i:
        c.data.append(f)
    else:
        c.data.append(e)

def dup(c):
    x = c.data.pop()
    c.data.extend([x, x])

table = {
    '.': Function(lambda c: c.data.pop()(c), name='.'),
    ',': Function(lambda c: None, name=','),
    ']': singletons[']'],
    ')': singletons[')'],
    '}': singletons['}'],
    '[': Function(lambda c: convert(c, singletons[']'], lambda x: x), name='['),
    '(': Function(lambda c: convert(c, singletons[')'], lambda x: FFunction(x)(c)), name='('),
    '{': Function(lambda c: convert(c, singletons['}'], lambda x: FFunction(x)), name='{'),
    '!': Function(lambda c: print(c.data.pop()), name='!'),
    '+': Function(lambda c: c.data.append(c.data.pop() + c.data.pop()), name='+'),
    '-': Function(lambda c: c.data.append(c.data.pop() - c.data.pop()), name='-'),
    '/': Function(lambda c: c.data.append(c.data.pop() / c.data.pop()), name='/'),
    '*': Function(lambda c: c.data.append(c.data.pop() * c.data.pop()), name='*'),
    'varfall': Function(varfall, name='varfall'),
    'vardear': Function(vardear, name='vardear'),
    'vessel': Function(vessel, name='vessel'),
    'am?': Function(if_statement, name='am?'),
    '@': Function(dup, name='dup'),
    '>': Function(lambda c: c.data.append(c.data.pop() > c.data.pop()), name='>'),
    '<': Function(lambda c: c.data.append(c.data.pop() < c.data.pop()), name='<'),
}