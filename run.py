import os
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import and run the application
from src.app import main

if __name__ == "__main__":
    # Change working directory to project root
    os.chdir(project_root)
    main()