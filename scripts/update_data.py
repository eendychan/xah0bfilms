#!/usr/bin/env python3
import json
import os
from datetime import datetime

def update_data():
    """Обновление данных о контенте"""
    
    # Читаем текущие данные
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Загружено {len(data)} записей")
    except FileNotFoundError:
        print("data.json не найден")
        return False
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        return False
    
    updated = False
    
    # Пример: добавляем дату обновления
    for item in data:
        if 'lastUpdated' not in item:
            item['lastUpdated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated = True
    
    # Сохраняем обновленные данные
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("✓ Данные сохранены")
        return updated
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False

if __name__ == "__main__":
    success = update_data()
    exit(0 if success else 1)
