import numpy as np
from e8qec import (
    ALLOWED, INVARIANT, REFLECT, BALANCE,
    CHARGES, JUMPS, DARK, LINDBLAD, E8_DET, E8_EVEN, N,
)

ZERO = np.zeros(N, dtype=int)

BALANCED = np.zeros(N, dtype=int)
BALANCED[0] = 3
BALANCED[16] = 2

ASYMMETRIC = np.zeros(N, dtype=int)
ASYMMETRIC[0] = 1

def test_zero_allowed():
    assert ALLOWED(ZERO)

def test_balanced_allowed():
    assert ALLOWED(BALANCED)

def test_asymmetric_rejected():
    assert not ALLOWED(ASYMMETRIC)

def test_zero_invariant():
    assert INVARIANT(ZERO)

def test_asymmetric_not_invariant():
    assert not INVARIANT(ASYMMETRIC)

def test_balance_zero_for_symmetric():
    assert BALANCE(BALANCED) == 0.0

def test_balance_positive_for_asymmetric():
    assert BALANCE(ASYMMETRIC) > 0.0

def test_e8_even_unimodular():
    assert E8_DET == 1
    assert E8_EVEN

def test_dark_state_exists():
    K = DARK(JUMPS()[0])
    assert K.shape[0] == 5
    assert K.shape[1] >= 1
