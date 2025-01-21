from odoo import api, fields, models

from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_campaign_id = fields.Many2one("sale.campaign", string="Campaña")
    campaign_discount = fields.Float(string="Descuento de Campaña", compute="set_campaign_discount")

    @api.depends("sale_campaign_id")
    def set_campaign_discount(self):
        """ Establecer el monto del descuento total"""
        for rec in self:
            if rec.sale_campaign_id and rec.amount_total:
                if rec.sale_campaign_id.discount_type == "percentage":
                    rec.write({"campaign_discount": ((rec.amount_total * rec.sale_campaign_id.discount_value) / 100)})
                else:
                    if rec.sale_campaign_id.discount_value > rec.amount_total:
                        raise ValidationError('El Descuento es Mayor a la Compra')
                    else:
                        rec.write({"campaign_discount": (rec.amount_total - rec.sale_campaign_id.discount_value)})
            else:
                rec.write({"campaign_discount": 0})
