import streamlit as st
#from pages import budgeting, expense_tracker, financial_planning, sip_calculator, emi_calculator  # Corrected imports

st.set_page_config(
    page_title="Financial Empowerment for Women",
    page_icon="icon.webp"  # Ensure the image is in the same directory
)

# **Add title**
st.title("Financial Empowerment for Women")

# **Add an image**
st.image("icon.webp", caption="Empowering Women Financially", use_container_width=True)

# **Add content for each section directly**
st.subheader("Budgeting")

st.subheader("Expense Tracker")

st.subheader("Financial Planning")

st.subheader("SIP Calculator")

st.subheader("EMI Calculator")
