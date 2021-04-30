from .parse import parse_program
from .default import table
from .ftypes import Special, Function

class ExecutionContext(object):
    def __init__(self):
        self.ip = 0
        self.code = []
        self.data = []
        self.world = {}
    
    def compile(self, code):
        for expr in parse_program(code):
            (t, v) = expr
            if t == 'b':
                self.code.append(table[v])
            elif t in ['n', 's']:
                self.code.append(Function(lambda c, v=v: c.data.append(v), name=v))
    
    def run(self):
        while self.ip < len(self.code):
            self.op(self.code[self.ip])
    
    def op(self, o):
        #print(self.code, self.data)
        #print(repr(o))
        o(self)
        self.ip += 1
    
    def execute_file(self, fn):
        with open(fn, 'r') as f:
            self.compile(f.read())
            self.run()