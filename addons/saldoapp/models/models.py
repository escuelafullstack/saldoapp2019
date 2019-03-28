# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Diario(models.Model):
    _name = "sa.diario"
    _description = "Diario de Movimientos"

    fecha = fields.Date("Fecha")
    total_ingresos = fields.Float("Total Ingresos",compute="compute_totales")
    total_egresos = fields.Float("Total Gastos",compute="compute_totales")
    movimiento_ids = fields.One2many("sa.movimiento","diario_id")

    @api.multi
    @api.depends("movimiento_ids.monto")
    def compute_totales(self):
        for record in self:
            record.total_ingresos = sum([mov.monto for mov in record.movimiento_ids if mov.tipo == "ingreso"])
            record.total_egresos = sum([mov.monto for mov in record.movimiento_ids if mov.tipo == "egreso"])

class Movimiento(models.Model):
    _name = "sa.movimiento" #sa_movimiento
    _description = "Movimientos del día"
    #_rec_name = "concepto"
    
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
        return res
        
    
class Categoria(models.Model):
    _name = "sa.categoria"
    _description = "Categoría"

    name  = fields.Char("Categoria")
    icon = fields.Binary("Icono")

