import streamlit as st
import random
import time

st.set_page_config(
    page_title="Matematik Game",
    page_icon='➗',
    layout="centered",
    initial_sidebar_state="auto",
)
st.title("Matematik Çalışma 5. Sınıf ➗😎")


# initializing with a random number
if "rn1" not in st.session_state:
    st.session_state["rn1"] = random.randint(10,100)

if "rn2" not in st.session_state:
    st.session_state["rn2"] = random.randint(1,10)
if "giris" not in st.session_state:
    st.session_state["giris"] = 1
# callback function to change the random number stored in state
def change_number():
    st.session_state["rn1"] = random.randint(11,100)
    st.session_state["rn2"] = random.randint(1,10)
    st.session_state["giris"] = st.session_state["giris"] +1
    return

if "dogru_cevap_sayisi" not in st.session_state:
    st.session_state["dogru_cevap_sayisi"] = 0


## button to generate a new random number
st.button("Yeni Soru Getir", on_click=change_number)
sayi1 = st.session_state["rn1"]
sayi2 = st.session_state["rn2"] 
soru_sayi = st.session_state["giris"]

dogru_cevap = sayi1 // sayi2
#st.write(dogru_cevap)
#st.info(sayi1,'/',sayi2)
#st.info(sayi2)


# start the timer
#start_time = time.time()
#st.write(start_time)
with st.form('Form', clear_on_submit=True):
    st.info(f"Soru{soru_sayi} :    {sayi1} / {sayi2} kaçtır ?")
    yanit = st.number_input('Bölüm kaçtır?', min_value=1, step=None, value=None)
    #yanit = st.number_input('Bölüm kaçtır',   step=1, value=int)
    submit = st.form_submit_button('Yanıtı Gönder')
    st.session_state["dogru_cevap_sayisi"]

# stop the timer


# calculate the elapsed time

if submit:
    if yanit == dogru_cevap:
        #end_time = time.time()
        #elapsed_time = end_time - start_time
        #st.write(elapsed_time)
        #st.info("Doğru! Bu soruyu {:.0f} saniyede cevapladın.".format(elapsed_time))
        st.info(f"{yanit} ...  Doğru cevap, tebrikler...")
        st.session_state["dogru_cevap_sayisi"] += 1

    else:
        st.error(f"{yanit} ...  Yanlış cevap, tekrar deneyiniz.")
