import streamlit as st


st.set_page_config(
    page_title="Matematik Game",
    page_icon='➗',
    layout="centered",
    initial_sidebar_state="auto",
)
st.title("Matematik Çalışma 5. Sınıf ➗😎")




import random
import time

x = random.randint(11, 100)
y = random.randint(1, 10)
print("Bölünen sayısı =", x)
print("Bölen sayısı =", y)
dogru_bolum = x // y
dogru_kalan = x % y

while True:
    start_time = time.time()  # Başlangıç zamanını al

    bolum = st.number_input('Bölüm')



    if bolum == dogru_bolum:
        st.write("Doğru bölüm cevabı!")
        st.write("Kalan sonucunu yaz")
        kalan = st.number_input('Kalan')
        end_time = time.time()  # Yeni bitiş zamanını al
        elapsed_time = end_time - start_time  # Yeni geçen süreyi hesapla

        if kalan == dogru_kalan:
            st.info("Doğru kalan cevabı!")
            st.info(f"Toplam süre: {elapsed_time:.0f} saniye")  # Süreyi yazdır
            break
    else:
        st.error("Yanlış cevap. Tekrar deneyin.")
