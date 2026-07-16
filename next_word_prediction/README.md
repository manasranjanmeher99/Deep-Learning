# 🎬 Next Word Prediction using LSTM

A Deep Learning project that predicts the next word(s) based on an input text using an LSTM (Long Short-Term Memory) neural network. The model is trained on the **TMDB 5000 Movies** dataset and learns sequential word relationships from movie titles.

---

## 📌 Project Overview

This project demonstrates how to build a Next Word Prediction model using TensorFlow and Keras.

The workflow includes:

- Loading movie title data
- Text preprocessing
- Tokenization
- Sequence generation
- Padding sequences
- One-hot encoding labels
- Building an LSTM model
- Training the model
- Saving the trained model
- Predicting the next words

---

## 📂 Project Structure

```
next-word-prediction/
│
├── next_word_prediction.ipynb      # Jupyter Notebook
├── tmdb_5000_movies.csv            # Dataset
├── nwp.h5                          # Trained Model
├── README.md
└── requirements.txt
```

---

## 🚀 Features

- Text preprocessing
- Keras Tokenizer
- Variable-length sequence generation
- Sequence padding
- One-hot label encoding
- LSTM-based language model
- Predict multiple next words
- Save and reuse trained model

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Jupyter Notebook

---

## 📊 Dataset

Dataset Used:

**TMDB 5000 Movies Dataset**

The model is trained using the **original_title** column from the dataset.

Example movie titles:

- Avatar
- Spider-Man 3
- The Dark Knight
- Cloudy with a Chance of Meatballs

---

## ⚙️ Model Architecture

```
Embedding Layer
        │
        ▼
LSTM (100 Units)
        │
        ▼
LSTM (100 Units)
        │
        ▼
Dense (100 ReLU)
        │
        ▼
Dense (Softmax)
```

### Model Configuration

- Embedding Dimension: **14**
- LSTM Layers: **2**
- Hidden Units: **100**
- Optimizer: **Adam**
- Learning Rate: **0.004**
- Loss Function: **Categorical Crossentropy**
- Epochs: **100**

---

## 📈 Workflow

```
Movie Titles
      │
      ▼
Text Cleaning
      │
      ▼
Tokenizer
      │
      ▼
Generate Sequences
      │
      ▼
Padding
      │
      ▼
One-Hot Encoding
      │
      ▼
Train LSTM Model
      │
      ▼
Save Model
      │
      ▼
Predict Next Words
```

---

## ▶️ Installation

Clone the repository

```bash
https://github.com/manasranjanmeher99/Deep-Learning/new/main/next_word_prediction.git
```

Move into the project

```bash
cd next-word-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## ▶️ Running the Project

Open

```
next_word_prediction.ipynb
```

Run each notebook cell sequentially.

---

## 💻 Example Predictions

Input

```
avatar
```

Prediction

```
avatar man's lenin all kill yet
```

---

Input

```
dark knight
```

Prediction

```
dark knight angeles this for o welle anything titanic plan gente in
```

---

Input

```
cloudy
```

Prediction

```
cloudy with a chance of meatballs
```

> Predictions depend on the trained model and dataset.

---

## 📦 Saved Model

After training, the model is saved as:

```
nwp.h5
```

This model can be loaded later for inference without retraining.

---

## 📋 Requirements

```
tensorflow
numpy
pandas
jupyter
```

or install

```bash
pip install tensorflow numpy pandas notebook
```

---

## 🎯 Future Improvements

- Train on a larger text corpus
- Add preprocessing (lowercase, punctuation removal)
- Use Bidirectional LSTM
- Integrate GRU architecture
- Implement Beam Search decoding
- Deploy with Streamlit
- Create REST API using Flask/FastAPI
- Add model evaluation metrics

---

## 📸 Output

Example predictions:

```
Input:
Spider-Man 3

↓

Predicted:
Spider-Man 3 glory you soldiers to boots
```

```
Input:
Avatar

↓

Predicted:
avatar man's lenin all kill yet
```

---

## 👨‍💻 Author

**Manas Ranjan Meher**

GitHub:
https://github.com/manasranjanmeher99

LinkedIn:
https://www.linkedin.com/in/manas-ranjan-meher-606181280/

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
