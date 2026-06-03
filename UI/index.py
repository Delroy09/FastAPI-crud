import streamlit as st

import gmodel as m

st.write("First app")

st.write(m.run())

st.line_chart(m.run())

window = st.slider("Forecast window", 1,30)