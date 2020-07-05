
class nil:
    """Represents the special empty pair nil in Scheme."""
    def __repr__(self):
        return 'nil'
    def __len__(self):
        return 0
    def __getitem__(self, i):
        raise IndexError('Index out of range')
    def map(self, fn):
        return nil
nil = nil()

class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.second)
    def __str__(self):
        def helper(pair):
            if pair == nil:
                return ''
            return str(pair.first) + ' ' + helper(pair.second)
        return '(' + helper(self).strip() + ')'
    def __len__(self):
        return 1 + len(self.second)
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.second[i-1]
    def map(self, fn):
        return Pair(fn(self.first), self.second.map(fn))

from operator import add, sub, mul, truediv, eq, lt, gt
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '=': eq,
    '<': lt,
    '>': gt
    }

from ucb import trace

def calc_eval(exp):
    """Evaluates a Calculator expression represented as a Pair."""
    if isinstance(exp, Pair):
        if exp.first == 'and':
            while exp.second != nil:
                if calc_eval(exp.second.first) == False:
                    return False
                exp = exp.second
            return True
        else:
            operator = calc_eval(exp.first)
            operands = list(exp.second.map(calc_eval))
            return calc_apply(operator, operands)
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else:
        return exp

from functools import reduce
def calc_apply(op, args):
    return reduce(op, args)


