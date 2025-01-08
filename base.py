from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="qwen2.5:7b",
    temperature=0
    )