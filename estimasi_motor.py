import pickle
import streamlit as st

model = pickle.load(open('estimasi_motor.sav', 'rb'))

st.title('Estimasi harga motor bekas')

tahun = st.number_input('Input tahun motor')
odometer = st.number_input('Input KM motor')
pajak = st.number_input('Input pajak motor')
konsumsiBBM = st.number_input('Input konsumsiBBM motor')

predict = ''

if st.button('Estimasi harga'):
    predict = model.predict(
        [[tahun, odometer, pajak, konsumsiBBM]]
    )
    st.write('Estimasi harga motor bekas dalam Rupiah (Juta) :', predict
    )