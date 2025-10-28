# Simple Linear Regression (no libraries)



# Input data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Step 1: Calculate means
n = len(x)
sum_x = sum(x)
sum_y = sum(y)

mean_x = sum_x / n
mean_y = sum_y / n

# Step 2: Calculate b1 (slope)
num = 0
den = 0
for i in range(n):
    num += (x[i] - mean_x) * (y[i] - mean_y)
    den += (x[i] - mean_x) ** 2

b1 = num / den

# Step 3: Calculate b0 (intercept)
b0 = mean_y - b1 * mean_x

# Step 4: Print regression line
print(f"Regression coefficient (b1): {b1}")
print(f"Intercept (b0): {b0}")
print(f"Regression line: y = {b0:.2f} + {b1:.2f}x")

# Step 5: Example prediction
x_new = 6
y_pred = b0 + b1 * x_new
print(f"Predicted value at x={x_new}: {y_pred:.2f}")
