x, y, z = 1, 2, 3
y = [x, [y, [z, []]]]
x = [y[1][0], y, [y[1][1][1]]]
z = len(y[1][1][1])

# Constructor
def tree(label, branches=[]):
    '''
    for branch in branches:
        assert is_tree(branch)
    '''
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

def sum_range(t):
    def helper(t):
        if is_leaf(t):
            return [label(t), label(t)]
        else:
            a = min([helper(branch)[1] for branch in branches(t)])
            b = max([helper(branch)[0] for branch in branches(t)])
            x = label(t)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y

def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not
        contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a, b = no_eleven(n-1), no_eleven(n-2)
        return [[6] + s for s in a] + [[1, 6] + s for s in b]

def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
        addition.
    >>> plus = tree('+', [tree(2), tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = tree('*', [tree(2), tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = tree('*', [tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(tree('*'))
    1
    """
    if label(t) == '+':
        return sum([eval_with_add(branch) for branch in branches(t)])
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total
            for _ in range(eval_with_add(b)):
                total = total + term
        return total
    else:
        return label(t)
