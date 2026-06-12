FROM python:3.12-slim
WORKDIR /app
COPY wol-remote.py .
COPY index.html .
RUN pip install --no-cache-dir fastapi uvicorn gunicorn
EXPOSE 8090
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8090"]