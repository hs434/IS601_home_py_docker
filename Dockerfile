FROM python:3

ADD src /ExperimentTests_hw_2.py /
ADD src /Experiment_hw_1.py /

RUN pip install pystrich

CMD [ "python", "./src/ExperimentTests_hw_2.py" ]
