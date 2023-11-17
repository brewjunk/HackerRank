import math as m
AB = int(input())
BC = int(input())
print(round(m.degrees(m.atan(AB/BC))),chr(176),sep='')



concept: BM=1/2 * AC ; BM=1/2 * (AM+MC) ; and we know AM == MC ; BM=1/2 * (MC+MC) ; BM=1/2 * (2MC) ; BM=MC ;

and

BMC is an isosceles triangle ; therefore angle BAC == angle BCA and angles(BAC == BCA == MBC)

then tan(θ)=AB/BC therefore θ = atan(AB/BC) #atan in the sence "taninverse"
