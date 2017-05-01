# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class tcc_personas(osv.osv):
	_name = 'tcc.personas'
	_inherits = {'res.users': 'user_id'}

	_columns = {
		'is_persona': fields.boolean('Persona'),
		'consejocomunal_id': fields.many2one('tcc.consejocomunales','Consejo Comunal',required=True),
		'familia_id': fields.many2one('tcc_familia.tcc_familia','Nombre del Grupo Familiar',required=True),
		'cedula': fields.integer('Cedula',required=True),
		'rif': fields.char('R.I.F.',dize=10),
		's_nombre': fields.char('Segundo Nombre'),
		'p_apellido': fields.char('Primer Apellido',required=True),
		's_apellido': fields.char('Segundo Apellido'),
		'fecha_nacimiento': fields.date('Fecha de Nacimiento'),
		'estado_civil': fields.selection([('Soltero','Soltero'),('Casado','Casado'),('Divorsiado','Divorsiado')],'Estado Civil'),
		'nacionalidad': fields.selection([('venezolana','Venezolana'),('extranjera','Extranjera')],'Nacionalidad'),
		'telefono': fields.char('Telefono'),
		'sexo': fields.selection([('masculino','Masculino'),('femenino','Femenino')],'Sexo'),
		'instruccion': fields.selection([('analfabeta','Analfabeta'),('primaria','Primaria'),('bachiller','Bachiller'),('tsu','T.S.U.'),('universitario','Universitario')],'Grado de instruccion'),
		'discapacidad': fields.boolean('Discapacidad'),
		'jefe_familia': fields.boolean('Es jefe de familia'),
		'trabaja': fields.boolean('Trabaja'),
		'profesion': fields.char('Profesion u oficio'),
		'etnia': fields.boolean('Pertenece a alguna etnia indigena'),
		'status': fields.selection([('vivo','Con Vida'),('muerto','Fallecido')],'Estado'),
		'active': fields.boolean('Activo',default=True),
	}
	
	_defaults = {
		'is_persona':True
        }

