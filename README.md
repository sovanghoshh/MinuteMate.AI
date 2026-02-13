# 🕒 MinuteMate

**The AI-Powered Async Agent for Modern Teams.**

MinuteMate is an intelligent ecosystem that bridges the gap between live discussions and actionable workflows. By combining real-time Chrome audio capture, Whisper-based transcription, and Gemini-driven analysis, MinuteMate ensures that no insight is lost and every task is synced across **GitHub**, **Notion**, and **Slack**.

---

## 🚀 Features

* **🎙 Dual-Channel Recording:** Seamlessly captures both tab audio and microphone input via a Manifest V3 Chrome Extension.
* **🤖 Intelligent Processing:** Leverages **OpenAI Whisper** for high-fidelity transcription and **Google Gemini** for context-aware summarization.
* **🐙 GitHub & Notion Sync:** Automatically transforms meeting action items into GitHub issues or Notion database entries.
* **📤 Slack Automation:** Delivers instant meeting summaries and automated daily standup reports to your team channels.
* **📊 Async Standups:** Aggregates team activity from GitHub commits and Notion updates to provide a clear progress overview without the need for a meeting.

---

## 🛠 Tech Stack

| Component | Technologies Used |
| --- | --- |
| **Backend** | FastAPI, Python, Boto3 |
| **AI/ML** | OpenAI Whisper, Google Gemini API |
| **Frontend** | Chrome Extension (MV3), JavaScript, CSS/HTML |
| **Integrations** | Slack API, GitHub REST API, Notion SDK |
| **DevOps** | GitHub Actions, Environment Secret Management |

---

## 📂 Project Structure

```text
MINUTEMATE
├── .github/
│   └── workflows/
│       └── main.yml
├── backend/
│   ├── dailysync/
│   │   ├── check_models.py
│   │   ├── create_notiondb.py
│   │   ├── fix_issues.py
│   │   ├── flask_app.py
│   │   ├── github_integration.py
│   │   ├── main.py
│   │   ├── notion_integration.py
│   │   ├── setup_env.py
│   │   ├── slack_sender.py
│   │   ├── summarize_llm.py
│   │   ├── test_notion_token.py
│   │   ├── test_whisper.py
│   │   └── user_mapping.json
│   └── whisper_api/
│       ├── app.py
│       └── meeting_summary_info.json
├── extension/
│   ├── background.js
│   ├── LOGO.png
│   ├── manifest.json
│   ├── offscreen.html
│   ├── offscreen.js
│   ├── popup.html
│   ├── popup.js
│   └── styles.css
├── web_app/
│   ├── app.js
│   └── index.html
└── .env           

```

---

## ⚡ Quick Start

### 1. Prerequisites

* Python 3.9+
* Node.js (for extension development)
* API Keys: `GEMINI_API_KEY`, `SLACK_BOT_TOKEN`, `NOTION_TOKEN`, `GITHUB_TOKEN`

### 2. Backend Setup

```bash
cd backend/dailysync
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python backend/dailysync/flask_app.py

```

### 3. Extension Installation

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the `extension/` folder from this repository.

---

## 💡 The Problem We're Solving

Distributed teams often suffer from "Meeting Fatigue" and "Context Switching."

* **Manual Notes** are often incomplete or forgotten.
* **Standups** take up valuable deep-work time.
* **Tool Fragmentation** leads to tasks being lost between Slack threads and GitHub issues.

**MinuteMate** creates a single source of truth by automating the documentation and synchronization process.

