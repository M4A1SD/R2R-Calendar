#!/usr/bin/env python
"""
Installation script for the assistant_team package.
This script provides an easy way to install the package in development mode.
"""

import subprocess
import sys
import os

def install_package():
    """Install the assistant_team package in development mode."""
    print("🚀 Installing assistant_team package...")
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Install the package in development mode
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-e", script_dir
        ])
        
        print("Installation complete!")
        print("You can now import the package with: import assistant_team")
        print("Try running: python -c 'from assistant_team import kickoff; kickoff()'")
        
    except subprocess.CalledProcessError as e:
        print(f"Installation failed with error: {e}")
        print("Make sure you have pip installed and try again.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_package() 