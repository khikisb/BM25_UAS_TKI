# rank.py

__author__ = 'Nick Hirakawa'

from math import log

k1 = 1.2  # Parameter k1 untuk BM25
k2 = 100  # Parameter k2 untuk BM25
b = 0.75  # Parameter b untuk BM25
R = 0.0  # Jumlah dokumen yang relevan dengan pertanyaan

def score_BM25(n, f, qf, r, N, dl, avdl):
    # Fungsi untuk menghitung skor BM25

    K = compute_K(dl, avdl)  # Menghitung nilai K menggunakan fungsi compute_K
    first = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))  # Perhitungan bagian pertama skor BM25
    second = ((k1 + 1) * f) / (K + f)  # Perhitungan bagian kedua skor BM25
    third = ((k2 + 1) * qf) / (k2 + qf)  # Perhitungan bagian ketiga skor BM25
    return first * second * third  # Mengembalikan skor BM25

def compute_K(dl, avdl):
    # Fungsi untuk menghitung nilai K

    return k1 * ((1 - b) + b * (float(dl) / float(avdl)))  # Menghitung dan mengembalikan nilai K berdasarkan panjang dokumen (dl) dan rata-rata panjang dokumen (avdl)
