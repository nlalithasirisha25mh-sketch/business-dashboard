
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="IBeX - IBS Exchange",
    page_icon="🔄",
    layout="wide"
)

# ============================================================
# APP TITLE
# ============================================================

st.title("🔄 IBeX")
st.markdown("### **One IBS Community. Buy • Sell • Rent • Lend • Help.**")
st.markdown(
    "IBeX is a verified IBS-only peer-to-peer platform for "
    "second-hand products, rentals, lending, campus assistance and delivery."
)

st.markdown("---")


# ============================================================
# SAMPLE MARKETPLACE DATA
# ============================================================
# These are DEMONSTRATION records used to show how the
# prototype would work after IBeX is launched.

marketplace_data = {
    "Listing ID": [
        "L001", "L002", "L003", "L004", "L005",
        "L006", "L007", "L008", "L009", "L010"
    ],
    "Item": [
        "Scientific Calculator",
        "Black Formal Heels",
        "Hair Dryer",
        "Iron",
        "Ethnic Kurta Set",
        "Extension Board",
        "Sports Shoes",
        "Backpack",
        "Tripod",
        "Study Table"
    ],
    "Category": [
        "Academic",
        "Fashion",
        "Personal Care",
        "Hostel Utility",
        "Fashion",
        "Electronics",
        "Sports",
        "Bags",
        "Electronics",
        "Hostel Utility"
    ],
    "Type": [
        "Sell", "Rent", "Rent", "Lend", "Rent",
        "Sell", "Sell", "Lend", "Rent", "Sell"
    ],
    "Price": [
        500, 50, 30, 20, 100,
        300, 800, 25, 40, 1200
    ],
    "Security Deposit": [
        0, 300, 200, 150, 500,
        0, 0, 150, 300, 0
    ],
    "Condition": [
        "Excellent", "Good", "Excellent", "Good", "Excellent",
        "Good", "Good", "Excellent", "Good", "Good"
    ],
    "Block": [
        "Block A", "Block B", "Block A", "Block C", "Block B",
        "Block A", "Block C", "Block B", "Block A", "Block C"
    ],
    "Status": [
        "Available", "Available", "Available", "Available", "Available",
        "Available", "Available", "Available", "Available", "Available"
    ]
}

marketplace_df = pd.DataFrame(marketplace_data)


# ============================================================
# SAMPLE DELIVERY / HELP DATA
# ============================================================

service_data = {
    "Request ID": ["R001", "R002", "R003", "R004", "R005"],
    "Request Type": [
        "Parcel Pickup",
        "Essential Pickup",
        "Parcel Pickup",
        "Document Delivery",
        "Medical Assistance"
    ],
    "Pickup": [
        "Main Gate",
        "Nearby Pharmacy",
        "Main Gate",
        "Admin Block",
        "Pharmacy"
    ],
    "Drop": [
        "Block A",
        "Block B",
        "Block C",
        "Block A",
        "Block B"
    ],
    "Reward": [20, 30, 15, 15, 30],
    "Points": [30, 40, 25, 25, 40],
    "Status": ["Open", "Open", "Completed", "Completed", "Open"]
}

service_df = pd.DataFrame(service_data)


# ============================================================
# SAMPLE TRANSACTION DATA
# ============================================================

transaction_data = {
    "Transaction ID": [
        "T001", "T002", "T003", "T004", "T005",
        "T006", "T007", "T008", "T009", "T010"
    ],
    "Type": [
        "Sell", "Rent", "Lend", "Sell", "Rent",
        "Sell", "Rent", "Lend", "Sell", "Rent"
    ],
    "Item": [
        "Calculator", "Hair Dryer", "Iron", "Extension Board",
        "Formal Heels", "Sports Shoes", "Tripod", "Backpack",
        "Study Table", "Ethnic Wear"
    ],
    "Amount": [
        500, 30, 40, 300, 50,
        800, 80, 50, 1200, 100
    ],
    "Delivery Fee": [
        0, 20, 0, 20, 20,
        0, 20, 0, 20, 20
    ],
    "Commission": [
        25, 2, 2, 15, 3,
        40, 4, 3, 60, 5
    ],
    "Status": [
        "Completed", "Completed", "Completed", "Completed", "Completed",
        "Completed", "Completed", "Completed", "Completed", "Completed"
    ]
}

