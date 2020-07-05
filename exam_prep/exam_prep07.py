from container import Tree, Link

def linky_paths(t):
    """
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(Link(1), [Tree(Link(2, Link(1)))])
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> linky_paths(t)
    >>> t
    Tree(Link(1), [Tree(Link(2, Link(1))), Tree(Link(3, Link(1)), [Tree(Link(4, Link(3, Link(1))))])])
    """
    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        for branch in t.branches:
            helper(branch, t.label)
    helper(t, Link.empty)

def find_file_path(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),
    ...    Tree('ecc',
    ...    [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path(t, 'file.py')
    '/data/ecc/file.py'
    >>> find_file_path(t, 'none.py')
    """
    def helper(t, file_str, path_so_far):
        if t.label == file_str:
            return path_so_far + '/' + file_str
        elif t.is_leaf():
            return None
        for branch in t.branches:
            result = helper(branch, file_str, path_so_far + '/' + t.label)
            if result != None:
                return result
    return helper(t, file_str, '')

def convert_to_string(link):
    """
    >>> link = Link('data', Link('file2.py'))
    >>> convert_to_string(link)
    '/data/file2.py'
    """
    if link == Link.empty:
        return ''
    return '/' + link.first + convert_to_string(link.rest)

def all_paths_linked(t):
    """
    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> all_paths_linked(t1)
    [Link(1, Link(2)), Link(1, Link(3))]
    >>> all_paths_linked(t2)
    [Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1, Link(3, Link(5)))]
    """
    if t.is_leaf():
        return [Link(t.label)]
    result = []
    for branch in t.branches:
        result += [Link(t.label, path) for path in all_paths_linked(branch)]
    return result

def find_file_path2(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),
    ...    Tree('ecc',
    ...    [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path2(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path2(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path2(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path2(t, 'file.py')
    '/data/ecc/file.py'
    >>> find_file_path2(t, 'none.py')
    """
    for link in all_paths_linked(t):
        original = link
        while link != Link.empty:
            if link.first == file_str:
                return convert_to_string(original)
            link = link.rest

def skip(lnk, n):
    """
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk, 2)
    >>> lnk
    Link(1, Link(3, Link(5)))
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> skip(lnk, 2)
    >>> lnk
    Link(1, Link(3, Link(5)))
    >>> lnk2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk2, 4)
    >>> lnk2
    Link(1, Link(2, Link(3, Link(5, Link(6)))))
    """
    count = 1
    def skipper(lst):
        nonlocal count
        count += 1
        if lst == Link.empty or lst.rest == Link.empty:
            return
        elif count % n == 0:
            lst.rest = lst.rest.rest
            count = 1
        skipper(lst.rest)
    skipper(lnk)
