from django.db import models

class genero(models.Model):
    genero = models.CharField("genero:",max_length=45)
    def __str__(self):
        return self.genero

class estado(models.Model):
    estado = models.CharField("estado:",max_length=45)
    def __str__(self):
        return self.estado

class cliente(models.Model):
    nombre = models.CharField("Nombre:",max_length=45)
    apellido = models.CharField("apellido:",max_length=45)
    dni = models.IntegerField(null=True)
    domicilio =  models.CharField("domicilio:",max_length=45)
    telefono = models.CharField("telefono:",max_length=45)
    mail = models.EmailField(max_length=75)
    genero = models.ForeignKey('genero', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class forma_de_pago(models.Model):
    tipo_de_pago = models.CharField("tipo_de_pago:",max_length=45)
    precio =  models.FloatField() 
    nombre_cliente = models.CharField(max_length=40)
    telefono = models.CharField(max_length=45)
    estado = models.BooleanField()
    def __str__(self):
        return self.tipo_de_pago

class tipo_de_habitacion(models.Model):
    tipo = models.CharField(max_length=40)
    num_ambientes = models.IntegerField(null=True)
    def __str__(self):
        return self.tipo

class habitacion(models.Model):
    num_habitacion = models.CharField(max_length=40)
    precio = models.IntegerField(null=True)
    tipo_de_habitacion = models.ForeignKey('tipo_de_habitacion', on_delete=models.CASCADE)
    estado = models.ForeignKey('estado', on_delete=models.CASCADE)
    def __str__(self):
        return self.num_habitacion
   

class reserva(models.Model):
    fecha_reserva = models.DateField("fecha_reserva")
    fecha_ingreso = models.DateField("fecha_ingreso")
    fecha_salida = models.DateField("fecha_salida")
    cliente = models.ForeignKey('cliente', on_delete=models.CASCADE)
    def __str__(self):
        return self.cliente

class pago(models.Model):
    forma_de_pago = models.ForeignKey('forma_de_pago', on_delete=models.CASCADE)
    reserva = models.ForeignKey('reserva', on_delete=models.CASCADE)
    def __str__(self):
        return self.reserva  

class detalle_pago(models.Model):
    observaciones = models.CharField(max_length=40)
    pago = models.ForeignKey('Pago', on_delete=models.CASCADE)
    reserva = models.ForeignKey('reserva', on_delete=models.CASCADE)
    def __str__(self):
        return self.pago

class detalle_reserva(models.Model):
    pago = models.ForeignKey('pago', on_delete=models.CASCADE)
    habitacion = models.ForeignKey('habitacion', on_delete=models.CASCADE)
    def __str__(self):
        return self.reserva


    
