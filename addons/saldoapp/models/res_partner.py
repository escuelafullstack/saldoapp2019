from odoo import models,api,fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    fecha_nac = fields.Date("Fecha de Nacimiento")
    apellidos = fields.Char("Apellidos")


    def btn_establecer_fecha(self):
        self.fecha_nac = fields.Date.today()
