# PDF Merger

> A simple command-line tool to merge multiple PDF files into a single document. Perfect for combining documents, reports, and presentations with just one command.

## Features

- **Simple command-line interface**: Merge PDFs with a single command
- **Automatic output naming**: Generate merged filenames automatically
- **Multiple file support**: Combine as many PDFs as needed
- **Custom output names**: Specify your own output filename
- **Error handling**: Validate files and provide clear error messages
- **Cross-platform**: Works on Windows, macOS, and Linux

## Tech Stack

- **Python 3** – Core scripting language
- **PyPDF2** – PDF manipulation library
- **argparse** – Command-line argument parsing
- **pathlib** – Modern path handling

## Getting Started

Clone the repository and navigate to the directory

```bash
git clone git@github.com:yourusername/pdf-merge.git
cd pdf-merge
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Basic usage (automatic output filename):
```bash
python3 merge.py fichier1.pdf fichier2.pdf fichier3.pdf
```

Custom output filename:
```bash
python3 merge.py document1.pdf document2.pdf --output combined.pdf
```

Merge all PDFs in current directory:
```bash
python3 merge.py *.pdf --output all_documents.pdf
```

## Examples

```bash
# Merge two documents
python3 merge.py report1.pdf report2.pdf

# Merge multiple files with custom name
python3 merge.py file1.pdf file2.pdf file3.pdf --output final_document.pdf

# Merge files with specific output location
python3 merge.py *.pdf --output ~/Documents/merged.pdf
```

## Output

The tool will:
- Validate input files exist and are PDFs
- Merge files in the order specified
- Generate output in the current directory (or specified path)
- Show success/failure status with file location

## License

MIT License - feel free to use and modify as needed
