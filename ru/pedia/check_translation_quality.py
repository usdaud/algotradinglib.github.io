#!/usr/bin/env python3
"""
Скрипт проверки качества перевода
Критерии:
1. Длина файла: русский должен быть 70-85% от английского (допустимо 60-100%)
2. Количество слов: русский должен быть 75-90% от английского (допустимо 65-100%)
3. Наличие кириллицы в содержимом
"""
import os
import re
from pathlib import Path

EN_BASE = r"C:\StockSharp\AlgoTradingLib\en\pedia"
RU_BASE = r"C:\StockSharp\AlgoTradingLib\ru\pedia"

# Критерии качества
MIN_SIZE_RATIO = 0.60  # минимум 60% от размера английского файла
MAX_SIZE_RATIO = 1.00  # максимум 100%
OPTIMAL_SIZE_MIN = 0.70  # оптимально от 70%
OPTIMAL_SIZE_MAX = 0.85  # оптимально до 85%

MIN_WORD_RATIO = 0.65  # минимум 65% от количества слов
MAX_WORD_RATIO = 1.00  # максимум 100%
OPTIMAL_WORD_MIN = 0.75  # оптимально от 75%
OPTIMAL_WORD_MAX = 0.90  # оптимально до 90%

MIN_CYRILLIC_PERCENT = 40  # минимум 40% кириллических символов

def count_words(text):
    """Подсчет слов в тексте"""
    # Убираем markdown разметку, код и формулы
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\$[^$]+\$', '', text)
    # Считаем слова
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_cyrillic(text):
    """Подсчет процента кириллических символов"""
    if not text:
        return 0
    cyrillic = len(re.findall(r'[а-яА-ЯёЁ]', text))
    total_letters = len(re.findall(r'[a-zA-Zа-яА-ЯёЁ]', text))
    if total_letters == 0:
        return 0
    return (cyrillic / total_letters) * 100

def check_file_quality(en_path, ru_path):
    """Проверка качества перевода одного файла"""
    result = {
        'en_path': en_path,
        'ru_path': ru_path,
        'exists': False,
        'issues': []
    }

    if not ru_path.exists():
        result['issues'].append('FILE_MISSING')
        return result

    result['exists'] = True

    # Читаем файлы
    try:
        en_text = en_path.read_text(encoding='utf-8')
        ru_text = ru_path.read_text(encoding='utf-8')
    except Exception as e:
        result['issues'].append(f'READ_ERROR: {e}')
        return result

    # Размеры файлов
    en_size = len(en_text)
    ru_size = len(ru_text)
    size_ratio = ru_size / en_size if en_size > 0 else 0

    result['en_size'] = en_size
    result['ru_size'] = ru_size
    result['size_ratio'] = size_ratio

    # Количество слов
    en_words = count_words(en_text)
    ru_words = count_words(ru_text)
    word_ratio = ru_words / en_words if en_words > 0 else 0

    result['en_words'] = en_words
    result['ru_words'] = ru_words
    result['word_ratio'] = word_ratio

    # Процент кириллицы
    cyrillic_percent = count_cyrillic(ru_text)
    result['cyrillic_percent'] = cyrillic_percent

    # Проверка критериев
    if size_ratio < MIN_SIZE_RATIO:
        result['issues'].append(f'SIZE_TOO_SHORT: {size_ratio:.1%} (min {MIN_SIZE_RATIO:.0%})')
    elif size_ratio > MAX_SIZE_RATIO:
        result['issues'].append(f'SIZE_TOO_LONG: {size_ratio:.1%}')
    elif not (OPTIMAL_SIZE_MIN <= size_ratio <= OPTIMAL_SIZE_MAX):
        result['issues'].append(f'SIZE_WARNING: {size_ratio:.1%} (optimal {OPTIMAL_SIZE_MIN:.0%}-{OPTIMAL_SIZE_MAX:.0%})')

    if word_ratio < MIN_WORD_RATIO:
        result['issues'].append(f'WORDS_TOO_FEW: {word_ratio:.1%} (min {MIN_WORD_RATIO:.0%})')
    elif word_ratio > MAX_WORD_RATIO:
        result['issues'].append(f'WORDS_TOO_MANY: {word_ratio:.1%}')
    elif not (OPTIMAL_WORD_MIN <= word_ratio <= OPTIMAL_WORD_MAX):
        result['issues'].append(f'WORDS_WARNING: {word_ratio:.1%} (optimal {OPTIMAL_WORD_MIN:.0%}-{OPTIMAL_WORD_MAX:.0%})')

    if cyrillic_percent < MIN_CYRILLIC_PERCENT:
        result['issues'].append(f'LOW_CYRILLIC: {cyrillic_percent:.1f}% (min {MIN_CYRILLIC_PERCENT}%)')

    return result

