class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        x = init
        x_new = init
        for i in range(iterations):
            x_new = x - learning_rate * (2*x)
            x = x_new

        return round(x_new, 5)
