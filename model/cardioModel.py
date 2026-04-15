# Importar librerías
import mesa
import numpy as np
import random

# Importar la clase Paciente y variables de configuración
from agents.paciente import Paciente
from configuration import settings

class CardioModel(mesa.Model):
    '''Modelo que gestiona la simulación de pacientes'''

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

                # ¿Abandona la dieta?
                abandona = random.random() < settings.TASA_ABANDONO_MED
                semana_abandono = random.randint(1, 12) if abandona else None # Abandona en alguna semana entre la 1 y la 12

                # HÁBITOS BASE (Lo que comía antes de empezar la dieta)
                calorias_base = max(1000, np.random.normal(settings.ENERGIA_MEDIA_MED_INICIAL, settings.ENERGIA_STD_MED_INICIAL))
                pct_prot_base = np.random.normal(settings.PROT_PCT_MEDIA_MED_INICIAL, settings.PROT_PCT_STD_MED_INICIAL)
                pct_carb_base = np.random.normal(settings.CARB_PCT_MEDIA_MED_INICIAL, settings.CARB_PCT_STD_MED_INICIAL)
                pct_grasa_base = np.random.normal(settings.GRASA_PCT_MEDIA_MED_INICIAL, settings.GRASA_PCT_STD_MED_INICIAL)


                # OBJETIVOS DE LA DIETA MEDITERRÁNEA
                calorias = max(1000, np.random.normal(settings.ENERGIA_MEDIA_MED, settings.ENERGIA_STD_MED))
                pct_prot = np.random.normal(settings.PROT_PCT_MEDIA_MED, settings.PROT_PCT_STD_MED)
                pct_carb = np.random.normal(settings.CARB_PCT_MEDIA_MED, settings.CARB_PCT_STD_MED)
                pct_grasa = np.random.normal(settings.GRASA_PCT_MEDIA_MED, settings.GRASA_PCT_STD_MED)


            # Grupo dieta baja en grasas
            else:
                grupo = 'Baja en Grasas'
                es_mujer = random.random() < settings.PROPORCION_MUJERES_LOW_FAT
                edad = max(18, int(np.random.normal(settings.EDAD_MEDIA, settings.EDAD_STD)))

                # ¿Abandona la dieta?
                abandona = random.random() < settings.TASA_ABANDONO_LOW_FAT
                semana_abandono = random.randint(1, 12) if abandona else None # Abandona en alguna semana entre la 1 y la 12

                # HÁBITOS BASE (Lo que comía antes de empezar la dieta)
                calorias_base = max(1000, np.random.normal(settings.ENERGIA_MEDIA_LOW_FAT_INICIAL, settings.ENERGIA_STD_LOW_FAT_INICIAL))
                pct_prot_base = np.random.normal(settings.PROT_PCT_MEDIA_LOW_FAT_INICIAL, settings.PROT_PCT_STD_LOW_FAT_INICIAL)
                pct_carb_base = np.random.normal(settings.CARB_PCT_MEDIA_LOW_FAT_INICIAL, settings.CARB_PCT_STD_LOW_FAT_INICIAL)
                pct_grasa_base = np.random.normal(settings.GRASA_PCT_MEDIA_LOW_FAT_INICIAL, settings.GRASA_PCT_STD_LOW_FAT_INICIAL)

                # OBJETIVOS DE LA DIETA BAJA EN GRASAS
                calorias = max(1000, np.random.normal(settings.ENERGIA_MEDIA_LOW_FAT, settings.ENERGIA_STD_LOW_FAT))
                pct_prot = np.random.normal(settings.PROT_PCT_MEDIA_LOW_FAT, settings.PROT_PCT_STD_LOW_FAT)
                pct_carb = np.random.normal(settings.CARB_PCT_MEDIA_LOW_FAT, settings.CARB_PCT_STD_LOW_FAT)
                pct_grasa = np.random.normal(settings.GRASA_PCT_MEDIA_LOW_FAT, settings.GRASA_PCT_STD_LOW_FAT)

                # # Variables de salud iniciales basadas en Campana de Gauss
                # col_total = np.random.normal(settings.COL_TOTAL_MEDIA_LOW_FAT, settings.COL_TOTAL_STD_LOW_FAT)
                # col_ldl = np.random.normal(settings.COL_LDL_MEDIA_LOW_FAT, settings.COL_LDL_STD_LOW_FAT)


            # Instanciar el agente Paciente con sus características
            paciente = Paciente(i, self, grupo, es_mujer, edad, abandona, semana_abandono,
                                calorias_base, pct_prot_base, pct_carb_base, pct_grasa_base,
                                calorias, pct_prot, pct_carb, pct_grasa)
            self.schedule.add(paciente)
    
    def step(self):
        '''Función que se ejecuta en cada paso de la simulación.'''
        # self.datacollector.collect(self)
        print(f"\n--- Iniciando Semana {self.current_step} ---")
        self.schedule.step()
        self.current_step += 1