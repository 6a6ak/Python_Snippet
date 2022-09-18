import numpy as np
import matplotlib.pyplot as plt
data={
    'a': np.arange(50),
    'b': np.random.randint(0,50,50),
    'c':np.random.randn(50)
}
plt.scatter (data['a'],data['c'])
plt.ylabel('Y');plt.xlabel('X')
plt.show()