suanfa = ['random_state', 'solver', 'liblinear', 'lbfgs', 'newton-cg', 'sag', 'saga']

for i in range(len(suanfa) - 1):
    for j in range(100, 1001, 100):
        for k in range(1000, 10000, 1000):
            lr = LR(C=j, random_state=k, solver=suanfa[i])
            lr.fit(x_train, y_train)
            R = lr.predict(x_test)
            # result(y_test, R)
