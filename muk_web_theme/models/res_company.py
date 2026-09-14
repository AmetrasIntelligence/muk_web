###################################################################################
#
#    Copyright (c) 2017-today MuK IT GmbH.
#
#    This file is part of MuK Backend Theme
#    (see https://mukit.at).
#
#    License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
###################################################################################

from odoo import models, fields


class ResCompany(models.Model):
    
    _inherit = 'res.company'
    
    #----------------------------------------------------------
    # Fields
    #----------------------------------------------------------
    
    background_image = fields.Binary(
        string='Apps Menu Background Image',
        attachment=True
    )

    #----------------------------------------------------------
    # Helper
    #----------------------------------------------------------

    def _get_background_image_unique(self):
        """ Returns a token that changes with the background image, used to
        version the image URL so browsers do not keep a cached copy after
        the image was replaced.
        """
        self.ensure_one()
        attachment = self.env['ir.attachment'].sudo().search([
            ('res_model', '=', 'res.company'),
            ('res_id', '=', self.id),
            ('res_field', '=', 'background_image'),
        ], limit=1)
        return attachment.checksum[:8] if attachment else False
