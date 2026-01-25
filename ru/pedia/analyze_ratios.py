#!/usr/bin/env python3
"""
Скрипт анализа соотношений размеров EN/RU файлов.
Определяет реальные статистические границы для критериев качества.
"""
import os
import re
import sys
import statistics
from pathlib import Path

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')

EN_BASE = Path(r"C:\StockSharp\AlgoTradingLib\en\pedia")
RU_BASE = Path(r"C:\StockSharp\AlgoTradingLib\ru\pedia")

def count_words(text):
    """Подсчёт слов без учёта кода и формул"""
    # Убираем блоки кода
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Убираем inline код
    text = re.sub(r'`[^`]+`', '', text)
    # Убираем формулы
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\$[^$]+\$', '', text)
    # Считаем слова
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_chars(text):
    """Подсчёт символов без учёта кода"""
    # Убираем блоки кода
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    return len(text)

def cyrillic_percent(text):
    """Процент кириллических символов среди всех букв"""
    if not text:
        return 0
    cyrillic = len(re.findall(r'[а-яА-ЯёЁ]', text))
    total_letters = len(re.findall(r'[a-zA-Zа-яА-ЯёЁ]', text))
    if total_letters == 0:
        return 0
    return (cyrillic / total_letters) * 100

def analyze_pair(en_path, ru_path):
    """Анализ пары файлов EN/RU"""
    try:
        en_text = en_path.read_text(encoding='utf-8')
        ru_text = ru_path.read_text(encoding='utf-8')
    except Exception as e:
        return None

    en_size = len(en_text)
    ru_size = len(ru_text)

    en_chars = count_chars(en_text)
    ru_chars = count_chars(ru_text)

    en_words = count_words(en_text)
    ru_words = count_words(ru_text)

    cyr_pct = cyrillic_percent(ru_text)

    if en_size == 0 or en_words == 0 or en_chars == 0:
        return None

    return {
        'en_size': en_size,
        'ru_size': ru_size,
        'size_ratio': ru_size / en_size,
        'en_chars': en_chars,
        'ru_chars': ru_chars,
        'chars_ratio': ru_chars / en_chars,
        'en_words': en_words,
        'ru_words': ru_words,
        'words_ratio': ru_words / en_words,
        'cyrillic_pct': cyr_pct
    }

