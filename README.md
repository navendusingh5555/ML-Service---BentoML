# Iris Flower Classification Service 🚀

A production-grade machine learning microservice built using "BentoML (v1.4+)" and "Scikit-Learn" to classify Iris flower species. This project demonstrates modern MLOps practices by packaging a classical machine learning model into a highly scalable, strictly validated REST API with automated documentation.

---

## ✨ Features

* Modern Class-Based Architecture: Utilizes BentoML’s latest `@bentoml.service` framework for clean, self-contained service lifecycles.
* Automated Swagger UI Documentation: Instantly generates an interactive OpenAPI/Swagger testing dashboard out of the box.
* Smart Input Reshaping: Built-in resilience layer that automatically handles single-sample vectors (1D arrays) and reshapes them to the 2D arrays expected by Scikit-Learn, eliminating common API payload errors.
* Production Deployment Ready: Pre-configured with a `bentofile.yaml` to build standardized, self-contained Bento deployment archives.

---

## 🛠️ Tech Stack

* Core Framework:** BentoML (v1.4+)
* Machine Learning:** Scikit-Learn
* Data Processing:** NumPy & Pandas
* Environment Management:** Python 3.11 / 3.12 (Recommended for ML stability)

---

## 📂 Project Structure


MLService/
├── service.py          # Core BentoML service class & API routing
├── bentofile.yaml      # BentoML packaging and dependency configuration
├── test.py             # Local script for raw model verification
└── venv/               # Local virtual environment