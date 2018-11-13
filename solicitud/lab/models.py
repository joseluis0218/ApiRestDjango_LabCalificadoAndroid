from django.db import models

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True, max_length=100, null=False)
    correo = models.EmailField(max_length=150, blank=False)
    tipo = models.CharField(max_length=150,blank=False)
    motivo = models.CharField(max_length=150,blank=False)
    voucher = models.FileField(upload_to='storage/images/', max_length=250, null=True)

    class Meta:
        db_table = "solicitudes"

    def __str__(self):
        return self.tipo

    def __unicode__(self):
        return self.tipo