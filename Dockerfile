FROM python:3

ADD ExperimentTests.py /
ADD Experiment.py /

RUN pip install pystrich

CMD [ "python", "./ExperimentTests.py" ]
