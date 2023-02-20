FROM python:3.7
RUN mkdir /check
ADD ./service_2/run_server.py /check/run_server.py
ADD ./service_2/requirements.txt /check/requirements.txt
WORKDIR /check
RUN pip install -r ./requirements.txt
EXPOSE 3002

CMD ["gunicorn", "-b", "0.0.0.0:3002", "run_server:app", "--workers", "3", "--threads", "25", "--timeout", "660"]