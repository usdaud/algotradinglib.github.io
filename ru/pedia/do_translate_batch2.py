#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

os.chdir('r')

files_to_translate = [
    "реальная_норма_прибыли.md",
    "реальное_время.md",
    "множитель_реализации.md",
    "реализованный_доход.md",
    "реализованные_доходы_и_убытки.md",
    "реализованный_убыток.md",
    "анализ_реализованной_доходности.md",
    "управление_реализованным_риском.md",
    "реализованная_волатильность.md",
    "модели_реализованной_волатильности.md",
    "реализованная_доходность_облигаций.md",
    "анализ_данных_в_реальном_времени.md",
    "валовой_расчет_в_реальном_времени.md",
    "данные_рынка_в_реальном_времени.md",
    "котировка_в_реальном_времени.md",
    "корректировка_стратегии_в_реальном_времени.md",
    "системы_торговли_в_реальном_времени.md",
    "волатильность_в_реальном_времени.md",
    "переоценка_портфеля.md",
    "алгоритмы_переоценки.md",
    "частота_переоценки.md",
    "риск_переоценки.md",
]

translated_count = 0
failed_files = []

for filepath in files_to_translate:
    if not os.path.exists(filepath):
        print(f"SKIP: {filepath} (not found)")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Translating: {filepath}...", end='', flush=True)
        
        # Use claude to translate
        # Create temp files to avoid encoding issues
        temp_input = f'/tmp/input_{translated_count}.txt'
        temp_output = f'/tmp/output_{translated_count}.txt'
        
        with open(temp_input, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Call claude
        cmd = f'claude ask "Translate this markdown to Russian. Keep all markdown structure, formulas, links, code, tables exactly as is. Return ONLY the Russian translation without any explanation or preamble:" < {temp_input} > {temp_output} 2>&1'
        
        result = os.system(cmd)
        
        if result == 0 and os.path.exists(temp_output):
            with open(temp_output, 'r', encoding='utf-8') as f:
                translated_content = f.read().strip()
            
            if translated_content and len(translated_content) > len(content) * 0.3:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(translated_content)
                translated_count += 1
                print(" OK")
            else:
                print(" SKIP (short output)")
                failed_files.append(filepath)
        else:
            print(" ERROR")
            failed_files.append(filepath)
        
        # Cleanup
        for f in [temp_input, temp_output]:
            if os.path.exists(f):
                os.remove(f)
    
    except Exception as e:
        print(f" ERROR: {str(e)[:40]}")
        failed_files.append(filepath)

print(f"\n\nSummary:")
print(f"Translated: {translated_count} files")
print(f"Failed: {len(failed_files)} files")
if failed_files:
    print(f"Failed files: {', '.join(failed_files[:5])}")
