'''
Main prediction module for dgaintel package
'''
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import numpy as np
from tensorflow.keras.models import load_model
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
import shlex
import subprocess

import config

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
SAVED_MODEL_PATH = os.path.join(DIR_PATH, 'trained_model_5_3_2.h5')

MODEL = load_model(SAVED_MODEL_PATH)
CHAR2IDX = {'-': 0, '.': 1, '0': 2, '1': 3, '2': 4, '3': 5,
            '4': 6, '5': 7, '6': 8, '7': 9, '8': 10, '9': 11,
            '_': 12, 'a': 13, 'b': 14, 'c': 15, 'd': 16, 'e': 17,
            'f': 18, 'g': 19, 'h': 20, 'i': 21, 'j': 22, 'k': 23,
            'l': 24, 'm': 25, 'n': 26, 'o': 27, 'p': 28, 'q': 29,
            'r': 30, 's': 31, 't': 32, 'u': 33, 'v': 34, 'w': 35,
            'x': 36, 'y': 37, 'z': 38}

count=0

def _inputs(domains):
    if isinstance(domains, list):
        return [domain.lower() for domain in domains]

    return [domains.lower()]

def _get_prediction(domain_name, prob=None):
    global count
    es = Elasticsearch(f"http://{config.SELKS_IP}:{config.SELKS_PORT}/")
    if not prob:
        prob = get_prob([domain_name], raw=True)

    if prob >= 0.5:
        count = count+1
        doc = {
            'author': 'QuynhQuynh',
            'text': 'Elasticsearch predict DGA domain: {} is DGA with probability {:f}\n'.format(domain_name, prob),
            'timestamp': datetime.now() + timedelta(hours=7),
        }
        #res = es.index(index="logstash-predict-dga-domain", id=count+1, document=doc)
        res = es.index(index="test-index", id=count, document=doc)
        cmd = cmd = f'curl -XPOST -H \'Authorization: Bearer 4aR8NTB193w54OWYHC7IWZANL13SyjUt\' -H \'Content-Type: application/json\' http://{config.SELKS_IP}:{config.SELKS_PORT}//api/alert -d \'\x7B  "title": "DGA alert",  "description": "DGA alert",  "type": "external",  "source": "instance"{str(datetime.now())},  "sourceRef": "alert-ref"\x7D\''
        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()


        return '{} is DGA with probability {:f}\n'.format(domain_name, prob)

    count = count+1
    doc = {
            'author': 'QuynhQuynh',
            'text': 'Elasticsearch predict DGA domain: {} is genuine with probability {:f}\n'.format(domain_name, prob),
            'timestamp': datetime.now() + timedelta(hours=7),
    }
    #res = es.index(index="logstash-predict-dga-domain", id=count+1, document=doc)
    res = es.index(index="test-index", id=count, document=doc)
    return '{} is genuine with probability {:f}\n'.format(domain_name, prob)

def get_prob(domains, raw=False, internal=False):
    '''
    Core inference function; calls model on vectorized batch of domain names.
    Input: list of domains (list)
    Output: len(domains) == 1: single probability value
            raw=False: list of tuples of format (domain_name, probability)
            raw=True: np.ndarray of probabilities
    '''
    if not isinstance(domains, list):
        domains = _inputs(domains)

    vec = np.zeros((len(domains), 82))

    for i, domain in enumerate(domains):
        for j, char in enumerate(domain):
            vec[i, j] = CHAR2IDX[char] if char in CHAR2IDX else -1


    prob = MODEL(vec).numpy()
    prob = prob.transpose()[0]

    if not internal:
        if prob.shape[0] == 1:
            return prob.sum()

        if raw:
            return prob

    return list(zip(domains, list(prob)))

def get_prediction(domains, to_file=None, show=True):
    '''
    Wrapper for printing out/writing full predictions on a domain or set of domains
    Input: domain (str), list of domains (list), domains in .txt file (FileObj)
    Output: show to stdout
        show=False: list of prediction strings (list)
        to_file=<filename>.txt: writes new file at <filename>.txt with predictions
    '''
    raw_probs = get_prob(_inputs(domains), internal=True)
    preds = [_get_prediction(domain, prob=prob) for domain, prob in raw_probs]

    if to_file:
        assert os.path.splitext(to_file)[1] == ".txt"

        with open(os.path.join(os.getcwd(), to_file), 'w') as outfile:
            outfile.writelines(preds)
        return None

    if show:
        for pred in preds:
            print(pred.strip('\n'))
        return None

    return preds

def main():
    '''
    Main function for testing purposes.
    '''
    get_prediction(['microsoft.com',
                    'squarespace.com',
                    'hsfkjdshfjasdhfk.com',
                    'fdkhakshfda.com',
                    'foilfencersarebad.com',
                    'discojjfdsf.com',
                    'fasddafhkj.com',
                    'wikipedai.com'])

if __name__ == '__main__':
    main()
