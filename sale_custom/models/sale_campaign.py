from odoo import fields, models

ls_discount_type = [("fixed", "Fijo"),
                    ("percentage", "Porcentage")]


class SaleCampaign(models.Model):
    _name = "sale.campaign"
    _description = "Campañas de Ventas"
    _order = "name"
    _rec_name = "name"

    name = fields.Char(string="Nombre de la Campaña", required=True)
    discount_type = fields.Selection(ls_discount_type, string="Tipo de Descuento")
    discount_value = fields.Float(string="Valor de Descuento")
    street = fields.Char(string="Dirección")
    start_date = fields.Date(string="Fecha Inicio")
    end_date = fields.Date(string="Fecha Fin")
