import snappy
# Jester volume symmetry vol(Y(k,1))=vol(Y(-k-13,1))
# vol(t12072(s,1))=vol(t12072(-s-1,1))
Y = snappy.Manifold('DT: [(10,-20,-16,24,-14,22,18,-8,-4),(6,12,-2)],'
    '[1,1,0,1,0,0,1,1,1,0,1,0]')
Y.dehn_fill((0,1),1)
Y = Y.filled_triangulation()
Yid = Y.identify()
print("Jester knot exterior Y")
print("Volume =", Y.volume())
print("Isometric to census manifold:", Yid, "\n")
#T = snappy.Manifold("t12072")
print("Volumes of some integral Dehn fillings:\n")
print(f"{'k':^5}  {'vol(Y(k,1r))':>15}  {'vol(Y(-k-13r,1r))':>18}  {'equal?':>7}")
print("-" * 52)
k_values = list(range(-1000, -994)) + list(range(-20, 21)) + list(range(994, 1001))
for k in k_values:
    Y1 = Y.copy()
    Y1.dehn_fill((k,1),0)
    v1 = Y1.volume()
    Y2 = Y.copy()
    Y2.dehn_fill((-k-13,1),0)
    v2 = Y2.volume()
    equal = abs(v1 - v2) < 1e-10
    print(f"{k:5d}  {v1:15.10f}  {v2:18.10f} {str(equal):>7}")
print()
print("Verify vol(Y(k,1))=vol(Y(-k-13,1)) for -1000<=k<=1000:")
flag = True
for k in range(-1000,1001):
    Y1 = Y.copy()
    Y1.dehn_fill((k,1),0)
    v1 = Y1.volume()
    Y2 = Y.copy()
    Y2.dehn_fill((-k-13,1),0)
    v2 = Y2.volume()
    equal = abs(v1 - v2) < 1e-10
    #print(f"{k} {v1} {v2}")
    if equal:
        continue
    else:
        flag = False
        print(f"Volumes unequal at k = {k}")
        break
print(f"{flag}")