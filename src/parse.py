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
    def __init__(self):
        self.queries = []

    def parse(self, text):
        self.queries = [x.rstrip().split() for x in text.split('\n')[:-1]]

    def get_queries(self):
        return self.queries


if __name__ == '__main__':
    qp = QueryParser()

    # Accept user input for queries
    user_input = st.text_area("Enter queries (separated by newlines):")

    # Parse the user input
    qp.parse(user_input)

    # Retrieve and print the queries
    st.write(qp.get_queries())

