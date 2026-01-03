from llama_cpp import Llama

llm = Llama(
    model_path="models/llama3-turkish.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6
)

SYSTEM_PROMPT = """
Sen bir içerik denetleme sistemisin.
Verilen metin yasaklı, illegal veya zararlı bir içerik içeriyor mu?
Sadece EVET veya HAYIR cevabı ver.
"""

def llm_detect(text):
    prompt = f"""
        {SYSTEM_PROMPT}

        Metin:
        {text}

        Cevap:
        """

    output = llm(prompt, max_tokens=5, stop=["\n"])
    answer = output["choices"][0]["text"].strip().upper()
    return answer == "EVET"
