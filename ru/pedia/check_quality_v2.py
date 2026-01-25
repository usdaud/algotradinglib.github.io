#!/usr/bin/env python3
"""
Скрипт проверки качества переводов EN -> RU
Критерии основаны на статистическом анализе 8700+ файлов.

Запуск: python check_quality_v2.py
"""
import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')

EN_BASE = Path(r"C:\StockSharp\AlgoTradingLib\en\pedia")
RU_BASE = Path(r"C:\StockSharp\AlgoTradingLib\ru\pedia")

# ============================================================================
# КРИТЕРИИ КАЧЕСТВА (основаны на анализе реальных данных)
# ============================================================================

# SIZE RATIO (RU bytes / EN bytes)
# Среднее: 0.83, 5-95%: 0.64-1.02
SIZE_CRITICAL_MIN = 0.40    # Критически мало (ниже 1-го перцентиля)
SIZE_WARNING_MIN = 0.55     # Предупреждение
SIZE_OPTIMAL_MIN = 0.64     # Оптимальный минимум (5-й перцентиль)
SIZE_OPTIMAL_MAX = 1.02     # Оптимальный максимум (95-й перцентиль)
SIZE_WARNING_MAX = 1.20     # Предупреждение (слишком много)
SIZE_CRITICAL_MAX = 2.00    # Критически много

# WORDS RATIO (RU words / EN words)
# Среднее: 0.75, 5-95%: 0.54-0.94
WORDS_CRITICAL_MIN = 0.30   # Критически мало (перевод явно неполный)
WORDS_WARNING_MIN = 0.45    # Предупреждение
WORDS_OPTIMAL_MIN = 0.54    # Оптимальный минимум (5-й перцентиль)
WORDS_OPTIMAL_MAX = 0.94    # Оптимальный максимум (95-й перцентиль)
WORDS_WARNING_MAX = 1.10    # Предупреждение
WORDS_CRITICAL_MAX = 1.50   # Критически много

# CYRILLIC % (процент кириллицы в русском файле)
# Медиана: 96.85%, но 25% файлов имеют 0%
CYRILLIC_CRITICAL_MIN = 10  # Критически мало (файл не переведён)
CYRILLIC_WARNING_MIN = 50   # Предупреждение (возможно частичный перевод)
CYRILLIC_OPTIMAL_MIN = 70   # Оптимальный минимум

# ============================================================================

def count_words(text):
    """Подсчёт слов без учёта кода и формул"""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\$[^$]+\$', '', text)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def cyrillic_percent(text):
    """Процент кириллических символов среди всех букв"""
    if not text:
        return 0
    cyrillic = len(re.findall(r'[а-яА-ЯёЁ]', text))
    total_letters = len(re.findall(r'[a-zA-Zа-яА-ЯёЁ]', text))
    if total_letters == 0:
        return 0
    return (cyrillic / total_letters) * 100

def get_title(text):
    """Извлечь первый заголовок из markdown файла"""
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('# '):
            return line[2:].strip()
    return None

def classify_file(en_text, ru_text):
    """
    Классификация качества перевода.
    Возвращает: (status, issues, metrics)
    status: OK, WARNING, BAD, UNTRANSLATED
    """
    issues = []

    en_size = len(en_text)
    ru_size = len(ru_text)
    en_words = count_words(en_text)
    ru_words = count_words(ru_text)
    cyr_pct = cyrillic_percent(ru_text)

    metrics = {
        'en_size': en_size,
        'ru_size': ru_size,
        'size_ratio': ru_size / en_size if en_size > 0 else 0,
        'en_words': en_words,
        'ru_words': ru_words,
        'words_ratio': ru_words / en_words if en_words > 0 else 0,
        'cyrillic_pct': cyr_pct
    }

    size_ratio = metrics['size_ratio']
    words_ratio = metrics['words_ratio']

    status = 'OK'

    # Проверка кириллицы (главный индикатор перевода)
    if cyr_pct < CYRILLIC_CRITICAL_MIN:
        issues.append(f'UNTRANSLATED: {cyr_pct:.1f}% cyrillic (need >{CYRILLIC_CRITICAL_MIN}%)')
        status = 'UNTRANSLATED'
    elif cyr_pct < CYRILLIC_WARNING_MIN:
        issues.append(f'LOW_CYRILLIC: {cyr_pct:.1f}% (want >{CYRILLIC_WARNING_MIN}%)')
        if status != 'UNTRANSLATED':
            status = 'WARNING'

    # Проверка соотношения слов
    if words_ratio < WORDS_CRITICAL_MIN:
        issues.append(f'INCOMPLETE: words {words_ratio:.0%} (need >{WORDS_CRITICAL_MIN:.0%})')
        if status not in ['UNTRANSLATED']:
            status = 'BAD'
    elif words_ratio < WORDS_WARNING_MIN:
        issues.append(f'SHORT: words {words_ratio:.0%} (want >{WORDS_WARNING_MIN:.0%})')
        if status == 'OK':
            status = 'WARNING'
    elif words_ratio > WORDS_CRITICAL_MAX:
        issues.append(f'OVERFILLED: words {words_ratio:.0%} (max {WORDS_CRITICAL_MAX:.0%})')
        if status == 'OK':
            status = 'WARNING'

    # Проверка размера
    if size_ratio < SIZE_CRITICAL_MIN:
        issues.append(f'SIZE_LOW: {size_ratio:.0%} (need >{SIZE_CRITICAL_MIN:.0%})')
        if status not in ['UNTRANSLATED', 'BAD']:
            status = 'BAD'
    elif size_ratio > SIZE_CRITICAL_MAX:
        issues.append(f'SIZE_HIGH: {size_ratio:.0%} (max {SIZE_CRITICAL_MAX:.0%})')
        if status == 'OK':
            status = 'WARNING'

    return status, issues, metrics

