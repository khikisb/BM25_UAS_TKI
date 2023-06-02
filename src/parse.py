# parse.py

__author__ = 'Nick Hirakawa'

import re


class CorpusParser:
    # Kelas CorpusParser digunakan untuk memparsing file korpus

    def __init__(self, filename):
        self.filename = filename
        self.regex = re.compile('^#\s*\d+')
        self.corpus = dict()

    def parse(self):
        # Metode parse() membaca file korpus dan memparsing teksnya
        with open(self.filename, encoding='utf-8') as f:
            s = ''.join(f.readlines())
        blobs = s.split('#')[1:]  # Memisahkan teks berdasarkan tanda '#' pada korpus
        for x in blobs:
            text = x.split()
            docid = text.pop(0)  # Menghapus docid dari teks dan menyimpannya
            self.corpus[docid] = text  # Menyimpan teks ke dalam kamus (dictionary) dengan docid sebagai kunci

    def get_corpus(self):
        # Metode get_corpus() mengembalikan kamus yang berisi korpus yang telah diparsing
        return self.corpus


class QueryParser:
    # Kelas QueryParser digunakan untuk memparsing file pertanyaan (query)

    def __init__(self, filename):
        self.filename = filename
        self.queries = []

    def parse(self):
        # Metode parse() membaca file pertanyaan dan memparsing teksnya
        with open(self.filename encoding='utf-8') as f:
            lines = ''.join(f.readlines())
        self.queries = [x.rstrip().split() for x in lines.split('\n')[:-1]]  # Memisahkan teks menjadi baris dan membagi kata-kata di setiap baris menjadi elemen-elemen dalam daftar
        # .rstrip() digunakan untuk menghapus karakter baris baru (\n) di akhir setiap baris

    def get_queries(self):
        # Metode get_queries() mengembalikan daftar pertanyaan yang telah diparsing
        return self.queries


if __name__ == '__main__':
    # Jika kode ini dieksekusi sebagai program utama
    qp = QueryParser('text/queries.txt')
    print(qp.get_queries())
