import random
from datetime import datetime, timedelta

output = "data/loans.txt"

users = [f"U{str(i).zfill(5)}" for i in range(1, 51)]
books = [f"B{str(i).zfill(5)}" for i in range(1, 51)]

statuses = ["borrowed", "returned"]

with open(output, "w") as f:
    f.write("loan_id|user_id|book_id|loan_date|due_date|status\n")

    for i in range(1, 101):
        loan_id = f"LS{str(i).zfill(6)}"
        user_id = random.choice(users)
        book_id = random.choice(books)

        loan_date = datetime.now() - timedelta(days=random.randint(0, 30))
        due_date = loan_date + timedelta(days=14)
        status = random.choice(statuses)

        f.write(
            f"{loan_id}|{user_id}|{book_id}|"
            f"{loan_date.strftime('%Y-%m-%d')}|"
            f"{due_date.strftime('%Y-%m-%d')}|"
            f"{status}\n"
        )

print("loans.txt generated")
