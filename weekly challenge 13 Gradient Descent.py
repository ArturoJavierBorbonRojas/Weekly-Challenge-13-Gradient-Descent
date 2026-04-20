import numpy as np
import matplotlib.pyplot as plt

# Weekly Challenge 13: Gradient Descent Optimization
# Author: Ing. Arturo Javier Borbon Rojas

# 1 We are going to define the cost function and its derivative
# we will use this equation: f(x) = x**2
def cost_function(x):
    return x**2

# 2 The derivative is 2x. This equation give is the slope at any point.
def gradient(x):
    return 2*x

# 3 We set the Hyperparameters
#learning_rate= 0.1 # The size of a step we take aka alpha
learning_rate= np.random.uniform(0.01, 0.3)
iterations = 20  # Max number of steps
#start_x = 8.0   # Our starting position on the curve
start_x= np.random.randint(0,10)

# 4 We print our data
print("-"* 50)
print("Gradient Descent Process")
print("Our values")
print(f"""Initial x: {start_x}
          Learning Rate:{learning_rate}
      """)
print("-"* 50)

# 5 We start the algorithm
x_current = start_x
history_x =[x_current]
history_y = [cost_function(x_current)]

for i in range(iterations):
    # Here the calculate the slope (its derivative) at the current position
    current_gradient= gradient(x_current)

    # Update the position: take a step in the opposite direction of the slope
    x_new = x_current - (learning_rate * current_gradient)

    # The save this for visualization
    history_x.append(x_new)
    history_y.append(cost_function(x_new))

    # Print progress
    print(f"""Step {i+1} 
            x: {x_new}
            Cost (Error): {cost_function(x_new)} 
""")
    

    # Update current x for the next loop
    x_current= x_new

print("-"*50)
print(f"Optimization finished. The minium was found at x={x_current}")


# 6 Visualization with Matplotlib
# We generate a cruve for the background
x_curve= np.linspace(-9,9,100)
y_curve= cost_function(x_curve)

plt.figure(figsize=(6,6))

# Plot the cost function The hill
plt.plot(x_curve,y_curve, color="blue", linewidth=2, label="Cost Function f(x)=x^2")

# Plot the path of our optimization point
plt.plot(history_x, history_y, color="red", marker="o", linestyle=":", markersize=5, label="Gradient Descent Path")

# Hihjlight the starting and ending points
plt.scatter(history_x[0], history_y[0], color="green", s=150, zorder=5, label="Start")
plt.scatter(history_x[-1], history_y[-1], color="gold", marker="*", s=250, edgecolor="black", zorder=5, label="Mininum (Goal)")

plt.title("Gradient Descent Optimization")
plt.xlabel("Parameter (x)")
plt.ylabel("Cost/Error (y)")
plt.legend()
plt.grid(True)
plt.show()
