import mesa
import numpy as np

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, grupo, es_mujer, edad, abandona, semana_abandono,
                 calorias_base, pct_prot_base, pct_carb_base, pct_grasa_base,
                 calorias, pct_prot, pct_carb, pct_grasa):
        super().__init__(model)

        # Perfil del paciente
        self.unique_id = unique_id
        self.grupo = grupo
        self.sexo = "Mujer" if es_mujer else "Hombre"
        self.edad = edad

        # Lógica de abandono de la dieta
        self.abandona = abandona
        self.semana_abandono = semana_abandono if abandona else None

        # HÁBITOS BASE (Lo que comía antes de empezar la dieta) (PORCENTAJES)
        self.calorias_base = calorias_base
        self.pct_prot_base = pct_prot_base
        self.pct_carb_base = pct_carb_base
        self.pct_grasa_base = pct_grasa_base

        # Calorías (kcal) y macronuientes esenciales OBJETIVO (PORCENTAJES)
        self.calorias_objetivo = calorias
        self.pct_prot_objetivo = pct_prot
        self.pct_carb_objetivo = pct_carb
        self.pct_grasa_objetivo = pct_grasa

    def comer(self):
        '''Simula la ingesta semanal del paciente'''

        # Asumimos que el paciente tiene una desviación del 5% respecto a su objetivo
        VARIABILIDAD_SEMANAL = 0.05

        # Comprobar abandono: ¿En qué semana estamos?
        if self.abandona and self.model.current_step >= self.semana_abandono:
            # Si el paciente abandona, vuelve a sus hábitos base
            self.calorias_objetivo = self.calorias_base
            self.pct_prot_objetivo = self.pct_prot_base
            self.pct_carb_objetivo = self.pct_carb_base
            self.pct_grasa_objetivo = self.pct_grasa_base
            estado = "ABANDONO"

        else:
            # El paciente sigue con su dieta asignada
            estado = "ACTIVO"

        # 1. Calorías reales consumidas cada semana (con variabilidad)
        self.calorias = max(1000, np.random.normal(self.calorias_objetivo, self.calorias_objetivo * VARIABILIDAD_SEMANAL))

        # 2. Aplicar variabilidad a los porcentajes de macronutrientes objetivo
        proteinas_pct = max(0.01, np.random.normal(self.pct_prot_objetivo, self.pct_prot_objetivo * VARIABILIDAD_SEMANAL))
        carbohidratos_pct = max(0.01, np.random.normal(self.pct_carb_objetivo, self.pct_carb_objetivo * VARIABILIDAD_SEMANAL))
        grasas_pct = max(0.01, np.random.normal(self.pct_grasa_objetivo, self.pct_grasa_objetivo * VARIABILIDAD_SEMANAL))

        # 3. Normalizar los porcentajes para que sumen 100%
        suma_total = proteinas_pct + carbohidratos_pct + grasas_pct
        proteinas_pct_real = proteinas_pct / suma_total
        carbohidratos_pct_real = carbohidratos_pct / suma_total
        grasas_pct_real = grasas_pct / suma_total

        # 4. Convertimos los porcentajes a gramos (1g proteína = 4 kcal, 1g carbohidrato = 4 kcal, 1g grasa = 9 kcal)
        self.proteinas = (self.calorias * proteinas_pct_real) / 4.0
        self.carbohidratos = (self.calorias * carbohidratos_pct_real) / 4.0
        self.grasas = (self.calorias * grasas_pct_real) / 9.0 

        return estado # Devuelve el estado del paciente (activo o abandono)

    def actualizar_biomarcadores(self):
        '''Función para actualizar los biomarcadores de salud del paciente en función de su ingesta real'''
        # Aquí se implementaría la lógica para actualizar los biomarcadores (colesterol total, LDL, HDL, etc.)
        pass

    def step(self):
        '''Función que se ejecuta en cada paso (semana) de la simulación'''

        # Simular ingesta semanal del paciente
        estado_paciente = self.comer()

        # Actualizar los biomarcadores de salud en función de la ingesta 
        # self.actualizar_biomarcadores()

        # Prueba con 5 pacientes para analizar su evolución semanal de ingesta
        if self.unique_id < 30:
            pct_proteinas = (self.proteinas * 4 / self.calorias) * 100
            pct_carbohidratos = (self.carbohidratos * 4 / self.calorias) * 100
            pct_grasas = (self.grasas * 9 / self.calorias) * 100
            print(f'    • Paciente {self.unique_id} ({self.grupo}) [{estado_paciente}] -> '
                    f'Calorías: {self.calorias:.1f} kcal, '
                    f'Proteínas: {self.proteinas:.1f}g ({pct_proteinas:.1f}%), '
                    f'Carbohidratos: {self.carbohidratos:.1f}g ({pct_carbohidratos:.1f}%), '
                    f'Grasas: {self.grasas:.1f}g ({pct_grasas:.1f}%)')

        # # Simulación completa de ingesta semanal
        # pct_proteinas = (self.proteinas * 4 / self.calorias) * 100
        # pct_carbohidratos = (self.carbohidratos * 4 / self.calorias) * 100
        # pct_grasas = (self.grasas * 9 / self.calorias) * 100
        # print(f'    • Paciente {self.unique_id} ({self.grupo}) [{estado_paciente}] -> '
        #         f'Calorías: {self.calorias:.1f} kcal, '
        #         f'Proteínas: {self.proteinas:.1f}g ({pct_proteinas:.1f}%), '
        #         f'Carbohidratos: {self.carbohidratos:.1f}g ({pct_carbohidratos:.1f}%), '
        #         f'Grasas: {self.grasas:.1f}g ({pct_grasas:.1f}%)')