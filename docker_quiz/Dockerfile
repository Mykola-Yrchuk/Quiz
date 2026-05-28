FROM python:3.11

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y python3-tk

RUN pip install -r requirements.txt

CMD ["python", "quiz.py"]