transactions_df = pd.DataFrame(transaction_data)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("IBeX")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "🛍️ Marketplace",
        "🚚 Delivery & Help",
        "🏥 Medical Assistance",
        "⭐ Points & Rewards",
        "📊 Customer Insights",
        "💰 Platform Economics"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.header("🏠 IBeX Dashboard")

    st.info(
        "Prototype demonstration using illustrative marketplace data "
        "and real customer-discovery survey responses."
    )

    # KPIs
    total_listings = len(marketplace_df)
    completed_transactions = len(transactions_df)
    gmv = transactions_df["Amount"].sum()
    revenue = transactions_df["Commission"].sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Active Listings", total_listings)
    col2.metric("Completed Transactions", completed_transactions)
    col3.metric("Transaction Value", f"₹{gmv:,.0f}")
    col4.metric("Commission Revenue", f"₹{revenue:,.0f}")

    st.markdown("---")

    col5, col6, col7, col8 = st.columns(4)

    col5.metric("Delivery Requests", len(service_df))
    col6.metric("Open Requests",
                len(service_df[service_df["Status"] == "Open"]))
    col7.metric("Available Items",
                len(marketplace_df[marketplace_df["Status"] == "Available"]))
    col8.metric("Avg. Transaction",
                f"₹{transactions_df['Amount'].mean():,.0f}")

    st.markdown("---")

    st.subheader("Platform Activity")

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**Marketplace Activity by Type**")

        type_counts = marketplace_df["Type"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(type_counts.index, type_counts.values)
        ax.set_ylabel("Number of Listings")
        ax.set_xlabel("Transaction Type")
        plt.xticks(rotation=30)
        plt.tight_layout()
        st.pyplot(fig)

    with col_b:
        st.markdown("**Listings by Category**")

        category_counts = marketplace_df["Category"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(category_counts.index, category_counts.values)
        ax.set_ylabel("Number of Listings")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

    st.markdown("---")

    st.subheader("♻️ IBeX Value Creation")

    c1, c2, c3 = st.columns(3)

    c1.metric("Items Available for Reuse", total_listings)
    c2.metric("Rental / Lending Listings",
              len(marketplace_df[
                  marketplace_df["Type"].isin(["Rent", "Lend"])
              ]))
    c3.metric("Second-Hand Listings",
              len(marketplace_df[
                  marketplace_df["Type"].isin(["Sell"])
              ]))

    st.caption(
        "All marketplace figures shown above are illustrative prototype data."
    )


# ============================================================
# MARKETPLACE
# ============================================================

elif page == "🛍️ Marketplace":

    st.header("🛍️ IBeX Marketplace")

    st.write(
        "Find items to buy, rent or borrow — or list products you no longer use."
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_type = st.selectbox(
            "Transaction Type",
            ["All", "Sell", "Rent", "Lend"]
        )

    with col2:
        selected_category = st.selectbox(
            "Category",
            ["All"] + sorted(marketplace_df["Category"].unique().tolist())
        )

    filtered_df = marketplace_df.copy()

    if selected_type != "All":
        filtered_df = filtered_df[
            filtered_df["Type"] == selected_type
        ]

    if selected_category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_category
        ]

    st.markdown("---")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("➕ Create a Listing")

    col1, col2 = st.columns(2)

    with col1:
        item_name = st.text_input("Item Name")
        item_category = st.selectbox(
            "Item Category",
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
        listing_type = st.selectbox(
            "Listing Type",
            ["Sell", "Rent", "Lend"]
        )

    with col2:
        price = st.number_input(
            "Price / Rental Fee (₹)",
            min_value=0,
            value=20
        )

        if listing_type in ["Rent", "Lend"]:
            deposit = st.number_input(
                "Refundable Security Deposit (₹)",
                min_value=0,
                value=100
            )
        else:
            deposit = 0

        block = st.selectbox(
            "Hostel Block",
            ["Block A", "Block B", "Block C", "Block D"]
        )

    if st.button("List Item on IBeX"):

        if item_name.strip() == "":
            st.warning("Please enter an item name.")

        else:
            st.success(
                f"✅ {item_name} has been listed successfully on IBeX!"
            )

            if listing_type in ["Rent", "Lend"]:
                st.write(
                    f"Rental/Lending Fee: ₹{price} | "
                    f"Refundable Deposit: ₹{deposit}"
                )


# ============================================================
# DELIVERY & HELP
# ============================================================

elif page == "🚚 Delivery & Help":

    st.header("🚚 Delivery & Campus Assistance")

    st.write(
        "Request or provide small-scale assistance within the IBS community."
    )

    st.subheader("Available Requests")

    st.dataframe(
        service_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("📦 Request Assistance")

    request_type = st.selectbox(
        "Request Type",
        [
            "Parcel Pickup",
            "Essential Pickup",
            "Document Delivery",
            "Other Help"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        pickup = st.text_input(
            "Pickup Location",
            placeholder="e.g., Main Gate"
        )

    with col2:
        drop = st.text_input(
            "Drop Location",
            placeholder="e.g., Block B"
        )

    reward = st.number_input(
        "Reward Offered (₹)",
        min_value=10,
        max_value=200,
        value=20
    )

    if st.button("Post Assistance Request"):

        if pickup.strip() == "" or drop.strip() == "":
            st.warning("Please enter pickup and drop locations.")

        else:
            st.success("✅ Assistance request posted!")
            st.write(
                f"Reward offered: ₹{reward}. "
                "A verified IBS student can accept the request."
            )

    st.markdown("---")

    st.subheader("💡 How It Works")

    c1, c2, c3 = st.columns(3)

    c1.write("**1️⃣ Post Request**")
    c1.write("Tell the community what assistance you need.")

    c2.write("**2️⃣ Student Accepts**")
    c2.write("A verified IBS student accepts the task.")

    c3.write("**3️⃣ Complete & Earn**")
    c3.write("Complete the task and earn money + IBeX points.")


# ============================================================
# MEDICAL ASSISTANCE
# ============================================================

elif page == "🏥 Medical Assistance":

    st.header("🏥 Medical Assistance")

    st.info(
        "This prototype focuses on basic assistance and non-prescription "
        "essential products. Regulated prescription medicines would require "
        "appropriate legal and institutional controls."
    )

    st.subheader("Request Basic Assistance")

    assistance = st.selectbox(
        "What do you need?",
        [
            "First-aid supplies",
            "ORS / hydration supplies",
            "Thermometer",
            "Sanitary products",
            "Basic essential item",
            "Help reaching a medical facility"
        ]
    )

    urgency = st.selectbox(
        "Urgency",
        ["Normal", "Urgent"]
    )

    reward = st.number_input(
        "Reward for Helper (₹)",
        min_value=0,
        max_value=200,
        value=20
    )

    if st.button("Request Medical Assistance"):
        st.success(
            f"✅ Request created for: {assistance}"
        )

        st.write(
            f"Urgency: {urgency} | "
            f"Helper Reward: ₹{reward}"
        )


# ============================================================
# POINTS & REWARDS
# ============================================================

elif page == "⭐ Points & Rewards":

    st.header("⭐ IBeX Points & Rewards")

    st.write(
        "Users earn points by contributing to the IBeX community."
    )

    points = 245

    st.metric("Your IBeX Points", points)

    st.markdown("---")

    st.subheader("How You Earn Points")

    points_table = pd.DataFrame({
        "Activity": [
            "Complete parcel delivery",
            "Help with essential request",
            "Complete medical assistance",
            "Successful lending",
            "Successful rental",
            "Return rental on time"
        ],
        "Points": [
            "+30",
            "+40",
            "+40",
            "+20",
            "+20",
            "+30"
        ]
    })

    st.dataframe(
        points_table,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🎁 Redeem Points")

    reward_choice = st.selectbox(
        "Choose a reward",
        [
            "₹20 Delivery Discount — 500 points",
            "Free Listing — 750 points",
            "Priority Listing — 1,000 points"
        ]
    )

    if st.button("Redeem Reward"):
        st.info(
            "Prototype action: reward redemption would be processed "
            "through the IBeX platform."
        )


# ============================================================
# CUSTOMER INSIGHTS
# ============================================================

elif page == "📊 Customer Insights":

    st.header("📊 Customer Discovery Insights")

    st.write(
        "These insights are based on the real responses collected "
        "through the IBeX customer-discovery survey."
    )

    st.info("Current survey sample: 38 IBS respondents")

    # --------------------------------------------------------
    # Load survey data
    # --------------------------------------------------------

    try:
        survey_df = pd.read_csv("survey_responses.csv")

        st.success("Survey data loaded successfully.")

        st.subheader("Survey Response Overview")

        st.metric("Total Respondents", len(survey_df))

        st.markdown("---")

        # Q1
        q1 = survey_df.iloc[:, 1].value_counts()

        st.subheader("1. Difficulty Finding Items")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(q1.index, q1.values)
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

        # Q13
        q13 = survey_df.iloc[:, 13].value_counts()

        st.subheader("2. Perceived Usefulness of IBeX")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(q13.index, q13.values)
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

        # Q16
        q16 = survey_df.iloc[:, 16].value_counts()

        st.subheader("3. Willingness to Rent Using Security Deposit")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(q16.index, q16.values)
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

        # Q17
        q17 = survey_df.iloc[:, 17].value_counts()

        st.subheader("4. Willingness to Use Parcel Delivery")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(q17.index, q17.values)
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

        # Q18
        q18 = survey_df.iloc[:, 18].value_counts()

        st.subheader("5. Willingness to Help for IBeX Points")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(q18.index, q18.values)
        ax.set_ylabel("Number of Respondents")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        st.pyplot(fig)

        st.markdown("---")

        with st.expander("View Survey Data"):
            st.dataframe(
                survey_df,
                use_container_width=True
            )

    except FileNotFoundError:

        st.warning(
            "Survey data file not found. Please upload "
            "'survey_responses.csv' to the GitHub repository."
        )


# ============================================================
# PLATFORM ECONOMICS
# ============================================================

elif page == "💰 Platform Economics":

    st.header("💰 IBeX Platform Economics")

    st.write(
        "Illustrative economics model showing how IBeX could generate revenue."
    )

    st.markdown("---")

    # Revenue assumptions

    st.subheader("Revenue Streams")

    col1, col2, col3 = st.columns(3)

    with col1:
        subscription_price = st.number_input(
            "Monthly Subscription (₹)",
            min_value=0,
            value=199
        )

    with col2:
        commission_rate = st.number_input(
            "Transaction Commission (%)",
            min_value=0.0,
            max_value=20.0,
            value=5.0
        )

    with col3:
        delivery_commission = st.number_input(
            "Delivery Platform Fee (₹)",
            min_value=0,
            value=5
        )

    st.markdown("---")

    # Calculations

    total_transaction_value = transactions_df["Amount"].sum()

    commission_revenue = (
        total_transaction_value * commission_rate / 100
    )

    completed_deliveries = len(
        service_df[service_df["Status"] == "Completed"]
    )

    delivery_revenue = completed_deliveries * delivery_commission

    demo_subscribers = 10

    subscription_revenue = (
        demo_subscribers * subscription_price
    )

    total_revenue = (
        commission_revenue
        + delivery_revenue
        + subscription_revenue
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Transaction Value",
        f"₹{total_transaction_value:,.0f}"
    )

    c2.metric(
        "Commission Revenue",
        f"₹{commission_revenue:,.0f}"
    )

    c3.metric(
        "Delivery Revenue",
        f"₹{delivery_revenue:,.0f}"
    )

    c4.metric(
        "Subscription Revenue",
        f"₹{subscription_revenue:,.0f}"
    )

    st.markdown("---")

    st.subheader("Revenue Composition")

    revenue_df = pd.DataFrame({
        "Revenue Stream": [
            "Transaction Commission",
            "Delivery Fees",
            "Subscriptions"
        ],
        "Revenue": [
            commission_revenue,
            delivery_revenue,
            subscription_revenue
        ]
    })

    st.dataframe(
        revenue_df,
        use_container_width=True,
        hide_index=True
    )

    st.metric(
        "Illustrative Total Platform Revenue",
        f"₹{total_revenue:,.0f}"
    )

    st.caption(
        "Financial figures are illustrative assumptions for prototype "
        "demonstration and are not actual IBeX revenue."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "IBeX | IBS-Only Peer-to-Peer Platform | "
    "Prototype developed for Managing Platform Business | IFHE Hyderabad"
)
