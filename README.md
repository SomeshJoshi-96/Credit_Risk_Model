# 💳 Credit Risk Modelling

A **Streamlit** web app designed to predict a borrower's likelihood of defaulting on a loan, generate a personalized credit score, and assign an intuitive risk rating—all instantly within your browser.

---

## 🚀 Key Features

| ⚡ Feature                   | 🔎 Description                                              |
| --------------------------- | ----------------------------------------------------------- |
| **Real-Time Predictions**   | Instant calculation of risk metrics upon user input.        |
| **Dynamic Ratios**          | Automatically computes important financial ratios.          |
| **User-Friendly Interface** | Interactive and intuitive UI powered by Streamlit.          |
| **Notebook-Based Workflow** | Transparent model training process documented in notebooks. |
| **Easy Integration**        | Easily replace models without modifying frontend code.      |

---

## 📸 Screenshots

*(Please insert screenshots of your application here.)*

![Screenshot 1](path/to/screenshot1.png)

![Screenshot 2](path/to/screenshot2.png)

---

## 🗂️ Project Structure

```text
Credit_Risk_Model/
├── main.py                     # Streamlit web application entry point
├── prediction_helper.py        # Preprocessing and prediction functions
├── artifacts/                  # Trained models and preprocessing artifacts
├── data/                       # Dataset files
├── jupyter_notebooks/          # Exploratory analysis and training notebooks
├── screenshots/                # Application screenshots
├── requirements.txt            # Project dependencies
└── README.md                   # Project overview (this file)
```

---

## 🚀 Quick Start

Follow these steps to quickly set up and run the application locally:

```bash
# Clone the repository
git clone https://github.com/<your-github-username>/Credit_Risk_Model.git
cd Credit_Risk_Model

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run main.py
```

Navigate to [http://localhost:8501](http://localhost:8501) to view the app in action.

---

## ⚙️ How It Works

1. Enter borrower details through the web interface.
2. Data preprocessing includes:

   * Encoding categorical variables.
   * Feature scaling.
   * Calculating derived metrics (like Loan-to-Income).
3. Processed data is fed into the machine learning model.
4. Model outputs default probability, credit score, and risk rating.

---

## 📚 Model Training and Evaluation

The model training and evaluation process is detailed thoroughly within the Jupyter notebooks provided in the `jupyter_notebooks` directory. You can explore different model architectures and preprocessing techniques documented clearly in each notebook.

---

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository and create your feature branch (`git checkout -b feature/new-feature`).
2. Commit your changes (`git commit -m "Add new feature"`).
3. Push to the branch (`git push origin feature/new-feature`).
4. Open a pull request.

---

## 🛣️ Future Enhancements

* Integrate SHAP or LIME for enhanced model interpretability.
* Develop monitoring tools to detect data drift.
* Expand interactive visualizations for deeper insights.
* Deploy publicly on platforms like Streamlit Cloud.
