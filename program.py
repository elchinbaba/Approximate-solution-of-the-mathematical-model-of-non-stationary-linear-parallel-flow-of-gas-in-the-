import math
def P(x,t,k,mu,m,p,L):
    kappa = k/(mu*m)
    c0 = kappa/2*(p[0]*p[0]-p[1]*p[1])
    c1 = ((p[0]*p[0]-3*p[1]*p[1])*p[0]+2*p[1]*p[1]*p[1])/(3*(p[0]*p[0]-p[1]*p[1]))
    c2 = c0*c1;
    c3 = math.sqrt(2*c2);
    if 0<=x<=c3*math.sqrt(t):
        return math.sqrt(p[1]*p[1]+(p[0]*p[0]-p[1]*p[1])/c3*x/math.sqrt(t))
    if c3<=x<L:
        return p[0]
print("P={}".format(P(0.5,0.1,0.1,0.2,0.3,(0.5,0.6),1)))