import requests
import os

docs_path = "/home/ernest/Desktop/AI_AD_course/topic-1-advanced/docs"

for doc in os.listdir(docs_path):
    doc_path = os.path.join(docs_path, doc)
    if os.path.isfile(doc_path):
        text = open(doc_path).read()
        resp = requests.post(
            "http://0.0.0.0:8001/add_to_rag_db/",
            json={"text": text},
            headers={"Authorization": os.getenv("aYpVtQxRmGzLsBnCfDiKjUxWqHvNwYcFbXlPrVdTw")}
        )
        if resp.status_code != 200: 
            print(f"error uploading document {doc}")
