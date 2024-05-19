# Define the parameters for the secp256k1 curve
P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
A = 0x0000000000000000000000000000000000000000000000000000000000000000
B = 0x0000000000000000000000000000000000000000000000000000000000000007
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
def point_add(p, q):
    if p is None:
        return q
    if q is None:
        return p
    x_p, y_p = p
    x_q, y_q = q
    if p != q:
        slope = (y_q - y_p) * pow(x_q - x_p, -1, P) % P
    else:
        slope = (3 * x_p * x_p + A) * pow(2 * y_p, -1, P) % P
    x_r = (slope * slope - x_p - x_q) % P
    y_r = (slope * (x_p - x_r) - y_p) % P
    return x_r, y_r
def scalar_multiply(k, point):
    result = None
    for i in range(256):
        if k & (1 << i):
            result = point_add(result, point)
        point = point_add(point, point)
    return result

# Generate a private key (an integer between 1 and N-1)
private_key = 0x5375726268692070697975736820726f73686e69

# Calculate the corresponding public key (point on the curve)
x, y = scalar_multiply(private_key, (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8))

# Ensure x and y are within the valid range [1, P-1] and satisfy the elliptic curve equation
if 1 < x < P - 1 and 1 < y < P - 1 and (y**2) % P == (x**3 + A * x + B) % P:
    print("Public Key (x, y):", hex(x), hex(y))
else:
    print("Invalid public key")