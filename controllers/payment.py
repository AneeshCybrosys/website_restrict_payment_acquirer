from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleController(WebsiteSale):
    def _get_shop_payment_values(self, order, **kwargs):
        print('asas',order)
        res = super(WebsiteSaleController,self)._get_shop_payment_values(order, **kwargs)
        ids = []
        for rec in res['acquirers']:
            if rec.minimum_amount <= res['amount'] <= rec.maximum_amount:
                ids.append(rec.id)
        res['acquirers'] = request.env['payment.acquirer'].sudo().browse(ids)
        return res
