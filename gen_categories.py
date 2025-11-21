import csv, os
os.makedirs('data', exist_ok=True)
cats = [(f"C{i:03d}", name) for i,name in enumerate(
    ["Fiction","Science","History","Math","Technology","Art","Philosophy","Comics","Business","SelfHelp"], start=1)]
with open('data/categories.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['category_id','category_name'])
    w.writerows(cats)
print("categories.csv generated")
