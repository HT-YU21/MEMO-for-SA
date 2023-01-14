# MEMO-for-SA
MEMO: A Novel Dataset for Multi-lEvel and Multi-dOmain Sentiment Analysis

# ALSA-models on MEMO

** Introduction
The aim is to experiment with the previous ALSA models over the new dataset named MEMO and baseline datasets to evaluate and compare the performance of the MEMO dataset.

There are no new ideas to improve the previous ALSA models.

** Usage

Download pretrained GloVe embeddings with this [link](https://nlp.stanford.edu/projects/glove/) and extract glove.42B.300d.txt into the main folder

Train by using the following command:

- python train.py --model_name bert_spc --dataset memo

# Credits

**ALSA METHODS**

- Codes of ALSA methods heavily relies on [Sentic-GCN](https://github.com/BinLiang-NLP/Sentic-GCN) and [ABSA-PyTorch](https://github.com/songyouwei/ABSA-PyTorch)
in the paper:

[Aspect-Based Sentiment Analysis via Affective Knowledge Enhanced Graph Convolutional Networks](https://www.sentic.net/sentic-gcn.pdf)

Bin Liang, Hang Su, Lin Gui, Erik Cambria, Ruifeng Xu. Knowledge-Based Systems, 2021: 107643.

- Here, we would like to express our heartfelt thanks to all the authors of [Sentic-GCN](https://github.com/BinLiang-NLP/Sentic-GCN) and [ABSA-PyTorch](https://github.com/songyouwei/ABSA-PyTorch)

**DLSA and SLSA METHODS**

- Codes of DLSA and SLSA methods heavily relies on [Sentiment-analysis](https://github.com/davide97l/Sentiment-analysis)
- Here, we would like to express our heartfelt thanks to all the authors of [Sentiment-analysis](https://github.com/davide97l/Sentiment-analysis)

