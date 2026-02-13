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
MinuteMate/
├── .github/workflows/   # CI/CD pipelines
├── backend/
│   ├── dailysync/       # Standup automation & LLM summarization
│   └── whisper_api/     # Whisper transcription service
├── extension/           # Chrome Extension (Manifest V3)
│   ├── background.js    # Service worker for audio handling
│   └── popup.js         # User interface for recording
└── web_app/             # Alternative dashboard for meeting uploads

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
python main.py

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

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

### Contact

**Sovan Ghosh** [sovanghosh.official@gmail.com](mailto:sovanghosh.official@gmail.
