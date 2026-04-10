# 🤖 AI Government Scheme Recommender

An AI-powered system that helps users discover **relevant government schemes** based on their eligibility using a combination of **rule-based logic and AI (Google Gemini)**.

---

## 🚀 Features

* 🎯 Personalized scheme recommendations
* 🧠 AI-generated eligibility explanation (Gemini API)
* 📊 Rule-based eligibility matching
* 🧾 Step-by-step user input
* ⚡ Fast and simple command-line interface

---

## 🛠️ Tech Stack

* **Python**
* **Google Gemini API (`google-genai`)**
* Rule-based logic
* CLI (Command Line Interface)

---

## 📂 Project Structure

```
AI-Gov-Scheme-Recommender/
│
├── main.py                # Entry point
├── data.py                # Scheme dataset
├── eligibility.py         # Matching logic
├── ai_reason.py           # AI explanation module
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── .gitignore             # Ignored files
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Gov-Scheme-Recommender.git
cd AI-Gov-Scheme-Recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Do NOT upload `.env` to GitHub

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧪 Example

### Input:

```
Age: 21  
Income: 200000  
Occupation: student  
Category: General  
State: Maharashtra  
```
<img width="1920" height="1080" alt="Screenshot 2026-04-10 135753" src="https://github.com/user-attachments/assets/7a9e5292-694e-4a74-be02-564e18a36d04" />
<img width="1920" height="1080" alt="Screenshot 2026-04-10 135814" src="https://github.com/user-attachments/assets/3b13cb2a-616e-4406-916f-650fec8aaa78" />


### Output:

```
📌 NSP Scholarship  
✅ Eligible because your income is below ₹2.5 lakh and you are a student  

📌 Ayushman Bharat  
✅ Eligible due to low income  
```

---
<img width="1920" height="1080" alt="Screenshot 2026-04-10 171158" src="https://github.com/user-attachments/assets/cfe3a38f-b7fb-4e32-9492-8e5b1e0089a7" />



## 🧠 How It Works

1. User enters details (age, income, occupation, etc.)
2. System creates a user profile
3. Rule-based engine checks eligibility
4. Gemini AI generates explanation
5. Final schemes are displayed

---

## 📊 Use Cases

* Students looking for scholarships
* Farmers seeking subsidies
* Low-income families
* Rural population

---

## 🔮 Future Improvements

* 🌐 Web / Mobile App
* 🌍 Multilingual support
* 🎤 Voice input
* 🔗 Integration with government APIs

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🎯 Project Goal

To bridge the gap between **citizens and government benefits** using AI.

---

⭐ If you like this project, consider giving it a star!
