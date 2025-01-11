from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="qwen2.5:7b",
    temperature=0
    )

llm_generate = OllamaLLM(
    model="qwen2.5:3b",
    temperature=0
    )