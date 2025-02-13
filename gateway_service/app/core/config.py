import os

# DATABASE_URL = "postgresql://user:password@postgres/dbname"

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
table = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql://{user}:{password}@postgres/{table}"

print(DATABASE_URL)
ADMIN_TOKEN = os.getenv("ADMIN_KEY")
RATE_LIMIT = 5  # max requests per minute
RATE_LIMIT_KEY_PREFIX = "rate_limit"
INFERENCE_ROUTING = {"gpt-4o-mini": "gpt-4-mini", "gpt-4o": "gpt-4o"}
