# 🏠 House Price Prediction Web App

A full-stack web application designed to predict house prices using a trained Machine Learning model. The project features a clean UI, intuitive data entry, and price formatting in Indian numbering style (lakhs/crores).

## 📁 Project Structure

ML PROJECT 1 
├── Datasets/           
│   └── Housing.csv

├── Model/                 
│   ├── LinearModel.py     
│   ├── model_linear.pkl   
│   └── PredictionScript.py

├── templates/             
│   └── index.html

├── app.py               

## 🚀 How to Run

1. **Set up environment:** Ensure you have your virtual environment (`env`) activated.
2. **Run the Flask App:**
   ```bash
   python app.py
   ```
3. **Open in Browser:** Navigate to `http://127.0.0.1:5000` to access the prediction dashboard.

## ⚙️ Key Features

- **Machine Learning Integration:** Uses a pre-trained linear regression model (`model_linear.pkl`).
- **Indian Numbering Format:** Price outputs are automatically formatted as `XX,XX,XXX` (e.g., `65,78,990`) using a custom Jinja2 filter in `app.py`.
- **User-Friendly UI:** Modern, responsive design with input validation and clear result display.

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Data/ML:** Pandas, Scikit-Learn, Pickle
