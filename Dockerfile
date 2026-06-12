FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY . .
RUN cd todo_project && ls -laht
EXPOSE ${FLASK_RUN_PORT}
CMD cd todo_project && flask run
