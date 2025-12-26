# Titanic Survival Prediction — End-to-End ML Deployment

This project demonstrates a **complete end-to-end machine learning workflow**, starting from model training and feature engineering, and ending with a **production-ready deployment** using **FastAPI** and **Docker**.

The objective is to predict whether a passenger survived the Titanic disaster based on demographic and travel features, and expose the trained model as a **real-time inference API**.

---

## Project Highlights

- End-to-end ML pipeline (training → inference → deployment)
- Feature engineering and model training in Jupyter
- Model serialization and reuse
- Real-time inference via FastAPI
- Fully containerized using Docker
- Publicly runnable via Docker Hub

This mirrors how machine learning models are deployed in real industry systems.

---

## Tech Stack

- **Python**
- **XGBoost**
- **Pandas, Scikit-learn**
- **FastAPI**
- **Docker**
- **Docker Hub**

---

## Model Features

The model is trained on the following features:

| Feature | Description |
|------|-------------|
| `sex` | Passenger gender (encoded) |
| `pclass` | Ticket class (1, 2, 3) |
| `age` | Passenger age (imputed) |
| `fare` | Ticket fare |
| `embarked` | Port of embarkation |
| `alone` | Whether the passenger was traveling alone |

**Target variable:** `survived`

---

## Project Structure

