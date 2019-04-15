import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('Hard Policy.csv',delimiter=',')
data2 = pd.read_csv('Hard Value.csv',delimiter=',')


ax = data.plot(x='iter',y='convergence', label='Policy Iteration')
data2.plot(x='iter',y='convergence', ax=ax, label='Value Iteration')
ax.set_title("Hard Problem - Convergence (Delta) vs Iterations")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('Convergence')
plt.grid(True)
plt.savefig('./images/harditerconv')
plt.close()

ax = data.plot(x='iter',y='reward', label='Policy Iteration')
data2.plot(x='iter',y='reward', ax=ax, label='Value Iteration')
ax.set_title("Hard Problem - Reward vs Iterations")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('Reward')
plt.grid(True)
plt.savefig('./images/harditerrew')
plt.close()

ax = data.plot(x='iter',y='time', label='Policy Iteration')
data2.plot(x='iter',y='time', ax=ax, label='Value Iteration')
ax.set_title("Hard Problem - Time vs Iterations")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('Time')
plt.grid(True)
plt.savefig('./images/harditertime')
plt.close()

ax = data.plot(x='iter',y='steps', label='Policy Iteration')
data2.plot(x='iter',y='steps', ax=ax, label='Value Iteration')
ax.set_title("Hard Problem - Steps vs Iterations")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('# of Steps')
plt.grid(True)
plt.savefig('./images/harditersteps')
plt.close()


data = pd.read_csv('Hard Q-Learning L0.1 q0.0 E0.3.csv', delimiter=',')
data2 = pd.read_csv('Hard Q-Learning L0.9 q0.0 E0.3.csv', delimiter=',')
ax = data.plot(x='iter',y='convergence', label='alpha 0.1')
data2.plot(x='iter',y='convergence', ax=ax, label='alpha 0.9')
ax.set_title("Hard Problem - Q-Learning Effect of alpha")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('Convergence')
plt.grid(True)
plt.savefig('./images/hardqlrconv')
plt.close()



data = pd.read_csv('Hard Q-Learning L0.1 q0.0 E0.1.csv', delimiter=',')
data2 = pd.read_csv('Hard Q-Learning L0.1 q0.0 E0.3.csv', delimiter=',')
data3 = pd.read_csv('Hard Q-Learning L0.1 q0.0 E0.4.csv', delimiter=',')
ax = data.plot(x='iter', y='convergence', label='epsilon 0.1')
data2.plot(x='iter',y='convergence', ax=ax, label='epsilon 0.3')
data3.plot(x='iter',y='convergence', ax=ax, label='epsilon 0.4')
ax.set_title("Hard Problem - Q-Learning Effect of Epsilon")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('Convergence')
plt.grid(True)
plt.savefig('./images/hardqlepsilon',dpi=500)
plt.close()



data = pd.read_csv('Hard Q-Learning L0.1 q0.0 E0.4.csv', delimiter=',')
ax = data.plot(x='iter',y='reward', label='Policy Iteration')
ax.set_title("Hard Problem - Q-Learning (alpha=0.1,epsilon=0.4)")
ax.set_xlabel('# of Iterations')
ax.set_ylabel('Reward')
plt.grid(True)
plt.savefig('./images/hardqll01e04')
plt.close()	

