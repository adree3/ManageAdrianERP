# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

class Sprint(models.Model):
    _name = 'manageadrian.sprint'
    _description = 'manageadrian.sprint'
    
    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    description = fields.Text(string="Descripción")

    duration = fields.Integer(default=15,string="Duración (días)") 
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de fin", compute="_compute_end_date", store=True)

    
    tareas_id = fields.One2many( string="Tareas",comodel_name="manageadrian.task", inverse_name="carrera_id")

    # Muchas carreras tienen un proyecto
    project_id = fields.Many2one("manageadrian.project", string="Project", required=True, ondelete="cascade")


    


    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for sprint in self:
            if sprint.start_date and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date