# Task 1
Try using a reranker. The reranker is defined in the 
```yaml
  rerank:
    container_name: rerank_service
    image: ghcr.io/huggingface/text-embeddings-inference:cpu-1.5
    volumes:
      - ./data:/data
    command: ["--model-id", "mixedbread-ai/mxbai-rerank-base-v1"]
``` - a part of `rag_service/docker-compose.yaml`.

As you can see, the defalt reranker is `mixedbread-ai/mxbai-rerank-base-v1`. However, by default it is not used, which is established by the parameter `use_reranker: bool = False` of the constructor `class RAGRequest(BaseModel)` in the file `rag_service/src/main.py`.
You need to make it `True` to switch on reranking. A
lso, you can change the parameters `top_k_retrieve`, `top_k_rank`, if necessary.

The **deliverables** if this stage are:
1. A comparison of how the retrieved context changes after adding a reranker. Try at least 10 different prompts.
2. Measure the responce time for RAG with and without a reranker for at least 10 different prompts and for at least 3 different values of top_k_rank.
3. The analysis of pros and cons of using a reranker. The evaluation aspects should include the relevance of the top-k documents and the response time.


**Solution**

1.Rerank comparison

```python
prompt = ""
with_rerank_resp = ""
no_rerank_resp = ""
```
