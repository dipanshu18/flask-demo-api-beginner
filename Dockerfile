FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD [ "flask", "run", "--host", "0.0.0.0" ]