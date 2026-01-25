#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import subprocess
import sys
from pathlib import Path

# Mapping of English file names to Russian file names
FILE_MAPPING = {
    'p_e_10_ratio.md': 'соотношение_p_e_10.md',
    'p2b.md': 'цена_к_балансовой.md',
    'pac-man_defense.md': 'защита_пак_мен.md',
    'paga.md': 'пага.md',
    'paid-in_capital.md': 'внесённый_капитал.md',
    'paid-up_capital.md': 'оплаченный_капитал.md',
    'painting_the_tape.md': 'окрашивание_ленты.md',
    'pair_trading.md': 'парная_торговля.md',
    'pairs_arbitrage.md': 'парная_арбитраж.md',
    'pairs_trade.md': 'парная_сделка.md',
    'pairs_trading.md': 'парная_торговля_стратегия.md',
    'pairs_trading_signals.md': 'сигналы_парной_торговли.md',
    'pakistan_stock_exchange_(psx).md': 'пакистанская_фондовая_биржа.md',
    'palau_stock_exchange_(pse).md': 'фондовая_биржа_палау.md',
    'pancakeswap.md': 'панкейксвап.md',
    'paper_money.md': 'бумажные_деньги.md',
    'paper_trade.md': 'бумажная_торговля.md',
    'paper_trading.md': 'бумажная_торговля_практика.md',
    'papua_new_guinea_stock_exchange_(pngx).md': 'фондовая_биржа_папуа.md',
    'par.md': 'номинал.md',
    'par_value.md': 'номинальная_стоимость.md',
    'par_yield_curve.md': 'кривая_доходности_номинала.md',
    'parabolic_curve_patterns.md': 'параболические_паттерны.md',
}

def remove_internal_links(content):
    """Remove internal markdown links, keeping only the text."""
    content = re.sub(r'\[([^\]]+)\]\(\.\./[^)]+\.md\)', r'\1', content)
    return content

def translate_with_claude(text, file_name):
    """Translate text using Claude via command line."""
    # Create a prompt file
    prompt = f"""Translate the following financial/trading article from English to Russian.
Keep the same structure and formatting (markdown, code blocks, etc).
Keep all financial terms, company names, and acronyms as is or with standard Russian translations.
Keep technical terms unchanged if they are widely used in Russian finance.

{text}"""

    # Use claude command (assuming it's installed and configured)
    try:
        result = subprocess.run(
            ['claude', '-'],
            input=prompt.encode('utf-8'),
            capture_output=True,
            timeout=60
        )
        if result.returncode == 0:
            return result.stdout.decode('utf-8')
    except Exception as e:
        print(f"Error translating {file_name}: {e}")

    return text  # Return original if translation fails

def main():
    en_dir = Path("C:\\StockSharp\\AlgoTradingLib\\en\\pedia\\p")
    ru_dir = Path("C:\\StockSharp\\AlgoTradingLib\\ru\\pedia\\p")

    # Create Russian directory if it doesn't exist
    ru_dir.mkdir(parents=True, exist_ok=True)

    translated = 0
    skipped = 0

    for en_file, ru_file in FILE_MAPPING.items():
        en_path = en_dir / en_file
        ru_path = ru_dir / ru_file

        # Check if Russian file already exists
        if ru_path.exists():
            skipped += 1
            continue

        # Read English file
        try:
            with open(en_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {en_file}: {e}")
            continue

        # Remove internal links
        content = remove_internal_links(content)

        # Translate content using Claude
        translated_content = translate_with_claude(content, en_file)

        # Save Russian file
        try:
            with open(ru_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)
            translated += 1
        except Exception as e:
            print(f"Error writing {ru_file}: {e}")

    print(f"Переведено файлов: {translated} (пропущено: {skipped})")

if __name__ == "__main__":
    main()
