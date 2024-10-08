# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:53:44 2024

@author: user
"""

import streamlit as st

# Header
st.markdown("<h1 style='text-align: center;'>Cost Model</h1>", unsafe_allow_html=True)

# Title of the app
#st.title('Cost Model')

# Input: Percentage Value (A)
A = st.text_input("Enter the percentage value :", "", key='A')
A_style = """
    <style>
    [data-testid="stTextInput"] > div:first-child {
        background-color: yellow;
    }
    </style>
"""
st.markdown(A_style, unsafe_allow_html=True)

# Input: Wage Rate (B)
B = st.text_input("Enter the wage rate :", "", key='B')
B_style = """
    <style>
    [data-testid="stTextInput"] > div:nth-child(2) {
        background-color: blue;
    }
    </style>
"""
st.markdown(B_style, unsafe_allow_html=True)

# Input: Process Rate (C)
C = st.text_input("Enter the process rate :", "", key='C')
C_style = """
    <style>
    [data-testid="stTextInput"] > div:nth-child(3) {
        background-color: orange;
    }
    </style>
"""
st.markdown(C_style, unsafe_allow_html=True)

# Dropdown: Task Type
task_type = st.selectbox("Select the task type:", ["unload", "putaway", "pick", "pack", "select"])

# Button to calculate cost per unit (D)
if st.button('Calculate'):
    if A and B and C:
        try:
            A = float(A)
            B = float(B)
            C = float(C)
            D = (B / C) * (A / 100)
            st.write(f"Cost per unit : {D:.2f}")
        except ValueError:
            st.write("Please enter valid numeric values for A, B, and C.")
    else:
        st.write("Please fill in all the fields to calculate the cost per unit.")
