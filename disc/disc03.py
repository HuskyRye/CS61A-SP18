def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def tree_max(t):
    """Return the max of a tree"""
    if is_leaf(t):
        return label(t)
    return max([label(t)] + [tree_max(branch) for branch in branches(t)])

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 1
    return max([height(branch) + 1 for branch in branches(t)])

def square_tree(t):
    """Return a tree with the square of every element in t"""
    if is_leaf(t):
        return tree(label(t)**2)
    return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])

def find_path(tree, x):
    if label(tree) == x:
        return [x]
    for branch in branches(tree):
        ret = find_path(branch, x)
        if ret:
            return [label(tree)] + ret
    return None

def prune(t, k):
    if k == 0:
        return tree(label(t))
    return tree(label(t), [prune(branch, k-1) for branch in branches(t)])
