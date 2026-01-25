#!/usr/bin/env python3
import os

RU_DIR = r"C:\StockSharp\AlgoTradingLib\ru\pedia\r"

# Проверяем какие русские файлы не имеют заголовка
files_without_title = []
files_with_title = 0

for fname in sorted(os.listdir(RU_DIR)):
    if fname.endswith('.md'):
        fpath = os.path.join(RU_DIR, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline().strip()
                if first_line.startswith('# '):
                    files_with_title += 1
                else:
                    files_without_title.append((fname, first_line[:100] if first_line else "[Empty file]"))
        except:
            files_without_title.append((fname, "[Error reading]"))

print(f"Русских файлов всего: {files_with_title + len(files_without_title)}")
print(f"С заголовками: {files_with_title}")
print(f"БЕЗ заголовков: {len(files_without_title)}")
print()

if files_without_title:
    print("Файлы БЕЗ заголовков:")
    for fname, first_line in files_without_title:
        print(f"  {fname:45s} -> {first_line}")
