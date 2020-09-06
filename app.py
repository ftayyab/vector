from vector import Vector

def run():
    v = Vector([8.218, -9.341])
    w = Vector([-1.129, 2.111])
    #print v == w
    #print v.add(w)

    v = Vector([7.119, 8.215])
    w = Vector([-8.223, 0.878])
    #print v.sub(w)

    v = Vector([1.671, -1.012, -0.318])
    n = 7.41
    #print v.scalarMul(n)

    v = Vector([-0.221, 7.437])
    #print v.magnitude()

    v = Vector([8.813, -1.331, -6.247])
    #print v.magnitude()

    v = Vector([5.581, -2.136])
    #print v.normalize()

    v = Vector([1.996, 3.108, -4.554])
    #print v.normalize()

    v = Vector([7.887, 4.138])
    w = Vector([-8.802, 6.776])
    #print v.product(w)

    v = Vector([-5.955, -4.904, -1.874])
    w = Vector([-4.496, -8.755, 7.103])
    #print v.product(w)
    
    v = Vector([3.183, -7.627])
    w = Vector([-2.668, 5.319])
    #print v.productAngle(w)

    v = Vector([7.35, 0.221, 5.188])
    w = Vector([2.751, 8.259, 3.985])
    #print v.productAngle(w, False)

    v = Vector([-7.579, -7.88])
    w = Vector([22.737, 23.64])

    #print v.is_parallel(w)
    #print v.is_ortogonal(w)

    v = Vector([-2.029, 9.97, 4.172])
    w = Vector([-9.231, -6.639, -7.245])

    #print v.is_parallel(w)
    #print v.is_ortogonal(w)

    v = Vector([-2.328, -7.284, -1.214])
    w = Vector([-1.821, 1.072, -2.94])

    #print v.is_parallel(w)
    #print v.is_ortogonal(w)
    
    v = Vector([2.118, 4.827])
    w = Vector([0, 0 ])

    #print v.is_parallel(w)
    #print v.is_ortogonal(w)

    v = Vector([3.039, 1.879])
    b = Vector([0.825, 2.036])

    v_parallel  = v.project(b)
    
    v = Vector([-2.328, -7.284, -1.214])
    
    v_prependicular = v.sub(v_parallel)
    
    #v = Vector([5.581, -2.136])
    #print v.normalize()
    #print v.project(w)

if __name__=='__main__':
    run()