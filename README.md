# MEMO-for-SA
MEMO: A Novel Dataset for Multi-lEvel and Multi-dOmain Sentiment Analysis

MEMO introduces a new dataset called multi-level and multi-domain for sentiment analysis. Each opinion contains a short text with at least two sentences and two aspects with different domains and sentiment polarities. 

# ALSA-models on MEMO

**Introduction**

The aim is to experiment with the previous ALSA models over the new dataset named MEMO and baseline datasets to evaluate and compare the performance of the MEMO dataset.

There are no new ideas to improve the previous ALSA models.

**Usage**

Download the folder "ALSA-models" above.

Download pretrained GloVe embeddings with this [link](https://nlp.stanford.edu/projects/glove/) and extract glove.42B.300d.txt into the main folder.

Download the folder "ALSA" above and put it into the folder "ALSA-models". Folder "ALSA" contains the datasets.

Train by using the following command:

- python train.py --model_name bert_spc --dataset memo

# SLSA-models on MEMO

**Introduction**

The aim is to experiment with the previous SLSA models over the new dataset named MEMO and baseline datasets to evaluate and compare the performance of the MEMO dataset.

There are no new ideas to improve the previous SLSA models.

**Usage**

Download the folder "SLSA-models" above.
Download pretrained GloVe embeddings with this [link](https://nlp.stanford.edu/projects/glove/) and extract glove.42B.300d.txt into the embed folder.

Download the folder "SLSA" above put it into the folder "SLSA-models". Folder "SLSA" contains the datasets.
Train by using the following command:

- python main.py -m "cnn" -dp "SLSA/memo"

# DLSA-models on MEMO

**Introduction**

The aim is to experiment with the previous DLSA models over the new dataset named MEMO and baseline datasets to evaluate and compare the performance of the MEMO dataset.

There are no new ideas to improve the previous DLSA models.

**Usage**

Download the folder "DLSA-models" above.
Download pretrained GloVe embeddings with this [link](https://nlp.stanford.edu/projects/glove/) and extract glove.42B.300d.txt into the folder "embed".

Download the folder "DLSA" above put it into the folder "DLSA-models". Folder "DLSA" contains the datasets.
Train by using the following command:

- python main.py -m "cnn" -dp "DLSA/memo_big"


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

