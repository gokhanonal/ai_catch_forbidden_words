# GENEL MİMARİ

Client
  ↓
FastAPI
  ↓
[1] Regex (Exact Match)
  ↓
[2] Fuzzy Match (Typo tolerant)
  ↓
[3] Semantic Similarity (Sentence Embedding)
  ↓
[4] Local LLM (llama.cpp – reasoning & edge cases)
  ↓
Risk Score + Decision

# 🧠 Kullanılan Teknolojiler
API	FastAPI
Exact match	regex
Typo tolerant	rapidfuzz
Semantic	sentence-transformers (Türkçe destekli)
LLM	llama.cpp (GGUF model, CPU)
Dil	Türkçe

# 🤖 Local LLM Seçimi (CPU Friendly)
Önerilen modeller (GGUF):

BoraBora-Turkish-Llama-3-8B-Instruct.Q4_K_M.gguf
mistral-7b-instruct-v0.2.Q4_K_M.gguf
llama-3-8b-instruct.Q4_K_M.gguf

📌 Q4 quantization → CPU + 8–16GB RAM yeterli

#📦 Kurulum
**Libs**
```bash
pip install -r requirements.txt
````
**LLAMA.CPP Apple Silicon / Intel Mac için:**
```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```
# 📁 Proje Yapısı
forbidden_ai/
│
├── app.py
├── detector/
│   ├── regex_detector.py
│   ├── fuzzy_detector.py
│   ├── semantic_detector.py
│   ├── llm_detector.py
│   └── risk_engine.py
│
├── data/
│   └── forbidden_phrases_tr.txt
│
└── models/
    └── llama3-turkish.Q4_K_M.gguf


# RUN
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```