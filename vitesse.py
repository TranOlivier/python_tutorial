#fonction calcul d'une vitesse v = d/t

import io
d = float(input('enter a distance: '))


t = float(('enter a time: '))


#d = 19.7
#t = 6.892
v = d / t
print ('Distance = {}m, Time = {}s,Velocity = {} m/s'.format(d,t,str(v)[:5]))
print ('Distance = {}m, Time = {}s,Velocity = {:.3f} m/s'.format(d,t,v))