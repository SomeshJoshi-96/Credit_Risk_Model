import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Credit Risk Modelling", page_icon="📊")
st.title("📊 Credit Risk Modelling")

st.markdown("---")

with st.form("risk_form"):
    st.header("Applicant Details")

    # Row 1: Basic info
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=28,
                              help="Applicant's age in years")
    with col2:
        income = st.number_input("Income", min_value=0, value=1_200_000,
                                 help="Annual income in your currency")
    with col3:
        loan_amount = st.number_input("Loan Amount", min_value=0, value=2_560_000,
                                      help="Total requested loan amount")

    # Calculate and show Loan to Income Ratio dynamically
    loan_to_income_ratio = loan_amount / income if income > 0 else 0
    st.markdown(f"**Loan to Income Ratio:** `{loan_to_income_ratio:.2f}`")

    st.header("Loan & Credit Details")
    col4, col5, col6 = st.columns(3)
    with col4:
        loan_tenure_months = st.number_input("Loan Tenure (months)", min_value=1, value=36,
                                             help="Number of months to repay the loan")
    with col5:
        avg_dpd_per_delinquency = st.number_input("Average Days Past Due (DPD)", min_value=0, value=20,
                                                  help="Average days payment is overdue")
    with col6:
        num_open_accounts = st.number_input("Open Loan Accounts", min_value=1, max_value=20, value=2,
                                            help="Number of open loan accounts")

    # Use an expander for detailed credit info
    with st.expander("Credit Ratios (Advanced)"):
        col7, col8 = st.columns(2)
        with col7:
            delinquency_ratio = st.number_input("Delinquency Ratio (%)", min_value=0, max_value=100, value=30,
                                                help="Percentage of delinquent loans")
        with col8:
            credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", min_value=0, max_value=100, value=30,
                                                       help="Percentage of credit limit used")

    st.header("Loan Characteristics")
    col9, col10, col11 = st.columns(3)
    with col9:
        residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"],
                                      help="Type of residence")
    with col10:
        loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"],
                                    help="Purpose of the loan")
    with col11:
        loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"],
                                 help="Type of loan collateral")

    submit = st.form_submit_button("Calculate Risk")

if submit:
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.markdown("---")
    st.header("Prediction Results")

    col12, col13, col14 = st.columns(3)
    col12.metric("Default Probability", f"{probability:.2%}")
    col13.metric("Credit Score", f"{credit_score}")
    col14.metric("Rating", f"{rating}")
