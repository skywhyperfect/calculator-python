import streamlit as st

st.set_page_config(page_title="Калькулятор", page_icon="🧮")

st.title("🧮 Крутой калькулятор")
st.write("Сделано на Python + Streamlit 😎")

a = st.number_input("Первое число", value=0.0)
b = st.number_input("Второе число", value=0.0)

op = st.selectbox("Операция", ["+", "-", "*", "/", "**", "%"])

if st.button("Вычислить"):
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            st.error("На ноль делить нельзя 🚫")
            result = None
        else:
            result = a / b
    elif op == "**":
        result = a ** b
    elif op == "%":
        result = a % b

    if result is not None:
        st.success(f"Ответ: {result}")