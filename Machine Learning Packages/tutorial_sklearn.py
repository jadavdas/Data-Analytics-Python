# %% Skikit-learn
'''Skikit-learn is one of the most popular ML libraries for classical ML algorithms. It is built on top of two basic
Python libraries, viz., NumPy and SciPy. Scikit-learn supports most of the supervised and unsupervised learning algorithms.
Scikit-learn can also be used for data-mining and data-analysis, which makes it a great tool who is starting out with ML.
'''

# Python script using Scikit-learn for Decision Tree Clasifier

# Sample Decision Tree Classifier
from sklearn import datasets
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def exIris():
    # load the iris datasets
    iris = datasets.load_iris()

    x = iris.data[:,0]
    y = iris.data[:,1]

    x2 = iris.data[:, 2]
    y2 = iris.data[:, 3]

    species = iris.target

    x_min, x_max = x.min() - 0.5, x.max() + 0.5
    y_min, y_max = y.min() - 0.5, y.max() + 0.5

    x2_min, x2_max = x2.min() - 0.5, x2.max() + 0.5
    y2_min, y2_max = y2.min() - 0.5, y2.max() + 0.5

    x_reduced = PCA(n_components=3).fit_transform(iris.data)

    plt.figure()
    plt.subplot(2,2,1)
    plt.title('Iris Dataset - Classification By Sepal Sizes')
    plt.scatter(x, y, c = species)
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

    plt.subplot(2, 2, 2)
    plt.title('Iris Dataset - Classification By Petal Sizes')
    plt.scatter(x2, y2, c=species)
    plt.xlabel('Petal length')
    plt.ylabel('Petal width')
    plt.xlim(x2_min, x2_max)
    plt.ylim(y2_min, y2_max)
    plt.xticks(())
    plt.yticks(())

    plt.show()

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_title('Iris Dataset by PCA', size=14)
    ax.scatter(x_reduced[:,0], x_reduced[:,1], x_reduced[:,2], c=species)
    ax.set_xlabel('First eigenvector')
    ax.set_ylabel('Second eigenvector')
    ax.set_zlabel('Third eigenvector')
    plt.show()


def exKNN():
    np.random.seed(0)
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    i = np.random.permutation(len(iris.data))
    x_train = x[i[:-10]]
    y_train = y[i[:-10]]
    x_test = x[i[-10:]]
    y_test = y[i[-10:]]
    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)

    print(knn.predict(x_test))
    print(y_test)

    from matplotlib.colors import ListedColormap

    # Sepal
    iris = datasets.load_iris()
    x = iris.data[:, :2]  # X-axis: sepal length-width
    y = iris.target  # species

    x_min, x_max = x[:, 0].min() - .5, x[:, 0].max() + .5
    y_min, y_max = x[:, 1].min() - .5, x[:, 1].max() + .5

    # MESH
    cmap_light = ListedColormap(['#AAAAFF', '#AAFFAA', '#FFAAAA'])
    h = 0.02
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    knn = KNeighborsClassifier()
    knn.fit(x, y)
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])  # np.ravel: Return a contiguous flattened array
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot the training points
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()

    ## Petal
    iris = datasets.load_iris()
    x = iris.data[:, 2:4]  # X-axis: sepal length-width
    y = iris.target  # species

    x_min, x_max = x[:, 0].min() - .5, x[:, 0].max() + .5
    y_min, y_max = x[:, 1].min() - .5, x[:, 1].max() + .5

    # MESH
    cmap_light = ListedColormap(['#AAAAFF', '#AAFFAA', '#FFAAAA'])
    h = 0.02
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    knn = KNeighborsClassifier()
    knn.fit(x, y)
    Z = knn.predict(
        np.c_[xx.ravel(), yy.ravel()])  # np.c_ :Translates slice objects to concatenation along the second axis
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot the training points
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()


def exDiabets():
    diabetes = datasets.load_diabetes()
    diabetes.data[0]  # first ten values of first patient

    # try wit age measurements, you will get something close to 1
    np.sum(diabetes.data[:, 0] ** 2)

    from sklearn import linear_model
    linreg = linear_model.LinearRegression()
    diabetes = datasets.load_diabetes()
    x_train = diabetes.data[:-20]  # train set of 442 - last 20
    y_train = diabetes.target[:-20]
    x_test = diabetes.data[-20:]  # test set of last 20
    y_test = diabetes.target[-20:]

    # now apply the training set thru the use of the fit() funct.
    linreg.fit(x_train, y_train)
    print(linreg.coef_)
    print(linreg.predict(x_test))
    print(linreg.score(x_test, y_test))

    # taking account a single physiological factor (age in this case)
    diabetes = datasets.load_diabetes()
    x_train = diabetes.data[:-20]  # train set of 442 - last 20
    y_train = diabetes.target[:-20]
    x_test = diabetes.data[-20:]  # test set of last 20
    y_test = diabetes.target[-20:]

    x0_test = x_test[:, 0]
    x0_train = x_train[:, 0]
    x0_test = x0_test[:, np.newaxis]
    x0_train = x0_train[:, np.newaxis]
    linreg = linear_model.LinearRegression()
    linreg.fit(x0_train, y_train)
    y = linreg.predict(x0_test)
    plt.scatter(x0_test, y_test, color='k')
    plt.plot(x0_test, y, color='b', linewidth=3)
    plt.show()

    diabetes = datasets.load_diabetes()
    x_train = diabetes.data[:-20]  # train set of 442 - last 20
    y_train = diabetes.target[:-20]
    x_test = diabetes.data[-20:]  # test set of last 20
    y_test = diabetes.target[-20:]
    plt.figure(figsize=(8, 12))
    for f in range(0, 10):  # need this to loop through each feature (10 models)
        xi_test = x_test[:, f]  # f is each col or feature
        xi_train = x_train[:, f]  # loop through all rows
        xi_test = xi_test[:, np.newaxis]  # build a new dimension to hold next datum
        xi_train = xi_train[:, np.newaxis]  # with train data too
        linreg.fit(xi_train, y_train)  # now we fit (model)
        y = linreg.predict(xi_test)  # use prediction
        plt.subplot(5, 2, f + 1)  # 5 by 2 graphs, f+1 to iterate next one
        plt.scatter(xi_test, y_test, color='k')
        plt.plot(xi_test, y, color='b', linewidth=3)
        
    plt.show()

if __name__ == '__main__':
    # exIris()
    # exKNN()
    exDiabets()
