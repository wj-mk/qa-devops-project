FROM python:3.7
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]

RUN python3 -m pytest --cov --cov-report term-missing