# Importar librerías
import mesa
import numpy as np

# Importar la clase Paciente y variables de configuración
from agents.paciente import Paciente
from configuration import settings

class CardioModel(mesa.Model):
    '''Modelo que gestiona la simulación de pacientes.'''

    def __init__(self, num_pacientes):
        super().__init__()

        self.num_pacientes = num_pacientes
        self.current_step = 0

        # RandomActivation para que los pacientes se actualicen en orden aleatorio cada paso
        self.schedule = mesa.time.RandomActivation(self)

        # Generar características iniciales basadas en distribuciones normales
        edades = np.random.normal(settings.EDAD_MEDIA, settings.EDAD_STD, self.num_pacientes)
        colesteroles = np.random.normal(settings.COLESTEROL_MEDIA, settings.COLESTEROL_STD, self.num_pacientes)
        presiones_arteriales = np.random.normal(settings.PRESION_ARTERIAL_MEDIA, settings.PRESION_ARTERIAL_STD, self.num_pacientes)

        # Crear agentes uno a uno con las características generadas
        for i in range(self.num_pacientes):
            edad_agente = max(18, int(edades[i]))
            colesterol_agente = round(max(100.0, colesteroles[i]), 2)
            presion_arterial_agente = round(max(80.0, presiones_arteriales[i]), 2)

            # Instanciar el agente Paciente con sus características y agregarlo al modelo
            paciente = Paciente(i, self, edad_agente, colesterol_agente, presion_arterial_agente)
            self.schedule.add(paciente)
    
    def step(self):
        '''Función que se ejecuta en cada paso de la simulación.'''
        print(f'--- Paso {self.current_step} -----------------------------------------------------------')
        self.schedule.step()
        self.current_step += 1