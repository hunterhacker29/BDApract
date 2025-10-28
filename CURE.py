import math

# ---------------------------
# 1️⃣ Sample dataset
# ---------------------------
data = [
    [1, 2], [2, 1], [3, 1],   # cluster 1
    [8, 9], [9, 8], [8, 8],   # cluster 2
    [15, 1], [16, 2], [15, 2] # cluster 3
]

# ---------------------------
# 2️⃣ Distance function
# ---------------------------
def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

# ---------------------------
# 3️⃣ Merge clusters
# ---------------------------
def merge_clusters(c1, c2):
    return c1 + c2

# ---------------------------
# 4️⃣ CURE simplified
# ---------------------------
# Start: each point is a cluster
clusters = [[p] for p in data]

# Number of final clusters
k = 3

while len(clusters) > k:
    min_dist = float('inf')
    pair_to_merge = (0, 1)
    
    # Find closest pair of clusters
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            # Distance between clusters = min distance between points
            d = min(euclidean(p1, p2) for p1 in clusters[i] for p2 in clusters[j])
            if d < min_dist:
                min_dist = d
                pair_to_merge = (i, j)
    
    # Merge the closest clusters
    i, j = pair_to_merge
    clusters[i] = merge_clusters(clusters[i], clusters[j])
    clusters.pop(j)  # remove merged cluster

# ---------------------------
# 5️⃣ Print final clusters
# ---------------------------
for idx, cluster in enumerate(clusters):
    print(f"Cluster {idx+1}: {cluster}")






print("OR")





import math

# ---------------------------
# 1️⃣ Sample dataset (static)
# ---------------------------
p1 = [1, 2]
p2 = [2, 1]
p3 = [3, 1]

p4 = [8, 9]
p5 = [9, 8]
p6 = [8, 8]

# ---------------------------
# 2️⃣ Euclidean distance function (simple)
# ---------------------------
def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# ---------------------------
# 3️⃣ Merge clusters manually
# ---------------------------
# Step 1: merge cluster 1 points
cluster1 = [p1, p2, p3]

# Step 2: merge cluster 2 points
cluster2 = [p4, p5, p6]

# ---------------------------
# 4️⃣ Print clusters
# ---------------------------
print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)

# ---------------------------
# 5️⃣ Example: distance between clusters
# ---------------------------
d = distance(cluster1[0], cluster2[0])
print("Distance between first points of clusters:", d)
