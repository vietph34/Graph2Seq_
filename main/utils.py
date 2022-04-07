import configure as conf
import codecs
import numpy as np
import os

def load_word_embedding(embedding_path):
    with codecs.open(embedding_path, 'r', 'utf-8') as f:
        word_idx = {}
        vecs = []
        for line in f:
            line = line.strip()
            if len(line.split(" ")) == 2:
                continue
            info = line.split(' ')
            word = info[0]
            vec = [float(v) for v in info[1:]]
            if len(vec) != 300:
                continue
            vecs.append(vec)
            word_idx[word] = len(word_idx.keys()) + 1

    return word_idx, np.array(vecs)

def write_word_idx(word_idx, path):
    dir = path[:path.rfind('/')]
    if not os.path.exists(dir):
        os.makedirs(dir)

    with codecs.open(path, 'w', 'utf-8') as f:
        for word in word_idx:
            f.write(word+" "+str(word_idx[word])+'\n')

def read_word_idx_from_file(path):
    word_idx = {}
    with codecs.open(path, 'r', 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            info = line.strip().split(" ")
            if len(info) != 2:
                word_idx[' '] = int(info[0])
            else:
                word_idx[info[0]] = int(info[1])
    return word_idx


def decode_text(pred_idx, idx_word):
    # if conf.decoder_type != "beam":
    #     pred_idx = pred_idx[0]
    # else:
    #     pred_idx = np.transpose(pred_idx)
    #     pred_idx = pred_idx[0]

    text = ""
    for __ in range(len(pred_idx)):
        ids = pred_idx[__]
        if isinstance(ids, list):
            for id in ids:
                if id == 2:
                    break
                if id != 0:
                    text += idx_word[id] + " "
                else:
                    text += conf.GO + " "
        else:
            if ids == 2:
                break
            if ids != 0:
                text += idx_word[ids] + " "
            else:
                text += conf.GO + " "
    return text