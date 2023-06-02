# query.py

__author__ = 'Nick Hirakawa'

from invdx import build_data_structures
from rank import score_BM25
import operator


class QueryProcessor:
    def __init__(self, queries, corpus):
        self.queries = queries  # Daftar pertanyaan (query) yang akan diproses
        self.index, self.dlt = build_data_structures(corpus)  # Membangun struktur data indeks dan inverted list dari korpus

    def run(self):
        results = []  # Daftar hasil pertanyaan yang akan dikembalikan
        for query in self.queries:
            results.append(self.run_query(query))  # Menjalankan proses query untuk setiap pertanyaan
        return results

    def run_query(self, query):
        query_result = dict()  # Dictionary untuk menyimpan hasil skor setiap dokumen dalam pertanyaan
        for term in query:
            if term in self.index:  # Memeriksa apakah term ada dalam indeks
                doc_dict = self.index[term]  # Mengambil entri indeks untuk term tersebut
                for docid, freq in doc_dict.items():  # Untuk setiap dokumen dan frekuensi kata dalam dokumen tersebut
                    score = score_BM25(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
                                       dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length())  # Menghitung skor BM25
                    if docid in query_result:  # Dokumen ini telah di-skor sebelumnya
                        query_result[docid] += score  # Menambahkan skor ke dokumen yang ada dalam hasil query
                    else:
                        query_result[docid] = score  # Menyimpan skor ke dokumen yang baru dalam hasil query
        return query_result
