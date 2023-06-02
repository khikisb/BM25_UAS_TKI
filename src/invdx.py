# invdx.py
# Sebuah indeks terbalik
__author__ = 'Nick Hirakawa'


class InvertedIndex:
    """
    Mewakili struktur data indeks terbalik.
    """

    def __init__(self):
        """
        Menginisialisasi indeks terbalik yang kosong.
        """
        self.index = dict()

    def __contains__(self, item):
        """
        Memeriksa apakah sebuah kata ada dalam indeks terbalik.
        """
        return item in self.index

    def __getitem__(self, item):
        """
        Mengambil data indeks untuk sebuah kata.
        """
        return self.index[item]

    def add(self, word, docid):
        """
        Menambahkan sebuah kata beserta ID dokumen ke indeks terbalik.
        Jika kata sudah ada, frekuensi kemunculan kata dalam dokumen akan ditambah.
        Jika kata belum ada, akan dibuat entri baru dalam indeks dengan frekuensi awal satu.
        """
        if word in self.index:
            if docid in self.index[word]:
                self.index[word][docid] += 1
            else:
                self.index[word][docid] = 1
        else:
            self.index[word] = {docid: 1}

    def get_document_frequency(self, word, docid):
        """
        Mengembalikan frekuensi kemunculan sebuah kata dalam dokumen tertentu.
        Membuang LookupError jika kata atau ID dokumen tidak ditemukan.
        """
        if word in self.index:
            if docid in self.index[word]:
                return self.index[word][docid]
            else:
                raise LookupError(f'{word} tidak ada dalam dokumen {docid}')
        else:
            raise LookupError(f'{word} tidak ada dalam indeks')

    def get_index_frequency(self, word):
        """
        Mengembalikan frekuensi sebuah kata dalam indeks,
        yaitu jumlah dokumen yang mengandung kata tersebut.
        Membuang LookupError jika kata tidak ditemukan dalam indeks.
        """
        if word in self.index:
            return len(self.index[word])
        else:
            raise LookupError(f'{word} tidak ada dalam indeks')


class DocumentLengthTable:
    """
    Mewakili tabel yang menyimpan panjang dokumen.
    """

    def __init__(self):
        """
        Menginisialisasi tabel panjang dokumen yang kosong.
        """
        self.table = dict()

    def __len__(self):
        """
        Mengembalikan jumlah dokumen dalam tabel.
        """
        return len(self.table)

    def add(self, docid, length):
        """
        Menambahkan panjang sebuah dokumen ke dalam tabel.
        """
        self.table[docid] = length

    def get_length(self, docid):
        """
        Mengembalikan panjang sebuah dokumen.
        Membuang LookupError jika ID dokumen tidak ditemukan.
        """
        if docid in self.table:
            return self.table[docid]
        else:
            raise LookupError(f'{docid} tidak ditemukan dalam tabel')

    def get_average_length(self):
        """
        Mengembalikan panjang rata-rata dari semua dokumen dalam tabel.
        """
        total_length = sum(self.table.values())
        return float(total_length) / float(len(self.table))


def build_data_structures(corpus):
    """
    Membangun indeks terbalik dan tabel panjang dokumen dari korpus yang diberikan.
    Mengembalikan indeks dan tabel yang telah dibangun.
    """
    idx = InvertedIndex()
    dlt = DocumentLengthTable()
    for docid in corpus:

        # Membangun indeks terbalik
        for word in corpus[docid]:
            idx.add(str(word), str(docid))

        # Membangun tabel panjang dokumen
        length = len(corpus[str(docid)])
        dlt.add(docid, length)

    return idx, dlt
