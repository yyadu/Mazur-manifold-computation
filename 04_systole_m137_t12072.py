import snappy
# Systole of m137 and t12072
for name in ["m137", "t12072"]:
    M = snappy.Manifold(name)
    g = M.length_spectrum_alt(count=1, verified=True, bits_prec=100)[0]
    print(f"sys({name}) =", g.length.real())