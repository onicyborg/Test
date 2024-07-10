import streamlit as st


def is_prime(n):
    """Function to check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(start, end):
    """Function to find prime numbers in a given range"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


st.title("🎈 Sistem Pencari Bilangan Prima")
st.write("Silahkan Masukkan Range Angka yang Ingin Anda Cari Bilangan Primanya.")

# Input from the user
start_num = st.number_input("Masukkan Angka Pertama:", value=1, step=1)
end_num = st.number_input("Masukkan Angka Kedua:", value=100, step=1)

# Button to submit the range
if st.button("Find Primes"):
    if start_num > end_num:
        st.write("Angka Pertama Harus Lebih Besar Dari Angka Kedua.")
    else:
        prime_numbers = find_primes(start_num, end_num)
        if prime_numbers:
            st.write(f"Bilangan Prima antara {start_num} dan {end_num}:")
            st.write(", ".join(map(str, prime_numbers)))
        else:
            st.write(
                f"Tidak ada ditemukan angka prima antara {start_num} dan {end_num}.")

# Adding name and NIM
st.write("Dibuat oleh: Yunita Nur Alfiyanti")
st.write("NIM: 152310112")
