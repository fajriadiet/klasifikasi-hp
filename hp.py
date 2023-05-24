import pickle
import streamlit as st
import numpy as np

# membaca model
model = pickle.load(open('hp_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav','rb'))

#judul web
st.title('Prediksi Range Harga HP')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    battery_power = st.number_input('Kekuatan Baterai HP')
    blue = st.number_input('Bluetooh (1 = ada dan 0 = tidak)')
    clock_speed = st.number_input('kecepatan mikroprosesor dalam mengeksekusi instruksi')
    dual_sim = st.number_input('Memiliki dukungan dual sim atau tidak (1 = ada dan 0 = tidak)')
    fc = st.number_input('Mega piksel kamera depan')
    four_g = st.number_input('Memiliki 4G atau tidak (1 = ada dan 0 = tidak)')
    int_memory = st.number_input('Memori Internal dalam Gigabyte')
    m_dep = st.number_input('Kedalaman Ponsel dalam cm')
    mobile_wt = st.number_input('Berat ponsel')
    n_cores = st.number_input('Jumlah inti prosesor')

with col2 :
    pc = st.number_input('Mega piksel Kamera Utama')
    px_height = st.number_input('Tinggi Resolusi Piksel')
    px_width = st.number_input('Lebar Resolusi Piksel')
    ram = st.number_input('Memori Akses Acak dalam Mega Byte')
    sc_h = st.number_input('Tinggi Layar ponsel dalam cm')
    sc_w = st.number_input('Lebar Layar ponsel dalam cm')
    talk_time = st.number_input('waktu terlama satu kali pengisian daya baterai dapat ')
    three_g = st.number_input('Memiliki 3G atau tidak (1 = ada dan 0 = tidak)')
    touch_screen = st.number_input('Memiliki layar sentuh atau tidak (1 = ada dan 0 = tidak)')
    wifi = st.number_input('Memiliki wifi atau tidak')

# code untuk prediksi
prediction = ''
input_data = (battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt,
              n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi)

input_data_as_numpy_array = np.array(input_data)

input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshape)

# membuat tombol untuk prediksi
if st.button('Tes Harga HP'):
    hp_prediction = model.predict(std_data)
    if (hp_prediction[0] == 3):
        prediction = 'Harga HP Terlalu Mahal'
    elif (prediction[0] == 2):
        prediction = 'Harga HP Cukup Mahal'
    elif (prediction[0] == 1):
        prediction = 'Harga HP Normal/Sesuai Standar'
    else:
        prediction = 'Harga HP Murah'
    st.success(prediction)