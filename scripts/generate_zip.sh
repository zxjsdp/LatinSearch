#!/usr/bin/env bash

# This script is used to generate zip archives for download

# This script must be called as:
#  scripts/generate_zip.sh

UNAMES="$(uname -s)"

# Check if run this script in the right directory
if [ ! -e LICENSE ]
then
    echo "Run this script in the same folder with LICENSE"
    echo "  Usage: scripts/generate_zip.sh"
    exit
fi

mkdir LatinSearch
cd latin_search/

# Import fdi_generator.py to get .pyc bytecode file
echo "Generating .pyc file..."
python -c "import latinsearch"

# Rename .pyc file to .pyw file
echo "Generating .pyw file..."
mv latinsearch.pyc ../LatinSearch/LatinSearch.pyw

cd ..

echo "Copying necessary files to LatinSearch..."
# Copying file to LatinSearch folder
cp -rf latin_search/* README.md LICENSE LatinSearch

# Delete original LatinSearch.zip
rm LatinSearch.zip

if [[ $UNAMES == 'Linux' ]] || [[ $UNAMES == 'Darwin'  ]]
then
    # Use zip on Linux & Mac OSX
    echo "Zip files on Windows..."
    zip -r LatinSearch.zip LatinSearch
elif [[ $UNAMES == CYGWIN* ]] || [[ $UNAMES == MINGW* ]]
then
    # Use zip on Windows
    echo "Zip files..."
    scripts/zip -r LatinSearch.zip LatinSearch
else
    echo "Unknown Platform! Zip failed!!"
fi

# Cleaning job
echo "Cleaning ..."
rm -rf LatinSearch
