from django.contrib import admin

from .models import cliente, forma_de_pago, tipo_de_habitacion, habitacion, reserva, pago, detalle_pago, detalle_reserva, genero, estado


admin.site.register(cliente)
admin.site.register(forma_de_pago)
admin.site.register(tipo_de_habitacion)
admin.site.register(habitacion)
admin.site.register(reserva)
admin.site.register(pago)
admin.site.register(detalle_pago)
admin.site.register(genero)
admin.site.register(estado)