import streamlit as st
from parse import QueryParser, CorpusParser
from query import QueryProcessor
import operator

def run_query(query):
    # Inisialisasi QueryParser dengan file queries.txt
    qp = QueryParser(filename='../text/queries.txt')
    # Inisialisasi CorpusParser dengan file corpus.txt
    cp = CorpusParser(filename='../text/corpus.txt')

    # Parsing queries dari file queries.txt
    qp.parse()
    # Mendapatkan daftar queries
    queries = qp.get_queries()
    # Parsing corpus dari file corpus.txt
    cp.parse()
    # Mendapatkan daftar dokumen dalam corpus
    corpus = cp.get_corpus()

    # Inisialisasi QueryProcessor dengan queries dan corpus
    proc = QueryProcessor(queries, corpus)

    # Menjalankan proses pencarian query
    results = proc.run()

    qid = 0  # ID untuk query
    for result in results:
        # Mengurutkan hasil pencarian berdasarkan nilai (dalam urutan menurun)
        sorted_x = sorted(result.items(), key=operator.itemgetter(1))
        sorted_x.reverse()

        index = 1  # Index untuk ranking hasil pencarian

        # Mengambil 100 hasil pencarian teratas
        for i in sorted_x[:100]:
            tmp = (qid, i[0], index, i[1])
            # Menampilkan hasil pencarian dengan format yang ditentukan
            st.write('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
            index += 1

        qid += 1  # Menaikkan ID query untuk query selanjutnya

def main():
    st.title("Query Processor")

    query = st.text_input("Masukkan query:")
    if query:
        run_query(query)

if __name__ == '__main__':
    main()
