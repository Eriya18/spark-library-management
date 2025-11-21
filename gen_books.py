import json, random, os
from datetime import datetime

os.makedirs('data', exist_ok=True)
NUM=150
genres=['Fiction','Science','History','Math','Technology','Art']

books=[]
for i in range(1,NUM+1):
    books.append({
        "book_id": f"B{i:05d}",
        "title": f"Book Title {i}",
        "author": f"Author {random.randint(1,40)}",
        "published_year": random.randint(1990,2023),
        "category_id": f"C{random.randint(1,10):03d}"
    })

with open('data/books.json','w') as f:
    json.dump(books,f,indent=2)
print("books.json generated")