def main():
    print("=" * 80)
    print("АНАЛИЗ СООТНОШЕНИЙ РАЗМЕРОВ EN/RU ФАЙЛОВ")
    print("=" * 80)
    print()

    all_data = []

    # Анализируем файлы из всех папок
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        en_folder = EN_BASE / letter
        ru_folder = RU_BASE / letter

        if not en_folder.exists() or not ru_folder.exists():
            continue

        en_files = list(en_folder.glob('*.md'))
        count = 0

        for en_file in en_files:
            ru_file = ru_folder / en_file.name
            if ru_file.exists():
                data = analyze_pair(en_file, ru_file)
                if data:
                    data['folder'] = letter
                    data['filename'] = en_file.name
                    all_data.append(data)
                    count += 1

        print(f"Папка {letter}: проанализировано {count} файлов")

    print()
    print(f"Всего проанализировано: {len(all_data)} пар файлов")
    print()

    if not all_data:
        print("Нет данных для анализа!")
        return

    # Извлекаем метрики
    size_ratios = [d['size_ratio'] for d in all_data]
    chars_ratios = [d['chars_ratio'] for d in all_data]
    words_ratios = [d['words_ratio'] for d in all_data]
    cyrillic_pcts = [d['cyrillic_pct'] for d in all_data]

    def print_stats(name, values):
        print(f"\n{name}:")
        print(f"  Минимум:    {min(values):.3f}")
        print(f"  Максимум:   {max(values):.3f}")
        print(f"  Среднее:    {statistics.mean(values):.3f}")
        print(f"  Медиана:    {statistics.median(values):.3f}")
        print(f"  Станд.откл: {statistics.stdev(values):.3f}")

        mean = statistics.mean(values)
        std = statistics.stdev(values)
        print(f"  mean-2std:  {mean - 2*std:.3f}")
        print(f"  mean+2std:  {mean + 2*std:.3f}")

        # Перцентили
        sorted_vals = sorted(values)
        n = len(sorted_vals)
        p5 = sorted_vals[int(n * 0.05)]
        p25 = sorted_vals[int(n * 0.25)]
        p75 = sorted_vals[int(n * 0.75)]
        p95 = sorted_vals[int(n * 0.95)]
        print(f"  5%:         {p5:.3f}")
        print(f"  25%:        {p25:.3f}")
        print(f"  75%:        {p75:.3f}")
        print(f"  95%:        {p95:.3f}")

    print("=" * 80)
    print("СТАТИСТИКА")
    print("=" * 80)

    print_stats("SIZE RATIO (RU bytes / EN bytes)", size_ratios)
    print_stats("CHARS RATIO (RU chars / EN chars) без кода", chars_ratios)
    print_stats("WORDS RATIO (RU words / EN words)", words_ratios)
    print_stats("CYRILLIC % в русских файлах", cyrillic_pcts)

    # Предлагаемые критерии
    print()
    print("=" * 80)
    print("РЕКОМЕНДУЕМЫЕ КРИТЕРИИ")
    print("=" * 80)

    # На основе перцентилей
    size_sorted = sorted(size_ratios)
    words_sorted = sorted(words_ratios)
    cyr_sorted = sorted(cyrillic_pcts)
    n = len(size_sorted)

    print()
    print("SIZE RATIO (байты):")
    print(f"  Критически мало:  < {size_sorted[int(n*0.01)]:.2f} (1-й перцентиль)")
    print(f"  Допустимый мин:   {size_sorted[int(n*0.05)]:.2f} (5-й перцентиль)")
    print(f"  Нормальный диап:  {size_sorted[int(n*0.25)]:.2f} - {size_sorted[int(n*0.75)]:.2f}")
    print(f"  Допустимый макс:  {size_sorted[int(n*0.95)]:.2f} (95-й перцентиль)")

    print()
    print("WORDS RATIO (слова):")
    print(f"  Критически мало:  < {words_sorted[int(n*0.01)]:.2f} (1-й перцентиль)")
    print(f"  Допустимый мин:   {words_sorted[int(n*0.05)]:.2f} (5-й перцентиль)")
    print(f"  Нормальный диап:  {words_sorted[int(n*0.25)]:.2f} - {words_sorted[int(n*0.75)]:.2f}")
    print(f"  Допустимый макс:  {words_sorted[int(n*0.95)]:.2f} (95-й перцентиль)")

    print()
    print("CYRILLIC %:")
    print(f"  Критически мало:  < {cyr_sorted[int(n*0.01)]:.1f}% (1-й перцентиль)")
    print(f"  Допустимый мин:   {cyr_sorted[int(n*0.05)]:.1f}% (5-й перцентиль)")

    # Выявляем проблемные файлы (выбросы)
    print()
    print("=" * 80)
    print("ПОТЕНЦИАЛЬНО ПРОБЛЕМНЫЕ ФАЙЛЫ (выбросы)")
    print("=" * 80)

    # Файлы с очень низким соотношением слов (возможно неполный перевод)
    threshold_words = words_sorted[int(n * 0.05)]
    threshold_cyr = cyr_sorted[int(n * 0.05)]

    print()
    print(f"Файлы с WORDS_RATIO < {threshold_words:.2f} (5-й перцентиль):")
    low_words = [d for d in all_data if d['words_ratio'] < threshold_words]
    for d in sorted(low_words, key=lambda x: x['words_ratio'])[:20]:
        print(f"  {d['folder']}/{d['filename']}: {d['words_ratio']:.2f} ({d['ru_words']}/{d['en_words']} слов)")

    print()
    print(f"Файлы с CYRILLIC < {threshold_cyr:.1f}% (5-й перцентиль):")
    low_cyr = [d for d in all_data if d['cyrillic_pct'] < threshold_cyr]
    for d in sorted(low_cyr, key=lambda x: x['cyrillic_pct'])[:20]:
        print(f"  {d['folder']}/{d['filename']}: {d['cyrillic_pct']:.1f}%")

    # Сохраняем результаты
    report_path = RU_BASE / 'RATIOS_ANALYSIS.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("АНАЛИЗ СООТНОШЕНИЙ EN/RU ФАЙЛОВ\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Проанализировано файлов: {len(all_data)}\n\n")

        f.write("СТАТИСТИКА:\n")
        f.write("-" * 60 + "\n")

        for name, values in [
            ("SIZE_RATIO", size_ratios),
            ("WORDS_RATIO", words_ratios),
            ("CYRILLIC_%", cyrillic_pcts)
        ]:
            mean = statistics.mean(values)
            std = statistics.stdev(values)
            sorted_v = sorted(values)
            f.write(f"\n{name}:\n")
            f.write(f"  Min: {min(values):.3f}, Max: {max(values):.3f}\n")
            f.write(f"  Mean: {mean:.3f}, Median: {statistics.median(values):.3f}\n")
            f.write(f"  Std: {std:.3f}\n")
            f.write(f"  P5: {sorted_v[int(n*0.05)]:.3f}, P95: {sorted_v[int(n*0.95)]:.3f}\n")

    print(f"\nОтчёт сохранён: {report_path}")

if __name__ == '__main__':
    main()
