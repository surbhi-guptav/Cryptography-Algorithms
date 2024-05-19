import matplotlib.pyplot as plt
import numpy as np

# Define the elliptic curve parameters
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0x0000000000000000000000000000000000000000000000000000000000000000
B = 0x0000000000000000000000000000000000000000000000000000000000000007

# Given point
x = 0x336b0c20d45bfd8a3cbfe564773f9857edff30ce04e2e0db1b23302b6247f869
y = 0xf01e1fec960a07710e362462235b5c1f4aca83b888cba5fc954c5a77345d1332

# Check if the point is on the curve
if (y**2) % P == (x**3 + A * x + B) % P:
    # Generate points for the curve
    x_values = np.linspace(0, P, 1000)
    y_values_positive = np.sqrt(x_values**3 + A * x_values + B) % P
    y_values_negative = -np.sqrt(x_values**3 + A * x_values + B) % P

    # Plot the elliptic curve
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values_positive, label='Positive y')
    plt.plot(x_values, y_values_negative, label='Negative y')
    plt.scatter(x, y, color='red', label='Given Point (x, y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Elliptic Curve')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("The provided point is not on the elliptic curve.")