def scan_folder(letter):
    """Сканирование папки с определенной буквой"""
    en_folder = Path(EN_BASE) / letter
    ru_folder = Path(RU_BASE) / letter

    if not en_folder.exists():
        return []

    results = []
    en_files = sorted(en_folder.glob('*.md'))

    for en_file in en_files:
        # Ищем соответствующий русский файл по заголовку
        en_title = None
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                if first_line.startswith('# '):
                    en_title = first_line[2:].strip()
        except:
            pass

        # Ищем русский файл с таким же заголовком
        ru_file = None
        if ru_folder.exists():
            for rf in ru_folder.glob('*.md'):
                try:
                    with open(rf, 'r', encoding='utf-8') as f:
                        ru_first = f.readline().strip()
                        if ru_first.startswith('# '):
                            ru_title = ru_first[2:].strip()
                            if ru_title == en_title:
                                ru_file = rf
                                break
                except:
                    pass

        if ru_file is None:
            ru_file = ru_folder / en_file.name

        result = check_file_quality(en_file, ru_file)
        results.append(result)

    return results

def main():
    """Главная функция"""
    letters = 'abcdefghijklmnopqrstuvwxyz'

    all_results = []
    folder_stats = {}

    print("Проверка качества переводов...")
    print("=" * 100)

    for letter in letters:
        print(f"\nПроверка папки {letter}...")
        results = scan_folder(letter)
        all_results.extend(results)

        # Статистика по папке
        total = len(results)
        missing = sum(1 for r in results if not r['exists'])
        with_issues = sum(1 for r in results if r['exists'] and r['issues'])
        ok = total - missing - with_issues

        folder_stats[letter] = {
            'total': total,
            'missing': missing,
            'with_issues': with_issues,
            'ok': ok
        }

        print(f"  Всего файлов: {total}, Отсутствуют: {missing}, С проблемами: {with_issues}, OK: {ok}")

    # Сводный отчет
    print("\n" + "=" * 100)
    print("\nСВОДКА ПО ПАПКАМ:")
    print(f"{'Папка':<8} {'Всего':<8} {'Нет':<8} {'Проблемы':<12} {'OK':<8} {'% OK':<8}")
    print("-" * 100)

    total_all = 0
    missing_all = 0
    issues_all = 0
    ok_all = 0

    for letter in letters:
        stats = folder_stats[letter]
        total = stats['total']
        missing = stats['missing']
        issues = stats['with_issues']
        ok = stats['ok']
        ok_percent = (ok / total * 100) if total > 0 else 0

        print(f"{letter:<8} {total:<8} {missing:<8} {issues:<12} {ok:<8} {ok_percent:>6.1f}%")

        total_all += total
        missing_all += missing
        issues_all += issues
        ok_all += ok

    print("-" * 100)
    ok_percent_all = (ok_all / total_all * 100) if total_all > 0 else 0
    print(f"{'ИТОГО':<8} {total_all:<8} {missing_all:<8} {issues_all:<12} {ok_all:<8} {ok_percent_all:>6.1f}%")

    # Список файлов с проблемами
    print("\n" + "=" * 100)
    print("\nФАЙЛЫ ТРЕБУЮЩИЕ ВНИМАНИЯ:")
    print("-" * 100)

    problem_files = [r for r in all_results if not r['exists'] or r['issues']]

    if problem_files:
        for r in problem_files:
            en_name = r['en_path'].name
            folder = r['en_path'].parent.name
            print(f"\n{folder}/{en_name}")
            if not r['exists']:
                print("  ❌ ФАЙЛ НЕ НАЙДЕН")
            else:
                for issue in r['issues']:
                    print(f"  ⚠️  {issue}")
                print(f"     Размер: {r['ru_size']:,} / {r['en_size']:,} ({r['size_ratio']:.1%})")
                print(f"     Слова: {r['ru_words']:,} / {r['en_words']:,} ({r['word_ratio']:.1%})")
                print(f"     Кириллица: {r['cyrillic_percent']:.1f}%")
    else:
        print("\n✅ Все файлы в порядке!")

    # Сохранение отчета
    report_path = Path(RU_BASE) / 'QUALITY_REPORT.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("ОТЧЕТ О КАЧЕСТВЕ ПЕРЕВОДОВ\n")
        f.write("=" * 100 + "\n\n")
        f.write(f"Всего файлов: {total_all}\n")
        f.write(f"Отсутствуют: {missing_all}\n")
        f.write(f"С проблемами: {issues_all}\n")
        f.write(f"OK: {ok_all} ({ok_percent_all:.1f}%)\n\n")

        if problem_files:
            f.write("ФАЙЛЫ ТРЕБУЮЩИЕ ВНИМАНИЯ:\n")
            f.write("-" * 100 + "\n\n")
            for r in problem_files:
                en_name = r['en_path'].name
                folder = r['en_path'].parent.name
                f.write(f"{folder}/{en_name}\n")
                if not r['exists']:
                    f.write("  ФАЙЛ НЕ НАЙДЕН\n")
                else:
                    for issue in r['issues']:
                        f.write(f"  {issue}\n")
                f.write("\n")

    print(f"\n\nОтчет сохранен в: {report_path}")

if __name__ == '__main__':
    main()
