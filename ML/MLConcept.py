#1 import data
#2 clean the data
#3 split the data trainingset/test set
#4 create a model import algo like use library
#5 check the output

from sklearn.datasets import load_iris;
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
iris = load_iris()
X=iris.data
Y=iris.target
X, y = load_iris(return_X_y=True)
knn=KNeighborsClassifier(n_neighbors=3) #because 3 number of flowers in dataset

feature_names = iris.feature_names
target_names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.1)
print(X_train.shape)
print(X_test.shape)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(metrics.accuracy_score(y_test,y_pred),"checking accurency")


# test size is small trade off how much data is for training and testing
# to improve add more columns
# we can use different classifier like decision tree classifier 

sample = [[4,4,5,6],[4,4,5,6]]
prediction = knn.predict(sample)
pred_speics= [iris.target_names[p] for p in prediction]
print(pred_speics)