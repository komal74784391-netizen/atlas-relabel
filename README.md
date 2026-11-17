# atlas-relabel

Reference implementation for **Adaptive Relabeling under Annotation Budgets**, accepted at CADS 2025.

## Repository contents

- `src/` — annotation policies, budget accounting, and calibration utilities
- `experiments/` — sweep driver used to produce the paper's figures
- `configs/` — configuration files for the CADS 2025 experiments
- `results/` — sweep outputs and summary tables
- `cli_interface.json` — machine-readable interface of the relabeling CLI

## Quick start

```bash
pip install -r requirements.txt
python experiments/relabel_sweep.py --config configs/cads2025.yaml
```

## Citation

> A. Diaz, M. Serrano, T. Iqbal. Adaptive Relabeling under Annotation Budgets. CADS 2025.
