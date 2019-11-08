import numpy as np

data = np.array([[50, 11, 18, 12], [18, 12, 23, 2], [21, 11, 35, 42], [47, 2, 12, 40]])
result = np.array([7681, 4019, 7160, 8080])
password = ''.join([chr(int(round(i))) for i in list(np.linalg.solve(data, result))])
print(password)