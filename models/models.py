# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrEmployeeExtension(models.Model):
    _inherit = 'hr.employee'

    social_security_number = fields.Char(
        string="Número de Seguridad Social (NSS)",
        help="12 caracteres: 2 de provincia + 8 identificativos + 2 de control"
    )
    dni = fields.Char(
        string="DNI",
        help="8 dígitos + 1 letra de control"
    )

    @api.constrains('social_security_number')
    def _check_social_security_number(self):
        """Validar que el NSS tenga el formato correcto"""
        for record in self:
            if record.social_security_number:
                nss = record.social_security_number.strip()
                
                # Verificar longitud
                if len(nss) != 12:
                    raise ValidationError(
                        "El Número de Seguridad Social debe tener exactamente 12 caracteres."
                    )
                
                # Verificar que todos sean dígitos
                if not nss.isdigit():
                    raise ValidationError(
                        "El Número de Seguridad Social debe contener solo dígitos."
                    )
                
                # Estructura: 2 de provincia + 8 identificativos + 2 de control
                provincia = nss[:2]
                identificativo = nss[2:10]
                control = nss[10:12]
                
                # Validación básica de estructura
                if not (provincia.isdigit() and identificativo.isdigit() and control.isdigit()):
                    raise ValidationError(
                        "El NSS debe tener el formato: 2 dígitos provincia + 8 dígitos identificativos + 2 dígitos control."
                    )

    @api.constrains('dni')
    def _check_dni(self):
        """Validar que el DNI tenga el formato correcto con letra de control"""
        for record in self:
            if record.dni:
                dni = record.dni.strip().upper()
                
                # Verificar longitud
                if len(dni) != 9:
                    raise ValidationError(
                        "El DNI debe tener exactamente 9 caracteres (8 dígitos + 1 letra)."
                    )
                
                # Separar número y letra
                numero = dni[:8]
                letra = dni[8]
                
                # Verificar que los primeros 8 caracteres sean dígitos
                if not numero.isdigit():
                    raise ValidationError(
                        "Los primeros 8 caracteres del DNI deben ser dígitos."
                    )
                
                # Verificar que el último carácter sea una letra
                if not letra.isalpha():
                    raise ValidationError(
                        "El último carácter del DNI debe ser una letra."
                    )
                
                # Tabla de letras de control del DNI
                letras_control = "TRWAGMYFPDXBNJZSQVHLCKE"
                
                # Calcular letra correcta
                letra_correcta = letras_control[int(numero) % 23]
                
                # Validar letra
                if letra != letra_correcta:
                    raise ValidationError(
                        f"La letra de control del DNI es incorrecta. Debería ser '{letra_correcta}'."
                    )
