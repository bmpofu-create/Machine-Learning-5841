
# Distracted Driver Classification — Machine Learning Project

This project implements a **deep learning model** for distracted driver detection.  
It includes data preprocessing, model training, evaluation, and a clean project structure suitable for reproducibility and deployment.

Large trained model files are **not stored in the repository** due to GitHub’s 100MB limit.  
A download link is provided instead.

---

##  Project Structure

```
Machine-Learning-5841/
│── data/                     # Raw and processed datasets
│── figures/                  # Plots, charts, and visualizations
│── notebooks/                # Jupyter notebooks for exploration & training
│── reports/                  # Project reports, summaries, documentation
│── saved_model/              # Folder for placing downloaded model files
│── src/                      # Source code (app.py,training, preprocessing, utils)
│── saved_models_on_drive.txt # Link to download large model files                    
│── README.md                 # How to run the project
```

---

##  How to Run This Project

Follow these steps to set up and run the project on your machine.

---

### **1️ Clone the Repository**

```bash
git clone https://github.com/bmpofu-create/Machine-Learning-5841.git
cd Machine-Learning-5841
```

---

### **2 Create and Activate a Virtual Environment**

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### **3️ Install Dependencies*

```bash
pip install -r requirements.txt
```

---

### **4️ Download the Trained Model**

GitHub cannot store large `.h5` or `.keras` files, so the model is hosted externally.

Open the file:

```
saved_models_on_drive.txt
```

Download the model from the link inside, then place it into:

```
saved_model/
```

Example:

```
saved_model/best_model.h5
```

---

### **5️ Run the Application (if using Streamlit)**

If your project includes a Streamlit app:

```bash
streamlit run app.py
```

---

### **6️ Run Training or Evaluation Scripts**

Inside `src/`, you may have scripts like:

```bash
python src/train.py
python src/evaluate.py
python src/preprocess.py
```

Adjust based on your actual file names.

---

##  Features

- Deep learning model for distracted driver classification  
- Clean, modular project structure  
- Jupyter notebooks for experimentation  
- External model hosting for large files  
- Reproducible environment with `requirements.txt`  
- Ready for deployment or further research  

---


## 📝 Notes

- Large model files are **not** included in the repo  
- Use the link in `saved_models_on_drive.txt` to download them  
- Ensure the model is placed in the correct folder before running inference  

---

##  Contributing

Pull requests are welcome.  
For major changes, please open an issue first to discuss what you’d like to modify.

---


Just tell me what you want to enhance next.
