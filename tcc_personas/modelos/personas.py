# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class tcc_personas(osv.osv):
	_name = 'tcc.personas'
	_inherits = {'res.users': 'user_id'}

	_columns={
		'is_persona': fields.boolean('Persona'),
		'consejocomunal_id': fields.many2one('tcc.consejocomunales','Consejo Comunal',required=True),
		'familia_id': fields.many2one('tcc_familia.tcc_familia','Nombre del Grupo Familiar',required=True),
		'cedula': fields.integer('Cedula',required=True),
		'rif': fields.char('RIF',size=10),
		's_nombre': fields.char('Segundo Nombre'),
		'p_apellido': fields.char('Primer Apellido',required=True),
		's_apellido': fields.char('Segundo Apellido'),
		'fecha_nacimiento': fields.date('Fecha de Nacimiento'),
		'estado_civil': fields.selection([('soltero','Soltero'),('casado','Casado'),('divorciado','Divorciado')],'Estado Civil'),
		'nacionalidad': fields.selection([('venezolana','Venezolana'),('extranjera','Extranjera')],'Nacionalidad'),
		'telefono': fields.char('Telefono'),
		'sexo': fields.selection([('masculino','Masculino'),('femenino','Femenino')],'Sexo'),
		'grado_educa': fields.selection([('analfabeta','Analfabeta'),('primaria','Primaria'),('bachiller','Bachiller'),('tsu','TSU'),('universitario','Universitario')],'Grado de instruccion'),
		'profesion': fields.char('Profesion u oficio'),
		'discapacidad': fields.boolean('Discapacidad'),
		'jefe': fields.boolean('Jefe de familia'),
		'trabaja': fields.boolean('Trabaja'),
		'etnia': fields.boolean('Pertenece a una etnia indigena'),
		'status': fields.selection([('vivo','Con Vida'),('muerto','Fallecido')],'Estado'),
		'active': fields.boolean('Activo',default=True),
	}
	
	_sql_constraints=[
	('cedula_unique','UNIQUE (cedula)','Ya existe una persona con el mismo número de cédula'),
	('rif_unique','UNIQUE (rif)','Ya existe una persona con el mismo número de RIF')
	]

	_defaults={
		'is_persona':True
        }
