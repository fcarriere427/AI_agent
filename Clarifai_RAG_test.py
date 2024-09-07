from clarifai.rag import RAG # type: ignore

rag_agent = RAG.setup(user_id="t8xj1dxh0def", llm_url="https://clarifai.com/anthropic/completion/models/claude-3_5-sonnet")

rag_agent.upload(folder_path="./docs")

rag_agent.chat(messages="Summarize this pdf")