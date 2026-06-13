import bentoml

iris_clf_runner = bentoml.sklearn.load_model("iris_clf:latest")

print(iris_clf_runner.predict([[5.9, 3.0, 5.1, 1.8]]))