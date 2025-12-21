import numpy as np
temperature = np.array([30, 32, 35, 28, 40, 33, 29])
total_temp = np.sum(temperature)
avg_temp = total_temp / len(temperature)
print("Daily Temperatures:", temperature)
print("Total Temperature:", total_temp)
print("Average Temperature:", avg_temp)
print("High temperature days index (>35):", np.where(temperature > 35))
print("Low temperature days index (<30):", np.where(temperature < 30))
