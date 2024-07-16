import sqlite3
import os

DB_NAME = 'inventory.db'

def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Create the inventory table
        cursor.execute('''
            CREATE TABLE inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                qty INTEGER NOT NULL,
                level INTEGER NOT NULL,
                value REAL NOT NULL,
                type TEXT NOT NULL,
                stats TEXT
            )
        ''')
        
        # Insert example items
        items = [
            ('Sword', 10, 1, 100.0, 'Weapon', 'Attack:10, Defense:2'),
            ('Shield', 5, 1, 150.0, 'Armor', None),
            ('Potion', 20, 1, 50.0, 'Consumable', 'Heal:20'),
            ('Helmet', 7, 1, 80.0, 'Armor', 'Defense:8'),
            ('Boots', 12, 1, 60.0, 'Armor', 'Speed:5'),
            ('Bow', 8, 1, 120.0, 'Weapon', 'Attack:8, Range:15'),
            ('Arrow', 100, 1, 1.0, 'Ammo', 'Damage:5'),
            ('Magic Wand', 4, 1, 200.0, 'Weapon', 'Attack:12, Magic:10'),
            ('Ring', 15, 1, 50.0, 'Accessory', None),
            ('Necklace', 6, 1, 70.0, 'Accessory', 'Magic:7, Defense:3')
        ]
        
        cursor.executemany('''
            INSERT INTO inventory (name, qty, level, value, type, stats)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', items)
        
        conn.commit()
        conn.close()
        print("Database initialized and example items inserted.")
    else:
        print("Database already exists. Initialization skipped.")

if __name__ == '__main__':
    init_db()
