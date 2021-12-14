FROM python:3.7
COPY . .
RUN pip install -r requirements.txt
ENV DATABASE_URI=mysql+pymysql://root:password@mysql:3306/flask-db
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
