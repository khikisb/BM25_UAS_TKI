import streamlit as st
from parse import QueryParser, CorpusParser
from query import QueryProcessor
import operator

def run_query(query, corpus_text):
    # Inisialisasi CorpusParser dengan teks korpus
    cp = CorpusParser(corpus_text)

    # Parsing korpus dari teks korpus
    cp.parse()
    # Mendapatkan daftar dokumen dalam korpus
    corpus = cp.get_corpus()

    # Inisialisasi QueryProcessor dengan query dan korpus
    proc = QueryProcessor([query], corpus)  # Menggunakan query sebagai daftar queries

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
    corpus_file = st.file_uploader("Unggah file korpus (corpus.txt)", type="txt")

    if query and corpus_file is not None:
        corpus_text = corpus_file.read().decode("utf-8")  # Membaca teks korpus dari file yang diunggah
        run_query(query, corpus_text)

if __name__ == '__main__':
    main()
