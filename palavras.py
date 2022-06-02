import re
import time

import numpy as np
from scipy import spatial
from tqdm import tqdm


class LerArquivo():
    def __init__(self, file) -> None:
        self.file = file

    def count_generator(self, reader):
        b = reader(1024 * 1024)
        while b:
            yield b
            b = reader(1024 * 1024)

    def lines(self):
        with open(self.file, 'rb') as fp:
            c_generator = self.count_generator(fp.raw.read)
            return sum(buffer.count(b'\n') for buffer in c_generator)

    def read_file(self):
        lines = []
        pbar = tqdm(total=self.lines(), desc="Lendo palavras")
        with open(self.file, 'r') as f:
            for line in f:
                lines.append(line[:-1])
                pbar.update(1)
            pbar.close()
            return lines

    def copy_words(self):
        lines = []
        pbar = tqdm(total=self.lines(), desc="Lendo palavras")
        with open(self.file, 'r') as f:
            file_dest = open("/media/dados/Dev/dicts/dicio_pt_5.txt", "w")
            for line in f:
                if len(line[:-1]) == 5:
                    file_dest.write(line)
                pbar.update(1)
            pbar.close()
            file_dest.close()
            return lines

    def compare_files(self):
        lista_palavras = self.read_file()
        palavras_finais = []

        with open('/media/dados/Dev/dicts/glove_s300.txt', 'rb') as fp:
            c_generator = self.count_generator(fp.raw.read)
            linhas = sum(buffer.count(b'\n') for buffer in c_generator)
        pbar = tqdm(total=linhas, desc="Comparando palavras")

        # limit = 0
        # file_lines = ""
        emmbed_dict = {}
        with open('/media/dados/Dev/dicts/glove_s300.txt', 'r') as f:
            file = open("/media/dados/Dev/dicts/glove_s300_melhorado.txt", "w")
            for line in f:
                # if limit == 1000: break
                values = line.split()
                word = values[0]
                pbar.update(1)
                try:
                    if len(values) == 301:
                        if word in lista_palavras:
                            vector = np.asarray(values[1:], 'float32')
                            emmbed_dict[word] = vector
                            palavras_finais.append(word)
                            # file_lines += line
                            file.write(line)
                        # else:
                        #     pbar.update(desc=word)
                        #     print(word)
                except Exception as e:
                    print(e)
                # limit += 1
            pbar.close()
            file.close()
        # print(file_lines)


# arquivo = LerArquivo('/media/dados/Dev/dicts/dicio_pt.txt')
# arquivo.copy_words()
# arquivo.compare_files()


def count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


def lines(file):
    with open(file, 'rb') as fp:
        c_generator = count_generator(fp.raw.read)
        return sum(buffer.count(b'\n') for buffer in c_generator)


def make_emmbed_dict():
    emmbed_dict = {}
    file = "/media/dados/Dev/dicts/cc.it.300.vec"
    file = "/media/dados/Dev/dicts/glove_s300.txt"
    file = "/media/dados/Dev/dicts/glove_s300_melhorado.txt"
    pbar = tqdm(total=lines(file), desc="Lendo palavras")

    with open(file, 'r') as f:
        for line in f:
            # if limit == 594000: break
            values = line.split()
            word = values[0]
            pbar.update(1)
            try:
                if len(values) == 301:
                    if not re.search("[0-9.-A-Z]", word):
                        vector = np.asarray(values[1:], 'float32')
                        emmbed_dict[word] = vector
                    # else:
                    #     print(word)
            except Exception as e:
                print(e)
        # limit += 1
        pbar.close()
    return emmbed_dict


def search(search_word):
    print("Similar:", search_word.title())
    if " " not in search_word:
        resultado = find_similar_word(emmbed_dict[search_word])[1:100]
    else:
        resultado = find_similar_word(
            emmbed_dict["pasta"] + emmbed_dict["pomodoro"]
        )[2:100]
    resultado = [x for x in resultado if len(x) == 10]
    print(resultado)


def find_similar_word(emmbedes):
    nearest = sorted(emmbed_dict.keys(), key=lambda word: spatial.distance.euclidean(emmbed_dict[word], emmbedes))
    return nearest


start_time = time.time()
emmbed_dict = make_emmbed_dict()
search("pasta")
print("\nTime execution: ", time.time() - start_time)


""" ======================================================================= """

# import nlpnet
# start_time = time.time()
# nlpnet.set_data_dir('/media/dados/Dev/dicts/pos-pt/')
# tagger = nlpnet.POSTagger()
# frase = 'Pelo menos ainda segue positivo'
# print()
# print(f"A frase é:", frase)
# print()
# print(f"Análise morfológica:")
# texto = tagger.tag(frase)
# siglas = {
#             "NPROP": "Nome próprio",
#             "PU": "Pontuação",
#             "V": "Verbo",
#             "PREP": "Preposição",
#             "ADJ": "Adjetivo",
#             "ADV": "Advérbio",
#             "PDEN": "Pronome definido"
#             }
# for i in texto[0]:
#     print(f"{i[0]}\t\t{siglas[i[1]].upper()}")

# print("\nTime execution: ", time.time() - start_time)

# from mxnet import nd
# from mxnet.contrib import text

# glove_6b50d = text.embedding.create(
#     'glove', pretrained_file_name='glove.6B.50d.txt')

# print(len(glove_6b50d))

# def knn(W, x, k):
#     # The added 1e-9 is for numerical stability
#     cos = nd.dot(W, x.reshape((-1,))) / (
#         (nd.sum(W * W, axis=1) + 1e-9).sqrt() * nd.sum(x * x).sqrt())
#     topk = nd.topk(cos, k=k, ret_typ='indices').asnumpy().astype('int32')
#     return topk, [cos[i].asscalar() for i in topk]

# def get_similar_tokens(query_token, k, embed):
#     topk, cos = knn(embed.idx_to_vec,
#                     embed.get_vecs_by_tokens([query_token]), k+1)
#     for i, c in zip(topk[1:], cos[1:]):  # Remove input words
#         print('cosine sim=%.3f: %s' % (c, (embed.idx_to_token[i])))

# get_similar_tokens('chip', 30, glove_6b50d)
