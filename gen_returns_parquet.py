import pandas as pd
import random
from datetime import datetime, timedelta
import os

os.makedirs('data', exist_ok=True)
NUM=120
loans=[f"L{i:06d}" for i in range(1,301)]
users=[f"U{i:05d}" for i in range(1,201)]
books=[f"B{i:05d}" for i in range(1,151)]

rows=[]
for i in range(NUM):
    loan_id=random.choice(loans)
    returned_at = datetime.now() - timedelta(days=random.randint(0,30))
    rows.append({"loan_id": loan_id, "user_id": random.choice(users), "book_id": random.choice(books), "returned_at": returned_at})
df=pd.DataFrame(rows)
df.to_parquet('data/returns.parquet', index=False)
print("returns.parquet generated")
