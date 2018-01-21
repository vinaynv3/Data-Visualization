import matplotlib.pyplot as plt
from pollen import walks

vi=walks(5000)
vi.st_wk()
plt.figure(dpi=128, figsize=(10,6))
point=list(range(vi.num_wk))
plt.plot(vi.x_t,vi.y_t, linewidth=1, zorder=1)
plt.scatter(0,0, c='Red', edgecolors='none', s=64, zorder=2)
plt.scatter(vi.x_t[-1],vi.y_t[-1], c='Green', edgecolors='none', s=64, zorder=2)
plt.show()
