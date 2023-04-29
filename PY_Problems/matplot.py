import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,20)
y = np.arange(1,20)

plt.title('Dt')
plt.xlabel('time')
plt.ylabel('distance')
plt.plot(x,y)
print(plt.show())