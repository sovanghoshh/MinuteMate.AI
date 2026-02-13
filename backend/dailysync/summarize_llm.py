import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Verify the key is loading
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("❌ ERROR: GEMINI_API_KEY not found in .env")

genai.configure(api_key=GEMINI_API_KEY)

# Use the 2026 stable model
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

def summarize_user_activity(user_commits, user_tasks):
    prompt = f"""Generate a concise standup update in this exact format (no bullet numbers, no extra lines):

✅ What I did:
- [List completed items]

🚧 In progress:
- [List WIP items]

❌ Blockers:
- [List blockers or "None"]

Base this on:
GitHub Commits: {user_commits}
Notion Tasks: {user_tasks}"""

    try:
        # FIXED: Changed 'model' to 'gemini_model'
        response = gemini_model.generate_content(prompt)
        summary = response.text.strip()
        summary = summary.replace("• ", "- ")
        summary = "\n".join(line.strip() for line in summary.split("\n") if line.strip())
        return summary
    except Exception as e:
        print(f"❌ Summarization error: {e}")
        return f"⚠️ Update unavailable (Error: {e})"

if __name__ == "__main__":
    # Test block
    summary = summarize_user_activity(["Initial test"], ["Setup task"])
    print("📝 Generated Summary:\n", summary)