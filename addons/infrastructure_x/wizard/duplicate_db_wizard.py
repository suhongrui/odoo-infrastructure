# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, Warning, RedirectWarning
# from fabric.api import local, settings, abort, run, cd, env, sudo
# import os
class infrastructure_duplicate_db_wizard(osv.osv_memory):
    _name = "infrastructure.duplicate_db.wizard"
    _description = "Infrastructure Duplicate db Wizard"

    new_db_name = fields.Char(string='New db Name', required=True)
    change_user = fields.Boolean(string='Change Instance?')
    server_id = fields.Many2one('infrastructure.server', string='Server')
    instance_id = fields.Many2one('infrastructure.instance', string='Instance')

    @api.one
    def duplicate_db(self):
        # TODO implementar si hay cambio de usuario
        if self.change_user:
            raise Warning(_("Not Implemented Yet!"))
        active_ids = self.env.context.get('active_ids', False)
        if not active_ids:
            raise Warning(_("Can not duplicate database, no active_ids on context")) 
        for database in self.env['infrastructure.database'].search([('id', 'in', active_ids)]):
            database.duplicate_db(self.new_db_name)
