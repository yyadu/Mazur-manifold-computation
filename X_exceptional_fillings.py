import snappy
from sage.all import gap
# Mazur knot exterior X
X = snappy.Manifold('DT: [(14,12,-16,-10,18,-6),(-4,2,8)], [1,1,0,0,0,1,1,0,1]')
X.dehn_fill((0,1), 1)
X = X.filled_triangulation()
for n in range(5, 8):
    H = gap(f"AlternatingGroup({n})")
    print(f"Epimorphisms pi_1(X(k,1)) ->> A{n}")
    for k in range(-5, -1):
        CX = X.copy()
        CX.dehn_fill((k,1), 0)
        G = gap(CX.fundamental_group())
        Q = gap.GQuotients(G, H)
        print(f"  X({k},1): {len(Q)}")