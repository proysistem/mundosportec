from django.db import models
from apps.parametros.models import Sucursal

class Tipoproducto(models.Model):	
 	
 	tpo_idtipos = models.CharField('Cód. Tipo/Producto', max_length=1, primary_key=True, default="I")
 	tpo_detalle = models.CharField('Detalle', max_length=20)
 	tpo_abrevia = models.CharField('Abreviatura', max_length=10)

 	def __str__(self):
 		return (self.tpo_detalle)

class Unidad(models.Model):	
 	
 	und_idunida = models.CharField('Cód. Unidad', max_length=5, primary_key=True)
 	und_detalle = models.CharField('Detalle', max_length=20)

 	def __str__(self):
 		return (self.und_detalle)

class Division(models.Model):	
 	
 	div_detalle = models.CharField('Detalle', max_length=20)
 	div_abrevia = models.CharField('Abreviatura', max_length=10)
 	div_indicad = models.IntegerField('Un indicador', default=1)
 	div_statreg = models.BooleanField('Status del Registro', default=True)

 	def __str__(self):
 		return (self.div_detalle)

class Tabtalla(models.Model):	
 	
 	jgo_idtalla = models.CharField('Código de la Tabla', max_length=2)
 	jgo_divisio = models.ForeignKey(Division)
 	jgo_medid01 = models.CharField('Talla-01', max_length=6, null=True, blank=True)
 	jgo_medid02 = models.CharField('Talla-02', max_length=6, null=True, blank=True)
 	jgo_medid03 = models.CharField('Talla-03', max_length=6, null=True, blank=True)
 	jgo_medid04 = models.CharField('Talla-04', max_length=6, null=True, blank=True)
 	jgo_medid05 = models.CharField('Talla-05', max_length=6, null=True, blank=True) 
 	jgo_medid06 = models.CharField('Talla-06', max_length=6, null=True, blank=True)
 	jgo_medid07 = models.CharField('Talla-07', max_length=6, null=True, blank=True)
 	jgo_medid08 = models.CharField('Talla-08', max_length=6, null=True, blank=True)
 	jgo_medid09 = models.CharField('Talla-09', max_length=6, null=True, blank=True)
 	jgo_medid10 = models.CharField('Talla-10', max_length=6, null=True, blank=True)
 	jgo_medid11 = models.CharField('Talla-11', max_length=6, null=True, blank=True)
 	jgo_medid12 = models.CharField('Talla-12', max_length=6, null=True, blank=True)
 	jgo_medid13 = models.CharField('Talla-13', max_length=6, null=True, blank=True)

 	def __str__(self):
 		return "%s %s" % (self.jgo_idtalla, self.jgo_divisio)


class Marca(models.Model):	
 	
 	mrk_idmarca = models.CharField('Código de  Marca', max_length=5, primary_key=True)
 	mrk_detalle = models.CharField('Detalle', max_length=15)
 	mrk_abrevia = models.CharField('Abreviatura', max_length=5)
 	mrk_indicad = models.CharField('Indicador', max_length=1, default=1)
 	mrk_statreg = models.BooleanField('Status del Registro', default=True)

 	def __str__(self):
 		return (self.mrk_detalle) 	
 	
class Modelo(models.Model):	
 	
 	mod_idmodel = models.CharField('Código de Modelo', max_length=5, primary_key=True)
 	mod_idmarca = models.ForeignKey(Marca)
 	mod_detalle = models.CharField('Detalle', max_length=20)
 	mod_abrevia = models.CharField('Abreviatura', max_length=10)
 	mod_tabtall = models.ForeignKey(Tabtalla, null=True, blank=True)
 	mod_statreg = models.BooleanField('Status del Registro', default=True)

 	def __str__(self):
 		return (self.mod_detalle) 	
	
class Color(models.Model):	
 	
 	col_idcolor = models.CharField('Código de Color', max_length=5, primary_key=True)
 	col_detalle = models.CharField('Detalle', max_length=15)
 	col_abrevia = models.CharField('Abreviatura', max_length=10)
 	col_indicad = models.CharField('Indicador', max_length=1, default=1)
 	col_statreg = models.BooleanField('Status del Registro', default=True)

 	def __str__(self):
 		return (self.col_detalle)


#  O J O  en cap.9 curso DevCode, trato de imagenes
class Producto(models.Model):	
 	
