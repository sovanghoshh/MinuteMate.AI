import requests
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
def format_standup_message(per_user_updates):
    blocks = []
    fallback_text = "📅 Daily Standup Update\n\n"
    
    for user, summary in per_user_updates.items():
        # User header
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*👤 {user}*"
            }
        })
        
        # Process summary into clean lines
        summary_lines = []
        for line in summary.split("\n"):
            if line.strip():  # Skip empty lines
                summary_lines.append(line.strip())
        
        # Add summary content
        blocks.append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "\n".join(summary_lines)
            }
        })
        
        blocks.append({"type": "divider"})
        fallback_text += f"{user}:\n{summary}\n\n"
    
    return {
        "text": fallback_text.strip(),
        "blocks": blocks
    }
def send_to_slack(per_user_updates):
    if not SLACK_WEBHOOK_URL:
        raise ValueError("Slack Webhook URL missing!")
    
    payload = format_standup_message(per_user_updates)
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    
    if response.status_code != 200:
        print(f"❌ Slack Error: {response.text}")
    else:
        print("✅ Standup sent to Slack!")
# Example run
if __name__ == "__main__":
    fake_summary = {
        "Shreya": ["✅ Added commit sync", "🚧 Writing LLM summarizer"],
        "Raj": ["✅ Set up Notion DB", "❌ Blocked on Slack API auth"]
    }

    send_to_slack(fake_summary)
