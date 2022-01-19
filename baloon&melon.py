import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

N = 500
data_balloons = pd.DataFrame({ 'width': np.random.normal(20, 1, N ),
            'height': np.random.normal(15, 1, N ),
            'weight': np.random.normal(1, 2, N )
})

data_melon = pd.DataFrame({ 'width': np.random.normal(20, 1, N ),
            'height': np.random.normal(10, 1, N ),
            'weight': np.random.normal(100, 2, N )
})

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection = '3d')

ax.scatter(xs= data_balloons['width'], ys= data_balloons['height'], zs= data_balloons['weight'], color= 'green', marker= 'o', s= 20)
ax.scatter(xs= data_melon['width'], ys= data_melon['height'], zs= data_melon['weight'], color= 'red', marker= '^', s= 20)

ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Weight')

ax.set_title('balloon & melon')
plt.show()