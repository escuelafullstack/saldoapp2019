# -*- coding: utf-8 -*-

from odoo import models, fields, api 
from odoo.exceptions import UserError, ValidationError
from odoo.http import request

class Diario(models.Model):
    _name = "sa.diario"
    _description = "Diario de Movimientos"

    fecha = fields.Date("Fecha")
    total_ingresos = fields.Float("Total Ingresos",compute="compute_totales")
    total_egresos = fields.Float("Total Gastos",compute="compute_totales")

    total_ingresos_1 = fields.Float("Total Ingresos")
    total_egresos_1 = fields.Float("Total Gastos")
    movimiento_ids = fields.One2many("sa.movimiento","diario_id")

    currency_id = fields.Many2one("res.currency")

    @api.multi
    @api.depends("movimiento_ids.monto")
    def compute_totales(self):
        for record in self:
            record.total_ingresos = sum([mov.monto for mov in record.movimiento_ids if mov.tipo == "ingreso"])
            record.total_egresos = sum([mov.monto for mov in record.movimiento_ids if mov.tipo == "egreso"])

    @api.multi
    @api.onchange("movimiento_ids.monto")
    def compute_totales_1(self):
        for record in self:
            record.total_ingresos_1 = sum([mov.monto for mov in record.movimiento_ids if mov.tipo == "ingreso"])
            record.total_egresos_1 = sum([mov.monto for mov in record.movimiento_ids if mov.tipo == "egreso"])

class Movimiento(models.Model):
    _name = "sa.movimiento" 
    _description = "Movimientos del día"
    #_rec_name = "concepto"
    
    currency_id = fields.Many2one("res.currency")
    concepto = fields.Char("Concepto")
    monto = fields.Float("Monto",digits=(10,4))
    fecha = fields.Date("Fecha")
    tipo = fields.Selection(string="Tipo de Movimiento",selection=[("ingreso","Ingreso"),("egreso","Egreso")])
    imagen_comprobante = fields.Binary("Foto de Comprobante")
    pdf_comprobante = fields.Binary("PDF de Comprobante")
    igv = fields.Float("IGV")

    categoria_id = fields.Many2one("sa.categoria")
    diario_id = fields.Many2one("sa.diario")

    """
        write
        create
        unlink
        search
        search_read
        browse

        default_get
        mame_get
    """
    
    @api.model
    def create(self, values):
        fecha = values.get("fecha",False)
        #fecha = fields.Datetime.now()

        diario = self.env["sa.diario"].search([("fecha","=",fecha)],limit=1)
        
        if diario.exists():
            values.update({"diario_id":diario.id})
            mov = super(Movimiento, self).create(values)
        else: 
            if not values.get("fecha",False):
                raise ValidationError("La fecha es obligatorio")
                
            mov = super(Movimiento, self).create(values)

            diario = self.env["sa.diario"].create({
                "fecha":values.get("fecha",False),
                "movimiento_ids":[(6,0,[mov.id])]
            })
            
        
        return mov
    


    @api.multi
    @api.depends('concepto', 'monto')
    def name_get(self):
        result = []
        for record in self:
            if record.concepto:
                name = "["+str(record.id)+"]"+record.concepto +" - " +str(record.monto)
            else:
                record.concepto = " Vacío "
            result.append((record.id, name))
        return result
    
    
    @api.model
    def default_get(self, flds):
        res = super(Movimiento, self).default_get(flds)
        res.update({"fecha":fields.Datetime.now()})    
        currency_id = self.env["res.users"].browse(request.uid).company_id.currency_id.id
        res.update({"currency_id":currency_id})    
        return res
        
    
    @api.constrains('monto')
    def _check_(self):
        for record in self:
            if record.monto<0 or record.monto>100000:
                raise ValidationError("El monto debe estar comprendido entre 0 y 1 000 000")
            
    
class Categoria(models.Model):
    _name = "sa.categoria"
    _description = "Categoría"

    name  = fields.Char("Categoria")
    icon = fields.Binary("Icono")

