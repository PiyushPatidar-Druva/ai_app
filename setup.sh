#!/bin/bash

# AI Story to Video Converter Setup Script
# Repository: https://github.com/PiyushPatidar-Druva/ai_app
# This script automates the installation process for the AI Story to Video Converter

# Exit on error
set -e

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3.12 or higher."
    exit 1
fi

# Check for pip
if ! command -v pip &> /dev/null; then
    echo "pip is required but not installed. Please install pip."
    exit 1
fi

# Check for Rust
if ! command -v rustc &> /dev/null; then
    echo "Rust is required but not installed. Installing Rust..."
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

# Install core dependencies
echo "Installing core dependencies..."
pip install flask==3.0.2 \
    flask-cors==3.0.10 \
    gTTS==2.5.1 \
    Pillow==10.2.0 \
    moviepy==1.0.3 \
    python-dotenv==0.19.0 \
    requests==2.31.0

# Install AI/ML dependencies
echo "Installing AI/ML dependencies..."
pip install huggingface-hub \
    transformers==4.37.2 \
    diffusers==0.25.0 \
    torch==2.2.0 \
    torchvision==0.17.0 \
    torchaudio==2.2.0 \
    accelerate==1.5.2

# Create necessary directories
echo "Creating project directories..."
mkdir -p app/utils static/css static/js templates

# Create __init__.py files
echo "Creating Python package files..."
touch app/__init__.py app/utils/__init__.py

# Make the script executable
chmod +x setup.sh

echo "Setup completed successfully!"
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To start the application, run: python app.py" 