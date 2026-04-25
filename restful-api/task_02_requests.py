import requests
import csv

def fetch_and_print_posts():
    """Postları çəkir və başlıqlarını çap edir"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Tapşırıq tələbi: "Status Code: 200" formatında çap
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            # Hər bir postun 'title' (başlıq) dəyərini çap edirik
            print(post.get('title'))

def fetch_and_save_posts():
    """Postları çəkir və posts.csv faylına qeyd edir"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Tapşırıqda tələb olunan sütunlar: id, title, body
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']} 
            for p in posts
        ]
        
        # CSV faylını yaradırıq
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader() # Sütun adlarını yazır
            writer.writerows(structured_data) # Məlumatları yazır