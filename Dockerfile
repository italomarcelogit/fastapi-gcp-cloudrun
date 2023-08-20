FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV PORT=8080
CMD exec python main.py
