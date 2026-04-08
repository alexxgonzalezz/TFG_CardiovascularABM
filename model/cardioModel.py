# Importar librerías
import mesa
import numpy as np
import random

# Importar la clase Paciente y variables de configuración
from agents.paciente import Paciente
from configuration import settings
from mesa.datacollection import DataCollector

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
                grupo_dieta = 'Mediterránea'
                es_mujer = random.random() < settings.PROPORCION_MUJERES_MED
                es_fumador = random.random() < settings.PROPORCION_FUMADORES_MED

                # Variables de salud iniciales basadas en Campana de Gauss
                edad = max(18, int(np.random.normal(settings.EDAD_MEDIA, settings.EDAD_STD)))
                imc = np.random.normal(settings.IMC_MEDIA, settings.IMC_STD_MED)
                col_total = np.random.normal(settings.COL_TOTAL_MEDIA_MED, settings.COL_TOTAL_STD_MED)
                ldl = np.random.normal(settings.COL_LDL_MEDIA_MED, settings.COL_LDL_STD_MED)
                trigliceridos = np.random.normal(settings.TRIGLICERIDOS_MEDIA_MED, settings.TRIGLICERIDOS_STD_MED)
                glucosa = np.random.normal(settings.GLUCOSA_MEDIA_MED, settings.GLUCOSA_STD_MED)
                insulina = np.random.normal(settings.INSULINA_MEDIA_MED, settings.INSULINA_STD_MED)
                pas = np.random.normal(settings.PAS_MEDIA_MED, settings.PAS_STD_MED)

            # Grupo dieta baja en grasas
            else:
                grupo_dieta = 'Baja en grasas'
                es_mujer = random.random() < settings.PROPORCION_MUJERES_LOW_FAT
                es_fumador = random.random() < settings.PROPORCION_FUMADORES_LOW_FAT

                # Variables de salud iniciales basadas en Campana de Gauss
                edad = max(18, int(np.random.normal(settings.EDAD_MEDIA, settings.EDAD_STD)))
                imc = np.random.normal(settings.IMC_MEDIA, settings.IMC_STD_LOW_FAT)
                col_total = np.random.normal(settings.COL_TOTAL_MEDIA_LOW_FAT, settings.COL_TOTAL_STD_LOW_FAT)
                ldl = np.random.normal(settings.COL_LDL_MEDIA_LOW_FAT, settings.COL_LDL_STD_LOW_FAT)
                trigliceridos = np.random.normal(settings.TRIGLICERIDOS_MEDIA_LOW_FAT, settings.TRIGLICERIDOS_STD_LOW_FAT)
                glucosa = np.random.normal(settings.GLUCOSA_MEDIA_LOW_FAT, settings.GLUCOSA_STD_LOW_FAT)
                insulina =np.random.normal(settings.INSULINA_MEDIA_LOW_FAT, settings.INSULINA_STD_LOW_FAT)
                pas = np.random.normal(settings.PAS_MEDIA_LOW_FAT, settings.PAS_STD_LOW_FAT)

            # Instanciar el agente Paciente con sus características
            paciente = Paciente(i, self, grupo_dieta, es_mujer, es_fumador, edad, imc, col_total, ldl, trigliceridos, glucosa, insulina, pas)
            self.schedule.add(paciente)

        # Recolector de datos (DataCollector)
        self.datacollector = DataCollector(
            model_reporters={
                "Colesterol_Medio": lambda m: np.mean([a.col_total for a in m.schedule.agents])
            }
        )
    
    def step(self):
        '''Función que se ejecuta en cada paso de la simulación.'''
        self.datacollector.collect(self)
        print(f"\n--- Iniciando Mes {self.current_step} ---")
        self.schedule.step()
        self.current_step += 1