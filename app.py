import streamlit as st
import numpy as np
import requests
import base64
import json
import pickle
from PIL import Image

st.set_page_config(
    page_title="Fruit and Vegetable Quality Predictor",
    page_icon='🍎',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/mfadlili',
        'Report a bug': "https://github.com/mfadlili",
        'About': "# This is hacktiv8 FTDS milestone 2 Phase 2."
    }
)

st.title('Fruit and Vegetable Quality Predictor')
st.image('fruits_vegetables.jpg')
st.write('Only photos of apples, bananas, bitter gourd, capsicum, oranges, and tomatoes can be used to create predictions using this application. ')

def im2json(im):
    """Convert a Numpy array to JSON string"""
    imdata = pickle.dumps(im)
    jstr = json.dumps({"image": base64.b64encode(imdata).decode('ascii')})
    return jstr

select = st.selectbox('Please select image source:', ('Upload image', 'Take a photo'))

if select=='Upload image':
    file = st.file_uploader("", type=["jpg","png"])
    col1, col2 = st.columns(2)

    with col2:
        if st.button('Show the image'):
            if file is not None:
                st.image(file)

    with col1:
        if st.button('Predict'):
            URL = 'https://fruits-vegetables-backend.herokuapp.com/fruit'
            image = Image.open(file)
            img_array = np.array(image)
            file_to_json = im2json(img_array)
            r = requests.post(URL, json=file_to_json)
            hasil = r.json()['result']
            st.title(hasil)
else:
    picture = st.camera_input('Ambil foto anda.')
    if st.button('Predict '):
        URL = 'https://fruits-vegetables-backend.herokuapp.com/fruit'
        image = Image.open(picture)
        img_array = np.array(image)
        file_to_json = im2json(img_array)
        r = requests.post(URL, json=file_to_json)
        hasil = r.json()['result']
        st.title(hasil)
