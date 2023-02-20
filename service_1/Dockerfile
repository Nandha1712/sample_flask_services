FROM python:3.7
RUN mkdir /check
ADD ./service_1/requirements.txt /check/requirements.txt
WORKDIR /check
RUN pip install -r ./requirements.txt
ADD ./service_1/run_server.py /check/run_server.py
ADD ./custom_logger_utils.py /check/custom_logger_utils.py
EXPOSE 3001

CMD ["gunicorn", "-b", "0.0.0.0:3001", "run_server:app", "--workers", "3", "--threads", "25", "--timeout", "660"]