import mesa
import numpy as np

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, grupo, es_mujer, edad, abandona, semana_abandono,
                 calorias_base, pct_prot_base, pct_carb_base, pct_grasa_base, pct_grasa_sat_base, pct_grasa_mono_base, pct_grasa_poli_base, fibra_soluble_base,
                 calorias, pct_prot, pct_carb, pct_grasa, pct_grasa_sat, pct_grasa_mono, pct_grasa_poli, fibra_soluble,
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
        self.fibra_soluble_base = fibra_soluble_base

        # Calorías (kcal) y macronuientes esenciales OBJETIVO (PORCENTAJES)
        self.calorias_objetivo = calorias
        self.pct_prot_objetivo = pct_prot
        self.pct_carb_objetivo = pct_carb
        self.pct_grasa_objetivo = pct_grasa
        self.pct_grasa_sat_objetivo = pct_grasa_sat
        self.pct_grasa_mono_objetivo = pct_grasa_mono
        self.pct_grasa_poli_objetivo = pct_grasa_poli
        self.fibra_soluble_objetivo = fibra_soluble

        # Variables de salud iniciales
        self.col_total = col_total
        self.col_ldl = col_ldl

    def comer(self):
        '''Simula la ingesta semanal del paciente'''

        # Asumimos que el paciente tiene una desviación del 2,5% respecto a su dieta 
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
            self.fibra_soluble_objetivo = self.fibra_soluble_base
            estado = "ABANDONO"

        else:
            # El paciente sigue con su dieta asignada
            estado = "ACTIVO"

        # 1. Calorías reales consumidas cada semana (con variabilidad)
        self.calorias = max(1000, np.random.normal(self.calorias_objetivo, self.calorias_objetivo * VARIABILIDAD_SEMANAL))
        self.fibra_soluble = max(0, np.random.normal(self.fibra_soluble_objetivo, self.fibra_soluble_objetivo * VARIABILIDAD_SEMANAL))

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

        self.grasa_sat = self.grasas * raw_sat
        self.grasa_mono = self.grasas * raw_mono
        self.grasa_poli = self.grasas * raw_poli

        # Guardamos un porcentaje para "otras grasas"
        suma_grasas = self.grasa_sat + self.grasa_mono + self.grasa_poli
        self.otras_grasas = max(0, self.grasas - suma_grasas)

        self.estado_actual = estado

        return estado # Devuelve el estado del paciente (activo o abandono)


    def actualizar_biomarcadores(self):
        '''Función para actualizar el colesterol LDL en función de la dieta y el déficit calórico'''
        
        # 1. Guardamos el colesterol LDL con el que parte el paciente
        if not hasattr(self, 'col_ldl_base'):
            self.col_ldl_base = self.col_ldl
        col_ldl_inicial = self.col_ldl_base

        # 2. Calcular % de energía aportada por cada grasa ACTUALMENTE (Escala 0-100)
        S_actual = ((self.grasa_sat * 9.0) / self.calorias) * 100
        M_actual = ((self.grasa_mono * 9.0) / self.calorias) * 100
        P_actual = ((self.grasa_poli * 9.0) / self.calorias) * 100

        # 3. Calcular % de energía aportada por cada grasa en los HÁBITOS BASE (Escala 0-100)
        S_base = (self.pct_grasa_sat_base * self.pct_grasa_base) * 100
        M_base = (self.pct_grasa_mono_base * self.pct_grasa_base) * 100
        P_base = (self.pct_grasa_poli_base * self.pct_grasa_base) * 100

        # 4. Calcular los incrementos/decrementos (Deltas)
        delta_S = S_actual - S_base
        delta_M = M_actual - M_base
        delta_P = P_actual - P_base
        delta_F = self.fibra_soluble - self.fibra_soluble_base

        # 5. Calcular el déficit calórico
        deficit = self.calorias_base - self.calorias

        # 6. Aplicar la Ecuación Matemática Completa --> ajuste de pesos 
        # A) Efecto de la Dieta (Grasas + Fibra)
        # Le damos mayor importancia a las grasas monoinsaturadas por el factor AOVE
        cambio_ldl_grasas = (0.068 * delta_S) - (0.102 * delta_M) - (0.03 * delta_P) - (0.022 * delta_F)
        
        # B) Efecto de la pérdida de peso
        # Calculamos un factor entre 0 y 1 (donde 1 representa alcanzar un déficit de 700 kcal).
        # Establecemos que el beneficio máximo por adelgazar sea de -0.05 mmol/L.
        factor_deficit = max(0.0, min(1.0, deficit / 700.0))
        cambio_ldl_deficit = -0.05 * factor_deficit
        
        # 7. LDL Objetivo a largo plazo (Suma de los hábitos dietéticos + pérdida de peso)
        ldl_objetivo = col_ldl_inicial + cambio_ldl_grasas + cambio_ldl_deficit

        # 8. Función asintótica (curva de estabilización semanal)
        if ldl_objetivo < self.col_ldl:
            # Si el paciente mejora, baja rápido al principio y luego se estabiliza
            k = 0.35
        else:
            # Si el paciente empeora, el aumento es más gradual
            k = 0.15
        
        self.col_ldl = self.col_ldl + (ldl_objetivo - self.col_ldl) * k


    def step(self):
        '''Función que se ejecuta en cada semana de la simulación'''

        # Simular ingesta semanal del paciente
        estado_paciente = self.comer()

        # Actualizar los biomarcadores de salud en función de la ingesta 
        self.actualizar_biomarcadores()