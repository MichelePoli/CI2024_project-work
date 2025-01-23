import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


# Example: f0
def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5


# For problem 1: Formula -> (x0 div (cosh (log10 (abs (abs (tan (log 10.0)))))))
def f1(x: np.ndarray) -> np.ndarray:
    return x[0] / np.cosh(np.log10(np.abs(np.abs(np.tan(np.log(10.0))))))


# For problem 2: Formula -> (abs ((tanh (tan 34242.424242424226)) pow x0))
def f2(x: np.ndarray) -> np.ndarray:
    return np.abs(np.tanh(np.tan(34242.424242424226)) ** x[0])


# For problem 3: Formula -> (cosh (sqrt (abs (log2 (abs (abs (sqrt (1.6875 mod x1))))))))
def f3(x: np.ndarray) -> np.ndarray:
    return np.cosh(np.sqrt(np.abs(np.log2(np.abs(np.abs(np.sqrt(1.6875 % x[1])))))))


# For problem 4: Formula -> (sinh (exp (tanh ((8.020833333333332 div ((cos x1) mod 6.041666666666666)) sub 5.645833333333333))))
def f4(x: np.ndarray) -> np.ndarray:
    return np.sinh(np.exp(np.tanh(((8.020833333333332 / (np.cos(x[1]) % 6.041666666666666)) - 5.645833333333333))))


# For problem 5: Formula -> ((log2 (exp ((log2 ((sin 2.4791666666666665) mod 5.645833333333333)) mul (exp 3.6666666666666665)))) mul (tanh (exp ((log2 ((sin 2.4791666666666665) mod 5.645833333333333)) mul (exp 3.6666666666666665)))))
def f5(x: np.ndarray) -> np.ndarray:
    return (np.log2(np.exp(np.log2((np.sin(2.4791666666666665) % 5.645833333333333)) * np.exp(3.6666666666666665)))) * \
           np.tanh(np.exp(np.log2((np.sin(2.4791666666666665) % 5.645833333333333)) * np.exp(3.6666666666666665)))


# For problem 6: Formula -> (((((x1 mul (10.0 pow 0.3020408163265306)) mul (sqrt (cos (tanh 2.1204081632653065)))) sub (exp (cos (log10 (log10 1.3122448979591839))))) add (log2 (cosh (cosh 0.5040816326530613)))) div (cos (log (cosh (tanh ((sqrt x1) pow 2.7265306122448982))))))
def f6(x: np.ndarray) -> np.ndarray:
    return (((((x[1] * (10.0 ** 0.3020408163265306)) * np.sqrt(np.cos(np.tanh(2.1204081632653065)))) - 
             np.exp(np.cos(np.log10(np.log10(1.3122448979591839))))) + 
            np.log2(np.cosh(np.cosh(0.5040816326530613)))) / np.cos(np.log(np.cosh(np.tanh(np.sqrt(x[1]) ** 2.7265306122448982)))))


# For problem 7: Formula -> (exp (log2 (exp (x0 mul x1))))
def f7(x: np.ndarray) -> np.ndarray:
    return np.exp(np.log2(np.exp(x[0] * x[1])))


# For problem 8: Formula -> (cos (sqrt ((x5 pow x5) add (sin x3))))
def f8(x: np.ndarray) -> np.ndarray:
    return np.cos(np.sqrt((x[5] ** x[5]) + np.sin(x[3])))

