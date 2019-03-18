FROM python:3.7

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

# run command
CMD ["anima_launcher"]
