from cdo import *
import matplotlib.pyplot as plt

cdo = Cdo()

cdo.debug = True

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = cdo.fldmean(input='../../dados/netcdf/prec.2020.nc', returnCdf=True).variables['prec'][:]

plt.plot(x,y[:,0,0])

# Salva a figura no formato ".jpg" com dpi=300 e remove espaços excedentes.
plt.savefig('ex01.jpg', transparent=True, dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()

#cdo = Cdo(tempdir='diretorio_arquivos_temporarios')

#outfile = cdo.timmin(input='../../dados/netcdf/prec.2020.nc', options='-f nc')
#
#cdo.infon(input=outfile)

#cdo.sellonlatbox('-66,-51,-10,-2', 
#                  input = '-mulc,20 -selmon,3 ' + '../../dados/netcdf/prec.2020.nc', 
#                  output = 'out.nc', 
#                  options='-f nc4')

#cdo.seltimestep('3/5', 
#                input='../../dados/netcdf/PREC.IMERG.2019.pantanal.nc', 
#                output='out.nc', 
#                options='-r -f nc4')

#cdo.remapbil('../../dados/netcdf/GRACE.2020.pantanal.nc', input='../../dados/netcdf/PREC.IMERG.2019.pantanal.nc', output='out.nc')

#cdo.timmin(input = '../../dados/netcdf/prec.2020.nc',output = 'tmp.nc')

#print(dir(cdo))

#print(cdo.version())  # Verão do CDO instalada.

#cdo.infov(input='../../dados/netcdf/prec.2020.nc')


