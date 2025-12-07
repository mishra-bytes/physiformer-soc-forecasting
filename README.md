# Res-PhyT
## Overview

Residual Physics-Informed Transformer for battery State-of-Charge (SOC) forecasting.


## 📂 Project Structure

```text
res-phyt/
├── configs/                 # Configuration files (Hydra YAMLs)
│   ├── dataset/             # Dataset-specific paths and settings
│   └── model/               # Model hyperparameters and architecture settings
├── data/                    # Data storage (ignored by Git)
│   ├── raw/                 # Original immutable datasets
│   │   ├── bit/             # Beijing Institute of Technology .mat files
│   │   ├── nasa/            # NASA Ames Center .mat files
│   │   ├── oxford/          # Oxford Battery Degradation .mat files
│   │   └── tum/             # TUM BMW i3 .csv files
│   └── processed/           # Feature-engineered .npz tensors for training
├── notebooks/               # Jupyter notebooks for EDA and prototyping
├── src/                     # Source code package
│   ├── data/                # Data pipeline modules
│   │   ├── loaders/         # Parsers for specific file formats (BIT, NASA, etc.)
│   │   ├── components.py    # Scaler logic and type definitions
│   │   └── preprocessing.py # The 17-feature universal preprocessor
│   ├── models/              # PyTorch model definitions (Res-PhyT architecture)
│   └── utils/               # Helper scripts (logging, metrics, checkpointing)
├── requirements.txt         # Project dependencies
└── setup_project.py         # Script to initialize folder structure

'''




- **configs/**: Experiment settings (learning rate, batch size, model size) in YAML format
- **data/raw/**: Original data files (.mat, .csv) in read-only format
- **data/processed/**: Clean, feature-engineered .npz tensors for model training
- **notebooks/**: Sandbox for experiments, visualization, and prototyping
- **src/data/loaders/**: File format handlers for various data sources
- **src/data/preprocessing.py**: Feature engineering implementation (derivatives, Nernst, Arrhenius equations)
- **src/models/**: PyTorch implementation of Res-PhyT (Encoder, Decoder, Probability Head)
- **src/utils/**: Helper utilities (checkpoints, WandB logging, metrics calculation)
