#!/usr/bin/env python3
"""
Простой скрипт для обновления данных
"""

import json
import os
from datetime import datetime

def main():
    # Читаем данные
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Загружено {len(data)} записей")
    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    
    # Просто добавляем дату обновления
    updated = False
    for item in data:
        if 'updated' not in item:
            item['updated'] = datetime.now().isoformat()
            updated = True
    
    # Сохраняем
    if updated:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Данные обновлены")
        return True
    else:
        print("Нет изменений")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
