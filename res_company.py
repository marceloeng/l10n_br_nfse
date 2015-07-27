# -*- coding: utf-8 -*-

##############################################################################
#                                                                            #
#  Copyright (C) 2013 Proge Informática Ltda (<http://www.proge.com.br>).    #
#                                                                            #
#  Author Daniel Hartmann <daniel@proge.com.br>                              #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                            #
##############################################################################

# Adicionado para funcionamento no Odoo v8
from openerp.osv import osv, fields

class res_company(osv.osv):
    _inherit = 'res.company'
    _columns = {
        'tributacao': fields.selection(
            (('T', u'Tributação no municipio'),
             ('F', u'Tributação fora do municipio'),
             ('I', u'Isento'),
             ('J', u'ISS Suspenso por Decisão Judicial'),
             ),
            u'Tributação',
            ),
        }
    _defaults = {
        'tributacao': 'T',
        }


res_company()