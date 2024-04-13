import numpy as np
import matplotlib.pyplot as plt

# Define parameters
r = 0.1  # growth rate
K = 1000  # carrying capacity
dt = 0.1  # time step size
num_steps = 1000  # number of time steps

# Initialize array to store population sizes
N_values = np.zeros(num_steps+1)
N_values[0] = 10  # initial population size

# Iterate over time steps to compute population sizes
for n in range(num_steps):
    N_values[n+1] = N_values[n] + r * dt * N_values[n] * (1 - N_values[n] / K)

# Plot population size over time
plt.plot(np.arange(num_steps+1) * dt, N_values, label='Population Size')
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Rabbit Population Growth (Difference Equation)')
plt.grid(True)

# Highlight the sequence of population sizes
for n in range(num_steps):
    plt.plot([n * dt, (n + 1) * dt], [N_values[n], N_values[n+1]], 'w--')  # Make the line dashed

plt.legend()
plt.show()
