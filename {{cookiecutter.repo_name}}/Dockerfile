FROM python:3.7

COPY src/{{cookiecutter.folder_name}} ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR .

CMD ["python", "main.py"]
