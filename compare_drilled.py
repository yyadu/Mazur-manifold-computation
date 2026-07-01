import snappy
names = ["m137", "t12072", "m081", "m011", "m004", "m038",
    "v3519", "v3200", "v2919", "v2911", "v3184", "v3505"]
manifolds = [snappy.Manifold(name) for name in names]
print("Checking pairwise isometry...")
duplicate = False
for i in range(len(manifolds)):
    for j in range(i + 1, len(manifolds)):
        if manifolds[i].is_isometric_to(manifolds[j]):
            duplicate = True
            print(f"{names[i]} is isometric to {names[j]}")
if not duplicate:
    print("All 12 manifolds are pairwise nonisometric.")