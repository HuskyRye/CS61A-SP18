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

def about_equal(t1, t2):
    """Returns whether two trees are 'about equal.'
    Two trees are about equal if and only if they contain
    the same labels the same number of times.
    >>> x = tree(1, [tree(2), tree(2), tree(3)])
    >>> y = tree(3, [tree(2), tree(1), tree(2)])
    >>> about_equal(x, y)
    True
    >>> z = tree(3, [tree(2), tree(1), tree(2), tree(3)])
    >>> about_equal(x, z)
    False
    """
    def label_counts(t):
        if is_leaf(t):
            return {label(t): 1}
        else:
            counts = dict()
            for b in branches(t) + [tree(label(t))]:
                for labe, count in label_counts(b).items():
                    if labe not in counts:
                        counts[labe] = 0
                    counts[labe] += count
            return counts
    return label_counts(t1) == label_counts(t2)

def decrypt(s, d):
    """List all possible decoded strings of s.
    >>> codes = {
    ... 'alan': 'spooky',
    ... 'al': 'drink',
    ... 'antu': 'your',
    ... 'turing': 'ghosts',
    ... 'tur': 'scary',
    ... 'ing': 'skeletons',
    ... 'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
    """
    if s == '':
        return []
    ms = []
    if s in d:
        ms.append(d[s])
    for k in range(len(s)):
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                ms.append(d[first] + ' ' + rest)
    return ms

def ensure_consistency(fn):
    """
    Returns a function that calls fn on its argument, returns fn's
        return value, and returns None if fn's return value is different
        from any of its previous return values for those same argument.
        Also returns None if more than 20 calls are made.
        
    >>> def consistent(x):
    ...     return x
    >>>
    >>> lst = [1, 2, 3]
    >>> def inconsistent(x):
    ...     return x + lst.pop()
    >>>
    >>> a = ensure_consistency(consistent)
    >>> a(5)
    5
    >>> a(5)
    5
    >>> a(6)
    6
    >>> a(6)
    6
    >>> b = ensure_consistency(inconsistent)
    >>> b(5)
    8
    >>> b(5)
    >>> b(6)
    7
    """
    n = 0
    z = dict()
    def helper(x):
        nonlocal n
        n += 1
        if n > 20:
            return None
        val = fn(x)
        if x not in z:
            z[x] = [val]
        if z[x] == [val]:
            return val
        else:
            z[x] = [val]
            return None
    return helper
