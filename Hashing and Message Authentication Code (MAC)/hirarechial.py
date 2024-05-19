import hashlib

def merkle_hash(data):
    """Calculate the hash of a data block."""
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_tree(data):
    """Build a Merkle Tree from a list of data blocks."""
    if len(data) == 1:
        return data[0]
    
    # Ensure the number of data blocks is even.
    if len(data) % 2 != 0:
        data.append(data[-1])
    
    # Create a list to store the next level of the tree.
    next_level = []
    for i in range(0, len(data), 2):
        combined_hash = merkle_hash(data[i] + data[i + 1])
        next_level.append(combined_hash)
    
    # Recursively build the tree.
    return build_merkle_tree(next_level)

# Sample data blocks
data_blocks = ["ALice", "Bob","John"]

# Build the Merkle Tree
root_hash = build_merkle_tree(data_blocks)

print(f"Root Hash: {root_hash}")
