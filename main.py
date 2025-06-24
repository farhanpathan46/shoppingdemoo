import streamlit as st
import pandas as pd

st.set_page_config(page_title="Best Online Shop", layout="wide", page_icon="🛍️")

products = pd.DataFrame([
    {"id": 1, "name": "Wireless Earbuds", "price":499, "offer": "20% OFF", "image": "🎧"},
    {"id": 2, "name": "Smartwatch", "price": 5099 ,"offer": "10% OFF", "image": "⌚"},
    {"id": 3, "name": "Portable Speaker", "price": 5999, "offer": "BEST SELLER", "image": "🔊"},
    {"id": 4, "name": "Gaming Keyboard", "price": 7999, "offer": "15% OFF", "image": "⌨️"},
])

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "page" not in st.session_state:
    st.session_state.page = "home"

def add_to_cart(pid):
    if pid in st.session_state.cart:
        st.session_state.cart[pid] += 1
    else:
        st.session_state.cart[pid] = 1
    st.success("🛒 Added to Cart!")

with st.sidebar:
    st.markdown("## 🔗 Navigation")
    if st.button("🏠 Home"):
        st.session_state.page = "home"
    if st.button("🛍️ Products"):
        st.session_state.page = "products"
    if st.button("🛒 View Cart"):
        st.session_state.page = "cart"

st.markdown("<h1 style='color: #ff4b4b;'>🛍️ Best Price Online Shopping</h1>", unsafe_allow_html=True)
st.markdown("### 💸 Shop smart. Shop with us.")

if st.session_state.page == "home":
    st.image("https://cdn.pixabay.com/photo/2017/08/06/04/49/shopping-2581454_1280.jpg", use_column_width=True)
    st.markdown("## 🔥 Today's Top Deals")
    for _, row in products.iterrows():
        st.markdown(f"- **{row['image']} {row['name']}** - ${row['price']}  _( {row['offer']} )_")

elif st.session_state.page == "products":
    st.markdown("## 🛒 Available Products")
    for _, row in products.iterrows():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {row['image']} {row['name']}")
            st.markdown(f"💲 **${row['price']}**")
            st.markdown(f"🔖 _{row['offer']}_")
        with col2:
            st.button(f"Add to Cart - {row['id']}", key=f"add_{row['id']}", on_click=add_to_cart, args=(row['id'],))

elif st.session_state.page == "cart":
    st.markdown("## 🛒 Your Cart")
    total = 0
    if not st.session_state.cart:
        st.warning("Your cart is empty.")
    else:
        for pid, qty in st.session_state.cart.items():
            product = products.loc[products['id'] == pid].iloc[0]
            subtotal = product['price'] * qty
            total += subtotal
            st.markdown(f"- **{product['name']}** x {qty} = ${subtotal:.2f}")
        st.markdown(f"### 🧾 Total: **${total:.2f}**")

        st.markdown("---")
        st.markdown("### 💳 Enter Payment Details")

        name = st.text_input("Cardholder Name")
        card = st.text_input("Card Number", type="password")
        exp = st.text_input("Expiry Date (MM/YY)")
        cvv = st.text_input("CVV", type="password")

        if st.button("Confirm & Pay"):
            if not all([name, card, exp, cvv]):
                st.error("Please complete all payment fields.")
            else:
                st.success("✅ Payment Successful! Order placed.")
                st.session_state.cart = {}

