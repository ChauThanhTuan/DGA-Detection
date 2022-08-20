FROM ubuntu:20.04

RUN apt update

RUN apt install -y python3
RUN apt install -y pip

RUN pip install numpy
RUN pip install tensorflow
RUN pip install flask
RUN pip install flask_restful
RUN pip install elasticsearch

RUN mkdir PredictDGA
COPY trained_model_5_3_2.h5 PredictDGA/trained_model_5_3_2.h5
COPY selks_dga.py PredictDGA/selks_dga.py
COPY predictDGA.py PredictDGA/predictDGA.py
COPY config.py PredictDGA/config.py
COPY getDomain.py PredictDGA/getDomain.py

WORKDIR PredictDGA
RUN chmod +x selks_dga.py

CMD ["./selks_dga.py"]

EXPOSE 5000
