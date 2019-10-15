FROM python:3

ADD ExperimentTests_hw_2.py /
ADD Experiment_hw_1.py /

RUN pip install pystrich

CMD [ "python", "./ExperimentTests_hw_2.py" ]
