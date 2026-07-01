import snappy
# Compare the filling core with the systole and test uniqueness for m137(s,1)
print(f"{'s':^3}  {'core':^12}  {'systole':^12}"
      f"{'core=systole?':^15}  {'unique?':^8}")
print("-" * 56)
for s in range(-25, 26):
    if s in {-2, -1, 0, 1}:
        print(f"{s:3d}  {'---':>12}  {'---':>12}  {'nonhyperbolic':>15}")
        continue
    M = snappy.Manifold(f"m137({s},1)")
    core = M.cusp_info(0).core_length.real()
    try:
        LS = M.length_spectrum(1.5, include_words=True)
        systole = LS[0].length.real()
        unique = abs(LS[0].length.real() - LS[1].length.real()) > 1e-10
    except RuntimeError:
        LS = M.length_spectrum_alt(count=4, verified=True, bits_prec=200)
        systole = LS[0].length.real().center()
        ordinary = [g for g in LS if g.core_curve is None]
        unique = ordinary[0].length.real().upper() < \
            ordinary[1].length.real().lower()
    core_is_systole = abs(core - systole) < 1e-10
    print(f"{s:3d}  {core:12.8f}  {systole:12.8f}"
      f"{str(core_is_systole):^15}  {str(unique):^8}")