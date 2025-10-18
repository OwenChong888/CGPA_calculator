# CGPA Calculator for UTM Students 🎓

A simple web application built with Streamlit to help Universiti Teknologi Malaysia (UTM) students calculate their semester GPA and new CGPA.

**[➡️ Click Here to Use the Live App!]([https://your-streamlit-app-url.streamlit.app](https://cgpacalculator-t26mqbusg52khpk8cxyrjx.streamlit.app/))**

---

## 🚀 Features

* **Cumulative CGPA:** Takes your current CGPA and total completed credits into account.
* **Dynamic Course Entry:** Add or remove as many courses as you need for the semester.
* **Instant Calculation:** Get your results immediately upon submission.
* **Visual Feedback:**
    * Shows key metrics like **Semester GPA** and **New CGPA**.
    * Displays a **bar chart** of your pointers for each subject.
    * Provides a **detailed table** with quality points for each course.
* **Data Validation:** Ensures all required fields are filled before calculating.
* **Grade Reference:** Includes the official UTM grading table for easy reference.

---

## 🛠️ Tech Stack

* **Streamlit:** For creating and deploying the web app.
* **Pandas:** For data handling and calculations.
* **Matplotlib:** For generating the semester performance bar chart.

---

## 💻 How to Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/OwenChong888/CGPA_calculator.git](https://github.com/OwenChong888/CGPA_calculator.git)
    cd CGPA_calculator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
