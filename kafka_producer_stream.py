from kafka import KafkaProducer
import json, time, random
from datetime import datetime, timedelta
import socket
# Use localhost:9092 when running inside docker network
bootstrap = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=bootstrap, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
users=[f"U{i:05d}" for i in range(1,201)]
books=[f"B{i:05d}" for i in range(1,151)]

def make_event(i):
    loan_date = datetime.now().isoformat()
    return {
        "event_id": f"E{i:08d}",
        "loan_id": f"LS{i:06d}",
        "user_id": random.choice(users),
        "book_id": random.choice(books),
        "loan_date": loan_date,
        "due_date": (datetime.now()+timedelta(days=14)).isoformat(),
        "status": "borrowed"
    }

i=1
while True:
    ev = make_event(i)
    producer.send('library-loans', ev)
    print("sent", ev)
    i+=1
    time.sleep(2)
