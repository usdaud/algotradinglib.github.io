# Support Vector Machines (SVM)

[Support Vector Machines](../s/support_vector_machines_in_trading.md) (SVM) are a set of [supervised learning](../s/supervised_learning.md) methods used for classification, regression, and outliers detection. Developed initially for binary classification problems, SVMs are powerful, versatile algorithms well-suited for a wide [range](../r/range.md) of tasks.

## Fundamentals of SVM

### Basic Idea

The fundamental idea behind SVM is to find the best separating hyperplane that divides a dataset into classes. In a 2D space, this is analogous to drawing a line that best separates the data points into different classes. The goal is to maximize the [margin](../m/margin.md), i.e., the distance between the hyperplane and the closest data point from either class. This hyperplane is referred to as the optimal hyperplane.

### Mathematical Formulation

Given a set of training data points of the form:
\[ (x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n) \]
Where \( x_i \) is a vector representing the input features and \( y_i \) is the class label.

The SVM algorithm finds a hyperplane defined by:
\[ w \cdot x - b = 0 \]
Where \( w \) is the weight vector, \( x \) is the input vector, and \( b \) is the bias term.

The objective is to maximize the [margin](../m/margin.md), which is given by:
\[ \text{[Margin](../m/margin.md)} = \frac{2}{||w||} \]
This leads to a quadratic [optimization](../o/optimization.md) problem with constraints:
\[ \text{minimize} \quad \frac{1}{2} ||w||^2 \]
Subject to:
\[ y_i (w \cdot x_i - b) \geq 1 \]

### Support Vectors

The data points that are closest to the hyperplane are termed support vectors. These points are critical as they define the position and orientation of the hyperplane. If a point is outside the [margin](../m/margin.md), it is not a support vector and does not influence the model.

## Types of SVM

### Linear SVM

Linear SVM works well when the data is linearly separable, meaning a single line can separate the classes in a 2D space, or a hyperplane can separate them in a higher-dimensional space. The objective is to find this optimal hyperplane.

### Non-Linear SVM

When data is not linearly separable, SVM can still be used through the application of the kernel trick. The kernel function transforms the input space into a higher-dimensional space where a hyperplane can effectively separate the classes.

#### Common Kernel Functions

1. **Polynomial Kernel**: 
\[ K(x_i, x_j) = (x_i \cdot x_j + c)^d \]
2. **Radial [Basis](../b/basis.md) Function (RBF) Kernel / Gaussian Kernel**:
\[ K(x_i, x_j) = \exp(-\[gamma](../g/gamma.md) ||x_i - x_j||^2) \]
3. **Sigmoid Kernel**:
\[ K(x_i, x_j) = \tanh(\[alpha](../a/alpha.md) x_i \cdot x_j + c) \]

### SVM for Regression (SVR)

[Support Vector Regression](../s/support_vector_regression.md) (SVR) is an extension of SVM for regression tasks. SVR aims to find a function that deviates from the actual observed targets by a [value](../v/value.md) no greater than a specified [margin](../m/margin.md). The goal is to ensure that the predicted [value](../v/value.md) lies within a certain distance from the actual [value](../v/value.md), defined by a threshold parameter \( \epsilon \).

#### Formulation

SVR attempts to minimize the following loss function:
\[ \frac{1}{2} ||w||^2 + C \sum_{i=1}^n L_{\epsilon}(y_i, f(x_i)) \]

Where \( L_{\epsilon} \) is the epsilon-insensitive loss function:
\[ L_{\epsilon}(y, f(x)) = \max(0, |y - f(x)| - \epsilon) \]

### SVM for Outlier Detection

One-Class SVM, an extension of SVM, is particularly useful for outlier detection and [anomaly detection](../a/anomaly_detection.md). It fits an SVM model to the 'normal' data and identifies outliers that fall outside the learned decision boundary.

## Implementation of SVM

### Libraries and Tools

1. **scikit-learn**: A popular Python library for [machine learning](../m/machine_learning.md), which provides [robust](../r/robust.md) support for SVM through its `svm` module. [scikit-learn](https://scikit-learn.org/stable/modules/svm.html)
2. **LIBSVM**: A library for [Support Vector Machines](../s/support_vector_machines_in_trading.md) that is widely used for SVM implementation. [LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
3. **[TensorFlow](../t/tensorflow.md)**: An [open](../o/open.md)-source library for [machine learning](../m/machine_learning.md) that also supports SVM implementations. [TensorFlow SVM](https://www.tensorflow.org/overview)
4. **[KERAS](../k/keras.md)**: An [open](../o/open.md)-source software library that provides a Python interface for [artificial neural networks](../a/artificial_neural_networks.md) and also has modules to integrate SVM. [KERAS](https://keras.io/)

### Example Code in Python

Here is a simple example of implementing a linear SVM using `scikit-learn`:

```python
from sklearn [import](../i/import.md) svm
from sklearn.datasets [import](../i/import.md) make_classification
from sklearn.model_selection [import](../i/import.md) train_test_split

# Generate a random dataset
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a linear SVM classifier
clf = svm.SVC(kernel='linear')

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

print("Predictions: ", y_pred)
print("Accuracy: ", clf.score(X_test, y_test))
```

## Applications of SVM

### Financial Market Prediction

SVMs are extensively used in the [finance](../f/finance.md) [industry](../i/industry.md) for stock price prediction, [risk management](../r/risk_management.md), and [algorithmic trading](../a/algorithmic_trading.md). They can model complex relationships in financial data and provide [robust](../r/robust.md) predictive capabilities.

### Medical Diagnosis

In medical diagnosis, SVMs help in classifying diseases based on symptoms or test results. For instance, SVMs can distinguish between cancerous and non-cancerous cells.

### Bioinformatics

Bioinformatics involves large datasets, such as gene expression data. SVMs can classify and analyze this data effectively to identify gene functions and interactions.

### Image and Speech Recognition

SVMs are widely used in image and [speech recognition](../s/speech_recognition.md) systems. They help in handwriting recognition, face detection, and voice classification.

### Text Categorization

[Support Vector Machines](../s/support_vector_machines_in_trading.md) can efficiently categorize text, such as emails, news articles, and [social media](../s/social_media.md) posts, into predefined categories. They are useful in spam detection, [sentiment analysis](../s/sentiment_analysis.md), and topic classification.

## Challenges with SVM

1. **High Computational Cost**: Training SVM with large datasets can be time-consuming and require substantial computational resources.
2. **Choice of Kernel**: Selecting an appropriate kernel function and tuning its parameters is critical and can be challenging.
3. **Sensitivity to Parameter Selection**: The performance of SVM is sensitive to the choice of parameters like C (regularization) and γ ([gamma](../g/gamma.md) in RBF kernel).

## Summary

[Support Vector Machines](../s/support_vector_machines_in_trading.md) are powerful, versatile machine [learning algorithms](../l/learning_algorithms_in_trading.md) capable of handling classification, regression, and outlier detection tasks. They are particularly well-suited for complex, high-dimensional datasets. Despite their computational complexity and sensitivity to parameter tuning, their ability to find optimal hyperplanes and their proficiency with kernel methods make them an essential tool in a data scientist's arsenal.
