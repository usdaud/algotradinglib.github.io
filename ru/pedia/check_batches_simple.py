#!/usr/bin/env python3
import subprocess
import os

base_dir = r"C:\StockSharp\AlgoTradingLib\ru\pedia"
os.chdir(base_dir)

# Check each batch size
for batch_num in range(20):
    result = subprocess.run(['python', 'split_files.py', str(batch_num)],
                          capture_output=True, text=True)
    files = [f for f in result.stdout.strip().split('\n') if f.strip()]
    print(f"Batch {batch_num}: {len(files)} files")
    if batch_num >= 18:  # Show last few for inspection
        print(f"  First: {files[0] if files else 'N/A'}")
        print(f"  Last: {files[-1] if files else 'N/A'}")
