import snappy
# Compare the filling core with the systole and test uniqueness for t12072(s,1)
print(f"{'s':^3}  {'core':^12}  {'systole':^12}"
      f"{'core=systole?':^15}  {'unique?':^8}")
print("-" * 56)
for s in range(-35, 36):
    M = snappy.Manifold(f"t12072({s},1)")
    core = M.cusp_info(0).core_length.real()
    LS = M.length_spectrum_alt(count=4, verified=True, bits_prec=200)
    systole = LS[0].length.real()
    core_is_systole = abs(core - systole.center()) < 1e-10
    unique = systole.upper() < LS[1].length.real().lower()
    print(f"{s:3d}  {core:12.8f}  {systole.center():12.8f}"
        f"{str(core_is_systole):^15}  {str(unique):^8}")