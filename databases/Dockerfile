FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies for Cassandra CLI
RUN pip install cqlsh

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