def scan_all():
    """Сканирование всех файлов"""
    results = {
        'OK': [],
        'WARNING': [],
        'BAD': [],
        'UNTRANSLATED': [],
        'MISSING': []
    }

    folder_stats = {}

    for letter in 'abcdefghijklmnopqrstuvwxyz1':
        en_folder = EN_BASE / letter
        ru_folder = RU_BASE / letter

        if not en_folder.exists():
            continue

        stats = {'total': 0, 'OK': 0, 'WARNING': 0, 'BAD': 0, 'UNTRANSLATED': 0, 'MISSING': 0}

        for en_file in sorted(en_folder.glob('*.md')):
            stats['total'] += 1
            ru_file = ru_folder / en_file.name

            rel_path = f"{letter}/{en_file.name}"

            if not ru_file.exists():
                results['MISSING'].append({
                    'path': rel_path,
                    'en_path': en_file,
                    'status': 'MISSING',
                    'issues': ['FILE_NOT_FOUND']
                })
                stats['MISSING'] += 1
                continue

            try:
                en_text = en_file.read_text(encoding='utf-8')
            except Exception as e:
                results['BAD'].append({
                    'path': rel_path,
                    'en_path': en_file,
                    'ru_path': ru_file,
                    'status': 'BAD',
                    'issues': [f'EN_READ_ERROR: {e}']
                })
                stats['BAD'] += 1
                continue

            # Пробуем разные кодировки для русского файла
            ru_text = None
            encoding_used = None
            for enc in ['utf-8', 'utf-8-sig', 'cp1251', 'cp866', 'iso-8859-5']:
                try:
                    ru_text = ru_file.read_text(encoding=enc)
                    encoding_used = enc
                    break
                except:
                    continue

            if ru_text is None:
                results['BAD'].append({
                    'path': rel_path,
                    'en_path': en_file,
                    'ru_path': ru_file,
                    'status': 'BAD',
                    'issues': ['RU_READ_ERROR: cannot decode with any encoding']
                })
                stats['BAD'] += 1
                continue

            status, issues, metrics = classify_file(en_text, ru_text)

            result = {
                'path': rel_path,
                'en_path': en_file,
                'ru_path': ru_file,
                'status': status,
                'issues': issues,
                'metrics': metrics
            }

            results[status].append(result)
            stats[status] += 1

        folder_stats[letter] = stats
        print(f"Папка {letter}: {stats['total']} файлов | OK: {stats['OK']} | WARN: {stats['WARNING']} | BAD: {stats['BAD']} | UNTRANS: {stats['UNTRANSLATED']} | MISS: {stats['MISSING']}")

    return results, folder_stats

def generate_reports(results, folder_stats):
    """Генерация отчётов"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Подсчёт итогов
    total = sum(len(v) for v in results.values())
    ok_count = len(results['OK'])
    warn_count = len(results['WARNING'])
    bad_count = len(results['BAD'])
    untrans_count = len(results['UNTRANSLATED'])
    miss_count = len(results['MISSING'])

    need_work = bad_count + untrans_count + miss_count

    # ===== SUMMARY REPORT =====
    summary = f"""# ОТЧЁТ О КАЧЕСТВЕ ПЕРЕВОДОВ
