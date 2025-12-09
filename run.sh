#!/bin/bash

# Pet Adoption Center - Quick Start Script

set -e

cd "$(dirname "$0")"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Run the app
echo ""
echo "Starting Pet Adoption Center..."
echo "Open http://localhost:5000 in your browser"
echo "Press Ctrl+C to stop"
echo ""
python app.py
