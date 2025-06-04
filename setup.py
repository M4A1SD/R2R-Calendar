#!/usr/bin/env python3
"""
R2R Calendar - Automated Setup Script

This script automates the installation and setup of the R2R Calendar system.
It installs all necessary components and dependencies in the correct order.

Usage:
    python setup.py [--dev]

Options:
    --dev    Install development dependencies and tools

Author: R2R Calendar Team
License: MIT
"""

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SetupManager:
    """Manages the installation and setup of R2R Calendar components."""
    
    def __init__(self, dev_mode: bool = False):
        self.dev_mode = dev_mode
        self.project_root = Path(__file__).parent
        self.errors: List[str] = []
    
    def run_command(self, command: List[str], cwd: Optional[Path] = None, 
                   description: str = "") -> bool:
        """
        Run a shell command and handle errors.
        
        Args:
            command: Command to run as list of strings
            cwd: Working directory for the command
            description: Human-readable description of the command
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if description:
                logger.info(f"🔄 {description}")
            
            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.stdout:
                logger.debug(f"Output: {result.stdout}")
            
            logger.info(f"✅ {description or 'Command'} completed successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            error_msg = f"Failed to {description or 'run command'}: {e}"
            if e.stderr:
                error_msg += f"\nError output: {e.stderr}"
            
            logger.error(f"❌ {error_msg}")
            self.errors.append(error_msg)
            return False
        
        except Exception as e:
            error_msg = f"Unexpected error during {description}: {e}"
            logger.error(f"❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def check_python_version(self) -> bool:
        """Check if Python version meets requirements."""
        logger.info("🐍 Checking Python version...")
        
        if sys.version_info < (3, 10):
            error_msg = f"Python 3.10+ required, but found {sys.version_info.major}.{sys.version_info.minor}"
            logger.error(f"❌ {error_msg}")
            self.errors.append(error_msg)
            return False
        
        logger.info(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} is compatible")
        return True
    
    def check_git(self) -> bool:
        """Check if git is available."""
        logger.info("📡 Checking Git availability...")
        return self.run_command(["git", "--version"], description="Check Git installation")
    
    def install_main_server(self) -> bool:
        """Install main server dependencies."""
        logger.info("🖥️  Installing main server dependencies...")
        main_server_path = self.project_root / "main-server"
        
        return self.run_command(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            cwd=main_server_path,
            description="Install main server requirements"
        )
    
    def install_whatsapp_module(self) -> bool:
        """Install WhatsApp module."""
        logger.info("📱 Installing WhatsApp module...")
        whatsapp_path = self.project_root / "whatsapp-module"
        
        if not whatsapp_path.exists():
            logger.warning("⚠️  WhatsApp module directory not found, skipping...")
            return True
        
        return self.run_command(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            cwd=whatsapp_path,
            description="Install WhatsApp module in development mode"
        )
    
    def install_calendar_tool(self) -> bool:
        """Install Google Calendar tool."""
        logger.info("📅 Installing Google Calendar tool...")
        calendar_path = self.project_root / "G-calendar-tool"
        
        if not calendar_path.exists():
            logger.warning("⚠️  G-calendar-tool directory not found, skipping...")
            return True
        
        return self.run_command(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            cwd=calendar_path,
            description="Install Google Calendar tool in development mode"
        )
    
    def install_crewai(self) -> bool:
        """Install CrewAI assistant."""
        logger.info("🤖 Installing CrewAI assistant...")
        crewai_path = self.project_root / "CrewAI"
        
        if not crewai_path.exists():
            logger.warning("⚠️  CrewAI directory not found, skipping...")
            return True
        
        return self.run_command(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            cwd=crewai_path,
            description="Install CrewAI assistant in development mode"
        )
    
    def install_dev_tools(self) -> bool:
        """Install development tools."""
        if not self.dev_mode:
            return True
        
        logger.info("🛠️  Installing development tools...")
        dev_packages = [
            "pytest>=7.4.0,<8.0.0",
            "pytest-asyncio>=0.21.0,<1.0.0",
            "black>=23.0.0,<24.0.0",
            "flake8>=6.0.0,<7.0.0",
            "mypy>=1.7.0,<2.0.0",
            "pre-commit>=3.5.0,<4.0.0"
        ]
        
        for package in dev_packages:
            if not self.run_command(
                [sys.executable, "-m", "pip", "install", package],
                description=f"Install {package.split('>=')[0]}"
            ):
                return False
        
        return True
    
    def create_env_file(self) -> bool:
        """Create .env file from template if it doesn't exist."""
        logger.info("📝 Setting up environment configuration...")
        
        env_file = self.project_root / "main-server" / ".env"
        env_example = self.project_root / "main-server" / "env.example"
        
        if env_file.exists():
            logger.info("✅ .env file already exists")
            return True
        
        if not env_example.exists():
            logger.warning("⚠️  env.example file not found, skipping .env creation")
            return True
        
        try:
            # Copy template to .env
            with open(env_example, 'r') as src, open(env_file, 'w') as dst:
                dst.write(src.read())
            
            logger.info("✅ Created .env file from template")
            logger.info("📝 Please edit main-server/.env with your actual API keys and credentials")
            return True
            
        except Exception as e:
            error_msg = f"Failed to create .env file: {e}"
            logger.error(f"❌ {error_msg}")
            self.errors.append(error_msg)
            return False
    
    def setup_git_hooks(self) -> bool:
        """Set up Git pre-commit hooks for development."""
        if not self.dev_mode:
            return True
        
        logger.info("🔗 Setting up Git pre-commit hooks...")
        
        return self.run_command(
            ["pre-commit", "install"],
            cwd=self.project_root,
            description="Install pre-commit hooks"
        )
    
    def run_setup(self) -> bool:
        """Run the complete setup process."""
        logger.info("🚀 Starting R2R Calendar setup...")
        logger.info("=" * 60)
        
        setup_steps = [
            ("Python version check", self.check_python_version),
            ("Git availability check", self.check_git),
            ("Main server installation", self.install_main_server),
            ("WhatsApp module installation", self.install_whatsapp_module),
            ("Google Calendar tool installation", self.install_calendar_tool),
            ("CrewAI assistant installation", self.install_crewai),
            ("Development tools installation", self.install_dev_tools),
            ("Environment file setup", self.create_env_file),
            ("Git hooks setup", self.setup_git_hooks),
        ]
        
        failed_steps = []
        
        for step_name, step_function in setup_steps:
            if not step_function():
                failed_steps.append(step_name)
        
        logger.info("=" * 60)
        
        if failed_steps:
            logger.error("❌ Setup completed with errors!")
            logger.error("Failed steps:")
            for step in failed_steps:
                logger.error(f"  • {step}")
            
            if self.errors:
                logger.error("\nDetailed errors:")
                for error in self.errors:
                    logger.error(f"  • {error}")
            
            return False
        
        logger.info("🎉 Setup completed successfully!")
        logger.info("\n📋 Next steps:")
        logger.info("1. Edit main-server/.env with your API keys and credentials")
        logger.info("2. Set up your WhatsApp Business API and get ngrok URL")
        logger.info("3. Configure AWS DynamoDB and Google Calendar API")
        logger.info("4. Run: cd main-server && python whatsappBridgedAgent/main.py")
        logger.info("\n📚 For more information, see README.md")
        
        return True


def main():
    """Main entry point for the setup script."""
    parser = argparse.ArgumentParser(
        description="R2R Calendar setup script",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Install development dependencies and tools"
    )
    
    args = parser.parse_args()
    
    setup_manager = SetupManager(dev_mode=args.dev)
    success = setup_manager.run_setup()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main() 