import numpy as np
from e8qec import (
    MOD, N, HALF, D,
    CHARGE, LAW, MIRROR, SYM, CODE, WEIGHT,
    WEIGHT_ENUM, WEIGHTS, DISTANCE, DETECT, CORRECT,
    CODE_DIM, LOGICAL_QUDITS,
    L_LOCAL, DARK_LOCAL, DARK_DIM,
    SYNDROME, DECODE, NOISE, APPLY, FAIL,
)

ZERO = np.zeros(N, dtype=int)

def test_zero_in_code():
    assert CODE(ZERO)

def test_zero_syndrome():
    assert SYNDROME(ZERO) == (0, 0)

def test_law_rejects_single_charge():
    s = np.zeros(N, dtype=int)
    s[0] = 1
    assert not LAW(s)

def test_law_accepts_balanced():
    s = np.zeros(N, dtype=int)
    s[0] = 3
    s[16] = 2
    assert LAW(s)

def test_mirror_involution():
    s = np.arange(N) % MOD
    assert np.array_equal(MIRROR(MIRROR(s)), s)

def test_sym_requires_equal_halves():
    s = np.zeros(N, dtype=int)
    s[0] = 1
    assert not SYM(s)

def test_weights_are_even():
    assert all(w % 2 == 0 for w in WEIGHTS)

def test_weight_enum_sums_to_code_dim():
    assert sum(WEIGHT_ENUM.values()) == CODE_DIM

def test_distance_is_min_nonzero_weight():
    assert DISTANCE == min(w for w in WEIGHTS if w > 0)

def test_detect_correct_relations():
    assert DETECT == DISTANCE - 1
    assert CORRECT == (DISTANCE - 1) // 2

def test_logical_qudits_positive():
    assert LOGICAL_QUDITS >= 0

def test_dark_local_dimension():
    assert DARK_LOCAL.shape[1] == 2

def test_dark_dim_is_power():
    assert DARK_DIM == 2 ** N

def test_decoder_fixes_charge():
    s = np.zeros(N, dtype=int)
    s[0] = 3
    syn = SYNDROME(s)
    c = DECODE(syn)
    assert SYNDROME(APPLY(s, c)) == (0, 0)

def test_noise_is_in_range():
    rng = np.random.default_rng(0)
    e = NOISE(0.1, rng)
    assert np.all(e >= 0) and np.all(e < MOD)

def test_fail_on_clean_state_is_false():
    assert not FAIL(ZERO, ZERO)
