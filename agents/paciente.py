import mesa
import numpy as np

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, grupo, es_mujer, edad, grasa_sat, grasa_mono, grasa_poli, col_total, col_ldl):
        super().__init__(model)

        # Perfil del paciente
        self.unique_id = unique_id
        self.grupo = grupo
        self.sexo = "Mujer" if es_mujer else "Hombre"
        self.edad = edad

        # 1. Valores de ingesta objetivo (lo que la nutricionista le ha pedido que consuma diariamente)
        self.obj_grasa_sat = grasa_sat
        self.obj_grasa_mono = grasa_mono
        self.obj_grasa_poli = grasa_poli

        # 2. Ingesta real (lo que realmente consume) --> recalculada cada semana
        self.grasa_sat_real = 0.0
        self.grasa_mono_real = 0.0
        self.grasa_poli_real = 0.0

        # Biomarcadores de salud
        self.col_total = col_total
        self.col_ldl = col_ldl

    def comer(self):
        '''
        Simula la ingesta semanal del paciente'''

        # Asumimos que el paciente tiene una desviación del 15% respecto a su objetivo
        std_sat = self.obj_grasa_sat * 0.1
        std_mono = self.obj_grasa_mono * 0.1
        std_poli = self.obj_grasa_poli * 0.1

        self.ingesta_sat_actual = max(0, np.random.normal(self.obj_grasa_sat, std_sat))
        self.ingesta_mono_actual = max(0, np.random.normal(self.obj_grasa_mono, std_mono))
        self.ingesta_poli_actual = max(0, np.random.normal(self.obj_grasa_poli, std_poli))

    def step(self):
        '''
        Función que se ejecuta en cada paso (semana) de la simulación.
        '''

        # 1. Simular la ingesta semanal del paciente
        self.comer()

        # 2. Actualizar los biomarcadores de salud en función de la ingesta real
        # --- Desarrollo de la función de actualización de biomarcadores ---

        # Prueba con 3 pacientes para analizar su evolución semanal de ingesta
        if self.unique_id < 3:
            print(f'    • Paciente {self.unique_id} ({self.grupo}) -> '
                  f'Grasas Saturadas: {self.ingesta_sat_actual:.1f}g, '
                  f'Grasas Monoinsaturadas: {self.ingesta_mono_actual:.1f}g, '
                  f'Grasas Poliinsaturadas: {self.ingesta_poli_actual:.1f}g')