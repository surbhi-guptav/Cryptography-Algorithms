import networkx as nx
import matplotlib.pyplot as plt
# ''' Import necessary libraries:
# networkx as nx: This imports the NetworkX library and gives it the alias nx.
# matplotlib.pyplot as plt: This imports the Matplotlib library's Pyplot module and gives it the alias plt. '''


# Function to create a binary tree graph
def create_binary_graph(input_bits):
    if len(input_bits) != 4:
        raise ValueError("Input must be a 4-bit binary string")

    G = nx.DiGraph()

    # Create the root node
    G.add_node(input_bits)

    # Create child nodes and edges
    for i in range(16):
        child_input = format(i, '04b')  # Convert to 4-bit binary
        G.add_node(child_input)
        G.add_edge(input_bits, child_input)

    return G
# '''This function, create_binary_graph, takes a 4-bit binary input (input_bits) as an argument.
# It first checks if the length of the input is exactly 4 bits, raising an exception if not.
# It creates an empty directed graph (G) using NetworkX.
# It adds the root node to the graph using the input binary string.
# It then creates 16 child nodes (4-bit binary strings) and adds edges from the root node to each child node. '''



# Test the binary graph creation
input_4_bit = "1010"
binary_graph = create_binary_graph(input_4_bit)

# ''' Here, input_4_bit is set to "1010" as an example input.
# The create_binary_graph function is called with this input, and the resulting graph is stored in binary_graph.'''


# Draw the binary graph
pos = nx.spring_layout(binary_graph, seed=42)
nx.draw(binary_graph, pos, with_labels=True, node_size=3000, node_color="skyblue")
plt.show()

# '''The nx.spring_layout function is used to specify the layout of the graph nodes. In this case, it uses a spring layout algorithm.
# nx.draw is called to draw the graph. It specifies that node labels should be shown (with_labels=True), sets the node size to 3000, and colors the nodes with "skyblue."
# Finally, plt.show() displays the graph.'''