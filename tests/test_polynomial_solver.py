import numpy as np
from EquationSolver import solve_polynomial, display_polynomial

def test_real_roots():
    coeffs = [1, -5, 6]
    roots = solve_polynomial(coeffs)
    expected = [3.0, 2.0]
    np.testing.assert_allclose(sorted(roots), sorted(expected), rtol=1e-5)

def test_display_polynomial():
    coeffs = [1, 0, -4, 1]
    result = display_polynomial(coeffs)
    expected = "x^3 -4x +1 = 0"
    assert result.replace(" ", "") == expected.replace(" ", "")

def test_constant_polynomial():
    coeffs = [5]
    roots = solve_polynomial(coeffs)
    assert roots == []

def test_leading_zeros_trimmed():
    coeffs = [0, 1, -1, 0]
    roots = solve_polynomial(coeffs)
    expected = [1.0, 0.0]
    np.testing.assert_allclose(sorted(roots), sorted(expected), rtol=1e-5)

def test_complex_roots():
    coeffs = [1, 2, 5]
    roots = solve_polynomial(coeffs)
    assert all(np.iscomplex(roots))
