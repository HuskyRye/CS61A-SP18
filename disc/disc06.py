# Linked List Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def sum_nums(link):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    >>> b = Link(5)
    >>> sum_nums(b)
    5
    """
    '''
    if link.rest == Link.empty:
        return link.first
    return link.first + sum_nums(link.rest)
    '''
    result = 0
    while link != Link.empty:
        result += link.first
        link = link.rest
    return result

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    result = 1
    for link in lst_of_lnks:
        if link == Link.empty:
            return Link.empty
        result *= link.first
    return Link(result, multiply_lnks([link.rest for link in lst_of_lnks]))

def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    record = [lnk.first]
    while lnk.rest != Link.empty:
        if lnk.second in record:
            lnk.rest = lnk.rest.rest
        else:
            record.append(lnk.second)
            lnk = lnk.rest

def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [lst[index] * index for index in range(len(lst)) if index % 2 == 0]

def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    >>> quicksort_list([2, 1])
    [1, 2]
    """    
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [elem for elem in lst if elem < pivot]
    greater = [elem for elem in lst if pivot < elem]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)
    
def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if not lst:
        return 1
    return max(lst[0] * max_product(lst[2:]), max_product(lst[1:]))

# Tree Class
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


def eval_tree(tree):
    """Evaluates an expression tree with functions the root.
    >>> eval_tree(Tree(1))
    1
    >>> expr = Tree('*', [Tree(2), Tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(Tree('+', [expr, Tree(4), Tree(5)]))
    15
    """    
    if tree.is_leaf():
        return tree.label
    if tree.label == '+':
        return sum([eval_tree(branch) for branch in tree.branches])
    elif tree.label == '*':
        result = 1
        for branch in tree.branches:
            result *= eval_tree(branch)
        return result

def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> redundant_map(tree, double)
    Tree(2, [Tree(4), Tree(8, [Tree(16, [Tree(256)])])])
    """    
    t.label = f(t.label)
    new_f = lambda x: f(f(x))
    t.branches = [redundant_map(branch, new_f) for branch in t.branches]
    return t
