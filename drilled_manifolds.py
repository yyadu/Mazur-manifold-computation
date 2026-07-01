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



import snappy
# Show that t12072(3,1) has exactly two systolic geodesics
# and that a self-isometry interchanges them.
M = snappy.Manifold("t12072(3,1)")
S = M.symmetric_triangulation()
print("Verified beginning of the length spectrum of t12072(3,1):")
LS = S.length_spectrum_alt(count=4, verified=True, bits_prec=1000)
for g in LS:
    print(g)
print()
print("Drilling each systolic geodesic:")
for g in LS[:2]:
    T = S.copy()
    U = T.drill_word(g.word, verified=True, bits_prec=1000)
    print(f"{g.word:<20} {U.identify()}")
# Drill both systolic geodesics, yielding a 2-cusped hyperbolic 3-manifold.
S.dehn_fill([(0,0),(0,0)])
print()
print("Self-isometries of the drilled manifold:")
for iso in S.is_isometric_to(S, return_isometries=True):
    print(iso)