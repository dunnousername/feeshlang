class Special(object):
    pass

class Singleton(Special):
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if not isinstance(other, Singleton):
            return False
        return self.value == other.value

    def __repr__(self):
        return f'Singleton({repr(self.value)})'

class Function(Special):
    def __init__(self, f, name=None):
        self.f = f
        self.name = None
        if name is not None:
            self.name = f'Function(\'{name}\')'
    
    def __repr__(self):
        return self.name or super().__repr__()
    
    def __call__(self, context):
        self.f(context)

class Break(Exception):
    pass

class FFunction(Special):
    def __init__(self, code):
        self.code = code
        
    def __call__(self, context):
        tmp = context.code
        tmp_ip = context.ip
        context.code = self.code.copy()
        context.ip = 0
        context.run()
        context.code = tmp
        context.ip = tmp_ip
    
    def __repr__(self):
        return f'FFunction({repr(self.code)})'

singletons = {k: Singleton(k) for k in [
    ']',
    ')',
    '}',
]}