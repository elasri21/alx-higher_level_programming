#!/usr/bin/python3
"""Lazy multiply Module"""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy Module
    Args:
        m_a: matrix of integers
        m_b: matrix of integers
    Return: matrix product"""
    return numpy.matmul(m_a, m_b)
