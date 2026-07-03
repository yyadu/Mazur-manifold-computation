import snappy
# Volumes of Dehn fillings X(k,1) of X
X = snappy.Manifold('DT: [(14,12,-16,-10,18,-6),(-4,2,8)], [1,1,0,0,0,1,1,0,1]')
X.dehn_fill((0,1),1)
X = X.filled_triangulation()
Xid = X.identify()
print("Mazur knot exterior X")
print("Volume =", X.volume())
print("Isometric to census manifold:", Xid, "\n")
M = snappy.Manifold("m137")
print("Volumes of some integral Dehn fillings:\n")
print(f"{'k':^5}  {'vol(X(k,1r))':>15}  {'vol(m137(k+3r,1r))':>15}  {'equal?':>7}")
print("-" * 50)
k_values = list(range(-1000, -994)) + list(range(-20, 21)) + list(range(994, 1001))
for k in k_values:
    if k in {-5, -4, -3, -2}:
        print(f"{k:5d}  {'nonhyperbolic':>15}")
        continue
    DFX = X.copy()
    DFX.dehn_fill((k,1),0)
    vDFX = DFX.volume()
    DFM = M.copy()
    DFM.dehn_fill((k+3,1),0)
    vDFM = DFM.volume()
    equal = abs(vDFX - vDFM) < 1e-10
    print(f"{k:5d}  {vDFX:15.10f}  {vDFM:15.10f} {str(equal):>7}")
print()
print("Verify vol(X(k,1)) strictly increases as k increases from -1 to 1000:")
flag = True
X1 = X.copy()
X1.dehn_fill((-1,1),0)
v1 = X1.volume()
for k in range(0,1001):
    X2 = X.copy()
    X2.dehn_fill((k,1),0)
    v2 = X2.volume()
    #print(f"{k} {v1} {v2}")
    if v1 < v2:
        v1 = v2
        continue
    else:
        flag = False
        print(f"Volume stopped increasing at k = {k}")
        break
print(f"{flag}")
print()
print("Verify vol(X(k,1)) strictly increases as k decreases from -6 to -1000:")
flag = True
X1 = X.copy()
X1.dehn_fill((-6,1),0)
v1 = X1.volume()
for k in range(-7,-1001,-1):
    X2 = X.copy()
    X2.dehn_fill((k,1),0)
    v2 = X2.volume()
    #print(f"{k} {v1} {v2}")
    if v1 < v2:
        v1 = v2
        continue
    else:
        flag = False
        print(f"Volume stopped increasing at k = {k}")
        break
print(f"{flag}")