# Importar librerías
import mesa
import numpy as np
import random

# Importar la clase Paciente y variables de configuración
from agents.paciente import Paciente
from configuration import settings
# from mesa.datacollection import DataCollector

class CardioModel(mesa.Model):
    '''Modelo que gestiona la simulación de pacientes.'''

    def __init__(self, num_pacientes):
        super().__init__()

        self.num_pacientes = num_pacientes
        self.current_step = 1

        # RandomActivation para que los pacientes se actualicen en orden aleatorio cada paso
        self.schedule = mesa.time.RandomActivation(self)

        # Crear agentes uno a uno con las características generadas
        for i in range(self.num_pacientes):

            # Grupo dieta mediterránea
            if i < int(settings.PROPORCION_MED * self.num_pacientes):
                grupo = 'Mediterránea'
                es_mujer = random.random() < settings.PROPORCION_MUJERES_MED
                edad = max(18, int(np.random.normal(settings.EDAD_MEDIA, settings.EDAD_STD)))

                # Variables de ingesta (gramos / día) basadas en Campana de Gauss
                grasa_sat = max(1.0, np.random.normal(settings.GRASA_SAT_MEDIA_MED, settings.GRASA_SAT_STD_MED))
                grasa_mono = max(1.0, np.random.normal(settings.GRASA_MONO_MEDIA_MED, settings.GRASA_MONO_STD_MED))
                grasa_poli = max(1.0, np.random.normal(settings.GRASA_POLI_MEDIA_MED, settings.GRASA_POLI_STD_MED))

                # Variables de salud iniciales basadas en Campana de Gauss
                col_total = np.random.normal(settings.COL_TOTAL_MEDIA_MED, settings.COL_TOTAL_STD_MED)
                col_ldl = np.random.normal(settings.COL_LDL_MEDIA_MED, settings.COL_LDL_STD_MED)


            # Grupo dieta baja en grasas
            else:
                grupo = 'Baja en Grasas'
                es_mujer = random.random() < settings.PROPORCION_MUJERES_LOW_FAT
                edad = max(18, int(np.random.normal(settings.EDAD_MEDIA, settings.EDAD_STD)))

                # Variables de ingesta (gramos / día) basadas en Campana de Gauss
                grasa_sat = max(1.0, np.random.normal(settings.GRASA_SAT_MEDIA_LOW_FAT, settings.GRASA_SAT_STD_LOW_FAT))
                grasa_mono = max(1.0, np.random.normal(settings.GRASA_MONO_MEDIA_LOW_FAT, settings.GRASA_MONO_STD_LOW_FAT))
                grasa_poli = max(1.0, np.random.normal(settings.GRASA_POLI_MEDIA_LOW_FAT, settings.GRASA_POLI_STD_LOW_FAT))

                # Variables de salud iniciales basadas en Campana de Gauss
                col_total = np.random.normal(settings.COL_TOTAL_MEDIA_LOW_FAT, settings.COL_TOTAL_STD_LOW_FAT)
                col_ldl = np.random.normal(settings.COL_LDL_MEDIA_LOW_FAT, settings.COL_LDL_STD_LOW_FAT)


            # Instanciar el agente Paciente con sus características
            paciente = Paciente(i, self, grupo, es_mujer, edad, grasa_sat, grasa_mono, grasa_poli, col_total, col_ldl)
            self.schedule.add(paciente)

        # Recolector de datos (DataCollector)
        # self.datacollector = DataCollector(
        #     model_reporters={
        #         "Colesterol_Medio": lambda m: np.mean([a.col_total for a in m.schedule.agents])
        #     }
        # )
    
    def step(self):
        '''Función que se ejecuta en cada paso de la simulación.'''
        # self.datacollector.collect(self)
        print(f"\n--- Iniciando Semana {self.current_step} ---")
        self.schedule.step()
        self.current_step += 1