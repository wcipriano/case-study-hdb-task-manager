FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY . .
EXPOSE ${PORT}
CMD flask --app ${FLASK_APP} --debug run --host ${HOST} --port ${PORT}
