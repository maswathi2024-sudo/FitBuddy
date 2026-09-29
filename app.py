import streamlit as st

st.set_page_config(page_title="FitBuddy")

st.title("FitBuddy 💪 - Unoda Gym Partner")
st.write("Vanakkam! Unoda fitness goal enna?")

goal = st.selectbox("Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
weight = st.number_input("Weight (kg)", value=60)
height = st.number_input("Height (cm)", value=170)

if st.button("Enakku Plan Kudu 🚀"):
    st.success(f"Super! {goal} ku plan ready!")
    st.write(f"Weight: {weight}kg, Height: {height}cm")
    st.write("---")
    st.write("**Day 1:** Walking 30min + Pushups 15")
    st.write("**Day 2:** Squats 20 + Less Oil Food")
    st.write("**Day 3:** Rest + Water 3L")
    st.balloons()
