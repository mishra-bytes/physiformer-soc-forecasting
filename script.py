import os
from pathlib import Path

def create_structure():
    # Define the project root as the current directory
    root = Path.cwd()
    
    # List of directories to create
    dirs = [
        "configs/dataset",
        "configs/model",
        "data/raw/bit",
        "data/raw/nasa",
        "data/raw/oxford",
        "data/raw/tum",
        "data/processed",
        "notebooks",
        "src/data/loaders",
        "src/models",
        "src/utils"
    ]
    
    # Create directories
    for d in dirs:
        path = root / d
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {path}")

    # Create __init__.py files to make directories importable packages
    init_locs = [
        "src",
        "src/data",
        "src/data/loaders",
        "src/models",
        "src/utils"
    ]
    
    for loc in init_locs:
        init_file = root / loc / "__init__.py"
        init_file.touch()
        print(f"🐍 Created: {init_file}")

    # Create key empty files
    (root / "requirements.txt").touch()
    (root / "README.md").write_text("# Res-PhyT\nResidual Physics-Informed Transformer")
    
    print("\n🚀 Project structure ready! You can now start coding.")

if __name__ == "__main__":
    create_structure()