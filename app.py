import json
import os
import streamlit as st

from src.pipeline import LoyaltyPipeline

# ----------------------------
# App Setup
# ----------------------------
st.set_page_config(
    page_title="Agentic Loyalty Intelligence",
    layout="wide"
)

st.title("🧠 Agentic Life-Event Loyalty Intelligence")
st.caption("Detect lifestyle shifts and design Antavo-native loyalty actions")

# ----------------------------
# Sidebar — Data Source
# ----------------------------
st.sidebar.header("Customer Data")

CUSTOMER_DIR = "data/customers"
customer_files = sorted(
    [f for f in os.listdir(CUSTOMER_DIR) if f.endswith(".json")]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload customer JSON",
    type=["json"]
)

if uploaded_file:
    customer_data = json.load(uploaded_file)
    data_source = "Uploaded file"
else:
    selected_customer = st.sidebar.selectbox(
        "Select demo customer",
        customer_files
    )

    with open(os.path.join(CUSTOMER_DIR, selected_customer)) as f:
        customer_data = json.load(f)

    data_source = f"Demo customer: {selected_customer}"

# ----------------------------
# Sidebar — Customer Context
# ----------------------------
st.sidebar.divider()
st.sidebar.subheader("Customer Context")

st.sidebar.write(f"**Source:** {data_source}")
st.sidebar.write(f"**Customer ID:** {customer_data['customer_id']}")
st.sidebar.write(f"**Tier:** {customer_data['profile']['loyalty_tier']}")
st.sidebar.write(f"**Points:** {customer_data['profile']['points_balance']}")
st.sidebar.write(
    f"**Clubs:** {', '.join(customer_data['profile']['clubs']) or 'None'}"
)

run_analysis = st.sidebar.button("🔍 Analyze Customer")

# ----------------------------
# Main Layout
# ----------------------------
col1, col2, col3 = st.columns(3)

# ----------------------------
# Column 1 — Evidence
# ----------------------------
with col1:
    st.subheader("🧾 Customer Evidence")

    st.markdown("**Purchase History**")
    for month, purchases in customer_data["purchase_history"].items():
        st.markdown(f"**{month.upper()}**")
        for p in purchases:
            st.write(f"- {p['item']} ({p['category']})")

    st.markdown("**Customer Feedback**")
    for f in customer_data["feedback"]:
        st.write(f"• {f['text']}")

# ----------------------------
# Run Agentic Pipeline
# ----------------------------
if run_analysis:
    pipeline = LoyaltyPipeline()

    with st.status("🕵️ Agents are investigating...", expanded=True) as status:

        # Agent 1 — Behavior
        st.write("📊 **Behavior Agent**: Analyzing transaction patterns...")
        behavior_signals = pipeline.behavior_agent.analyze(
            customer_data["purchase_history"]
        )
        st.json(behavior_signals)

        # Agent 2 — Life Event
        st.write("🧠 **Life-Event Agent**: Reasoning about lifestyle shifts...")
        diagnosis = pipeline.life_event_agent.infer(
            behavior_signals,
            customer_data["feedback"]
        )
        st.write(
            f"Primary hypothesis: **{diagnosis['primary_hypothesis']}** "
            f"(Confidence: {diagnosis['confidence']})"
        )

        # Agent 3 — Strategy
        st.write("🏗️ **Loyalty Strategy Agent**: Designing Antavo intervention...")
        strategy = pipeline.strategy_agent.design(
            diagnosis=diagnosis,
            customer_id=customer_data["customer_id"]
        )

        status.update(
            label="Analysis complete",
            state="complete",
            expanded=False
        )

    # ----------------------------
    # Column 2 — Agent Reasoning
    # ----------------------------
    with col2:
        st.subheader("🧠 Agent Reasoning")

        st.markdown("**Behavioral Signals (Deterministic)**")
        st.json(behavior_signals)

        st.markdown("**Life-Event Diagnosis (Probabilistic)**")
        st.json(diagnosis)

    # ----------------------------
    # Column 3 — Loyalty Action
    # ----------------------------
    with col3:
        st.subheader("🎯 Loyalty Action")

        st.markdown(f"**Segment:** {strategy['segment']}")
        st.markdown(
            f"**Club Action:** {strategy['club_action']['action']} → "
            f"{strategy['club_action']['club_name']}"
        )

        st.markdown("**Rewards**")
        for r in strategy["rewards"]:
            st.markdown(
                f"- **{r['type']}**: {r['description']} ({r['duration']})"
            )

        st.markdown("**Channels:** " + ", ".join(strategy["channels"]))
        st.markdown(f"**Tone:** {strategy['message_tone']}")

        st.markdown("**Example Message**")
        st.info(strategy["example_message"])

        st.markdown("**Guardrails**")
        st.warning(strategy["guardrails"])

        st.markdown("**Prohibited Actions**")
        for action in strategy["prohibited_actions"]:
            st.write(f"• {action}")

        st.markdown("**Antavo API Payload (Simulated)**")
        st.json(strategy["antavo_api_payload"])

        st.divider()
        st.subheader("🧑‍⚖️ Human Approval")

        if st.button("✅ Approve & Push to Antavo"):
            st.toast("Campaign pushed to Antavo production environment 🚀")
