# e8_Qudit
# e8-qudit-qec

Autonomous quantum error correction on qudit d=5
with E8 × E8 conservation law and reflection symmetry.

## Structure
- `e8qec.py` — core: predicates, weight enumerator, L_heal, decoder, Monte Carlo
- `test_e8qec.py` — property tests
- `requirements.txt` — numpy

## Run
pip install -r requirements.txt
pytest test_e8qec.py

## Parameters
Computed from the framework:
- CODE_DIM, DISTANCE, DETECT, CORRECT, LOGICAL_QUDITS

## Notes
All numbers are derived, not assumed.
Run and read the module namespace directly.
