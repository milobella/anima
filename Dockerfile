FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

COPY . /usr/src/app

EXPOSE 8080
# run command
CMD ["python", "app.py"]
