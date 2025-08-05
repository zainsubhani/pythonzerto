from sklearn.datasets import load_iris;
from sklearn.model_selection import train_test_split
iris = load_iris()
X=iris.data
Y=iris.target
X, y = load_iris(return_X_y=True)

feature_names = iris.feature_names
target_names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.5)
print(X_train.shape)
print(X_test.shape)

