
import streamlit as st
import pandas as pd
import uuid
from datetime import datetime

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IBeX",
    page_icon="🟣",
    layout="wide"
)

# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #F7F2FF 0%, #FFFFFF 45%);
}

.main-title {
    font-size: 52px;
    font-weight: 800;
    color: #5B2C83;
    margin-bottom: 0px;
}

.tagline {
    font-size: 20px;
    color: #6B5B7B;
    margin-bottom: 25px;
}

.hero {
    background: linear-gradient(135deg, #5B2C83, #8E5BB7);
    padding: 32px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 3px 14px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.verified {
    color: #1F8A4C;
    font-weight: 600;
}

.price {
    font-size: 23px;
    font-weight: 700;
    color: #5B2C83;
}

.small-muted {
    color: #777;
    font-size: 14px;
}

.secure-box {
    background: #EFFAF3;
    border-left: 5px solid #2E8B57;
    padding: 15px;
    border-radius: 10px;
}

.reward-box {
    background: #FFF7E6;
    border-left: 5px solid #E3A008;
    padding: 15px;
    border-radius: 10px;
}

div.stButton > button {
    background-color: #6A359C;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #51247A;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "nav" not in st.session_state:
    st.session_state.nav = "🏠 Home"

if "selected_item" not in st.session_state:
    st.session_state.selected_item = None

if "orders" not in st.session_state:
    st.session_state.orders = []

if "points" not in st.session_state:
    st.session_state.points = 245

if "custom_listings" not in st.session_state:
    st.session_state.custom_listings = []

if "help_requests" not in st.session_state:
    st.session_state.help_requests = []


# ============================================================
# SAMPLE MARKETPLACE DATA
# ============================================================

marketplace_data = [

    {
        "id": "L001",
        "item": "Scientific Calculator",
        "category": "Academic",
        "type": "Buy",
        "price": 500,
        "deposit": 0,
        "condition": "Excellent",
        "rating": 4.8,
        "seller": "IBX Student 104",
        "location": "Hostel Block A",
        "transactions": 18
    },

    {
        "id": "L002",
        "item": "Black Formal Heels",
        "category": "Fashion",
        "type": "Rent",
        "price": 50,
        "deposit": 300,
        "condition": "Good",
        "rating": 4.7,
        "seller": "IBX Student 218",
        "location": "Hostel Block B",
        "transactions": 12
    },

    {
        "id": "L003",
        "item": "Hair Dryer",
        "category": "Personal Care",
        "type": "Rent",
        "price": 30,
        "deposit": 200,
        "condition": "Excellent",
        "rating": 4.9,
        "seller": "IBX Student 302",
        "location": "Hostel Block A",
        "transactions": 24
    },

    {
        "id": "L004",
        "item": "Electric Iron",
        "category": "Hostel Utility",
        "type": "Rent",
        "price": 20,
        "deposit": 150,
        "condition": "Good",
        "rating": 4.6,
        "seller": "IBX Student 187",
        "location": "Hostel Block C",
        "transactions": 10
    },

    {
        "id": "L005",
        "item": "Ethnic Kurta Set",
        "category": "Fashion",
        "type": "Rent",
        "price": 100,
        "deposit": 500,
        "condition": "Excellent",
        "rating": 4.9,
        "seller": "IBX Student 411",
        "location": "Hostel Block B",
        "transactions": 20
    },

    {
        "id": "L006",
        "item": "Extension Board",
        "category": "Electronics",
        "type": "Buy",
        "price": 300,
        "deposit": 0,
        "condition": "Good",
        "rating": 4.5,
        "seller": "IBX Student 096",
        "location": "Hostel Block A",
        "transactions": 8
    },

    {
        "id": "L007",
        "item": "Sports Shoes",
        "category": "Sports",
        "type": "Buy",
        "price": 800,
        "deposit": 0,
        "condition": "Good",
        "rating": 4.8,
        "seller": "IBX Student 355",
        "location": "Hostel Block C",
        "transactions": 15
    },

    {
        "id": "L008",
        "item": "Tripod",
        "category": "Electronics",
        "type": "Rent",
        "price": 40,
        "deposit": 300,
        "condition": "Good",
        "rating": 4.7,
        "seller": "IBX Student 274",
        "location": "Hostel Block A",
        "transactions": 16
    }

]

# Add user-created prototype listings
marketplace_data.extend(st.session_state.custom_listings)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("## 🟣 IBeX")
st.sidebar.caption("IBS Exchange")

pages = [
    "🏠 Home",
    "🛍️ Marketplace",
    "➕ List an Item",
    "🛒 Checkout",
    "📦 My Orders",
    "🚚 Delivery & Help",
    "🏥 Essential Assistance",
    "⭐ Rewards",
    "👤 Profile"
]

st.sidebar.radio(
    "Navigate",
    pages,
    key="nav"
)

st.sidebar.markdown("---")
st.sidebar.metric("⭐ Your IBeX Points", st.session_state.points)

st.sidebar.caption(
    "🔐 Verified IBS-only community"
)


# ============================================================
# HOME
# ============================================================

if st.session_state.nav == "🏠 Home":

    st.markdown('<div class="main-title">IBeX</div>',
                unsafe_allow_html=True)

    st.markdown(
        '<div class="tagline">'
        'Rent • Buy • Sell • Lend • Deliver • Help'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="hero">
        <h2>Everything you need. Within your campus.</h2>
        <p>
        A trusted IBS-only platform where students can access
        products, earn from unused items, help each other and
        make campus life easier.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🛍️ Available Items", len(marketplace_data))
    col2.metric("⭐ Your Points", st.session_state.points)
    col3.metric("📦 Your Orders", len(st.session_state.orders))
    col4.metric("✅ Verified Community", "IBS Only")

    st.markdown("---")

    st.subheader("What can you do on IBeX?")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
        <h3>🔄 Rent</h3>
        <p>Need something only for a day or event?
        Rent it instead of buying it.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="card">
        <h3>🛍️ Buy Second-Hand</h3>
        <p>Buy useful products from verified IBS students
        at affordable prices.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
        <h3>💰 Sell or Lend</h3>
        <p>Turn unused products into money instead of
        letting them sit unused.</p>
        </div>
        """, unsafe_allow_html=True)

    d, e, f = st.columns(3)

    with d:
        st.markdown("""
        <div class="card">
        <h3>🚚 Campus Delivery</h3>
        <p>Get parcels or items picked up when you're
        busy or unavailable.</p>
        </div>
        """, unsafe_allow_html=True)

    with e:
        st.markdown("""
        <div class="card">
        <h3>🏥 Essential Help</h3>
        <p>Request urgent basic necessities from the
        campus community.</p>
        </div>
        """, unsafe_allow_html=True)

    with f:
        st.markdown("""
        <div class="card">
        <h3>⭐ Earn Rewards</h3>
        <p>Help other students and earn IBeX points
        that can later unlock benefits.</p>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# MARKETPLACE
# ============================================================

elif st.session_state.nav == "🛍️ Marketplace":

    st.title("🛍️ Marketplace")

    st.caption(
        "Browse products listed by verified IBS students."
    )

    search = st.text_input(
        "🔍 Search",
        placeholder="Search calculator, dress, iron, charger..."
    )

    col1, col2 = st.columns(2)

    categories = sorted(
        list(set([x["category"] for x in marketplace_data]))
    )

    with col1:
        category_filter = st.selectbox(
            "Category",
            ["All"] + categories
        )

    with col2:
        type_filter = st.selectbox(
            "Looking to",
            ["All", "Buy", "Rent"]
        )

    filtered = marketplace_data

    if search:
        filtered = [
            item for item in filtered
            if search.lower() in item["item"].lower()
        ]

    if category_filter != "All":
        filtered = [
            item for item in filtered
            if item["category"] == category_filter
        ]

    if type_filter != "All":
        filtered = [
            item for item in filtered
            if item["type"] == type_filter
        ]

    st.markdown("---")

    if len(filtered) == 0:
        st.warning("No matching listings found.")

    for item in filtered:

        with st.container():

            colA, colB, colC = st.columns([4, 2, 1.5])

            with colA:

                st.markdown(
                    f"### {item['item']}"
                )

                st.markdown(
                    f"🟢 **{item['type']}** &nbsp;&nbsp; | &nbsp;&nbsp;"
                    f"{item['category']}"
                )

                st.write(
                    f"Condition: **{item['condition']}**"
                )

                st.write(
                    f"📍 {item['location']}"
                )

                st.markdown(
                    f"<span class='verified'>"
                    f"✓ Verified IBS Student</span>",
                    unsafe_allow_html=True
                )

                st.caption(
                    f"⭐ {item['rating']} rating • "
                    f"{item['transactions']} successful transactions"
                )

            with colB:

                if item["type"] == "Rent":

                    st.markdown(
                        f"<div class='price'>₹{item['price']}/day</div>",
                        unsafe_allow_html=True
                    )

                    st.caption(
                        f"Refundable deposit: ₹{item['deposit']}"
                    )

                else:

                    st.markdown(
                        f"<div class='price'>₹{item['price']}</div>",
                        unsafe_allow_html=True
                    )

            with colC:

                button_text = (
                    "Rent Now"
                    if item["type"] == "Rent"
                    else "Buy Now"
                )

                if st.button(
                    button_text,
                    key=f"select_{item['id']}"
                ):

                    st.session_state.selected_item = item
                    st.session_state.nav = "🛒 Checkout"
                    st.rerun()

            st.markdown("---")


# ============================================================
# LIST ITEM
# ============================================================

elif st.session_state.nav == "➕ List an Item":

    st.title("➕ List an Item")

    st.write(
        "Earn from items you no longer use or lend them "
        "to another IBS student."
    )

    st.info(
        "🎁 IBeX Freemium: first 5 listings are free. "
        "Additional listings may require a listing plan or subscription."
    )

    item_name = st.text_input("Item Name")

    category = st.selectbox(
        "Category",
        [
            "Academic",
            "Fashion",
            "Electronics",
            "Hostel Utility",
            "Personal Care",
            "Sports",
            "Bags",
            "Other"
        ]
    )

    listing_type = st.radio(
        "I want to",
        ["Sell", "Lend / Rent"]
    )

    condition = st.selectbox(
        "Condition",
        ["Excellent", "Good", "Fair"]
    )

    price = st.number_input(
        "Selling Price / Rental Fee per Day (₹)",
        min_value=0,
        value=50
    )

    deposit = 0

    if listing_type == "Lend / Rent":

        deposit = st.number_input(
            "Refundable Security Deposit (₹)",
            min_value=0,
            value=200
        )

    location = st.selectbox(
        "Location",
        [
            "Hostel Block A",
            "Hostel Block B",
            "Hostel Block C",
            "Hostel Block D"
        ]
    )

    st.text_area(
        "Description",
        placeholder="Add details about size, usage, accessories, etc."
    )

    if st.button("Publish Listing"):

        if item_name.strip() == "":
            st.warning("Please enter the item name.")

        else:

            new_listing = {
                "id": "L" + str(
                    1000 + len(st.session_state.custom_listings)
                ),
                "item": item_name,
                "category": category,
                "type": (
                    "Rent"
                    if listing_type == "Lend / Rent"
                    else "Buy"
                ),
                "price": price,
                "deposit": deposit,
                "condition": condition,
                "rating": 5.0,
                "seller": "You",
                "location": location,
                "transactions": 0
            }

            st.session_state.custom_listings.append(new_listing)

            st.success(
                f"✅ {item_name} has been listed successfully!"
            )

            st.balloons()


# ============================================================
# CHECKOUT
# ============================================================

elif st.session_state.nav == "🛒 Checkout":

    st.title("🛒 Secure Checkout")

    item = st.session_state.selected_item

    if item is None:

        st.warning(
            "You haven't selected an item yet."
        )

        if st.button("Go to Marketplace"):
            st.session_state.nav = "🛍️ Marketplace"
            st.rerun()

    else:

        st.subheader(item["item"])

        st.markdown(
            f"<span class='verified'>"
            f"✓ Verified IBS Seller</span>",
            unsafe_allow_html=True
        )

        days = 1

        if item["type"] == "Rent":

            days = st.number_input(
                "Rental Duration (Days)",
                min_value=1,
                max_value=30,
                value=1
            )

            base_price = item["price"] * days

        else:

            base_price = item["price"]

        delivery_option = st.radio(
            "Delivery Option",
            [
                "Self Pickup — FREE",
                "IBeX Campus Delivery — ₹20"
            ]
        )

        delivery_fee = (
            20
            if "₹20" in delivery_option
            else 0
        )

        deposit = (
            item["deposit"]
            if item["type"] == "Rent"
            else 0
        )

        total = (
            base_price
            + delivery_fee
            + deposit
        )

        st.markdown("---")

        st.subheader("Order Summary")

        c1, c2 = st.columns(2)

        with c1:
            st.write("Item / Rental Charge")
            st.write("Delivery")
            if item["type"] == "Rent":
                st.write("Refundable Security Deposit")

        with c2:
            st.write(f"₹{base_price}")
            st.write(f"₹{delivery_fee}")
            if item["type"] == "Rent":
                st.write(f"₹{deposit}")

        st.markdown("---")

        st.markdown(
            f"## Total Payable: ₹{total}"
        )

        if item["type"] == "Rent":

            st.success(
                f"₹{deposit} is a refundable security deposit "
                "and is returned after successful item return."
            )

        st.markdown("---")

        st.subheader("Payment Method")

        payment_method = st.radio(
            "Choose how you want to pay",
            [
                "📱 UPI / GPay / PhonePe",
                "💳 Card",
                "💵 Cash on Delivery"
            ]
        )

        if "UPI" in payment_method:

            st.markdown("""
            <div class="secure-box">
            🔐 <b>Secure UPI Payment</b><br>
            Payment would be processed through an authorised payment
            gateway. Your UPI details are not shared with the seller.
            </div>
            """, unsafe_allow_html=True)

            st.text_input(
                "UPI ID",
                placeholder="example@upi",
                type="password"
            )

            st.caption(
                "Prototype mode — no real payment will be deducted."
            )

        elif "Card" in payment_method:

            st.markdown("""
            <div class="secure-box">
            🔐 <b>Secure Card Payment</b><br>
            Card information would be handled directly by the
            payment gateway and is never visible to another IBeX user.
            </div>
            """, unsafe_allow_html=True)

            st.text_input(
                "Card Number",
                placeholder="•••• •••• •••• ••••",
                type="password"
            )

            c1, c2 = st.columns(2)

            with c1:
                st.text_input(
                    "Expiry",
                    placeholder="MM/YY"
                )

            with c2:
                st.text_input(
                    "CVV",
                    type="password"
                )

            st.caption(
                "Prototype mode — card details are not processed or stored."
            )

        else:

            st.markdown("""
            <div class="secure-box">
            💵 <b>Cash on Delivery</b><br>
            Pay when the product is handed over to you.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        button_label = (
            "Confirm Cash on Delivery"
            if "Cash" in payment_method
            else f"Pay ₹{total}"
        )

        if st.button(button_label):

            order_id = (
                "IBX-" +
                datetime.now().strftime("%y%m%d") +
                "-" +
                str(uuid.uuid4())[:6].upper()
            )

            payment_status = (
                "Cash on Delivery"
                if "Cash" in payment_method
                else "Test Payment Successful"
            )

            order = {
                "Order ID": order_id,
                "Item": item["item"],
                "Type": item["type"],
                "Amount": total,
                "Payment": payment_status,
                "Delivery": delivery_option,
                "Status": "Confirmed"
            }

            st.session_state.orders.append(order)

            st.session_state.points += 10

            st.success("✅ Order Confirmed!")

            st.balloons()

            st.markdown(
                f"### Order ID: `{order_id}`"
            )

            st.write(
                f"**Payment:** {payment_status}"
            )

            st.write(
                f"**Amount:** ₹{total}"
            )

            st.info(
                "⭐ You earned 10 IBeX points for this transaction!"
            )


# ============================================================
# MY ORDERS
# ============================================================

elif st.session_state.nav == "📦 My Orders":

    st.title("📦 My Orders")

    if len(st.session_state.orders) == 0:

        st.info(
            "You haven't placed any orders yet."
        )

    else:

        orders_df = pd.DataFrame(
            st.session_state.orders
        )

        st.dataframe(
            orders_df,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# DELIVERY & HELP
# ============================================================

elif st.session_state.nav == "🚚 Delivery & Help":

    st.title("🚚 IBeX Help & Delivery")

    st.write(
        "Busy in class? Need something brought from the main gate? "
        "Ask another IBS student."
    )

    tab1, tab2 = st.tabs(
        ["Request Help", "Available Tasks"]
    )

    with tab1:

        request_type = st.selectbox(
            "Request",
            [
                "Parcel Pickup",
                "Item Pickup",
                "Document Delivery",
                "Food / Snack Pickup",
                "Other Assistance"
            ]
        )

        pickup = st.text_input(
            "Pickup Location",
            placeholder="Main Gate"
        )

        drop = st.text_input(
            "Delivery Location",
            placeholder="Hostel Block B"
        )

        fee = st.number_input(
            "Reward for Helper (₹)",
            min_value=10,
            max_value=200,
            value=20
        )

        if st.button("Post Request"):

            if not pickup or not drop:

                st.warning(
                    "Enter both pickup and delivery locations."
                )

            else:

                request = {
                    "Task": request_type,
                    "Pickup": pickup,
                    "Drop": drop,
                    "Reward": fee,
                    "Status": "Open"
                }

                st.session_state.help_requests.append(request)

                st.success(
                    "✅ Your request has been posted."
                )

    with tab2:

        sample_tasks = [
            {
                "Task": "Parcel Pickup",
                "Pickup": "Main Gate",
                "Drop": "Hostel Block A",
                "Reward": 20,
                "Status": "Open"
            },
            {
                "Task": "Snack Pickup",
                "Pickup": "Campus Store",
                "Drop": "Hostel Block C",
                "Reward": 15,
                "Status": "Open"
            }
        ]

        all_tasks = (
            sample_tasks
            + st.session_state.help_requests
        )

        for i, task in enumerate(all_tasks):

            st.markdown(
                f"### {task['Task']}"
            )

            st.write(
                f"📍 {task['Pickup']} → {task['Drop']}"
            )

            st.write(
                f"💰 Reward: ₹{task['Reward']}"
            )

            if st.button(
                "Accept Task",
                key=f"task_{i}"
            ):

                st.session_state.points += 30

                st.success(
                    "✅ Task accepted! Complete it to earn your reward."
                )

                st.info(
                    "⭐ 30 IBeX points added in prototype mode."
                )

            st.markdown("---")


# ============================================================
# ESSENTIAL ASSISTANCE
# ============================================================

elif st.session_state.nav == "🏥 Essential Assistance":

    st.title("🏥 Essential Assistance")

    st.warning(
        "IBeX facilitates basic assistance only. "
        "Prescription medicines or regulated medical products "
        "would require appropriate institutional and legal controls."
    )

    need = st.selectbox(
        "What do you need?",
        [
            "Sanitary products",
            "ORS / hydration supplies",
            "Bandage / basic first aid",
            "Thermometer",
            "Basic essential item",
            "Help reaching campus medical support"
        ]
    )

    urgency = st.radio(
        "Urgency",
        ["Normal", "Urgent"]
    )

    helper_reward = st.number_input(
        "Helper Reward (₹)",
        min_value=0,
        max_value=200,
        value=20
    )

    if st.button("Request Assistance"):

        st.success(
            f"✅ Request posted for {need}."
        )

        st.info(
            "Only verified IBS users can respond."
        )


# ============================================================
# REWARDS
# ============================================================

elif st.session_state.nav == "⭐ Rewards":

    st.title("⭐ IBeX Rewards")

    st.metric(
        "Your Points",
        st.session_state.points
    )

    st.markdown("""
    <div class="reward-box">
    Help the IBS community, complete transactions and return
    rented items responsibly to earn more points.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    rewards = pd.DataFrame({
        "Activity": [
            "Successful Purchase / Rental",
            "Complete Parcel Pickup",
            "Help with Essential Request",
            "Successful Lending",
            "Return Rental On Time",
            "Positive Review"
        ],
        "Points": [
            "+10",
            "+30",
            "+40",
            "+20",
            "+30",
            "+10"
        ]
    })

    st.dataframe(
        rewards,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Redeem")

    reward = st.selectbox(
        "Available Rewards",
        [
            "₹20 Delivery Discount — 500 Points",
            "1 Free Listing — 750 Points",
            "Priority Listing — 1000 Points"
        ]
    )

    if st.button("Redeem"):

        st.info(
            "Prototype demonstration: redemption would be applied "
            "to the user's IBeX account."
        )


# ============================================================
# PROFILE
# ============================================================

elif st.session_state.nav == "👤 Profile":

    st.title("👤 My IBeX Profile")

    st.markdown("""
    <div class="card">
    <h3>IBX Student 001</h3>
    <p class="verified">✓ IBS Verified Profile</p>
    <p>⭐ 4.8 User Rating</p>
    <p>🔄 16 Successful Transactions</p>
    <p>🏆 Trusted Community Member</p>
    </div>
    """, unsafe_allow_html=True)

    st.metric(
        "IBeX Points",
        st.session_state.points
    )

    st.subheader("Privacy & Trust")

    st.write("✓ IBS-only verified access")
    st.write("✓ Masked user identity before transaction")
    st.write("✓ Ratings and reviews")
    st.write("✓ OTP-based handover verification")
    st.write("✓ Refundable rental security deposit")
    st.write("✓ Payment details are never shown to another user")


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "IBeX — IBS Exchange | Customer-facing prototype | "
    "Secure • Sustainable • Community Driven"
)
