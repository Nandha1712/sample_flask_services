FROM python:3.7
RUN mkdir /check
ADD ./service_0/app_file80.py /check/app_file80.py
ADD ./service_0/requirements.txt /check/requirements.txt
WORKDIR /check
RUN pip install -r ./requirements.txt
EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "run_server:app", "--workers", "3", "--threads", "25", "--timeout", "660"]
