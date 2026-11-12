FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PORT=3000
WORKDIR /app
RUN pip install --no-cache-dir 'Flask>=3.1,<4' 'gunicorn>=23,<24'
COPY app.py .
COPY backend ./backend
EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
