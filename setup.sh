#!/bin/bash

# AI Story to Video Converter Setup Script
# Repository: https://github.com/PiyushPatidar-Druva/ai_app
# This script automates the installation process for the AI Story to Video Converter

# Exit on error
set -e

echo "Setting up AI Story to Video Converter..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3.12 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip."
    exit 1
fi

# Check if Rust is installed
if ! command -v rustc &> /dev/null; then
    echo "Rust is not installed. Installing Rust..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source "$HOME/.cargo/env"
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install core dependencies first
echo "Installing core dependencies..."
pip install gTTS pillow moviepy requests

# Install AI/ML dependencies
echo "Installing AI/ML dependencies..."
pip install transformers
pip install diffusers
pip install torch torchvision torchaudio

# Create necessary directories
echo "Creating project directories..."
mkdir -p app/utils static templates

# Create __init__.py files
touch app/__init__.py
touch app/utils/__init__.py

echo "Setup completed successfully!"
echo "You can now activate the virtual environment with: source venv/bin/activate" 