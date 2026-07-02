import snappy
# Drill the unique systolic geodesic for the remaining
# hyperbolic fillings of t12072(s,1)
print(f"{'s':^3}  {'systole':^12}  {'systole drilled manifold'}")
print("-" * 67)
for s in [-3,-2,-1,0,1,2]:
    M = snappy.Manifold(f"t12072({s},1)")
    g = M.length_spectrum(2.0, include_words=True)[0]
    H = M.drill_word(g.word)
    print(f"{s:3d}  {g.length.real():12.8f}  {H.identify()}")