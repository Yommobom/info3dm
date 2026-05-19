import datasets2

X,Y = datasets2.load_nonlinear_example1()
ex_X = datasets2.polynomial2_features(X)
print(ex_X)
print(Y)