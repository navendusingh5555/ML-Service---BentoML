import bentoml
import numpy as np

# Use the @bentoml.service decorator to define the service
@bentoml.service
class IrisClassifier:
    
    def __init__(self):
        # Load the scikit-learn model when the service starts
        self.model = bentoml.sklearn.load_model("iris_clf:latest")

    # Use standard Python type hints for inputs and outputs instead of bentoml.io
    @bentoml.api
    def predict(self, data: np.ndarray) -> np.ndarray:
        # Run the standard predict method
        return self.model.predict(data)