from langchain_ollama import OllamaLLM

llm_freetalk = OllamaLLM(
    model="qwen2_5_7b_lora_sft_zh_20250113_4500_Q4MK:latest",
    temperature=0
    )

# 场景决策 最终需要更换为Bert
llm = OllamaLLM(
    model="qwen2.5:7b",
    temperature=0
    )

# 场景生成
llm_generate = OllamaLLM(
    model="qwen2.5:3b",
    temperature=0
    )