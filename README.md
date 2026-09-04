\# 🎓 AI Student Placement Predictor



An \*\*AI-powered Student Placement Prediction System\*\* that uses Machine Learning to predict a student's placement status and placement probability based on academic performance, technical skills, aptitude, communication skills, certifications, internships, and projects.



\## 🚀 Project Overview



The system helps students understand their placement readiness by analyzing their profile and providing:



\* 🤖 Machine Learning based placement prediction

\* 📊 Placement probability percentage

\* 💡 Personalized skill improvement recommendations

\* 📈 Interactive analytics dashboard

\* 🗄️ SQLite database for prediction history

\* 🌐 Flask-based web application

\* 📊 Student performance visualization



\## 🛠️ Technologies Used



| Technology   | Purpose             |

| ------------ | ------------------- |

| Python       | Programming         |

| Flask        | Web Application     |

| Pandas       | Data Processing     |

| NumPy        | Numerical Computing |

| Scikit-learn | Machine Learning    |

| SQLite       | Database            |

| HTML         | Web Interface       |

| CSS          | Dashboard Styling   |

| JavaScript   | Interactive Charts  |

| Chart.js     | Data Visualization  |

| Git \& GitHub | Version Control     |



\## 🤖 Machine Learning



Several classification algorithms were evaluated:



\* Logistic Regression

\* Random Forest

\* Gradient Boosting

\* Decision Tree



The final tuned model used in the application is:



\*\*Logistic Regression\*\*



Current evaluation on the synthetic test dataset:



\* Accuracy: \*\*68%\*\*

\* Precision: \*\*69.57%\*\*

\* Recall: \*\*64%\*\*

\* F1 Score: \*\*66.67%\*\*



> Note: The current dataset is synthetically generated for project development and demonstration. Model performance should not be interpreted as real-world placement accuracy.



\## 📥 Input Features



The system uses the following student features:



\* Age

\* Gender

\* CGPA

\* 10th Percentage

\* 12th Percentage

\* Aptitude Score

\* Coding Score

\* Communication Score

\* Technical Skills

\* Certifications

\* Internship Experience

\* Projects



\## 📊 Dashboard



The analytics dashboard provides:



1\. Total Predictions

2\. Placed Students

3\. Not Placed Students

4\. Average Placement Probability

5\. Placement Distribution

6\. CGPA vs Placement Prediction

7\. Coding Score vs Placement

8\. Probability Distribution

9\. Prediction History



\## 💡 Recommendation System



The application provides personalized recommendations based on student performance.



For example:



\* Improve CGPA

\* Practice coding

\* Improve aptitude

\* Improve communication skills

\* Complete technical certifications

\* Gain internship experience

\* Build real-world projects

\* Improve technical skills



\## 🗂️ Project Structure



```text

StudentPlacementAI/

│

├── data/

│   ├── student\_data.csv

│   └── prediction\_history.csv

│

├── models/

│   └── placement\_model.pkl

│

├── templates/

│   ├── index.html

│   ├── result.html

│   └── dashboard.html

│

├── static/

│   └── style.css

│

├── app.py

├── database.py

├── create\_dataset.py

├── train\_model.py

├── compare\_models.py

├── tune\_model.py

├── tuning\_results.txt

├── requirements.txt

├── README.md

└── .gitignore

```



\## ⚙️ Installation



\### 1. Clone the repository



```bash

git clone https://github.com/vinithreddy09/StudentPlacementAI.git

```



\### 2. Open the project



```bash

cd StudentPlacementAI

```



\### 3. Create a virtual environment



```bash

python -m venv venv

```



\### 4. Activate the virtual environment



Windows:



```bash

venv\\Scripts\\activate

```



\### 5. Install dependencies



```bash

pip install -r requirements.txt

```



\## ▶️ Run the Application



Start the Flask application:



```bash

python app.py

```



Open the application in your browser:



```text

http://127.0.0.1:5000

```



\### 📊 Dashboard



Open:



```text

http://127.0.0.1:5000/dashboard

```



\## 🔄 Machine Learning Workflow



```text

Student Dataset

&#x20;     ↓

Data Preprocessing

&#x20;     ↓

Feature Engineering

&#x20;     ↓

Train Multiple ML Models

&#x20;     ↓

Compare Model Performance

&#x20;     ↓

Hyperparameter Tuning

&#x20;     ↓

Select Best Model

&#x20;     ↓

Save Model

&#x20;     ↓

Flask Web Application

&#x20;     ↓

Student Input

&#x20;     ↓

Placement Prediction

&#x20;     ↓

Probability + Recommendations

&#x20;     ↓

SQLite Database

&#x20;     ↓

Analytics Dashboard

```



\## 🎯 Future Scope



Future improvements can include:



\* Use real-world student placement datasets

\* Improve model accuracy with larger datasets

\* Add XGBoost and other advanced models

\* Add explainable AI using SHAP

\* Add user authentication

\* Add college/admin login

\* Add student profile management

\* Add automated PDF reports

\* Add Power BI integration

\* Deploy the application to a cloud platform

\* Develop a mobile application



\## 👨‍💻 Author



\*\*Vinith Reddy\*\*



B.Tech Student



GitHub:

https://github.com/vinithreddy09



\## 📌 Disclaimer



This project is developed for \*\*academic, learning, and demonstration purposes\*\*. Placement predictions are model-based estimates and should not be treated as guaranteed employment outcomes.