# 	prd_iddivis = models.ForeignKey(Division, primary_key=True)
# 	prd_idmarca = models.ForeignKey(Marca, primary_key=True)
# 	prd_idmodel = models.ForeignKey(Modelo, primary_key=True)
# 	prd_idcolor = models.ForeignKey(Color, primary_key=True)
 	prd_product = models.CharField('Código del producto', max_length=20, primary_key=True)
 	prd_detalle = models.CharField('Detalle  del Producto', max_length=45)
 	prd_abrevia = models.CharField('Abreviatura  del Producto', max_length=25)
 	prd_tpoprod = models.ForeignKey(Tipoproducto)
 	prd_tabtall = models.ForeignKey(Tabtalla, null=True, blank=True)
 	prd_imgprod = models.ImageField(upload_to = "productos")
 	prd_statreg = models.BooleanField('Status del Registro', default=True)

 	def __str__(self):
 		return (self.prd_detalle)

class Existencia(models.Model):	
 	
# 	exs_sucursa = models.ForeignKey(Sucursal, primary_key=True)
# 	exs_product = models.ForeignKey(Producto, primary_key=True)
 	exs_product = models.ForeignKey(Producto, primary_key=True) # 'Sucursal + Código del producto'
 	exs_idunida = models.ForeignKey(Unidad)
 	exs_saldinc = models.DecimalField('Saldo inicial', max_digits = 11, decimal_places = 4)
 	exs_ingreso = models.DecimalField('Ingresos', max_digits = 11, decimal_places = 4)
 	exs_egresos = models.DecimalField('Egresos', max_digits = 11, decimal_places = 4)
 	exs_saldact = models.DecimalField('Saldo Actual', max_digits = 11, decimal_places = 4)
 	exs_comprom = models.DecimalField('S.Compromet.(Ped. de Client)', max_digits = 11, decimal_places = 4)
 	exs_xconfir = models.DecimalField('S. x confirm.(Ped.a Proveed)', max_digits = 11, decimal_places = 4)
 	exs_dsponib = models.DecimalField('Saldo disponible', max_digits = 11, decimal_places = 4)
 	exs_feching = models.DateTimeField('Fecha de ult. Ingreso', )
 	exs_fechegr = models.DateTimeField('Fecha Ult. Egreso', )
 	exs_fechinv = models.DateTimeField('Fecha de inventario', )
 	exs_costant = models.DecimalField('Costo promedio Anterior', max_digits = 15, decimal_places = 4)
 	exs_dispant = models.DecimalField('Disponible Anterior', max_digits = 15, decimal_places = 4)
 	exs_costact = models.DecimalField('Costo Actual', max_digits = 15, decimal_places = 4)
 	exs_cosprom = models.DecimalField('Costo promedio Actual', max_digits = 15, decimal_places = 4)
 	exs_distrib = models.DecimalField('Distribuidor', max_digits = 15, decimal_places = 4)
 	exs_mayoris = models.DecimalField('Mayorista', max_digits = 15, decimal_places = 4)
 	exs_detalle = models.DecimalField('Detallista', max_digits = 15, decimal_places = 4)
 	exs_publico = models.DecimalField('Publico', max_digits = 15, decimal_places = 4)
 	exs_special = models.DecimalField('Especial', max_digits = 15, decimal_places = 4)

 	def __str__(self):
 		return (self.ext_dsponib)


class Saldoxtalla(models.Model):	
	
