import snappy
# Jester knot exterior Y
Y = snappy.Manifold('DT: [(10,-20,-16,24,-14,22,18,-8,-4),(6,12,-2)],'
    '[1,1,0,1,0,0,1,1,1,0,1,0]')
Y.dehn_fill((0,1),1)
Y = Y.filled_triangulation()
Yid = Y.identify()
IsomY = Y.symmetry_group()
print("Jester knot exterior Y")
print("Volume =", Y.volume())
print("Isometric to census manifold:", Yid)
print("Cusp shape =", Y.cusp_info('shape'))
print("")
print("Is Y achiral?", IsomY.is_amphicheiral())
print("Order of isometry group =", IsomY.order())
print("Isometry group =", IsomY)
print("Self-isometries are:", IsomY.isometries(), "\n")
print("Isometries Y -> t12072 are:", Y.is_isometric_to(snappy.Manifold('t12072'),
    return_isometries=True))