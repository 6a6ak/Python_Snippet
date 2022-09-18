import numpy as np
import matplotlib.pyplot as plt
t=np.arange (0,5,0.1)
plt.plot ([1,2,3,4],[1,2,3,4], 'or')
plt.plot (t,t**2,'g^')
plt.plot (t,t**3,'b--')
plt.ylabel('Y');plt.xlabel('X')
plt.show()