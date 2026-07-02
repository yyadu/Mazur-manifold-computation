import snappy
# Drill the unique systolic geodesic for the remaining
# hyperbolic fillings of m137(s,1)
print(f"{'s':^3}  {'systole':^12}  {'systole drilled manifold'}")
print("-" * 82)
for s in [-4,-3,2,3]:
    M = snappy.Manifold(f"m137({s},1)")
    D = M.drill(0)
    D.dehn_fill((1,0),1)
    F = D.filled_triangulation([0])
    g = F.length_spectrum_alt(count=1, verified=True, bits_prec=200)[0]
    H = F.drill_word(g.word, verified=True, bits_prec=200)
    print(f"{s:3d}  {g.length.real().center():12.8f}  {H.identify()}")