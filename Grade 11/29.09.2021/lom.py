for i in range(1,40):
    for j in range(1,40):
        if 99<i*i+j*j<1000:
            summ = i*i+j*j
            for a in range(1,40):
                for b in range(a+1,40):
                    for c in range(b+1,40):
                        if a*a+b*b+c*c==summ:

                            for aa in range(1,40):
                                for bb in range(aa+1,40):
                                    for cc in range(bb+1,40):
                                        for dd in range(cc+1,40):
                                            if aa*aa+bb*bb+cc*cc+dd*dd==summ:

                                                for aaa in range(1, 40):
                                                    for bbb in range(aaa + 1, 40):
                                                        for ccc in range(bbb + 1, 40):
                                                            for ddd in range(ccc + 1, 40):
                                                                for fff in range(ddd + 1, 40):
                                                                    if aaa * aaa + bbb * bbb + ccc * ccc + ddd * ddd+fff*fff == summ:

                                                                        for aaaa in range(1, 40):
                                                                            for bbbb in range(aaaa + 1, 40):
                                                                                for cccc in range(bbbb + 1, 40):
                                                                                    for dddd in range(cccc + 1, 40):
                                                                                        for ffff in range(dddd + 1, 40):
                                                                                            for eeee in range(ffff + 1,40):
                                                                                                if aaaa * aaaa + bbbb * bbbb + cccc * cccc + dddd * dddd + ffff * ffff+eeee*eeee == summ:
                                                                                                    print(summ,i,j,'\n',a,b,c,'\n',aa,bb,cc,dd,'\n',aaa,bbb,ccc,ddd,fff,'\n',aaaa,bbbb,cccc,dddd,ffff,eeee)