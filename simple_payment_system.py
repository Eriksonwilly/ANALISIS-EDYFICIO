#!/usr/bin/env python3
"""
Sistema de Pagos Simple - CONSORCIO DEJ
Sistema básico de gestión de usuarios y pagos
"""

import json
import os
from datetime import datetime, timedelta
import hashlib

class SimplePaymentSystem:
    def __init__(self):
        self.users_file = "users.json"
        self.payments_file = "payments.json"
        self.users = {}
        self.payments = []
        self.load_data()
    
    def load_data(self):
        """Cargar datos desde archivos JSON"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)
        except Exception:
            self.users = {}
        
        try:
            if os.path.exists(self.payments_file):
                with open(self.payments_file, 'r', encoding='utf-8') as f:
                    self.payments = json.load(f)
        except Exception:
            self.payments = []
    
    def save_data(self):
        """Guardar datos en archivos JSON"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
        
        try:
            with open(self.payments_file, 'w', encoding='utf-8') as f:
                json.dump(self.payments, f, indent=2, ensure_ascii=False)
        except Exception:
            pass
    
    def hash_password(self, password):
        """Hashear contraseña"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, email, password, name):
        """Registrar nuevo usuario"""
        if email in self.users:
            return {"success": False, "message": "El email ya está registrado"}
        
        self.users[email] = {
            "email": email,
            "password": self.hash_password(password),
            "name": name,
            "plan": "gratuito",
            "created_at": datetime.now().isoformat(),
            "expires_at": None,
            "payment_pending": None
        }
        
        self.save_data()
        return {"success": True, "message": "Usuario registrado exitosamente"}
    
    def login_user(self, email, password):
        """Iniciar sesión de usuario"""
        if email not in self.users:
            return {"success": False, "message": "Usuario no encontrado"}
        
        user = self.users[email]
        if user["password"] != self.hash_password(password):
            return {"success": False, "message": "Contraseña incorrecta"}
        
        return {"success": True, "user": user}
    
    def upgrade_plan(self, email, plan, payment_method):
        """Actualizar plan de usuario"""
        if email not in self.users:
            return {"success": False, "message": "Usuario no encontrado"}
        
        # Crear pago pendiente
        payment_id = f"pay_{len(self.payments) + 1}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        payment = {
            "id": payment_id,
            "email": email,
            "plan": plan,
            "amount": self.get_plan_price(plan),
            "payment_method": payment_method,
            "status": "pendiente",
            "created_at": datetime.now().isoformat(),
            "confirmed_at": None
        }
        
        self.payments.append(payment)
        
        # Marcar pago pendiente en usuario
        self.users[email]["payment_pending"] = payment_id
        self.save_data()
        
        # Instrucciones de pago
        instructions = self.get_payment_instructions(payment_method, plan)
        
        return {
            "success": True,
            "message": "Pago registrado correctamente",
            "instructions": instructions,
            "payment_id": payment_id,
            "auto_confirmed": False
        }
    
    def confirm_payment(self, payment_id):
        """Confirmar pago"""
        for payment in self.payments:
            if payment["id"] == payment_id and payment["status"] == "pendiente":
                payment["status"] = "confirmado"
                payment["confirmed_at"] = datetime.now().isoformat()
                
                # Actualizar usuario
                email = payment["email"]
                if email in self.users:
                    self.users[email]["plan"] = payment["plan"]
                    self.users[email]["payment_pending"] = None
                    
                    # Calcular fecha de expiración
                    if payment["plan"] != "gratuito":
                        expires_at = datetime.now() + timedelta(days=30)
                        self.users[email]["expires_at"] = expires_at.isoformat()
                
                self.save_data()
                return {"success": True, "message": "Pago confirmado"}
        
        return {"success": False, "message": "Pago no encontrado o ya confirmado"}
    
    def get_pending_payments(self):
        """Obtener pagos pendientes"""
        return [p for p in self.payments if p["status"] == "pendiente"]
    
    def get_plan_price(self, plan):
        """Obtener precio del plan"""
        prices = {
            "gratuito": 0.0,
            "premium": 29.99,
            "empresarial": 99.99
        }
        return prices.get(plan, 0.0)
    
    def get_payment_instructions(self, payment_method, plan):
        """Obtener instrucciones de pago"""
        price = self.get_plan_price(plan)
        
        instructions = {
            "yape": f"Envía ${price:.2f} al número +51 999 888 777 con el concepto 'Plan {plan.title()}'",
            "plin": f"Envía ${price:.2f} al número +51 999 888 777 con el concepto 'Plan {plan.title()}'",
            "paypal": f"Envía ${price:.2f} a consorciodej@gmail.com con el concepto 'Plan {plan.title()}'",
            "transferencia": f"Transfiere ${price:.2f} a la cuenta BCP 193-12345678-0-12 con el concepto 'Plan {plan.title()}'",
            "efectivo": f"Paga ${price:.2f} en efectivo en nuestra oficina: Av. Arequipa 123, Lima"
        }
        
        return instructions.get(payment_method, "Contacta soporte para instrucciones de pago")

# Instancia global del sistema de pagos
payment_system = SimplePaymentSystem() 