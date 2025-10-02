#!/usr/bin/env python3
"""
PDF Merger - Simple command line tool to merge multiple PDF files
Usage: python3 merge.py fichier1.pdf fichier2.pdf ... [--output output.pdf]
"""

import sys
import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import argparse


def merge_pdfs(input_files, output_file):
    """
    Merge multiple PDF files into a single output file
    
    Args:</br>        input_files (list): List of PDF file paths to merge
        output_file (str): Output file path for the merged PDF
        
    Returns:</br>        bool: True if successful, False otherwise
    """
    try:
        # Create a PDF writer object
        pdf_writer = PdfWriter()
        
        # Validate input files exist
        for file_path in input_files:
            if not os.path.exists(file_path):
                print(f"Error: File '{file_path}' does not exist.")
                return False
            
            if not file_path.lower().endswith('.pdf'):
                print(f"Error: '{file_path}' is not a PDF file.")
                return False
        
        # Merge PDFs
        print("Merging PDF files...")
        for file_path in input_files:
            print(f"   Adding: {os.path.basename(file_path)}")
            pdf_reader = PdfReader(file_path)
            
            # Add all pages from current PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        
        # Write merged PDF to output file
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)
        
        print(f"Successfully merged {len(input_files)} files into '{os.path.basename(output_file)}'")
        return True
        
    except Exception as e:
        print(f"Error merging PDFs: {str(e)}")
        return False


def generate_output_filename(input_files):
    """
    Generate output filename based on input files
    
    Args:</br>        input_files (list): List of input file paths
        
    Returns:</br>        str: Generated output filename
    """
    if len(input_files) == 1:
        base_name = Path(input_files[0]).stem
        return f"{base_name}_merged.pdf"
    else:
        # Use first file's base name with _merged suffix
        base_name = Path(input_files[0]).stem
        return f"{base_name}_merged.pdf"


def main():
    """Main function to handle command line arguments and execute PDF merging"""
    parser = argparse.ArgumentParser(
        description="Merge multiple PDF files into a single document",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 merge.py document1.pdf document2.pdf
  python3 merge.py *.pdf --output combined.pdf
  python3 merge.py file1.pdf file2.pdf file3.pdf --output final.pdf
        """
    )
    
    parser.add_argument('files', nargs='+', help='PDF files to merge')
    parser.add_argument('-o', '--output', help='Output filename (optional)')
    
    args = parser.parse_args()
    
    # Check if files are provided
    if not args.files:
        print("Error: No PDF files specified.")
        parser.print_help()
        sys.exit(1)
    
    # Generate output filename if not provided
    if args.output:
        output_file = args.output
    else:
        output_file = generate_output_filename(args.files)
    
    # Ensure output file has .pdf extension
    if not output_file.lower().endswith('.pdf'):
        output_file += '.pdf'
    
    print(f"PDF Merger")
    print(f"Input files: {len(args.files)}")
    print(f"Output file: {output_file}")
    print("-" * 50)
    
    # Merge the PDFs
    success = merge_pdfs(args.files, output_file)
    
    if success:
        print(f"\nMerge completed successfully!")
        print(f"Merged file location: {os.path.abspath(output_file)}")
        sys.exit(0)
    else:
        print(f"\nMerge failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
