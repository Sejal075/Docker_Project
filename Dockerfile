FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r reqirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
