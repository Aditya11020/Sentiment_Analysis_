FROM python:3.9

COPY . /app
WORKDIR  /app

run pip install -r requirement.txt
EXPOSE 5000

CMD ["python3" , "app.py"]