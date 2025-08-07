# 🧠 Mood Tracker

A simple AI-powered mood tracking app that helps users log their daily emotions, analyze sentiment, visualize mental health trends, and receive self-care suggestions.

---

## 🌟 Features

- 📝 Daily mood logging via text
- 🔍 Sentiment & emotion classification using NLP
- 📈 Visualization of mood trends over time
- 🧘 Personalized mental health recommendations

---

## 🛠️ Tech Stack

- Python 3.12+
- Pandas, NumPy, Matplotlib
- Transformers (for sentiment analysis)
- Scikit-learn
- PyTorch

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/paiabhishekpai/mood-tracker.git
cd mood-tracker
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the environment

- On **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

All required Python packages are listed in `requirements.txt`. Versions are fixed to avoid binary incompatibility errors.

### Example:
```text
numpy==1.26.4
pandas==2.2.2
matplotlib==3.9.0
transformers==4.41.2
torch==2.3.0
scikit-learn==1.5.0
streamlit
```

---

## ▶️ How to Run

Once the environment is ready:

```bash
streamlit run app.py
```

You’ll be able to:
- Enter daily text logs
- See your mood analyzed
- View plots and receive suggestions

---

## 📊 Example Outputs

- "You’ve been feeling low for 3 days, consider journaling or meditation."
- Graphs showing mood patterns across days.

---
