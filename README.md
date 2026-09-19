# e8-qudit-qec
DOI Zenodo.22844636
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
numpy
pytest
git init
git add e8qec.py test_e8qec.py README.md requirements.txt
git commit -m "E8 x E8 qudit d=5 autonomous QEC core"
git remote add origin <repo>
git push -u origin main
