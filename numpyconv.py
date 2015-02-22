"""
Conversion from str and repr representations to NumPy.

Conversion to Mathematica.
"""

def from_repr(s):
    """
    Simplistic converter of strings from repr to float NumPy arrays.

    If the repr representation has ellipsis in it, then this will fail.

    Parameters
    ----------
    s : str
        The repr version of a NumPy array.

    Examples
    --------
    >>> s = "array([ 0.3,  inf,  nan])"
    >>> a = from_repr(s)

    """
    import numpy as np

    # Need to make sure eval() knows about inf and nan.
    # This also assumes default printoptions for NumPy.
    from numpy import inf, nan

    if s.startswith(u'array'):
        # Remove array( and )
        s = s[6:-1]

    a = np.array(eval(s))
    return a

def from_str(s):
    """
    Simplistic converter of strings from str to float NumPy arrays.

    If the str representation has ellipsis in it, then this will fail.

    Parameters
    ----------
    s : str
        The str version of a NumPy array.

    Examples
    --------
    >>> s = "array([ 0.3  inf  nan])"
    >>> a = from_str(s)

    """
    import numpy as np

    if s.startswith(u'array'):
        # Remove array( and )
        s = s[6:-1]

    if s.startswith(u'[['):
        # 2D array
        rows = s.strip()[1:-1].split('\n')
        rows = ['[' + ','.join(row.strip()[1:-1].strip().split()) + ']'
                for row in rows]
        ss = '[' + ',\n'.join(rows) + ']'
        a = from_repr(ss)
    elif s.startswith(u'['):
        # 1D
        ss = '[' + ','.join(s[1:-1].split(' ')) + ']'
        a = from_repr(ss)
    else:
        # Assume its a regular float. Force 1D so we can index into it.
        a = from_repr(s)
    return a

def to_mma(x):
    """
    Convert an array to Mathematica.

    """
    rows = []
    if len(x.shape) > 1:
        for row in x:
            rows.append(to_mma(row))
    else:
        return '{' + ','.join(map(str, x)) + '}'

    out = "{" + ',\n'.join(rows) + "}"
    out = out.replace('e', '*^')
    return out

def from_mma(x):
    """
    Convert an array from Mathematica to NumPy.

    """
    z = x.replace('{', '[').replace('}', ']')
    return from_repr(z)
