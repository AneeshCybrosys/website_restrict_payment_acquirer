# -*- coding: utf-8 -*-
from odoo import models, fields


class PaymentAcquirer(models.Model):
    _inherit = "payment.acquirer"

    currency_id = fields.Many2one('res.currency',
                                  default=lambda self:
                                  self.env.user.company_id.currency_id.id,
                                  string='Currency')
    minimum_amount = fields.Float(string='Minimum Amount')
    maximum_amount = fields.Float(string='Maximum Amount')
