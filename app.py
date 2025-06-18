import streamlit as st
import pandas as pd
import random

# Simulated email log
sample_data = [
    {"To": "alex@example.com", "Subject": "Follow-up on design mockups", "Sent": "2025-06-17", "Replied": "Yes", "Sentiment": "Positive"},
    {"To": "team@workspace.com", "Subject": "Quarterly goals review", "Sent": "2025-06-16", "Replied": "No", "Sentiment": ""},
    {"To": "hr@example.com", "Subject": "Reimbursement request", "Sent": "2025-06-15", "Replied": "Yes", "Sentiment": "Neutral"}
]

df = pd.DataFrame(sample_data)

st.title("MailMinder: Email Tracker + Sentiment Analyzer")
st.markdown("Track sent emails, detect replies, and auto-classify tone")

st.subheader("Email Log")
st.dataframe(df, use_container_width=True)

st.subheader("Analyze New Email Thread")
with st.form("analyze_form"):
    to = st.text_input("To")
    subject = st.text_input("Subject")
    body = st.text_area("Reply Message (simulate a response)")
    submitted = st.form_submit_button("Analyze")

if submitted:
    sentiment = random.choice(["Positive", "Neutral", "Negative"])
    st.success(f"Sentiment Detected: {sentiment}")
    df.loc[len(df.index)] = [to, subject, "2025-06-18", "Yes", sentiment]
    st.dataframe(df, use_container_width=True)
