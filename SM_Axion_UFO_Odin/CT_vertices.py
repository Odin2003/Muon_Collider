# This file was automatically created by FeynRules 2.3.47
# Mathematica version: 12.1.1 for Mac OS X x86 (64-bit) (June 19, 2020)
# Date: Tue 7 May 2024 15:38:29


from .object_library import all_vertices, all_CTvertices, Vertex, CTVertex
from . import particles as P
from . import CT_couplings as C
from . import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_131_18,(0,0,1):C.R2GC_131_19})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_106_5,(2,0,1):C.R2GC_106_6,(0,0,0):C.R2GC_106_5,(0,0,1):C.R2GC_106_6,(6,0,0):C.R2GC_109_10,(6,0,1):C.R2GC_136_25,(4,0,0):C.R2GC_104_1,(4,0,1):C.R2GC_104_2,(3,0,0):C.R2GC_104_1,(3,0,1):C.R2GC_104_2,(8,0,0):C.R2GC_105_3,(8,0,1):C.R2GC_105_4,(7,0,0):C.R2GC_110_12,(7,0,1):C.R2GC_135_24,(5,0,0):C.R2GC_104_1,(5,0,1):C.R2GC_104_2,(1,0,0):C.R2GC_104_1,(1,0,1):C.R2GC_104_2,(11,3,0):C.R2GC_108_8,(11,3,1):C.R2GC_108_9,(10,3,0):C.R2GC_108_8,(10,3,1):C.R2GC_108_9,(9,3,1):C.R2GC_107_7,(2,1,0):C.R2GC_106_5,(2,1,1):C.R2GC_106_6,(0,1,0):C.R2GC_106_5,(0,1,1):C.R2GC_106_6,(4,1,0):C.R2GC_104_1,(4,1,1):C.R2GC_104_2,(3,1,0):C.R2GC_104_1,(3,1,1):C.R2GC_104_2,(8,1,0):C.R2GC_105_3,(8,1,1):C.R2GC_137_26,(6,1,0):C.R2GC_132_20,(6,1,1):C.R2GC_132_21,(7,1,0):C.R2GC_110_12,(7,1,1):C.R2GC_110_13,(5,1,0):C.R2GC_104_1,(5,1,1):C.R2GC_104_2,(1,1,0):C.R2GC_104_1,(1,1,1):C.R2GC_104_2,(2,2,0):C.R2GC_106_5,(2,2,1):C.R2GC_106_6,(0,2,0):C.R2GC_106_5,(0,2,1):C.R2GC_106_6,(4,2,0):C.R2GC_104_1,(4,2,1):C.R2GC_104_2,(3,2,0):C.R2GC_104_1,(3,2,1):C.R2GC_104_2,(8,2,0):C.R2GC_105_3,(8,2,1):C.R2GC_134_23,(6,2,0):C.R2GC_109_10,(6,2,1):C.R2GC_109_11,(7,2,0):C.R2GC_133_22,(7,2,1):C.R2GC_106_6,(5,2,0):C.R2GC_104_1,(5,2,1):C.R2GC_104_2,(1,2,0):C.R2GC_104_1,(1,2,1):C.R2GC_104_2})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.ax ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_142_29})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_146_32})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_114_16})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_114_16})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_114_16})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.d, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_111_14})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.s] ] ],
               couplings = {(0,0,0):C.R2GC_111_14})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_111_14})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_113_15})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_113_15})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_113_15})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_113_15})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_113_15})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_113_15})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_128_17})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_128_17})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_128_17})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_128_17})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_128_17})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_128_17})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_144_30,(0,1,0):C.R2GC_145_31})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_144_30,(0,1,0):C.R2GC_145_31})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_144_30,(0,1,0):C.R2GC_145_31})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_85_52,(0,1,0):C.R2GC_69_38})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_85_52,(0,1,0):C.R2GC_69_38})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_85_52,(0,1,0):C.R2GC_69_38})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_138_27})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_138_27})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_141_28,(0,1,0):C.R2GC_138_27})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_138_27})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_138_27})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_138_27})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV2, L.VV3, L.VV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,2,1):C.R2GC_63_33,(0,0,2):C.R2GC_64_34,(0,1,0):C.R2GC_78_39})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_66_36})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_89_53})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_81_44,(0,0,1):C.R2GC_81_45})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_84_50,(0,0,1):C.R2GC_84_51})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_79_40,(0,0,1):C.R2GC_79_41})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_83_48,(1,0,1):C.R2GC_83_49,(0,1,0):C.R2GC_82_46,(0,1,1):C.R2GC_82_47})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_80_42,(0,0,1):C.R2GC_80_43})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_67_37})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.g, P.g, P.ax, P.ax ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_65_35})

