#!/bin/bash

# setup.sh
# Automated setup script for SQL Parser project

echo "=========================================="
echo "SQL Parser Setup Script"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Java is installed
echo "Checking Java installation..."
if command -v java &> /dev/null; then
    echo -e "${GREEN}✓ Java is installed${NC}"
    java -version
else
    echo -e "${RED}✗ Java is not installed${NC}"
    echo "Please install Java to use ANTLR4"
    echo "Ubuntu/Linux: sudo apt install default-jre"
    echo "macOS: brew install openjdk"
    exit 1
fi

echo ""

# Download ANTLR4 if not exists
ANTLR_JAR="antlr-4.13.1-complete.jar"
if [ -f "$ANTLR_JAR" ]; then
    echo -e "${GREEN}✓ ANTLR4 JAR found${NC}"
else
    echo -e "${YELLOW}Downloading ANTLR4...${NC}"
    curl -O https://www.antlr.org/download/$ANTLR_JAR
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ ANTLR4 downloaded successfully${NC}"
    else
        echo -e "${RED}✗ Failed to download ANTLR4${NC}"
        exit 1
    fi
fi

echo ""

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Python dependencies installed${NC}"
else
    echo -e "${RED}✗ Failed to install Python dependencies${NC}"
    exit 1
fi

echo ""

# Generate parser
echo "Generating parser from grammar..."
cd parser/grammar

# Create generated directory if it doesn't exist
mkdir -p ../generated

# Run ANTLR4
java -jar ../../$ANTLR_JAR -Dlanguage=Python3 -visitor -o ../generated SimpleSQL.g4

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Parser generated successfully${NC}"
else
    echo -e "${RED}✗ Failed to generate parser${NC}"
    cd ../..
    exit 1
fi

cd ../..

echo ""
echo "=========================================="
echo -e "${GREEN}✓ Setup completed successfully!${NC}"
echo "=========================================="
echo ""
echo "To run the parser:"
echo "  python main.py"
echo ""
echo "To test with custom SQL:"
echo "  python main.py --input my_query.sql --output my_output.json"
echo ""
