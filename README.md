# Rinaldi Guizot CV Assistant Bot

A Telegram bot that serves as an AI-powered CV assistant for Rinaldi Guizot. The bot can answer questions about his background, experience, skills, and contact information using the provided CV content.

## 🚀 Features

- **AI-Powered Q&A**: Uses OpenRouter API with LLMs to answer questions about Rinaldi's CV
- **Telegram Integration**: Easy-to-use Telegram interface for recruiters and potential employers
- **CV Content Processing**: Reads and processes the complete CV from a markdown file
- **Plain Text Responses**: Clean, formatted responses without markdown or HTML
- **Real-time Processing**: Instant responses to CV-related questions
- **Error Notifications**: Automatically notifies users in the Telegram chat if any errors occur during processing

## 📋 Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- OpenRouter API Key (from [OpenRouter](https://openrouter.ai/))

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd guizot-cv-ai-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   OPENAI_MODEL=stepfun/step-3.5-flash:free
   ```

## 🔧 Configuration

### Getting a Telegram Bot Token

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token provided

### Getting an OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for an account
3. Navigate to the API keys section
4. Create a new API key
5. Copy the API key

## 🚀 Usage

1. **Start the bot**
   ```bash
   python main.py
   ```

2. **Interact with the bot**
   - Search for your bot on Telegram
   - Send `/start` to begin
   - Ask questions about Rinaldi's CV such as:
     - "What is Rinaldi's experience with Android development?"
     - "What are his key skills?"
     - "What companies has he worked for?"
     - "What is his educational background?"

## 📁 Project Structure

```text
guizot-cv-ai-bot/
├── main.py                # Main bot application
├── cv_full_complete.md    # Complete CV content
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not tracked)
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🔍 How It Works

1. **CV Content Loading**: The bot reads the complete CV from `cv_full_complete.md`
2. **Question Processing**: User questions are processed through OpenRouter's LLM APIs
3. **Context-Aware Responses**: The AI uses only the CV content to answer questions
4. **Telegram Delivery**: Responses are formatted and sent back to the user

## 🧠 AI Model

- **Primary Model**: `stepfun/step-3.5-flash:free` (Configurable via `OPENAI_MODEL` environment variable)
- **Alternative Models** (examples):
  - `mistralai/mistral-7b-instruct`
  - `meta-llama/llama-3-8b-instruct`

## 📝 Key Features

- **Plain Text Only**: Responses are formatted in plain text for optimal Telegram display
- **No Markdown/HTML**: Clean formatting without special characters
- **Emoji Integration**: Uses emojis for better visual appeal
- **Error Handling & Notifications**: Graceful handling of missing information and direct global error notifications in Telegram chat
- **Security**: Environment variables for sensitive API keys

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure and private
- The bot only uses provided CV content - no external data sources

## 🐛 Troubleshooting

### Common Issues

1. **"Missing TELEGRAM_BOT_TOKEN or OPENROUTER_API_KEY"**
   - Check your `.env` file exists and contains valid tokens
   - Ensure no extra spaces around the values

2. **Bot not responding**
   - Verify the bot token is correct
   - Check that the bot is running without errors
   - Ensure you've started a conversation with the bot on Telegram

3. **API errors**
   - Verify your OpenRouter API key is valid
   - Check your OpenRouter account has sufficient credits
   - Ensure the model name is correct

---

**Last Updated**: March 2026