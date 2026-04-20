# Weekly-Challenge-13-Gradient-Descent
Welcome to Week 13! To kick off my second trimester of coding challenges, I decided to program the core mathematical engine behind Deep Learning and Neural Networks: Gradient Descent.

Gradient Descent is a first-order iterative optimization algorithm used to find a local minimum of a differentiable function. In Machine Learning, this function is the "Cost Function" (or Loss Function), and finding its minimum means we have minimized the AI's error.
In this case I used pseudorandom values in learning rate and start_x to add fun.

## ⚙️ How it works
1. **The Function:** We define a simple convex cost function, $f(x) = x^2$.
2. **The Derivative:** We calculate its gradient (slope), $f'(x) = 2x$.
3. **The Learning Rate:** We define an $\alpha$ (alpha) of `0.1` to control the step size.
4. **The Update Rule:** In a loop, the algorithm updates its position by taking a step in the opposite direction of the gradient using the formula:
   $$x_{new} = x_{old} - \alpha \cdot \nabla f(x_{old})$$
5. **Visualization:** Matplotlib plots the parabola and traces the "steps" the algorithm took to roll down the hill and find the minimum error (zero).

## 🚀 Complexity Analysis
* **Time Complexity:** $O(I)$ where $I$ is the number of iterations. The math operations inside the loop execute in constant $O(1)$ time.
* **Space Complexity:** $O(I)$ since we store the $x$ and $y$ values of every step to visualize the trajectory later.

## 🛠 Dependencies
* Python 3.x
* NumPy
* Matplotlib
