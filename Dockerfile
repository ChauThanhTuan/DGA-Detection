FROM ubuntu:20.04

RUN apt update

RUN apt install -y python3
RUN apt install -y pip

RUN pip install numpy
RUN pip install tensorflow
RUN pip install flask
RUN pip install flask_restful

RUN mkdir PredictDGA
COPY trained_model_5_3_2.h5 PredictDGA/trained_model_5_3_2.h5
COPY API.py PredictDGA/API.py
COPY predict.py PredictDGA/predict.py

WORKDIR PredictDGA
RUN chmod +x API.py

CMD ["./API.py"]

EXPOSE 5000
