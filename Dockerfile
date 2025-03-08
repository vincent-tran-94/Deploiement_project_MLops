FROM python:3.11-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY .  /app/

# Install packages from requirements.txt

RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.org -r requirements.txt

CMD ["python", "app.py"]