Дата: {timestamp}

## ИТОГО
- Всего файлов: {total}
- OK: {ok_count} ({ok_count/total*100:.1f}%)
- WARNING: {warn_count} ({warn_count/total*100:.1f}%)
- BAD: {bad_count} ({bad_count/total*100:.1f}%)
- UNTRANSLATED: {untrans_count} ({untrans_count/total*100:.1f}%)
- MISSING: {miss_count} ({miss_count/total*100:.1f}%)

**Требуют работы: {need_work} файлов ({need_work/total*100:.1f}%)**

## СТАТИСТИКА ПО ПАПКАМ
| Папка | Всего | OK | WARN | BAD | UNTRANS | MISS |
|-------|-------|-----|------|-----|---------|------|
"""

    for letter in sorted(folder_stats.keys()):
        s = folder_stats[letter]
        summary += f"| {letter} | {s['total']} | {s['OK']} | {s['WARNING']} | {s['BAD']} | {s['UNTRANSLATED']} | {s['MISSING']} |\n"

    # Итого
    summary += f"| **ИТОГО** | **{total}** | **{ok_count}** | **{warn_count}** | **{bad_count}** | **{untrans_count}** | **{miss_count}** |\n"

    (RU_BASE / 'QUALITY_SUMMARY.md').write_text(summary, encoding='utf-8')
    print(f"\nСохранён: QUALITY_SUMMARY.md")

    # ===== FILES TO TRANSLATE =====
    to_translate = []

    # Добавляем MISSING
    for r in results['MISSING']:
        to_translate.append({
            'path': r['path'],
            'reason': 'MISSING',
            'priority': 1,
            'en_words': 0,
            'ru_words': 0,
            'details': 'Файл отсутствует'
        })

    # Добавляем UNTRANSLATED
    for r in results['UNTRANSLATED']:
        m = r.get('metrics', {})
        to_translate.append({
            'path': r['path'],
            'reason': 'UNTRANSLATED',
            'priority': 2,
            'en_words': m.get('en_words', 0),
            'ru_words': m.get('ru_words', 0),
            'cyrillic': m.get('cyrillic_pct', 0),
            'details': f"Кириллица: {m.get('cyrillic_pct', 0):.1f}%"
        })

    # Добавляем BAD
    for r in results['BAD']:
        m = r.get('metrics', {})
        to_translate.append({
            'path': r['path'],
            'reason': 'BAD_QUALITY',
            'priority': 3,
            'en_words': m.get('en_words', 0),
            'ru_words': m.get('ru_words', 0),
            'words_ratio': m.get('words_ratio', 0),
            'details': '; '.join(r.get('issues', []))
        })

    # Сортируем по приоритету и пути
    to_translate.sort(key=lambda x: (x['priority'], x['path']))

    # Сохраняем список
    with open(RU_BASE / 'FILES_TO_TRANSLATE.txt', 'w', encoding='utf-8') as f:
        f.write("# Файлы требующие перевода/переперевода\n")
        f.write(f"# Дата: {timestamp}\n")
        f.write(f"# Всего: {len(to_translate)} файлов\n")
        f.write("#\n")
        f.write("# Формат: путь | причина | en_words | ru_words | детали\n")
        f.write("#" + "=" * 100 + "\n\n")

        current_reason = None
        for item in to_translate:
            if item['reason'] != current_reason:
                current_reason = item['reason']
                f.write(f"\n## {current_reason}\n")

            f.write(f"{item['path']} | {item['reason']} | {item['en_words']} | {item['ru_words']} | {item['details']}\n")

        f.write(f"\n# Итого: {len(to_translate)} файлов\n")

    print(f"Сохранён: FILES_TO_TRANSLATE.txt ({len(to_translate)} файлов)")

    # ===== DETAILED REPORTS =====

    # BAD files
    with open(RU_BASE / 'BAD_QUALITY_FILES.txt', 'w', encoding='utf-8') as f:
        f.write(f"# Файлы с плохим качеством перевода\n")
        f.write(f"# Дата: {timestamp}\n")
        f.write(f"# Всего: {bad_count} файлов\n\n")

        for r in sorted(results['BAD'], key=lambda x: x.get('metrics', {}).get('words_ratio', 0)):
            m = r.get('metrics', {})
            f.write(f"{r['path']}\n")
            f.write(f"  Проблемы: {'; '.join(r.get('issues', []))}\n")
            f.write(f"  Размер: {m.get('ru_size', 0):,}/{m.get('en_size', 0):,} ({m.get('size_ratio', 0):.0%})\n")
            f.write(f"  Слова: {m.get('ru_words', 0):,}/{m.get('en_words', 0):,} ({m.get('words_ratio', 0):.0%})\n")
            f.write(f"  Кириллица: {m.get('cyrillic_pct', 0):.1f}%\n\n")

    print(f"Сохранён: BAD_QUALITY_FILES.txt ({bad_count} файлов)")

    # UNTRANSLATED files
    with open(RU_BASE / 'UNTRANSLATED_FILES.txt', 'w', encoding='utf-8') as f:
        f.write(f"# Непереведённые файлы (низкий % кириллицы)\n")
        f.write(f"# Дата: {timestamp}\n")
        f.write(f"# Всего: {untrans_count} файлов\n\n")

        for r in sorted(results['UNTRANSLATED'], key=lambda x: x.get('metrics', {}).get('cyrillic_pct', 0)):
            m = r.get('metrics', {})
            f.write(f"{r['path']} | {m.get('cyrillic_pct', 0):.1f}% cyrillic\n")

    print(f"Сохранён: UNTRANSLATED_FILES.txt ({untrans_count} файлов)")

    # MISSING files
    with open(RU_BASE / 'MISSING_FILES.txt', 'w', encoding='utf-8') as f:
        f.write(f"# Отсутствующие файлы\n")
        f.write(f"# Дата: {timestamp}\n")
        f.write(f"# Всего: {miss_count} файлов\n\n")

        for r in sorted(results['MISSING'], key=lambda x: x['path']):
            f.write(f"{r['path']}\n")

    print(f"Сохранён: MISSING_FILES.txt ({miss_count} файлов)")

    # WARNING files
    with open(RU_BASE / 'WARNING_FILES.txt', 'w', encoding='utf-8') as f:
        f.write(f"# Файлы с предупреждениями\n")
        f.write(f"# Дата: {timestamp}\n")
        f.write(f"# Всего: {warn_count} файлов\n\n")

        for r in sorted(results['WARNING'], key=lambda x: x['path']):
            f.write(f"{r['path']} | {'; '.join(r.get('issues', []))}\n")

    print(f"Сохранён: WARNING_FILES.txt ({warn_count} файлов)")

def main():
    print("=" * 80)
    print("ПРОВЕРКА КАЧЕСТВА ПЕРЕВОДОВ EN -> RU")
    print("=" * 80)
    print()
    print("Критерии:")
    print(f"  SIZE RATIO: {SIZE_OPTIMAL_MIN:.0%}-{SIZE_OPTIMAL_MAX:.0%} (critical: <{SIZE_CRITICAL_MIN:.0%})")
    print(f"  WORDS RATIO: {WORDS_OPTIMAL_MIN:.0%}-{WORDS_OPTIMAL_MAX:.0%} (critical: <{WORDS_CRITICAL_MIN:.0%})")
    print(f"  CYRILLIC %: >{CYRILLIC_OPTIMAL_MIN}% (untranslated: <{CYRILLIC_CRITICAL_MIN}%)")
    print()
    print("Сканирование...")
    print()

    results, folder_stats = scan_all()

    print()
    print("=" * 80)
    print("ИТОГИ")
    print("=" * 80)

    total = sum(len(v) for v in results.values())
    print(f"Всего файлов: {total}")
    print(f"  OK:          {len(results['OK']):>5} ({len(results['OK'])/total*100:.1f}%)")
    print(f"  WARNING:     {len(results['WARNING']):>5} ({len(results['WARNING'])/total*100:.1f}%)")
    print(f"  BAD:         {len(results['BAD']):>5} ({len(results['BAD'])/total*100:.1f}%)")
    print(f"  UNTRANSLATED:{len(results['UNTRANSLATED']):>5} ({len(results['UNTRANSLATED'])/total*100:.1f}%)")
    print(f"  MISSING:     {len(results['MISSING']):>5} ({len(results['MISSING'])/total*100:.1f}%)")

    need_work = len(results['BAD']) + len(results['UNTRANSLATED']) + len(results['MISSING'])
    print()
    print(f"ТРЕБУЮТ РАБОТЫ: {need_work} файлов ({need_work/total*100:.1f}%)")

    print()
    print("Генерация отчётов...")
    generate_reports(results, folder_stats)

    print()
    print("Готово!")

if __name__ == '__main__':
    main()
