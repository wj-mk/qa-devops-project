FROM python:3.7
COPY . .
RUN pip install -r requirements.txt
ARG DATABASE_URI=$DATABASE_URI
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
