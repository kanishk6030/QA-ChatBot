FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

EXPOSE 8501

# Use environment variable LANGCHAIN_API_KEY for API key in Render settings
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
