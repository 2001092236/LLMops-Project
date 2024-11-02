curl -X 'POST' \
  'http://localhost:8000/chat/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "What was my last message?",
  "chat_history": [
    {
      "text": "Hi!",
      "role": "user"
    }
  ]
}'

# we got to chat endpoint in the running service (localhost:8000) and made a post query
# (post to the internet).
# we used json-type of the content (3-rd line)
# 