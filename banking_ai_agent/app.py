import streamlit as st
from banking_ai_agent.classifier import classify_message
from banking_ai_agent.feedback_handler import handle_positive_feedback, handle_negative_feedback
from banking_ai_agent.query_handler import handle_query
from banking_ai_agent.database import create_table

create_table()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def process_message(message, customer_name="Customer"):
    category = classify_message(message)

    if category == "positive":
        response = handle_positive_feedback(customer_name)
    elif category == "negative":
        response = handle_negative_feedback(message, customer_name)
    elif category == "query":
        response = handle_query(message)
    else:
        response = "I'm not sure how to handle that."

    return category, response

st.set_page_config(page_title="Banking Customer Support AI Agent", page_icon="🏦")
st.title("🏦 Banking Customer Support AI Agent")
st.caption("Classify customer messages, create tickets, and check ticket status.")

customer_name = st.text_input("Customer Name", value="Kassandra")
message = st.text_area("Enter customer message")

col1, col2 = st.columns(2)

with col1:
    submit_clicked = st.button("Submit")

with col2:
    clear_clicked = st.button("Clear Chat History")

if clear_clicked:
    st.session_state.chat_history = []
    st.rerun()

if submit_clicked:
    category, response = process_message(message, customer_name)

    st.session_state.chat_history.append({
        "message": message,
        "classification": category,
        "response": response
    })

    with st.container():
        st.subheader("Latest Result")
        st.markdown(f"**Classification:** {category}")
        st.markdown(f"**Response:** {response}")

with st.expander("Chat History", expanded=True):
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**Message:** {chat['message']}")
        st.markdown(f"**Classification:** {chat['classification']}")
        st.markdown(f"**Response:** {chat['response']}")
        st.markdown("---")