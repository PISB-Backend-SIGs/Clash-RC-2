FROM python:3.9-slim-buster

WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

ADD /main /app/main
ADD /test /app/test

CMD ["python", "./main/main.py"]

# RUN "docker cp 459aebef24ed:/main/op.txt /main/op.txt && tail -f /dev/null"
# tag =  prash1
