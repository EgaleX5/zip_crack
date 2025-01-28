#!/bin/bash

# Script to fully setup EgaleX5 tool for a non-sudo user with custom mirrors and manual installation

echo "[+] Starting the setup process for non-sudo user..."

# Step 1: Ensure Python3 and Pip3 are installed (will skip if already installed)
echo "[+] Checking Python3 installation..."
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 not found. Please install Python3 manually."
    exit 1
fi

echo "[+] Checking Pip3 installation..."
if ! command -v pip3 &> /dev/null; then
    echo "[!] Pip3 not found, installing pip3 manually using custom mirror..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py --user
fi

# Step 2: Set custom mirror for pip3
echo "[+] Setting custom mirror for pip installation..."
PIP_MIRROR="https://pypi.tuna.tsinghua.edu.cn/simple"
export PIP_INDEX_URL=$PIP_MIRROR

# Step 3: Install Python packages using a custom mirror
echo "[+] Installing required Python packages..."
pip3 install --user termcolor
pip3 install --user tqdm
pip3 install --user zipfile36 colorama

# Step 4: Install system dependencies (curl, unzip, zip, parallel) manually
echo "[+] Checking and installing required system dependencies..."

# Check and install curl
if ! command -v curl &> /dev/null; then
    echo "[!] curl is not installed. You need to install curl manually from your package manager."
fi

# Check and install unzip
if ! command -v unzip &> /dev/null; then
    echo "[!] unzip is not installed. You need to install unzip manually from your package manager."
fi

# Check and install zip
if ! command -v zip &> /dev/null; then
    echo "[!] zip is not installed. You need to install zip manually from your package manager."
fi

# Check and install parallel
if ! command -v parallel &> /dev/null; then
    echo "[!] parallel is not installed. You need to install parallel manually from your package manager."
fi

# Step 5: Clone EgaleX5 repository from GitHub
echo "[+] Cloning EgaleX5 GitHub repository..."
git clone https://github.com/EgaleX5/zip_crack.git
cd zip_crack

# Step 6: Verify Python package installations
echo "[+] Verifying Python packages..."
python3 -m pip show termcolor tqdm zipfile36 colorama

# Step 7: Final Setup Completion
echo "[+] Setup completed successfully!"

# Instructions for running the tool
echo "[+] To run EgaleX5 tool, navigate to the zip_crack directory and use the following command:"
echo "    python3 zip_crack.py"

echo "[+] Enjoy your new setup!"
