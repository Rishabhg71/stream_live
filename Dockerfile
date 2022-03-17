FROM python:3.8.10


# RUN ls home/
WORKDIR /app

COPY . .

RUN pip install flask flask_socketio


CMD ["python","app.py"]