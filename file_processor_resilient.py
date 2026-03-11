import os
import csv
import json
import time
import logging
import traceback

# 1. Setup logging for failures
logging.basicConfig(
    filename='file_processor.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_single_csv(filepath):
    """
    Parses a single CSV file, simulating data aggregation.
    Raises specific errors if the file is corrupted, empty, or incorrectly formatted.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Check if the file is empty or missing headers
        if not reader.fieldnames:
            raise ValueError("CSV is empty or missing valid headers.")
            
        row_count = 0
        for row in reader:
            row_count += 1
            # Simulate a wrong format check (e.g., expecting at least 2 columns)
            if len(row) < 2:
                raise TypeError(f"Row {row_count} has incorrect format: {row}")
                
        return row_count

def file_processor_resilient(directory):
    """
    Reads a directory of CSV files, processes them, handles errors gracefully, 
    incorporates retry logic, and generates a JSON report.
    """
    report = {
        "files_processed": 0,
        "files_failed": 0,
        "error_details": {}
    }
    
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
        
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"No CSV files found in '{directory}'.")
        return
        
    print(f"Found {len(csv_files)} CSV files. Starting processing...\n")
    
    for filename in csv_files:
        filepath = os.path.join(directory, filename)
        
        # Implement retry logic for PermissionError
        max_retries = 3
        attempts = 0
        success = False
        
        while attempts < max_retries and not success:
            try:
                rows_processed = process_single_csv(filepath)
                report["files_processed"] += 1
                success = True
                print(f"[SUCCESS] Processed {filename} ({rows_processed} rows)")
                
            except PermissionError as pe:
                attempts += 1
                print(f"[WARNING] Permission denied for {filename}. Retrying ({attempts}/{max_retries})...")
                if attempts < max_retries:
                    time.sleep(1) # Wait 1 second before retrying
                else:
                    # Log full traceback after all retries fail
                    error_msg = traceback.format_exc()
                    logging.error(f"Failed to process {filename} after {max_retries} attempts:\n{error_msg}")
                    report["files_failed"] += 1
                    report["error_details"][filename] = "PermissionError: Failed after 3 retries."
                    print(f"[ERROR] Skipped {filename} due to repeated PermissionErrors.")
                    
            except Exception as e:
                # Catch-all for other errors (ValueError, TypeError, FileNotFoundError, etc.)
                # Log full traceback
                error_msg = traceback.format_exc()
                logging.error(f"Failed to process {filename}:\n{error_msg}")
                report["files_failed"] += 1
                report["error_details"][filename] = f"{type(e).__name__}: {str(e)}"
                print(f"[ERROR] Processing failed for {filename}. Skipped. See log for details.")
                break # Do not retry for non-Permission errors
                
    # 5. Export a report file
    try:
        report_path = 'processing_report.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4)
        print(f"\nProcessing complete! Report saved to '{report_path}'.")
    except Exception as e:
        print(f"Failed to save report: {e}")

if __name__ == "__main__":
    # Test directory
    sample_dir = "csv_data_folder"
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)
        print(f"Created '{sample_dir}'. Please drop some dummy .csv files in there and run again to test.")
    else:
        file_processor_resilient(sample_dir)
