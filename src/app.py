import streamlit as st
from parse import QueryParser, CorpusParser
from query import QueryProcessor
import operator

class QueryParser:
    def __init__(self):
        self.queries = []

    def parse(self, queries):
        self.queries = [query.split() for query in queries]

    def get_queries(self):
        return self.queries


def main():
    st.title("Query Parser")
    st.write("Enter queries (separated by newlines):")
    
    # Accept user input for queries
    user_input = st.text_area("")

    # Split the user input into a list of queries
    queries = user_input.split('\n')

    # Initialize and parse queries using QueryParser
    qp = QueryParser()
    qp.parse(queries)
    
    # Retrieve and display the parsed queries
    parsed_queries = qp.get_queries()
    for query in parsed_queries:
        st.write(query)
    github_url = "https://raw.githubusercontent.com/khikisb/BM25_UAS_TKI/main/src/corpus.txt"
    file_content = load_file_from_github(github_url)

    cp = CorpusParser(file_content)   

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
            print('{:>1}\tQ0\t{:>4}\t{:>2}\t{:>12}\tNH-BM25'.format(*tmp))
            index += 1
            
        
        qid += 1  # Menaikkan ID query untuk query selanjutnya

   
        

if __name__ == '__main__':
    main()
