import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("My  App")

st.get_data = s3 


x = st.slider("Select a value for x")

st.write(f"x = {x}")

x_values = np.linspace(-10, 10, 100)
y_values = x_values**2

plt.plot(x, y_values)
st.pyplot()
