import numpy as np

# Four web pages. Entry [i, j] = 1 if page j links to page i
# Page order: Home, Services, Booking, Contact
links = np.array([
    [0., 1., 1., 1.],
    [1., 0., 0., 0.],
    [1., 1., 0., 1.],
    [0., 0., 1., 0.]
])

# Column-normalise so each page shares its vote equally among its links
M = links / links.sum(axis=0)

damping = 0.85
n = M.shape[0]
G = damping * M + (1 - damping) / n * np.ones((n, n))

values, vectors = np.linalg.eig(G)
i = np.argmax(np.real(values))
rank = np.abs(np.real(vectors[:, i]))
rank = rank / rank.sum()

print("Dominant eigenvalue:", round(float(np.real(values[i])), 6))
for name, r in zip(["Home", "Services", "Booking", "Contact"], rank):
    print(f"{name:<9} PageRank = {r:.4f}")
