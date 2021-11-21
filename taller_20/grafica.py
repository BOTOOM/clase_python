

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

t = 1.796
centro = 0
valor = 0.22
raiz = math.sqrt(valor)
x = np.linspace(centro - 6*raiz, centro + 6*raiz, 100)
plt.vlines(t, -0.1, 0.4, colors='g', lw=1, alpha=0.5)
plt.vlines(-t, -0.1, 0.4, colors='g', lw=1, alpha=0.5)
plt.vlines(2.757, -0.1, 0.4, colors='g', lw=1, alpha=0.5)
plt.plot(x, stats.norm.pdf(x, centro, raiz))
plt.show()