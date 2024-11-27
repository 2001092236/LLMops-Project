## RAG Project

In this task you will explore various parts of the RAG system shown in the practice session by Sergey Petrov.

This task will be graded by our instructors.

How projects are assessed by instructors

Our expert graders will check your solution by criteria from the task. For each project part, you’ll get a score and text feedback with recommendations on how to improve your work.

You’ll have one feedback iteration in every project. Assessing is necessary to expand your knowledge; it doesn’t block your progress.

To submit a project, attach a link to a PDF or your Google Colab notebook with a solution on the **"Review" tab**. Please make sure that your materials are accessible via the link.

## Project Task

To start with, clone the [repo](https://github.com/pilot7747/topic-1-advanced/tree/rag_service) to your VM and make sure that you’ve watched the practice session and understand the structure of the repo and the service endpoints.

1.  First, you will need a database to experiment with. The RAG project uses LanceDB, as described in the `config` file. In this task, you’ll work with the documentation of the `transformers` library. Download the [markdown\_to\_text.py](https://drive.google.com/file/d/1Q6wtX9Ldu7P1BadGROW-kxeCB66fr8Y0/view) file to your VM. Clone [https://github.com/huggingface/transformers](https://github.com/huggingface/transformers) to your VM and run markdown\_to\_text.py script to extract raw text from transformers/docs/source/en/. This is the script you need to run: `python prep_scripts/markdown_to_text.py --input-dir transformers/docs/source/en/ --output-dir docs` This will be your knowledge base, you don't need it to be a part of your repository. Use the `add_to_rag_db` endpoint to load every text into the database. Make several RAG API calls to check that the pipeline is working.
2.  Try using a reranker. The reranker is defined in the `rerank: container_name: rerank_service image: [ghcr.io/huggingface/text-embeddings-inference:cpu-1.5](http://ghcr.io/huggingface/text-embeddings-inference:cpu-1.5) volumes: - ./data:/data command: ["--model-id", "mixedbread-ai/mxbai-rerank-base-v1"]` part of `rag_service/docker-compose.yaml`. As you can see, the defalt reranker is [mixedbread-ai/mxbai-rerank-base-v1](https://huggingface.co/mixedbread-ai/mxbai-rerank-base-v1). However, by default it is not used, which is established by the parameter `use_reranker: bool = False` of the constructor `class RAGRequest(BaseModel)` in the file `rag_service/src/main.py`. You need to make it True to switch on reranking. Also, you can change the parameters `top_k_retrieve`, `top_k_rank` , if necessary. **The deliverables if this stage are:**
    -   A comparison of how the retrieved context changes after adding a reranker. Try at least 10 different prompts.
    -   Measure the responce time for RAG with and without a reranker for at least 10 different prompts and for at least 3 different values of `top_k_rank`.
    -   The analysis of pros and cons of using a reranker. The evaluation aspects should include the relevance of the top-k documents and the response time.
3.  Try at least three different LLMs and compare the results. At least one of them should be called using [Nebius AI Studio](https://studio.nebius.ai/) API. **The deliverables are:**
    -   Analysis of the differences between outputs and conclusions from the analysis. Try at least 10 different prompts for each LLM.
4.  Put together a simple evaluation dataset of 20 questions (+optionally answers) - you could do it manually or generate with an LLM. Use the [LLM-as-a-Judge](https://huggingface.co/learn/cookbook/en/llm_judge) approach to quantitatively evaluate your best setup.
    
    \[Bonus\] Explore the [Ragas](https://docs.ragas.io/en/stable/) docs for possible evaluation setups.
    
    **The deliverables are:**
    
    -   Your evaluation set and how you created it
    -   The evaluation setup (which LLM you used as a judge, what was the evaluation prompt etc)
    -   Evaluation results (quantitative metics and conclusions are required)
5.  Try a different embedding model from the top of the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) and justify your choice. If things are getting slow, switch to a gpu - don’t forget to switch to a corresponding [tei container](https://github.com/huggingface/text-embeddings-inference?tab=readme-ov-file#docker-images).
    
    The encoder is defined in this part
    
    `embed: container_name: embed_service image: [ghcr.io/huggingface/text-embeddings-inference:cpu-1.5](http://ghcr.io/huggingface/text-embeddings-inference:cpu-1.5) volumes: - ./data:/data command: ["--model-id", "BAAI/bge-small-en-v1.5"]`
    
    of `rag_service/docker-compose.yaml`. As you can see, the defalt encoder is [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5).
    
    **The deliverables are:**
    
    -   Which alternative embedding model you tried and why.
    -   The analysis of how retrieved documents differ between embedding models (is one better than the other?)
    -   The analysis of how the embedding time differs between models.
6.  \[Bonus\] Adjust the RAG setup to work smoothly for a multi-turn conversation.
    
    **The deliverables are:**
    
    -   The description of your approach in plain English.
    -   The modified code and a demonstration of how it improved the multi-turn conversation flow (before/after).
