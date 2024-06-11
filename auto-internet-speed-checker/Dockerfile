FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY speed_log.csv speed_log.csv
COPY script.py script.py

CMD ["python", "script.py"]

# docker build -t speedtest .
# docker run -v F:\Productivity\Github-Repos\cowlar-hyper-growth-1\auto-internet-speed-checker:/app speedtest
