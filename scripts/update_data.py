#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime
import random

def update_data():
    """Обновление данных о контенте"""
    
    # Читаем текущие данные
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("data.json не найден, создаем шаблон")
        data = []
    
    # Если данных нет, создаем базовую структуру
    if not data:
        data = [
            {
                "id": 1,
                "title": "Пример фильма",
                "category": "films",
                "banner": "https://example.com/banner.jpg",
                "status": "watched",
                "watchDate": datetime.now().strftime("%d.%m.%Y"),
                "description": "Пример описания",
                "episodesWatched": 1,
                "buttons": [
                    {
                        "text": "Смотреть запись",
                        "url": "https://twitch.tv/videos/000000000",
                        "color": "#9146ff",
                        "size": "large"
                    }
                ]
            }
        ]
    
    # В реальном использовании здесь будет:
    # 1. Парсинг Twitch API для получения новых стримов
    # 2. Парсинг AniList/Kinopoisk API для информации
    # 3. Обновление статусов и счетчиков
    
    updated = False
    
    # Пример логики: если есть элемент в процессе просмотра, увеличиваем счетчик
    for item in data:
        if item.get('status') == 'watching' and 'episodesWatched' in item:
            current = item['episodesWatched']
            # Увеличиваем на 1-2 эпизода (в реальности нужно парсить из Twitch)
            item['episodesWatched'] = current + random.randint(1, 2)
            updated = True
            print(f"Обновлен {item['title']}: {current} → {item['episodesWatched']} эпизодов")
            
            # Пример: добавляем новую кнопку при достижении определенного количества эпизодов
            if item['episodesWatched'] >= 50 and 'buttons' in item:
                # Проверяем, нет ли уже такой кнопки
                has_milestone_button = any(
                    '50 эпизодов' in b.get('text', '') 
                    for b in item['buttons']
                )
                if not has_milestone_button:
                    new_button = {
                        "text": f"🎉 50 эпизодов!",
                        "url": f"https://twitch.tv/videos/{random.randint(100000000, 999999999)}",
                        "color": "#ff9800",
                        "size": "small"
                    }
                    item['buttons'].append(new_button)
                    updated = True
                    print(f"Добавлена новая кнопка для {item['title']}")
    
    # Пример: добавляем тестовый элемент с кнопками при первом запуске
    if len(data) < 15 and random.random() < 0.2:
        colors = ['#9146ff', '#ff0000', '#4c75a3', '#0088cc', '#4caf50', '#ff9800', '#9c27b0']
        new_item = {
            "id": len(data) + 1,
            "title": f"Новый контент {len(data) + 1}",
            "category": random.choice(["films", "anime", "series"]),
            "banner": "https://placehold.co/600x900/222222/FFFFFF?text=New+Content",
            "status": random.choice(["watched", "watching", "onhold"]),
            "watchDate": datetime.now().strftime("%d.%m.%Y"),
            "description": f"Автоматически добавлено {datetime.now().strftime('%d.%m.%Y %H:%M')}",
            "episodesWatched": random.randint(1, 30) if random.choice([True, False]) else None,
            "buttons": [
                {
                    "text": "Смотреть на Twitch",
                    "url": f"https://twitch.tv/videos/{random.randint(100000000, 999999999)}",
                    "color": random.choice(colors),
                    "size": random.choice(["large", "small"])
                }
            ]
        }
        
        # Иногда добавляем вторую кнопку
        if random.random() > 0.5:
            new_item["buttons"].append({
                "text": random.choice(["Обсуждение", "Нарезка", "Тизер"]),
                "url": random.choice([
                    f"https://youtube.com/watch?v={random.randint(10000000, 99999999)}",
                    f"https://t.me/xah0b_chat",
                    f"https://vk.com/xah0b_club"
                ]),
                "color": random.choice(colors),
                "size": "small"
            })
        
        data.append(new_item)
        updated = True
        print(f"Добавлен новый элемент с кнопками: {new_item['title']}")
    
    # Сохраняем обновленные данные
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Данные сохранены. Всего записей: {len(data)}")
    print(f"✓ Обновлено: {'Да' if updated else 'Нет'}")
    
    return updated

if __name__ == "__main__":
    # Для тестирования вручную
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Тестовый режим...")
        update_data()
    else:
        # Режим для GitHub Actions
        try:
            updated = update_data()
            # Возвращаем код выхода для GitHub Actions
            sys.exit(0 if updated else 1)
        except Exception as e:
            print(f"Ошибка: {e}")
            sys.exit(1)
