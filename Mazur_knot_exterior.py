import snappy
# Mazur knot exterior X
X = snappy.Manifold('DT: [(14,12,-16,-10,18,-6),(-4,2,8)], [1,1,0,0,0,1,1,0,1]')
X.dehn_fill((0,1),1)
X = X.filled_triangulation()
Xid = X.identify()
IsomX = X.symmetry_group()
print("Mazur knot exterior X")
print("Volume =", X.volume())
print("Isometric to census manifold:", Xid)
print("Cusp shape =", X.cusp_info('shape'))
print("")
print("Is X achiral?", IsomX.is_amphicheiral())
print("Order of isometry group =", IsomX.order())
print("Isometry group =", IsomX)
print("Self-isometries are:", IsomX.isometries(), "\n")
print("Isometries X -> m137 are:", X.is_isometric_to(snappy.Manifold('m137'),
    return_isometries=True))