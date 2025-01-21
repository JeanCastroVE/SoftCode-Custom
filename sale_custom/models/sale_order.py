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

    def action_confirm(self):
        """ Asegurar que la fecha de la campaña se encuentre dentro de la fecha del presupuesto """
        res = super().action_confirm()
        if self.sale_campaign_id:
            if self.date_order.date() <= self.sale_campaign_id.end_date and self.date_order.date() >= self.sale_campaign_id.start_date:
                pass
            else:
                raise ValidationError('La Fecha del Presupuesto esta fuera del Rango de la Campaña')
        return res
