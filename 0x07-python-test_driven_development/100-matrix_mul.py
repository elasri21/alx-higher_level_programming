#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrix
    Args:
        m_a: matrix of intgers
        m_b: matrix of integers
    Return: Matrix of integers"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for l_ch in m_a:
        if not isinstance(l_ch, list):
            raise TypeError("m_a must be a list of lists")
    for l_ch in m_b:
        if not isinstance(l_ch, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for l_ch in m_a:
        if len(l_ch) == 0:
            raise ValueError("m_a can't be empty")
        for num in l_ch:
            if type(num) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for l_ch in m_b:
        if len(l_ch) == 0:
            raise ValueError("m_b can't be empty")
        for num in l_ch:
            if type(num) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    for l_ch in m_a:
            if len(l_ch) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
    for l_ch in m_b:
            if len(l_ch) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_matrix = [[] for i in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            res = 0
            for s in range(len(m_b)):
                res += m_a[i][s] * m_b[s][j]
            new_matrix[i].append(res)
    return (new_matrix)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
