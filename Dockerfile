FROM python

COPY . "/app/"

WORKDIR "/app/"

RUN pip install -r requirement.txt

CMD [ "python", "manage.py", "runserver" ]
