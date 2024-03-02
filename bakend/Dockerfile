FROM python:3.8

WORKDIR /backend

copy ./backend/requirements.txt /backend/requirements.txt
RUN pip install -r requirements.txt

COPY ./backend /backend

CMD ["python", "app.py"]