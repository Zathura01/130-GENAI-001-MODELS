from langchain_openai import OpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', api_key="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"
                            )

documents = [
    'doc 1: The capital of France is Paris.',
    'doc 2: The capital of Germany is Berlin.',
    'doc 3: The capital of Italy is Rome.',
]

docembeddings = embedding.embed_documents(documents)
query = 'What is the capital of France?'
quertembedding = embedding.embed_query(query)

scores = cosine_similarity([quertembedding], docembeddings)[0]
index, score = sorted(list(enumerate(scores)), key= lambda x: x[1])[-1]

print(f"Most similar document: {documents[index]} with score: {score}")