# 	tex_sucursa = models.ForeignKey(Sucursal, primary_key=True)
# 	tex_product = models.ForeignKey(Producto, primary_key=True)
 	tex_product = models.OneToOneField(Existencia, verbose_name='Producto', primary_key=True)  #, 'Sucursal + Código del producto'
 	tex_inici01 = models.DecimalField('Cant. inici-01', max_digits = 11, decimal_places = 4)
 	tex_inici02 = models.DecimalField('Cant. inici-02', max_digits = 11, decimal_places = 4)
 	tex_inici03 = models.DecimalField('Cant. inici-03', max_digits = 11, decimal_places = 4)
 	tex_inici04 = models.DecimalField('Cant. inici-04', max_digits = 11, decimal_places = 4)
 	tex_inici05 = models.DecimalField('Cant. inici-05', max_digits = 11, decimal_places = 4)
 	tex_inici06 = models.DecimalField('Cant. inici-06', max_digits = 11, decimal_places = 4)
 	tex_inici07 = models.DecimalField('Cant. inici-07', max_digits = 11, decimal_places = 4)
 	tex_inici08 = models.DecimalField('Cant. inici-08', max_digits = 11, decimal_places = 4)
 	tex_inici09 = models.DecimalField('Cant. inici-09', max_digits = 11, decimal_places = 4)
 	tex_inici10 = models.DecimalField('Cant. inici-10', max_digits = 11, decimal_places = 4)
 	tex_inici11 = models.DecimalField('Cant. inici-11', max_digits = 11, decimal_places = 4)
 	tex_inici12 = models.DecimalField('Cant. inici-12', max_digits = 11, decimal_places = 4)
 	tex_inici13 = models.DecimalField('Cant. inici-13', max_digits = 11, decimal_places = 4)
	
 	tex_ingre01 = models.DecimalField('Cant. ingre-01', max_digits = 11, decimal_places = 4)
 	tex_ingre02 = models.DecimalField('Cant. ingre-02', max_digits = 11, decimal_places = 4)
 	tex_ingre03 = models.DecimalField('Cant. ingre-03', max_digits = 11, decimal_places = 4)
 	tex_ingre04 = models.DecimalField('Cant. ingre-04', max_digits = 11, decimal_places = 4)
 	tex_ingre05 = models.DecimalField('Cant. ingre-05', max_digits = 11, decimal_places = 4)
 	tex_ingre06 = models.DecimalField('Cant. ingre-06', max_digits = 11, decimal_places = 4)
 	tex_ingre07 = models.DecimalField('Cant. ingre-07', max_digits = 11, decimal_places = 4)
 	tex_ingre08 = models.DecimalField('Cant. ingre-08', max_digits = 11, decimal_places = 4)
 	tex_ingre09 = models.DecimalField('Cant. ingre-09', max_digits = 11, decimal_places = 4)
 	tex_ingre10 = models.DecimalField('Cant. ingre-10', max_digits = 11, decimal_places = 4)
 	tex_ingre11 = models.DecimalField('Cant. ingre-11', max_digits = 11, decimal_places = 4)
 	tex_ingre12 = models.DecimalField('Cant. ingre-12', max_digits = 11, decimal_places = 4)
 	tex_ingre13 = models.DecimalField('Cant. ingre-13', max_digits = 11, decimal_places = 4)
 	
 	tex_egres01 = models.DecimalField('Cant. egres-01', max_digits = 11, decimal_places = 4)
 	tex_egres02 = models.DecimalField('Cant. egres-02', max_digits = 11, decimal_places = 4)
 	tex_egres03 = models.DecimalField('Cant. egres-03', max_digits = 11, decimal_places = 4)
 	tex_egres04 = models.DecimalField('Cant. egres-04', max_digits = 11, decimal_places = 4)
 	tex_egres05 = models.DecimalField('Cant. egres-05', max_digits = 11, decimal_places = 4)
 	tex_egres06 = models.DecimalField('Cant. egres-06', max_digits = 11, decimal_places = 4)
 	tex_egres07 = models.DecimalField('Cant. egres-07', max_digits = 11, decimal_places = 4)
 	tex_egres08 = models.DecimalField('Cant. egres-08', max_digits = 11, decimal_places = 4)
 	tex_egres09 = models.DecimalField('Cant. egres-09', max_digits = 11, decimal_places = 4)
 	tex_egres10 = models.DecimalField('Cant. egres-10', max_digits = 11, decimal_places = 4)
 	tex_egres11 = models.DecimalField('Cant. egres-11', max_digits = 11, decimal_places = 4)
 	tex_egres12 = models.DecimalField('Cant. egres-12', max_digits = 11, decimal_places = 4)
 	tex_egres13 = models.DecimalField('Cant. egres-13', max_digits = 11, decimal_places = 4)
 	
 	tex_actua01 = models.DecimalField('Cant. actua-01', max_digits = 11, decimal_places = 4)
 	tex_actua02 = models.DecimalField('Cant. actua-02', max_digits = 11, decimal_places = 4)
 	tex_actua03 = models.DecimalField('Cant. actua-03', max_digits = 11, decimal_places = 4)
 	tex_actua04 = models.DecimalField('Cant. actua-04', max_digits = 11, decimal_places = 4)
 	tex_actua05 = models.DecimalField('Cant. actua-05', max_digits = 11, decimal_places = 4)
 	tex_actua06 = models.DecimalField('Cant. actua-06', max_digits = 11, decimal_places = 4)
 	tex_actua07 = models.DecimalField('Cant. actua-07', max_digits = 11, decimal_places = 4)
 	tex_actua08 = models.DecimalField('Cant. actua-08', max_digits = 11, decimal_places = 4)
 	tex_actua09 = models.DecimalField('Cant. actua-09', max_digits = 11, decimal_places = 4)
 	tex_actua10 = models.DecimalField('Cant. actua-10', max_digits = 11, decimal_places = 4)
 	tex_actua11 = models.DecimalField('Cant. actua-11', max_digits = 11, decimal_places = 4)
 	tex_actua12 = models.DecimalField('Cant. actua-12', max_digits = 11, decimal_places = 4)
 	tex_actua13 = models.DecimalField('Cant. actua-13', max_digits = 11, decimal_places = 4)
  	
 	tex_compr01 = models.DecimalField('Cant. compr-01', max_digits = 11, decimal_places = 4)
 	tex_compr02 = models.DecimalField('Cant. compr-02', max_digits = 11, decimal_places = 4)
 	tex_compr03 = models.DecimalField('Cant. compr-03', max_digits = 11, decimal_places = 4)
 	tex_compr04 = models.DecimalField('Cant. compr-04', max_digits = 11, decimal_places = 4)
 	tex_compr05 = models.DecimalField('Cant. compr-05', max_digits = 11, decimal_places = 4)
 	tex_compr06 = models.DecimalField('Cant. compr-06', max_digits = 11, decimal_places = 4)
 	tex_compr07 = models.DecimalField('Cant. compr-07', max_digits = 11, decimal_places = 4)
 	tex_compr08 = models.DecimalField('Cant. compr-08', max_digits = 11, decimal_places = 4)
 	tex_compr09 = models.DecimalField('Cant. compr-09', max_digits = 11, decimal_places = 4)
 	tex_compr10 = models.DecimalField('Cant. compr-10', max_digits = 11, decimal_places = 4)
 	tex_compr11 = models.DecimalField('Cant. compr-11', max_digits = 11, decimal_places = 4)
 	tex_compr12 = models.DecimalField('Cant. compr-12', max_digits = 11, decimal_places = 4)
 	tex_compr13 = models.DecimalField('Cant. compr-13', max_digits = 11, decimal_places = 4)
	
 	tex_xconf01 = models.DecimalField('Cant. xconf-01', max_digits = 11, decimal_places = 4)
 	tex_xconf02 = models.DecimalField('Cant. xconf-02', max_digits = 11, decimal_places = 4)
 	tex_xconf03 = models.DecimalField('Cant. xconf-03', max_digits = 11, decimal_places = 4)
 	tex_xconf04 = models.DecimalField('Cant. xconf-04', max_digits = 11, decimal_places = 4)
 	tex_xconf05 = models.DecimalField('Cant. xconf-05', max_digits = 11, decimal_places = 4)
 	tex_xconf06 = models.DecimalField('Cant. xconf-06', max_digits = 11, decimal_places = 4)
 	tex_xconf07 = models.DecimalField('Cant. xconf-07', max_digits = 11, decimal_places = 4)
 	tex_xconf08 = models.DecimalField('Cant. xconf-08', max_digits = 11, decimal_places = 4)
 	tex_xconf09 = models.DecimalField('Cant. xconf-09', max_digits = 11, decimal_places = 4)
 	tex_xconf10 = models.DecimalField('Cant. xconf-10', max_digits = 11, decimal_places = 4)
 	tex_xconf11 = models.DecimalField('Cant. xconf-11', max_digits = 11, decimal_places = 4)
 	tex_xconf12 = models.DecimalField('Cant. xconf-12', max_digits = 11, decimal_places = 4)
 	tex_xconf13 = models.DecimalField('Cant. xconf-13', max_digits = 11, decimal_places = 4)
 	
 	tex_dispo01 = models.DecimalField('Cant. dispo-01', max_digits = 11, decimal_places = 4)
 	tex_dispo02 = models.DecimalField('Cant. dispo-02', max_digits = 11, decimal_places = 4)
 	tex_dispo03 = models.DecimalField('Cant. dispo-03', max_digits = 11, decimal_places = 4)
 	tex_dispo04 = models.DecimalField('Cant. dispo-04', max_digits = 11, decimal_places = 4)
 	tex_dispo05 = models.DecimalField('Cant. dispo-05', max_digits = 11, decimal_places = 4)
 	tex_dispo06 = models.DecimalField('Cant. dispo-06', max_digits = 11, decimal_places = 4)
 	tex_dispo07 = models.DecimalField('Cant. dispo-07', max_digits = 11, decimal_places = 4)
 	tex_dispo08 = models.DecimalField('Cant. dispo-08', max_digits = 11, decimal_places = 4)
 	tex_dispo09 = models.DecimalField('Cant. dispo-09', max_digits = 11, decimal_places = 4)
 	tex_dispo10 = models.DecimalField('Cant. dispo-10', max_digits = 11, decimal_places = 4)
 	tex_dispo11 = models.DecimalField('Cant. dispo-11', max_digits = 11, decimal_places = 4)
 	tex_dispo12 = models.DecimalField('Cant. dispo-12', max_digits = 11, decimal_places = 4)
 	tex_dispo13 = models.DecimalField('Cant. dispo-13', max_digits = 11, decimal_places = 4)

 	def __str__(self):
 		return (self.tex_product)