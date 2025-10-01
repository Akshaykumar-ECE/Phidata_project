# 📊 Phidata Multi-Agent Finance + Web Search Project

This project demonstrates how to build **multi-agent systems** using [Phidata](https://github.com/phidatahq/phidata), with **Groq's Llama-3.3 models** as the backbone.  
It combines a **Web Search Agent** and a **Finance Agent** to fetch, analyze, and present financial and general web data.

---

## ⚙️ Features

- 🌐 **Web Search Agent**  
  - Uses DuckDuckGo to search the web.  
  - Always includes the **source links**.  

- 💹 **Finance Agent**  
  - Uses Yahoo Finance tools to fetch:  
    - Real-time stock prices  
    - Analyst recommendations  
    - Stock fundamentals  
    - Latest company news  
  - Presents results in **table format** for clarity.  

- 🤝 **Multi-Agent Collaboration**  
  - Combines web search and finance tools into one system.  
  - Example query:  
    > "Summarize analyst recommendation and share the latest news for Nvidia"  
  - Produces structured, source-backed insights.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Akshaykumar-ECE/Phidata_project.git
   cd Phidata_project
