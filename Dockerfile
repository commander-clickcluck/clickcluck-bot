#Use official Pyhton image
FROM python:3.11-slim

#Set working directory
WORKDIR /app

#Copy all files to container
COPY ...

#install dependancies
RUN pip install --no-cache-dir -r requirements.txt

#run the bot
CMD["python","main.py"]