V_45 = CTVertex(name = 'V_45',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_131_29,(0,1,3):C.UVGC_131_30,(0,2,1):C.UVGC_91_59,(0,0,2):C.UVGC_92_60})

V_46 = CTVertex(name = 'V_46',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,2):C.UVGC_105_9,(2,0,3):C.UVGC_105_8,(0,0,2):C.UVGC_105_9,(0,0,3):C.UVGC_105_8,(6,0,1):C.UVGC_135_40,(6,0,2):C.UVGC_136_44,(6,0,3):C.UVGC_136_45,(6,0,4):C.UVGC_135_43,(4,0,2):C.UVGC_104_6,(4,0,3):C.UVGC_104_7,(3,0,2):C.UVGC_104_6,(3,0,3):C.UVGC_104_7,(8,0,2):C.UVGC_105_8,(8,0,3):C.UVGC_105_9,(7,0,1):C.UVGC_135_40,(7,0,2):C.UVGC_135_41,(7,0,3):C.UVGC_135_42,(7,0,4):C.UVGC_135_43,(5,0,2):C.UVGC_104_6,(5,0,3):C.UVGC_104_7,(1,0,2):C.UVGC_104_6,(1,0,3):C.UVGC_104_7,(11,3,2):C.UVGC_108_12,(11,3,3):C.UVGC_108_13,(10,3,2):C.UVGC_108_12,(10,3,3):C.UVGC_108_13,(9,3,2):C.UVGC_107_10,(9,3,3):C.UVGC_107_11,(2,1,2):C.UVGC_105_9,(2,1,3):C.UVGC_105_8,(0,1,2):C.UVGC_105_9,(0,1,3):C.UVGC_105_8,(4,1,2):C.UVGC_104_6,(4,1,3):C.UVGC_104_7,(3,1,2):C.UVGC_104_6,(3,1,3):C.UVGC_104_7,(8,1,1):C.UVGC_137_46,(8,1,2):C.UVGC_137_47,(8,1,3):C.UVGC_137_48,(8,1,4):C.UVGC_137_49,(6,1,2):C.UVGC_132_31,(6,1,3):C.UVGC_132_32,(6,1,4):C.UVGC_132_33,(7,1,0):C.UVGC_109_14,(7,1,2):C.UVGC_110_16,(7,1,3):C.UVGC_110_17,(5,1,2):C.UVGC_104_6,(5,1,3):C.UVGC_104_7,(1,1,2):C.UVGC_104_6,(1,1,3):C.UVGC_104_7,(2,2,2):C.UVGC_105_9,(2,2,3):C.UVGC_105_8,(0,2,2):C.UVGC_105_9,(0,2,3):C.UVGC_105_8,(4,2,2):C.UVGC_104_6,(4,2,3):C.UVGC_104_7,(3,2,2):C.UVGC_104_6,(3,2,3):C.UVGC_104_7,(8,2,1):C.UVGC_134_36,(8,2,2):C.UVGC_134_37,(8,2,3):C.UVGC_134_38,(8,2,4):C.UVGC_134_39,(6,2,0):C.UVGC_109_14,(6,2,2):C.UVGC_109_15,(6,2,3):C.UVGC_107_10,(7,2,2):C.UVGC_133_34,(7,2,3):C.UVGC_133_35,(7,2,4):C.UVGC_132_33,(5,2,2):C.UVGC_104_6,(5,2,3):C.UVGC_104_7,(1,2,2):C.UVGC_104_6,(1,2,3):C.UVGC_104_7})

V_47 = CTVertex(name = 'V_47',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.ax ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_142_54})

