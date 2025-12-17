import os
import re
from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# =========================
# Load environment
# =========================
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not TELEGRAM_BOT_TOKEN or not OPENROUTER_API_KEY:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN or OPENROUTER_API_KEY")

# =========================
# Load CV content (FULL CONTEXT)
# =========================
with open("cv_full_complete.md", encoding="utf-8") as f:
    CV_TEXT = f.read()

# =========================
# OpenRouter client
# =========================
llm_client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

MODEL = "mistralai/devstral-2512:free"
# Alternative:
# MODEL = "mistralai/mistral-7b-instruct"
# MODEL = "meta-llama/llama-3-8b-instruct"

# =========================
# System prompt (Telegram-safe HTML)
# =========================
SYSTEM_PROMPT = """
You are Rinaldi Guizot's recruiter-facing AI CV assistant.

Rules:
- Use ONLY the provided CV content
- Do NOT invent information
- If something is not in the CV, say so clearly

Formatting rules:
- Respond in PLAIN TEXT ONLY
- Do NOT use Markdown or HTML
- Do NOT use **, __, or any formatting symbols
- Use emojis and capitalization to highlight sections:
  - Section titles: emojis
  - Bullet points: start with • or ✅
"""

# =========================
# Core QA function
# =========================
def ask_cv(question: str) -> str:
    prompt = f"""
Below is the FULL CV content.

Use ONLY this information to answer the question.
If the answer does not exist in the CV, say so explicitly.

CV CONTENT:
{CV_TEXT}

QUESTION:
{question}
"""

    response = llm_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=600,
    )

    answer = response.choices[0].message.content or ""
    answer = answer.replace("<s>", "").replace("</s>", "").strip()

    return answer or "⚠️ No relevant information found in the CV."

# =========================
# Telegram handlers
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I’m Rinaldi Guizot’s CV assistant.\n\n"
        "Ask me anything about background, experience, skills, or contact info.",
        parse_mode="HTML",
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text.strip()
    answer = ask_cv(user_question)
    answer = normalize_telegram_text(answer)

    await update.message.reply_text(
        answer,
        disable_web_page_preview=True,
    )

def normalize_telegram_text(text: str) -> str:
    # Remove Markdown bold if it appears
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)

    # Optional: clean leftover underscores
    text = re.sub(r"__+", "", text)

    return text.strip()


# =========================
# Run bot
# =========================
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 CV bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
