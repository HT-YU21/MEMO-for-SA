# -*- coding: utf-8 -*-

import numpy as np
import spacy
import pickle

nlp = spacy.load('en_core_web_sm')


def dependency_adj_matrix(text):
    # https://spacy.io/docs/usage/processing-text
    document = nlp(text)
    seq_len = len(text.split())
    matrix = np.zeros((seq_len, seq_len)).astype('float32')
    
    for token in document:
        if token.i < seq_len:
            matrix[token.i][token.i] = 1
            # https://spacy.io/docs/api/token
            for child in token.children:
                if child.i < seq_len:
                    matrix[token.i][child.i] = 1

    return matrix

def process(filename):
    fin = open(filename, 'r', encoding='utf-8', newline='\n', errors='ignore')
    lines = fin.readlines()
    fin.close()
    idx2graph = {}
    fout = open(filename+'.tree', 'wb')
    for i in range(0, len(lines), 3):
        text_left, _, text_right = [s.lower().strip() for s in lines[i].partition("$T$")]
        aspect = lines[i + 1].lower().strip()
        adj_matrix = dependency_adj_matrix(text_left+' '+aspect+' '+text_right)
        idx2graph[i] = adj_matrix
    pickle.dump(idx2graph, fout)        
    fout.close() 

if __name__ == '__main__':
    process('./ALSA/twitter/train.raw')
    process('./ALSA/twitter/test.raw')
    process('./ALSA/memo/MEMO_Train.txt')
    process('./ALSA/memo/MEMO_Test.txt')
    process('./ALSA/mams/mams_train.txt')
    process('./ALSA/mams/mams_test.txt')
    process('./ALSA/restaurant/restaurant_train.raw')
    process('./ALSA/restaurant/restaurant_test.raw')
    process('./ALSA/laptop/laptop_train.raw')
    process('./ALSA/laptop/laptop_test.raw')
