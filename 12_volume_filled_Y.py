import snappy
# Volumes of Dehn fillings Y(k,1) of Y
Y = snappy.Manifold('DT: [(10,-20,-16,24,-14,22,18,-8,-4),(6,12,-2)],'
    '[1,1,0,1,0,0,1,1,1,0,1,0]')
Y.dehn_fill((0,1),1)
Y = Y.filled_triangulation()
Yid = Y.identify()
print("Jester knot exterior Y")
print("Volume =", Y.volume())
print("Isometric to census manifold:", Yid, "\n")
T = snappy.Manifold("t12072")
print("Volumes of some integral Dehn fillings:\n")
print(f"{'k':^5}  {'vol(Y(k,1r))':>15}  {'vol(t12072(k+6r,1r))':>18}  {'equal?':>7}")
print("-" * 53)
k_values = list(range(-1000, -994)) + list(range(-20, 21)) + list(range(994, 1001))
for k in k_values:
    DFY = Y.copy()
    DFY.dehn_fill((k,1),0)
    vDFY = DFY.volume()
    DFT = T.copy()
    DFT.dehn_fill((k+6,1),0)
    vDFT = DFT.volume()
    equal = abs(vDFY - vDFT) < 1e-10
    print(f"{k:5d}  {vDFY:15.10f}  {vDFT:18.10f} {str(equal):>7}")
print()
print("Verify vol(Y(k,1)) strictly increases as k increases from -6 to 1000:")
flag = True
Y1 = Y.copy()
Y1.dehn_fill((-6,1),0)
v1 = Y1.volume()
for k in range(-5,1001):
    Y2 = Y.copy()
    Y2.dehn_fill((k,1),0)
    v2 = Y2.volume()
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
print("Verify vol(Y(k,1)) strictly increases as k decreases from -7 to -1000:")
flag = True
Y1 = Y.copy()
Y1.dehn_fill((-7,1),0)
v1 = Y1.volume()
for k in range(-8,-1001,-1):
    Y2 = Y.copy()
    Y2.dehn_fill((k,1),0)
    v2 = Y2.volume()
    #print(f"{k} {v1} {v2}")
    if v1 < v2:
        v1 = v2
        continue
    else:
        flag = False
        print(f"Volume stopped increasing at k = {k}")
        break
print(f"{flag}")