FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt fastapi uvicorn gunicorn
COPY wol-remote.py .
COPY wollib ./wollib
COPY index.html .
EXPOSE 6020
CMD ["uvicorn", "wol-remote:app", "--host", "0.0.0.0", "--port", "6020"]