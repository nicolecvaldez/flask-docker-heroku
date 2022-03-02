
# # one time model creation
#
# import pickle
# import pandas as pd
# pd.set_option('display.max_columns', None)
# from sklearn import datasets
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn import svm
# from sklearn import metrics
# from sklearn.tree import DecisionTreeClassifier
#
#
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
#
# df = pd.DataFrame(X, columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])
# df["Species"] = y
#
# train, test = train_test_split(df, test_size=0.1)
# train_X = train[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
# train_y = train.Species
# test_X = test[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
# test_y = test.Species
#
# model = svm.SVC()
# model.fit(train_X, train_y)
# prediction=model.predict(test_X)
# print('The accuracy of the SVM is:', metrics.accuracy_score(prediction,test_y))
#
# model = LogisticRegression()
# model.fit(train_X, train_y)
# prediction = model.predict(test_X)
# print('The accuracy of the Logistic Regression is', metrics.accuracy_score(prediction,test_y))
#
# model = DecisionTreeClassifier()
# model.fit(train_X, train_y)
# prediction = model.predict(test_X)
# print('The accuracy of the Decision Tree is', metrics.accuracy_score(prediction,test_y))
#
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(train_X, train_y)
# prediction = model.predict(test_X)
# print('The accuracy of the KNN is',metrics.accuracy_score(prediction,test_y))
#
# with open('/Users/nicolevaldez/OneDrive - PLDT/python-docker/irisclassifier_knn.pkl', 'wb') as fid:
#     pickle.dump(model, fid)

# import packages
import pickle

def iris_predict(model_path, data_array):
    """
    Load iris model classifier and predict data input
    :param model_path:
    :param data_topredict:
    :return:
    """

    # get stored model
    with open(model_path, 'rb') as fid:
        model = pickle.load(fid)

    # predict if fraud
    pred = model.predict(data_array)[0]

    if pred == 0:
        pred_str = 'Iris Setosa'
    elif pred == 1:
        pred_str = 'Iris Virginica'
    elif pred == 2:
        pred_str = 'Iris Versicolor'
    else:
        pred_str = ""

    return pred_str
