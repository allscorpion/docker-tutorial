FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN apt-get update
RUN apt-get install -y python3
CMD ["python3", "main.py"]
