# Q&A Chatbot With Groq

This repository contains a small Streamlit-based Q&A chatbot that uses Groq models via LangChain. It provides a simple web UI to send user questions to a selected model and display the model's responses.

## Features

- Streamlit UI for interactive Q&A
- Selectable Groq models to choose different model sizes and capabilities
- Adjustable `temperature`: controls randomness of responses (0.0 = deterministic, 1.0 = more creative)
- Configurable `max_tokens`: limits the response length to control verbosity and cost
- Simple configuration via `.env` for API keys

## Prerequisites

- Python 3.10 or newer
- A Groq API key
- Git (optional)

## Setup (Windows)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& .venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:

```
LANGCHAIN_API_KEY=your_groq_api_key_here
```

## Setup (macOS / Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Create a `.env` file as shown above.

## Run the app

Start the Streamlit app:

```bash
streamlit run app.py
```

Open the URL shown by Streamlit (usually http://localhost:8501) and use the sidebar to:

- Enter your Groq API key (or rely on `.env`)
- Select model
- Adjust `temperature` and `max_tokens`

Type a question in the input box and press Enter to get a response.

## Deploying to Render (free tier)

1. Push your repository to GitHub (if not already):

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

2. In Render, create a new **Web Service** and connect your GitHub repo.

3. Choose **Docker** as the environment (Render will detect the `Dockerfile`) or choose the Python environment and set the start command to:

```bash
streamlit run app.py --server.port $PORT --server.address=0.0.0.0
```

4. Set environment variables/secrets in the Render dashboard:

- `LANGCHAIN_API_KEY` — your Groq API key

5. Deploy. The service will build the image using the `Dockerfile` and run the app. Streamlit uses port `8501` by default; Render injects `$PORT` if you use the non-Docker option.

Notes:
- Monitor build logs on Render for any missing system packages or build errors. Add required OS packages to the `Dockerfile` if needed.
- Keep secrets in Render's dashboard (do not commit API keys).

## Environment variables

- `LANGCHAIN_API_KEY` — your Groq API key used by LangChain/Groq.
- `LANGCHAIN_TRACKING_V2` — set to `true` to enable LangChain tracking (the app sets this automatically).
- `LANGCHAIN_PROJECT_NAME` — project name for LangChain tracking (the app sets this to `Chatbot`).

## Project structure

- `app.py` — main Streamlit application.
- `requirements.txt` — Python dependencies.
- `.gitignore` — ignores virtual environments, env files, and common artifacts.

## Dependencies

The project uses the packages listed in `requirements.txt`. Primary libraries include:

- `streamlit` — web UI
- `langchain-groq`, `langchain-core`, `langchain-community`, `langchain` — LangChain + Groq integration
- `python-dotenv` — load `.env` variables

## Notes & Security

- Do not commit your `.env` or API keys to version control. `.env` is included in `.gitignore`.
- If you plan to deploy, store secrets in a secure secret manager or CI/CD environment variables instead of `.env`.

## Troubleshooting

- If Streamlit doesn't start, ensure the virtual environment is active and dependencies installed.
- If the app responds with authentication errors, verify `LANGCHAIN_API_KEY` is correct and has the required permissions.

## License

Add a license file if you intend to publish this project publicly.
