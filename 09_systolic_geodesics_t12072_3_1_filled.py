import snappy
# Show that t12072(3,1) has exactly two systolic geodesics
# and that a self-isometry interchanges them
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