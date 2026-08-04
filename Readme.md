Aah, samajh gaya! Code block ke andar numbers aur markdown headers ka issue lag raha tha.

Yeh lo, bina kisi extra note, text ya step number ke—**poora clean `README.md` raw code:**

```markdown
# 🤖 AI Engineering Course

<p align="center">
  <img src="https://img.shields.io/github/stars/tushar1121s/ai-engineering-course?style=for-the-badge&color=2ea44f" alt="Stars" />
  <img src="https://img.shields.io/github/forks/tushar1121s/ai-engineering-course?style=for-the-badge&color=2ea44f" alt="Forks" />
  <img src="https://img.shields.io/github/repo-size/tushar1121s/ai-engineering-course?style=for-the-badge&color=218838" alt="Repo Size" />
</p>

<p align="center">
  <a href="#-overview"><img src="https://img.shields.io/badge/💡_OVERVIEW-2ea44f?style=for-the-badge&logoColor=white" /></a>
  <a href="#-tech-stack"><img src="https://img.shields.io/badge/⚙️_TECH_STACK-218838?style=for-the-badge&logoColor=white" /></a>
  <a href="#-roadmap--progress"><img src="https://img.shields.io/badge/🗺️_ROADMAP-2ea44f?style=for-the-badge&logoColor=white" /></a>
  <a href="#-getting-started"><img src="https://img.shields.io/badge/🚀_GETTING_STARTED-218838?style=for-the-badge&logoColor=white" /></a>
</p>

---

### Hands-On Production AI & LLM Engineering Journey

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![Package Manager](https://img.shields.io/badge/PackageManager-uv-261230?style=flat-square&logo=python&logoColor=white)
![SDK](https://img.shields.io/badge/SDK-Groq_API-f34f29?style=flat-square)
![LLM Model](https://img.shields.io/badge/LLM-Llama_3.3_70B-0467DF?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> A daily hands-on repository tracking my progress through building production-grade AI applications, mastering prompt engineering, agentic systems, and end-to-end AI pipelines.

---

## 💡 Overview

> [!TIP]
> **Production-First Mindset:** Moving beyond toy wrappers to build scalable, low-latency, and reliable LLM systems using modern tooling (`uv`, Groq, Llama 3.3).

> [!IMPORTANT]
> All API keys are strictly managed via local environment variables (`.env`) and kept untracked to adhere to enterprise security standards.

---

## ⚙️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | `Python 3.12+` | Core programming language |
| **Tooling** | `uv` | Next-gen extremely fast Python package manager |
| **LLM Provider** | `Groq API` | Llama-3.3-70b-versatile for ultra-fast completions |
| **Environment** | `python-dotenv` | Secure API key & config management |

---

## 🗺️ Roadmap & Progress

### 📂 Week 1: Core Fundamentals & Completions

| Day | Topic | Key Concepts | Status |
| :---: | :--- | :--- | :---: |
| **Day 01** | First LLM Call & Setup | `Groq SDK Setup`, `.env` Configuration, Role Messages (`system`, `user`, `assistant`), Basic Completions | ✅ Completed |
| **Day 02** | Parameter Tuning & System Roles | Advanced System Prompts, Temperature Scaling, Top-p, Control Parameters | ✅ Completed |
| **Day 03** | Tokens & Limits | Tokenization, Context Window Limits, Cost Optimization | ⏳ In Progress |

---

## 🚀 Getting Started

Follow these steps to set up and run the repository locally on your machine.

- **Clone the Repository**
```bash
git clone [https://github.com/tushar1121s/ai-engineering-course.git](https://github.com/tushar1121s/ai-engineering-course.git)
cd ai-engineering-course

```

* **Configure Environment Variables**
Create a `.env` file inside the respective day's folder (e.g., `week_1/day01_first_llm_call/.env`):

```env
GROQ_API_KEY=your_groq_api_key_here

```

* **Run Any Daily Module Using `uv**`
Navigate to the project root and run the execution script:

```bash
# Run Day 1 Hello LLM Script
uv run python week_1/day01_first_llm_call/hello_llm.py

# Run Day 2 System Prompt Script
uv run python week_1/day02/sys_temp.py

```

```

```