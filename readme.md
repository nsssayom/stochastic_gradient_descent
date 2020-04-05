# Stochastic Gradient Descent Demo using P5 Python

Stochastic gradient descent (often abbreviated SGD) is an iterative method for optimizing an objective function with suitable smoothness properties (e.g. differentiable or subdifferentiable). It can be regarded as a stochastic approximation of gradient descent optimization, since it replaces the actual gradient (calculated from the entire data set) by an estimate thereof (calculated from a randomly selected subset of the data). [1]

## Prerequisites

This project is built and tested with Ubuntu 18.04 LTS. The target system needs libglfw to be installed.

```bash
sudo apt-get install libglfw
```

## Deployment

Clone the git repository

```bash
git clone https://github.com/nsssayom/stochastic_gradient_descent.git
```

Create a **python3** virtual environemnt using [virtualenv](https://pypi.org/project/virtualenv/)

```bash
virtualenv -p python3 env
```

install the required libraries

```bash
source env/bin/activate
pip install p5
pip install Shapely
```

Now run the project

```bash
python3 main.py
```

## Usage

Click on the window to create data points. Gradient line will appear when there is more than one point on screen. Use UP and DOWN arrow key to adjust learning rate. Press **R** to reset data points and **ESC** to exit.

![Demonstration](https://i.imgur.com/jhWMQGI.png)

## Built With

* [Python](https://www.python.org/) - Programming Language
* [p5py](https://github.com/p5py/p5) - Python Library for high level drawing functionality
* [Shapely](https://github.com/Toblerity/Shapely) - Python Library for anipulation and analysis of geometric objects in the Cartesian plane.
* [pip](https://pip.pypa.io/en/stable/reference/) - Dependency Management
* [flake8](https://pypi.org/project/flake8/) - Linting and Code Formatting

## Author

* **Sayom Shakib**

This work is based on [Dr. Debajyoti Karmaker's](https://scholar.google.com.au/citations?user=7sHKEusAAAAJ) demostration of this algorithm implemented with [p5js](https://p5js.org/).

## License

This project is licensed under the GNU Public License.

## Reference

* Taddy, Matt (2019). "Stochastic Gradient Descent". Business Data Science: Combining Machine Learning and Economics to Optimize, Automate, and Accelerate Business Decisions. New York: McGraw-Hill. pp. 303–307. ISBN 978-1-260-45277-8.
