import numpy as np

MOD = 5
N = 32
HALF = N // 2

CHARGES = lambda s: (
    int(np.sum(np.asarray(s)[:HALF]) % MOD),
    int(np.sum(np.asarray(s)[HALF:]) % MOD),
)

ALLOWED = lambda s: sum(CHARGES(s)) % MOD == 0

REFLECT = lambda s: np.concatenate([np.asarray(s)[HALF:], np.asarray(s)[:HALF]])

INVARIANT = lambda s: np.array_equal(np.asarray(s), REFLECT(s))

BALANCE = lambda e: (
    lambda a, b: 0.0 if a + b == 0 else abs(a - b) / (a + b)
)(int(np.count_nonzero(np.asarray(e)[:HALF])),
  int(np.count_nonzero(np.asarray(e)[HALF:])))

L_LOCAL = np.zeros((MOD, MOD), dtype=complex)
L_LOCAL[0, 2] = 1.0
L_LOCAL[1, 3] = 1.0
L_LOCAL[0, 4] = 1.0

JUMPS = lambda r=1.0: [np.sqrt(r) * L_LOCAL]

LINDBLAD = lambda rho, H, jumps, r=1.0: (
    -1j * (H @ rho - rho @ H)
    + sum(
        r * (L @ rho @ L.conj().T
             - 0.5 * (L.conj().T @ L @ rho + rho @ L.conj().T @ L))
        for L in jumps
    )
)

STEADY = lambda H, jumps, r=1.0, dt=1e-3, tol=1e-10, iters=10000: (
    lambda step: (
        lambda f: f(f, np.eye(H.shape[0], dtype=complex) / H.shape[0])
    )(
        lambda self, rho: (
            rho if np.linalg.norm(LINDBLAD(rho, H, jumps, r)) < tol
            else self(self, _normalize(rho + dt * LINDBLAD(rho, H, jumps, r)))
        )
    )(-1)
)

_normalize = lambda rho: (
    lambda tr: rho / tr if tr > 0 else rho
)(np.trace(rho).real)

DARK = lambda L: (
    lambda u, s, vh, tol=1e-8: vh[int(np.sum(s > tol)):].conj().T
)(*np.linalg.svd(L))

E8_CARTAN = np.pad(2 * np.eye(8, dtype=int), ((0, 0), (0, 0))) - np.pad(
    np.eye(8, dtype=int, k=1) + np.eye(8, dtype=int, k=-1),
    ((0, 0), (0, 0)),
)

E8_DET = round(np.linalg.det(E8_CARTAN))

E8_EVEN = all(E8_CARTAN[i, i] % 2 == 0 for i in range(8))
