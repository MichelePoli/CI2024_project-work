import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Example: f0
# def f0(x: np.ndarray) -> np.ndarray:
#     return x[0] + np.sin(x[1]) / 5


# For problem 1: 
def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])


# For problem 2: 
def f2(x: np.ndarray) -> np.ndarray:
    return ((((x[0] + (0.75024 + -0.12047)) * np.square((330.89 - ((-0.86566 / x[0]) - (x[0] - (np.square(x[1]) * x[1] * x[2]))))))) / 0.086551)



# For problem 3: 
def f3(x: np.ndarray) -> np.ndarray:
    return (np.exp(np.sin((np.square(6.8302 - x[1])) + 3.9603))) + \
           ((11.053 - x[2]) + ((np.exp(0.00047697 - x[1])) - np.exp(x[1])) + np.square(x[0]))



# For problem 4: 
def f4(x: np.ndarray) -> np.ndarray:
    return np.exp(np.exp(np.cos(x[1]))) - np.sqrt(5)


# For problem 5:
def f5(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sin((np.exp((x[1] + x[0])) * -6.4885e-13)))


# For problem 6: 
def f6(x: np.ndarray) -> np.ndarray:
    return x[1] - np.abs(x[0] * np.cos(np.sqrt(np.abs(np.log(5) + np.pi) * 2)))


# For problem 7: 
def f7(x: np.ndarray) -> np.ndarray:
    return np.exp((((np.cos((x[1] * (x[1] - 0.13746))) + np.cos((x[0] * x[0]))) * -0.941) + (((x[1] * 0.78139) * x[0]) - 0.65089))) + 4.0888



# For problem 8: 
def f8(x: np.ndarray) -> np.ndarray:
    return x[5] * (np.exp(7) * np.log(np.pi))


