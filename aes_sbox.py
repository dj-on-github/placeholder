def sbox_prob(sbox_in, sbox_out):
    x = list(8)
    s = list(8)
    
    # Input
    for i in xrange(8):
        x[i] = sbox_in[i]
    
    x0 = x[7]
    x1 = x[6]
    x2 = x[5]
    x3 = x[4]
    x4 = x[3]
    x5 = x[2]
    x6 = x[1]
    x7 = x[0]
    
    # Upper Transform
    
    y14 = xor_prob(x3, x5)
    y13 = xor_prob(x0, x6)
    y9 = xor_prob(x0, x3)
    y8 = xor_prob(x0, x5)
    t0 = xor_prob(x1, x2)
    y1 = xor_prob(t0, x7)
    y4 = xor_prob(y1, x3)
    y12 = xor_prob(y13, y14)
    y2 = xor_prob(y1, x0)
    y5 = xor_prob(y1, x6)
    y3 = xor_prob(y5, y8)
    t1 = xor_prob(x4, y12)
    y15 = xor_prob(t1, x5)
    y20 = xor_prob(t1, x1)
    y6 = xor_prob(y15, x7)
    y10 = xor_prob(y15, t0)
    y11 = xor_prob(y20, y9)
    y7 = xor_prob(x7, y11)
    y17 = xor_prob(y10, y11)
    y19 = xor_prob(y10, y8)
    y16 = xor_prob(t0, y11)
    y21 = xor_prob(y13, y16)
    y18 = xor_prob(x0, y16)
    
    / Middle Transform
    t2 = and_prob(y12, y15)
    t3 = and_prob(y3, y6)
    t4 = xor_prob(t3, t2)
    t5 = and_prob(y4, x7)
    t6 = xor_prob(t5, t2)
    t7 = and_prob(y13, y16)
    t8 = and_prob(y5, y1)
    t9 = xor_prob(t8, t7)
    t10 = and_prob(y2, y7)
    t11 = xor_prob(t10, t7)
    t12 = and_prob(y9, y11)
    t13 = and_prob(y14, y17)
    t14 = xor_prob(t13, t12)
    t15 = and_prob(y8, y10)
    t16 = xor_prob(t15, t12)
    t17 = xor_prob(t4, t14)
    t18 = xor_prob(t6, t16)
    t19 = xor_prob(t9, t14)
    t20 = xor_prob(t11, t16)
    t21 = xor_prob(t17, y20)
    t22 = xor_prob(t18, y19)
    t23 = xor_prob(t19, y21)
    t24 = xor_prob(t20, y18)
    
    t25 = xor_prob(t21, t22)
    t26 = and_prob(t21, t23)
    t27 = xor_prob(t24, t26)
    t28 = and_prob(t25, t27)
    t29 = xor_prob(t28, t22)
    t30 = xor_prob(t23, t24)
    t31 = xor_prob(t22, t26)
    t32 = and_prob(t31, t30)
    t33 = xor_prob(t32, t24)
    t34 = xor_prob(t23, t33)
    t35 = xor_prob(t27, t33)
    t36 = and_prob(t24, t35)
    t37 = xor_prob(t36, t34)
    t38 = xor_prob(t27, t36)
    t39 = and_prob(t29, t38)
    t40 = xor_prob(t25, t39)
    
    t41 = xor_prob(t40, t37)
    t42 = xor_prob(t29, t33)
    t43 = xor_prob(t29, t40)
    t44 = xor_prob(t33, t37)
    t45 = xor_prob(t42, t41)
    z0 = and_prob(t44, y15)
    z1 = and_prob(t37, y6)
    z2 = and_prob(t33, x7)
    z3 = and_prob(t43, y16)
    z4 = and_prob(t40, y1)
    z5 = and_prob(t29, y7)
    z6 = and_prob(t42, y11)
    z7 = and_prob(t45, y17)
    z8 = and_prob(t41, y10)
    z9 = and_prob(t44, y12)
    z10 = and_prob(t37, y3)
    z11 = and_prob(t33, y4)
    z12 = and_prob(t43, y13)
    z13 = and_prob(t40, y5)
    z14 = and_prob(t29, y2)
    z15 = and_prob(t42, y9)
    z16 = and_prob(t45, y14)
    z17 = and_prob(t41, y8)
    
    # Bottom Transform
    t46 = xor_prob(z15, z16)
    t47 = xor_prob(z10, z11)
    t48 = xor_prob(z5, z13)
    t49 = xor_prob(z9, z10)
    t50 = xor_prob(z2, z12)
    t51 = xor_prob(z2, z5)
    t52 = xor_prob(z7, z8)
    t53 = xor_prob(z0, z3)
    t54 = xor_prob(z6, z7)
    t55 = xor_prob(z16, z17)
    t56 = xor_prob(z12, t48)
    t57 = xor_prob(t50, t53)
    t58 = xor_prob(z4, t46)
    t59 = xor_prob(z3, t54)
    t60 = xor_prob(t46, t57)
    t61 = xor_prob(z14, t57)
    t62 = xor_prob(t52, t58)
    t63 = xor_prob(t49, t58)
    t64 = xor_prob(z4, t59)
    t65 = xor_prob(t61, t62)
    t66 = xor_prob(z1, t63)
    s0 = xor_prob(t59, t63)
    s6 = 1.0-xor_prob((t56, t62))
    s7 = 1.0-xor_prob((t48, t60))
    t67 = xor_prob(t64, t65)
    s3 = xor_prob(t53, t66)
    s4 = xor_prob(t51, t66)
    s5 = xor_prob(t47, t65)
    s1 = 1.0-xor_prob((t64, s3))
    s2 = 1.0-xor_prob((t55, t67))
    
    # output
    s[0] = s7
    s[1] = s6
    s[2] = s5
    s[3] = s4
    s[4] = s3
    s[5] = s2
    s[6] = s1
    s[7] = s0
    
    for i in xrange(8):
        sbox_out[i] = s[i]
    
    return sbox_out