V_48 = CTVertex(name = 'V_48',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_146_58})

V_49 = CTVertex(name = 'V_49',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_114_25,(0,1,0):C.UVGC_102_3,(0,2,0):C.UVGC_102_3})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_114_25,(0,1,0):C.UVGC_102_3,(0,2,0):C.UVGC_102_3})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_114_25,(0,1,0):C.UVGC_139_51,(0,2,0):C.UVGC_139_51})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_111_18,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_111_18,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_111_18,(0,1,0):C.UVGC_100_1,(0,2,0):C.UVGC_100_1})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_113_24,(0,1,0):C.UVGC_112_19,(0,1,1):C.UVGC_112_20,(0,1,2):C.UVGC_112_21,(0,1,4):C.UVGC_112_22,(0,1,3):C.UVGC_112_23,(0,2,0):C.UVGC_112_19,(0,2,1):C.UVGC_112_20,(0,2,2):C.UVGC_112_21,(0,2,4):C.UVGC_112_22,(0,2,3):C.UVGC_112_23})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_113_24,(0,1,0):C.UVGC_112_19,(0,1,2):C.UVGC_112_20,(0,1,3):C.UVGC_112_21,(0,1,4):C.UVGC_112_22,(0,1,1):C.UVGC_112_23,(0,2,0):C.UVGC_112_19,(0,2,2):C.UVGC_112_20,(0,2,3):C.UVGC_112_21,(0,2,4):C.UVGC_112_22,(0,2,1):C.UVGC_112_23})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_113_24,(0,1,0):C.UVGC_112_19,(0,1,1):C.UVGC_112_20,(0,1,2):C.UVGC_112_21,(0,1,4):C.UVGC_112_22,(0,1,3):C.UVGC_140_52,(0,2,0):C.UVGC_112_19,(0,2,1):C.UVGC_112_20,(0,2,2):C.UVGC_112_21,(0,2,4):C.UVGC_112_22,(0,2,3):C.UVGC_140_52})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_113_24,(0,1,0):C.UVGC_112_19,(0,1,2):C.UVGC_112_20,(0,1,3):C.UVGC_112_21,(0,1,4):C.UVGC_112_22,(0,1,1):C.UVGC_112_23,(0,2,0):C.UVGC_112_19,(0,2,2):C.UVGC_112_20,(0,2,3):C.UVGC_112_21,(0,2,4):C.UVGC_112_22,(0,2,1):C.UVGC_112_23})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_113_24,(0,1,0):C.UVGC_112_19,(0,1,1):C.UVGC_112_20,(0,1,2):C.UVGC_112_21,(0,1,4):C.UVGC_112_22,(0,1,3):C.UVGC_112_23,(0,2,0):C.UVGC_112_19,(0,2,1):C.UVGC_112_20,(0,2,2):C.UVGC_112_21,(0,2,4):C.UVGC_112_22,(0,2,3):C.UVGC_112_23})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_113_24,(0,1,0):C.UVGC_112_19,(0,1,2):C.UVGC_112_20,(0,1,3):C.UVGC_112_21,(0,1,4):C.UVGC_112_22,(0,1,1):C.UVGC_112_23,(0,2,0):C.UVGC_112_19,(0,2,2):C.UVGC_112_20,(0,2,3):C.UVGC_112_21,(0,2,4):C.UVGC_112_22,(0,2,1):C.UVGC_112_23})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_128_26,(0,0,1):C.UVGC_128_27})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_128_26,(0,0,1):C.UVGC_128_27})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_128_26,(0,0,2):C.UVGC_143_55,(0,0,1):C.UVGC_128_27})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_128_26,(0,0,1):C.UVGC_128_27})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_128_26,(0,0,1):C.UVGC_128_27})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_128_26,(0,0,2):C.UVGC_143_55,(0,0,1):C.UVGC_128_27})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_144_56,(0,1,0):C.UVGC_145_57})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_141_53,(0,1,0):C.UVGC_138_50})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF4 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_101_2})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV5 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_103_4,(0,0,1):C.UVGC_103_5,(0,1,2):C.UVGC_130_28})

