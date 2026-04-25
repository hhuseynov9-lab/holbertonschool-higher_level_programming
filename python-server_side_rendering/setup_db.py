import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # Cədvəli yaradırıq
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Məlumatları daxil edirik (əgər yoxdursa)
    cursor.execute('DELETE FROM Products') # Köhnə məlumatları təmizləmək üçün
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()
    print("Database 'products.db' yaradıldı!")

if __name__ == '__main__':
    create_database()
