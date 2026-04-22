import mesa
import numpy as np

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, grupo, es_mujer, edad, abandona, semana_abandono,
                 calorias_base, pct_prot_base, pct_carb_base, pct_grasa_base, pct_grasa_sat_base, pct_grasa_mono_base, pct_grasa_poli_base,
                 calorias, pct_prot, pct_carb, pct_grasa, pct_grasa_sat, pct_grasa_mono, pct_grasa_poli,
                 col_total, col_ldl):
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
        self.pct_grasa_sat_base = pct_grasa_sat_base
        self.pct_grasa_mono_base = pct_grasa_mono_base
        self.pct_grasa_poli_base = pct_grasa_poli_base

        # Calorías (kcal) y macronuientes esenciales OBJETIVO (PORCENTAJES)
        self.calorias_objetivo = calorias
        self.pct_prot_objetivo = pct_prot
        self.pct_carb_objetivo = pct_carb
        self.pct_grasa_objetivo = pct_grasa
        self.pct_grasa_sat_objetivo = pct_grasa_sat
        self.pct_grasa_mono_objetivo = pct_grasa_mono
        self.pct_grasa_poli_objetivo = pct_grasa_poli

        # Variables de salud iniciales
        self.col_total = col_total
        self.col_ldl = col_ldl

    def comer(self):
        '''Simula la ingesta semanal del paciente'''

        # Asumimos que el paciente tiene una desviación del 2,5% respecto a su objetivo
        VARIABILIDAD_SEMANAL = 0.025

        # Comprobar abandono: ¿En qué semana estamos?
        if self.abandona and self.model.current_step >= self.semana_abandono:
            # Si el paciente abandona, vuelve a sus hábitos base
            self.calorias_objetivo = self.calorias_base
            self.pct_prot_objetivo = self.pct_prot_base
            self.pct_carb_objetivo = self.pct_carb_base
            self.pct_grasa_objetivo = self.pct_grasa_base
            self.pct_grasa_sat_objetivo = self.pct_grasa_sat_base
            self.pct_grasa_mono_objetivo = self.pct_grasa_mono_base
            self.pct_grasa_poli_objetivo = self.pct_grasa_poli_base
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

        # 5. Hacemos lo mismo para los tipos de grasa (saturada, monoinsaturada, poliinsaturada)
        raw_sat = max(0.01, np.random.normal(self.pct_grasa_sat_objetivo, self.pct_grasa_sat_objetivo * VARIABILIDAD_SEMANAL))
        raw_mono = max(0.01, np.random.normal(self.pct_grasa_mono_objetivo, self.pct_grasa_mono_objetivo * VARIABILIDAD_SEMANAL))
        raw_poli = max(0.01, np.random.normal(self.pct_grasa_poli_objetivo, self.pct_grasa_poli_objetivo * VARIABILIDAD_SEMANAL))

        suma_tipos_grasa = raw_sat + raw_mono + raw_poli
        self.grasa_sat_real = raw_sat / suma_tipos_grasa
        self.grasa_mono_real = raw_mono / suma_tipos_grasa
        self.grasa_poli_real = raw_poli / suma_tipos_grasa

        self.grasa_sat = self.grasas * self.grasa_sat_real
        self.grasa_mono = self.grasas * self.grasa_mono_real
        self.grasa_poli = self.grasas * self.grasa_poli_real

        self.estado_actual = estado

        return estado # Devuelve el estado del paciente (activo o abandono)

    def actualizar_biomarcadores(self):
        '''Función para actualizar los biomarcadores de salud del paciente en función de su ingesta real'''
        
        # 1. Guardamos el colesterol LDL con el que parte el paciente
        if not hasattr(self, 'col_ldl_base'):
            self.col_ldl_base = self.col_ldl

        # Usamos nueva variable para no cambiar valor
        col_ldl_inicial = self.col_ldl_base

        # 2. Comparar porcentajes de energía de grasas (Ingesta actual vs Habitos base)
        pct_sat_actual = (self.grasa_sat * 9.0) / self.calorias
        pct_mono_actual = (self.grasa_mono * 9.0) / self.calorias
        pct_poli_actual = (self.grasa_poli * 9.0) / self.calorias

        # Calculamos la mejora en términos de porcentajes respecto a los hábitos base
        # Bajar saturada y subir monoinsaturada y poliinsaturada es beneficioso
        mejora_sat = self.pct_grasa_sat_base - pct_sat_actual
        mejora_mono = pct_mono_actual - self.pct_grasa_mono_base
        mejora_poli = pct_poli_actual - self.pct_grasa_poli_base

        # 3. Puntuamos la mejora total 
        puntuacion_grasas = (mejora_sat * 1.5) + (mejora_mono * 0.3) + (mejora_poli * 0.7)
        calidad_grasas = max(0.0, min(1.0, puntuacion_grasas / 0.06)) # Normalizamos entre 0 y 1

        # 4. Impacto del déficit calórico (+déficit = +mejoría)
        deficit = self.calorias_base - self.calorias
        factor_calorias = max(0.0, min(1.0, deficit / 700.0)) # Un déficit de 700 kcal da puntuación máxima (1.0)

        # 5. Combinamos ambos factores para calcular la mejora total
        mejora_total = (calidad_grasas * 0.8) + (factor_calorias * 0.2) # Damos más peso a la calidad de las grasas que al déficit calórico

        # 6. Establecemos un límite de reducción del colesterol LDL (máximo 18% de mejora respecto al valor inicial)
        mejora_max_ldl = col_ldl_inicial * 0.18
        ldl_objetivo = col_ldl_inicial - (mejora_total * mejora_max_ldl)

        # 7. Función asíntotica (curva más pronunciada al principio y luego se estabiliza)
        if ldl_objetivo < self.col_ldl:
            # El paciente mejora rápido al principio y luego se estabiliza
            k = 0.35
        else:
            # Si el paciente empeora, el aumento es más gradual
            k = 0.15
        
        self.col_ldl = self.col_ldl + (ldl_objetivo - self.col_ldl) * k


    def step(self):
        '''Función que se ejecuta en cada paso (semana) de la simulación'''

        # Simular ingesta semanal del paciente
        estado_paciente = self.comer()

        # Actualizar los biomarcadores de salud en función de la ingesta 
        self.actualizar_biomarcadores()

        # # Prueba con 5 pacientes para analizar su evolución semanal de ingesta
        # if self.unique_id < 5:
        #     # Porcentajes de macronutrientes consumidos cada semana
        #     pct_proteinas = (self.proteinas * 4 / self.calorias) * 100
        #     pct_carbohidratos = (self.carbohidratos * 4 / self.calorias) * 100
        #     pct_grasas = (self.grasas * 9 / self.calorias) * 100

        #     # Porcentajes de tipos de grasa consumidos cada semana
        #     pct_sat = (self.grasa_sat / self.grasas) * 100
        #     pct_mono = (self.grasa_mono / self.grasas) * 100
        #     pct_poli = (self.grasa_poli / self.grasas) * 100

        #     print(f'    • Paciente {self.unique_id} ({self.grupo}) [{estado_paciente}] -> '
        #             f'Calorías: {self.calorias:.1f} kcal | '
        #             f'Macros: Prot -> {self.proteinas:.1f}g ({pct_proteinas:.1f}%), '
        #             f'Carb: {self.carbohidratos:.1f}g ({pct_carbohidratos:.1f}%), ' 
        #             f'Grasas: {self.grasas:.1f}g ({pct_grasas:.1f}%) '
        #             f'[Sat: {self.grasa_sat:.1f}g ({pct_sat:.1f}%), Mono: {self.grasa_mono:.1f}g ({pct_mono:.1f}%), Poli: {self.grasa_poli:.1f}g ({pct_poli:.1f}%)] | '
        #             f'Colesterol: {self.col_total:.1f} mmol/L | '
        #             f'LDL: {self.col_ldl:.1f} mmol/L')

        # # Simulación completa de ingesta semanal
        # pct_proteinas = (self.proteinas * 4 / self.calorias) * 100
        # pct_carbohidratos = (self.carbohidratos * 4 / self.calorias) * 100
        # pct_grasas = (self.grasas * 9 / self.calorias) * 100
        # print(f'    • Paciente {self.unique_id} ({self.grupo}) [{estado_paciente}] -> '
        #         f'Calorías: {self.calorias:.1f} kcal, '
        #         f'Proteínas: {self.proteinas:.1f}g ({pct_proteinas:.1f}%), '
        #         f'Carbohidratos: {self.carbohidratos:.1f}g ({pct_carbohidratos:.1f}%), '
        #         f'Grasas: {self.grasas:.1f}g ({pct_grasas:.1f}%)')