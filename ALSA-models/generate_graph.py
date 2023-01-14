# -*- coding: utf-8 -*-

import numpy as np
#import spacy
import pickle

#nlp = spacy.load('en_core_web_sm')


def load_sentic_word():
    """
    load senticNet
    """
    path = './senticNet/senticnet_word.txt'
    senticNet = {}
    fp = open(path, 'r')
    for line in fp:
        line = line.strip()
        if not line:
            continue
        word, sentic = line.split('\t')
        senticNet[word] = sentic
    fp.close()
    return senticNet


def dependency_adj_matrix(text, senticNet):
    word_list = text.split()
    seq_len = len(word_list)
    matrix = np.zeros((seq_len, seq_len)).astype('float32')
    
    for i in range(seq_len):
        word = word_list[i]
        if word in senticNet:
            sentic = float(senticNet[word]) + 1.0
        else:
            sentic = 0.5
        for j in range(seq_len):
            matrix[i][j] += sentic
        for k in range(seq_len):
            matrix[k][i] += sentic
        matrix[i][i] = 1

    return matrix

def process(filename):
    senticNet = load_sentic_word()
    fin = open(filename, 'r', encoding='utf-8', newline='\n', errors='ignore')
    lines = fin.readlines()
    fin.close()
    idx2graph = {}
    fout = open(filename+'.graph_s', 'wb')
    for i in range(0, len(lines), 3):
        text_left, _, text_right = [s.lower().strip() for s in lines[i].partition("$T$")]
        aspect = lines[i + 1].lower().strip()
        adj_matrix = dependency_adj_matrix(text_left+' '+aspect+' '+text_right, senticNet)
        idx2graph[i] = adj_matrix
    pickle.dump(idx2graph, fout)
    print('done !!!', filename)
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
