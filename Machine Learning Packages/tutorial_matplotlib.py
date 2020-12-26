# %% Matplotlib

''' Matpoltlib is a very popular Python library for data visualization. Like Pandas, it is not directly related to
Machine Learning. It particularly comes in handy when a programmer wants to visualize the patterns in the data. It is a
2D plotting library used for creating 2D graphs and plots. A module named pyplot makes it easy for programmers for plotting as
it provides features to control line styles, font properties, formatting axes, etc. It provides various kinds of graphs and plots
for data visualization, viz., histogram, error charts, bar chats, etc,
'''

#  Python program using Matplotib for forming a linear plot

# importing the necessary packages and modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
# from scipy.misc import imread, imresize

def ex1():
    # Prepare the data
    x = np.linspace(0, 10, 100)

    # Plot the data
    plt.plot(x, x, label='linear')

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

def ex2():
    # Compute the x and y coordinates for points on a sine curve
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)

    # Plot the points using matplotlib
    plt.plot(x, y)
    plt.show()  # You must call plt.show() to make graphics appear.

def ex3():
    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Plot the points using matplotlib
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    plt.show()

def ex3():
    # Compute the x and y coordinates for points on sine and cosine curves
    x = np.arange(0, 3 * np.pi, 0.1)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Set up a subplot grid that has height 2 and width 1,
    # and set the first such subplot as active.
    plt.subplot(2, 1, 1)

    # Make the first plot
    plt.plot(x, y_sin)
    plt.title('Sine')

    # Set the second subplot as active, and make the second plot.
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')

    # Show the figure.
    plt.show()

def ex4():
    img = imread('cat.jpg')
    img_tinted = img * [1, 0.95, 0.9]

    # Show the original image
    plt.subplot(1, 2, 1)
    plt.imshow(img)

    # Show the tinted image
    plt.subplot(1, 2, 2)

    # A slight gotcha with imshow is that it might give strange results
    # if presented with data that is not uint8. To work around this, we
    # explicitly cast the image to uint8 before displaying it.
    plt.imshow(np.uint8(img_tinted))
    plt.show()

def f(x, y):
    return (1 - y**5 + x**5) * np.exp(-x**2 - y**2)

def plotContour():
    dx = 0.01; dy = 0.01
    x = np.arange(-2.0, 2.0, dx)
    y = np.arange(-2.0, 2.0, dy)

    X, Y = np.meshgrid(x, y)
    C = plt.contour(X, Y, f(X, Y), 8, colors = 'red')
    # plt.contourf(X, Y, f(X, Y), 8)
    plt.contourf(X, Y, f(X, Y), 8, cmap = plt.cm.hot)
    plt.clabel(C, inline=1, fontsize=10)
    plt.show()

def plotPolar():
    N = 8
    theta = np.arange(0., 2 * np.pi, 2 * np.pi/N)
    radii = np.array([4, 7, 5, 3, 1, 5, 6, 7])
    plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
    #colors = np.array(['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#953579', '#4b5de4']) #rrggbb format
    colors = np.array(['lightgreen', 'darkred','navy','brown','violet','plum','yellow','darkgreen'])
    bars = plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0, color=colors)
    plt.show()

def plot3D():
    fig = plt.figure()
    ax = Axes3D(fig)

    x = np.arange(-2.0, 2.0, 0.1)
    y = np.arange(-2.0, 2.0, 0.1)

    X, Y = np.meshgrid(x, y)

    ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1, cmap=plt.cm.hot)
    ax.view_init(elev=30, azim=125)
    plt.show()

def plotScatter():
    xs = np.random.randint(30, 40, 100)
    ys = np.random.randint(20, 30, 100)
    zs = np.random.randint(10, 20, 100)

    xs2 = np.random.randint(50, 60, 100)
    ys2 = np.random.randint(30, 40, 100)
    zs2 = np.random.randint(50, 70, 100)

    xs3 = np.random.randint(10, 30, 100)
    ys3 = np.random.randint(40, 50, 100)
    zs3 = np.random.randint(40, 50, 100)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(xs, ys, zs)
    ax.scatter(xs2, ys2, zs2, c='r', marker='^')
    ax.scatter(xs3, ys3, zs3, c='g', marker='*')

    ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')
    plt.show()


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex3()
    # ex4()
    # plotContour()
    # plotPolar()
    # plot3D()
    plotScatter()