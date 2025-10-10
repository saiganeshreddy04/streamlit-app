import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Petrol Pump Billing System",
    page_icon="⛽",
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #2E7D32;
    text-align: center;
    margin-bottom: 2rem;
}
.fuel-card {
    background-color: #E8F5E8;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #4CAF50;
    margin: 1rem 0;
}
.receipt-box {
    background-color: #FFF3E0;
    padding: 1.5rem;
    border-radius: 10px;
    border: 2px solid #FF9800;
    margin: 1rem 0;
}
.total-payable {
    font-size: 1.5rem;
    font-weight: bold;
    color: #D32F2F;
    text-align: center;
}
.history-table {
    background-color: #F1F8E9;
    border-radius: 10px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# Fuel dictionary
fuels = {
    "Petrol": 110,
    "Diesel": 95
}

# Functions
def show_fuels():
    st.subheader("🛢️ Available Fuels")
    st.markdown('<div class="fuel-card">', unsafe_allow_html=True)
    for fuel, price in fuels.items():
        st.write(f"**{fuel}** → ₹{price} per litre")
    st.markdown('</div>', unsafe_allow_html=True)

def calculate_bill(fuel_type, litres):
    price = fuels.get(fuel_type, None)
    if price is None or litres <= 0 or litres > 100:
        return None, None, None
    subtotal = litres * price
    discount = 200 if litres > 50 else 0
    total = subtotal - discount
    return subtotal, discount, total

# Transaction history in memory
if 'transactions' not in st.session_state:
    st.session_state.transactions = pd.DataFrame(columns=[
        'Fuel Type', 'Litres', 'Price per Litre', 'Subtotal', 'Discount', 'Total Paid'
    ])

# Main app
st.markdown('<h1 class="main-header">⛽ Petrol Pump Billing System</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar instructions
with st.sidebar:
    st.header("📋 Instructions")
    st.write("""
    1. Select fuel type.
    2. Enter litres (1-100).
    3. Click 'Calculate Bill' to generate receipt.
    4. Discount: ₹200 for >50 litres.
    """)
    st.markdown("---")
    if st.button("Clear Transaction History"):
        st.session_state.transactions = pd.DataFrame(columns=[
            'Fuel Type', 'Litres', 'Price per Litre', 'Subtotal', 'Discount', 'Total Paid'
        ])
        st.success("✅ Transaction history cleared!")

# Layout columns
col1, col2 = st.columns([1, 1])

with col1:
    show_fuels()

with col2:
    st.subheader("💳 Billing")
    fuel_type = st.selectbox("Select Fuel Type:", options=list(fuels.keys()))
    litres = st.number_input(
        "Enter Litres (1-100):", min_value=0.01, max_value=100.0, value=10.0, step=0.5, format="%.2f"
    )

    if st.button("Calculate Bill", type="primary"):
        subtotal, discount, total = calculate_bill(fuel_type, litres)
        if subtotal is not None:
            # Store transaction
            new_row = pd.DataFrame([{
                'Fuel Type': fuel_type,
                'Litres': litres,
                'Price per Litre': fuels[fuel_type],
                'Subtotal': subtotal,
                'Discount': discount,
                'Total Paid': total
            }])
            st.session_state.transactions = pd.concat([new_row, st.session_state.transactions], ignore_index=True)

            # Show receipt
            st.markdown('<div class="receipt-box">', unsafe_allow_html=True)
            st.markdown("### 📄 Receipt")
            st.write(f"**Fuel Type:** {fuel_type}")
            st.write(f"**Litres:** {litres:.2f} L")
            st.write(f"**Price per Litre:** ₹{fuels[fuel_type]:.2f}")
            st.write(f"**Subtotal:** ₹{subtotal:.2f}")
            st.write(f"**Discount:** ₹{discount:.2f}")
            st.markdown(f'<p class="total-payable">**Total Payable: ₹{total:.2f}**</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.error("❌ Invalid input. Litres must be >0 and ≤100.")

# Transaction History
st.markdown("---")
st.subheader("📊 Transaction History")
if not st.session_state.transactions.empty:
    st.markdown('<div class="history-table">', unsafe_allow_html=True)
    st.dataframe(st.session_state.transactions, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.info(f"Total Transactions: {len(st.session_state.transactions)}")
else:
    st.info("No transactions yet. Start billing to see history here.")

# Footer
st.markdown("---")
st.markdown("*Thank you for visiting our Petrol Pump! 🚗💨*")
