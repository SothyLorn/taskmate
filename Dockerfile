FROM python:3.8

WORKDIR "/app/"

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . "/app/"

CMD [ "python", "manage.py", "runserver" ]
