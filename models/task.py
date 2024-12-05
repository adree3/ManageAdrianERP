# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

class Task(models.Model):
    _name = 'manageadrian.task'
    _description = 'manageadrian.task'
    
    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de fin")
    is_paused = fields.Boolean(string="¿Pausado?")

    code = fields.Char(string="Código", compute="_compute_code")

    carrera_id = fields.Many2one("manageadrian.sprint", compute="_get_sprint",string="Carrera", ondelete="cascade")

    tecnologias_id = fields.Many2many(
        comodel_name="manageadrian.technology", 
        relation="tecnologias_tareas", 
        column1="tecnologias_ids", 
        column2="tareas_ids", 
        string="Tecnologías"
    )

    # Muchas tareas tienen una historia
    history_id = fields.Many2one("manageadrian.history", string="History", required=True, ondelete="cascade")
    
    proyect_id= fields.Many2one("manageadrian.project", related = "history_id.project_id", readonly = True)
    

    def _compute_code(self):
        for task in self:
            task.code = "TSK_"+ str(task.id)

    @api.depends('history_id.project_id')
    def _get_sprint(self):
        for task in self:
            # Por defecto, limpiamos el campo
            task.carrera_id = False

            # Validamos que exista history_id y project_id
            if not task.history_id or not task.history_id.project_id:
                continue

            # Buscar los sprints asociados al proyecto
            sprints = self.env['manageadrian.sprint'].search([
                ('project_id', '=', task.history_id.project_id.id)
            ])

            # Asignar el primer sprint válido (si existe)
            for sprint in sprints:
                if sprint.end_date and sprint.end_date > datetime.datetime.now():
                    task.carrera_id = sprint.id
                    break  # Detenemos la búsqueda después de asignar

        