import streamlit as st
from io import StringIO
from pages.libs.converter1 import converter_process

st.title("Excel to JSON converter")

st.text("This is the excel to json converter.")

uploaded_file = st.file_uploader("Give me a file")

activebutton = st.button("activate")
message = st.empty()

if activebutton:
    converter_process(message.write)
    message.write("done")

    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        data = stringio.read()
        message.write(data)

        # with open("pages/file_cont/tempfile.txt", "w") as tempfile:
        #     tempfile.write(data)

        st.download_button(
            label="Download data as CSV",
            data=data,
            file_name='tempfile.txt',
            mime='text/csv',
        )