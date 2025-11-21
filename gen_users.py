import csv
import random
from datetime import datetime, timedelta
import os

os.makedirs('data', exist_ok=True)
NUM=200
with open('data/users.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['user_id','name','email','created_at'])
    base = datetime.now() - timedelta(days=365)
    for i in range(1,NUM+1):
        dt = base + timedelta(days=random.randint(0,365))
        writer.writerow([f"U{i:05d}", f"User{i}", f"user{i}@example.com", dt.strftime("%Y-%m-%d %H:%M:%S")])
print("users.csv generated")
