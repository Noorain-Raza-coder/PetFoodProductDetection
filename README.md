# 📦 Custom Object Detection and Classification Using YOLO

![Python](https://img.shields.io/badge/Python-3.13.3-blue?logo=python)
![YOLO](https://img.shields.io/badge/YOLO-v11%20Nano-green?logo=yolo)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📑 Table of Contents

- [📖 About the Project](#-about-the-project)
- [🚀 Approach](#-approach)
- [🛠️ Tools and Technologies Used](#-tools-and-technologies-used)
- [⚙️ Setup and Installation](#️-setup-and-installation)
- [🎯 Run Application and Make Predictions](#-run-application-and-make-predictions)
- [📌 Notes](#-notes)

---

## 📖 About the Project

This project aims to **detect** and **classify** different types of products from images using a custom-trained **YOLO v11 nano** model. I started by annotating the dataset manually, then trained the model, and finally tested it to make real-world predictions.

---

## 🚀 Approach

- **Data Annotation**:
  - Annotated images using **CVAT**.
  - Split:
    - **Total images** = 66
    - **Annotated images** = 51 (41 for training, 10 for validation)
    - **Test images** = 15 (unlabeled)

- **Model Training**:
  - Used **YOLO v11 nano pre-trained model**.
  - Created an instance of the YOLO model.
  - Trained with data augmentation parameters to improve generalization.

- **Model Saving and Testing**:
  - Saved the best model onto **Google Drive** for backup.
  - Loaded the trained model and performed prediction on test images.
  - Counted products/classes from the test predictions.

---

## 🛠️ Tools and Technologies Used

| Tool/Technology       | Purpose                                  |
|------------------------|------------------------------------------|
| **CVAT**               | Data annotation                         |
| **YOLO v11 Nano**       | Object Detection and Classification     |
| **Python 3.13.3**       | Programming Language                    |
| **Visual Studio Code** | Code Editor                             |
| **Google Drive**       | Model Storage                           |

---

## ⚙️ Setup and Installation

Follow these steps to set up and run the project:

1. **Install Python**:
   - Download and install **Python 3.13.3** from the [official Python website](https://www.python.org/downloads/).

2. **Install Visual Studio Code**:
   - Download and install [Visual Studio Code](https://code.visualstudio.com/).

3. **Clone the Repository**:
   ```bash
   git clone <repository_link>
   cd <project_folder>

4. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv myvenv      # Create virtual environment
   myvenv/Scripts/activate    # Activate environment (Windows)

5. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt


## 🎯  Run Application and Make Predictions

1. **Run the app to make predictions on test images:**
   ```bash
   python app.py
   
2. **After running:**
  - Predictions will be made on all test images.
  - Results will be saved in the results directory.
  - A dictionary displaying the count of products/classes will be printed.


## 📌 Notes

- Ensure that your best model (best.pt) is loaded correctly from Google Drive before running predictions.
- Keep your test images in the expected input folder.
- Confirm all libraries from requirements.txt are installed to avoid runtime issues.


# *THANK YOU*
