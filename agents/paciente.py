import mesa
import numpy as np

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, grupo, es_mujer, edad, abandona, semana_abandono,
                 calorias_base, pct_prot_base, pct_carb_base, pct_grasa_base, pct_grasa_sat_base, pct_grasa_mono_base, pct_grasa_poli_base, fibra_soluble_base, col_dietetico_base,
                 calorias, pct_prot, pct_carb, pct_grasa, pct_grasa_sat, pct_grasa_mono, pct_grasa_poli, fibra_soluble, col_dietetico,
                 col_total, col_ldl, insulina):
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
        self.col_dietetico_base = col_dietetico_base

        # Calorías (kcal) y macronutrientes esenciales OBJETIVO (PORCENTAJES)
        self.calorias_objetivo = calorias
        self.pct_prot_objetivo = pct_prot
        self.pct_carb_objetivo = pct_carb
        self.pct_grasa_objetivo = pct_grasa
        self.pct_grasa_sat_objetivo = pct_grasa_sat
        self.pct_grasa_mono_objetivo = pct_grasa_mono
        self.pct_grasa_poli_objetivo = pct_grasa_poli
        self.fibra_soluble_objetivo = fibra_soluble
        self.col_dietetico_objetivo = col_dietetico

        # Variables de salud iniciales
        self.col_total = col_total
        self.col_ldl = col_ldl
        self.insulina = insulina

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
            self.col_dietetico_objetivo = self.col_dietetico_base
            estado = "ABANDONO"

        else:
            # El paciente sigue con su dieta asignada
            estado = "ACTIVO"

        # 1. Calorías reales consumidas cada semana + fibra soluble + colesterol dietético (con variabilidad)
        self.calorias = max(1000, np.random.normal(self.calorias_objetivo, self.calorias_objetivo * VARIABILIDAD_SEMANAL))
        self.fibra_soluble = max(0, np.random.normal(self.fibra_soluble_objetivo, self.fibra_soluble_objetivo * VARIABILIDAD_SEMANAL))
        self.col_dietetico = max(0, np.random.normal(self.col_dietetico_objetivo, self.col_dietetico_objetivo * VARIABILIDAD_SEMANAL))

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

        # Devolvemos el estado actual del paciente (ACTIVO o ABANDONO)
        return estado

    def actualizar_colesterol_total(self):
        '''Función para actualizar el colesterol total en función de la dieta'''

        # 1. Guardamos el colesterol total con el que parte el paciente
        if not hasattr(self, 'col_total_base'):
            self.col_total_base = self.col_total

        col_total_inicial = self.col_total_base

        # 2. Calcular % de energía aportada por cada grasa durante la DIETA
        S_dieta = ((self.grasa_sat * 9.0) / self.calorias) * 100
        M_dieta = ((self.grasa_mono * 9.0) / self.calorias) * 100
        P_dieta = ((self.grasa_poli * 9.0) / self.calorias) * 100

        # 3. Calcular % de energía aportada por cada grasa en los HÁBITOS BASE
        S_base = (self.pct_grasa_sat_base * self.pct_grasa_base) * 100
        M_base = (self.pct_grasa_mono_base * self.pct_grasa_base) * 100
        P_base = (self.pct_grasa_poli_base * self.pct_grasa_base) * 100

        # 4. Calcular los incrementos/decrementos (deltas)
        # 4.1 Tipos de grasa
        delta_S = S_dieta - S_base
        delta_M = M_dieta - M_base
        delta_P = P_dieta - P_base

        # 4.2 Añadimos el efecto de la fibra soluble
        delta_F = self.fibra_soluble - self.fibra_soluble_base

        # 4.3 Añadimos el efecto del colesterol dietético
        c_inicial = (self.col_dietetico_base / self.calorias_base) * 1000  # mg de colesterol por 1000 kcal en los hábitos base
        c_dieta = (self.col_dietetico / self.calorias) * 1000  # mg de colesterol por 1000 kcal en la dieta

        # 4.4 Añadimos el efecto del déficit calórico
        deficit = self.calorias_base - self.calorias

        # 5. Aplicar ecuación matemática para bajada de Colesterol Total
        # 5.1 Efecto de los tipos de grasa (Mensink and Katan, 2003)
        cambio_ct_mgdl = 1.2 * (1.8 * delta_S - 0.1 * delta_M - 0.5 * delta_P)
        cambio_ct_grasas = cambio_ct_mgdl / 38.67  # Convertir de mg/dL a mmol/L

        # 5.2 Efecto de la fibra soluble (0.045 mmol/L por cada gramo adicional de fibra soluble)
        cambio_ct_fibra = -0.045 * delta_F

        # 5.3 Efecto del colesterol dietético (Ecuación de Keys)
        cambio_ct_colesterol = 1.5 * (np.sqrt(c_dieta) - np.sqrt(c_inicial)) / 38.67  # Convertir de mg/dL a mmol/L

        # 5.4 Efecto del déficit calórico
        cambio_ct_deficit = -0.08 * (deficit / 700.0)  # Beneficio máximo de -0.08 mmol/L por alcanzar un déficit de 700 kcal

        # 6. Colesterol Total objetivo
        col_total_objetivo = col_total_inicial + cambio_ct_grasas + cambio_ct_fibra + cambio_ct_colesterol + cambio_ct_deficit

        if col_total_objetivo < self.col_total:
            k = 0.35  # Si el paciente mejora, baja rápido al principio y luego se estabiliza
        else:
            k = 0.15  # Si el paciente empeora, el aumento es más gradual
        
        self.col_total = self.col_total + (col_total_objetivo - self.col_total) * k


    def actualizar_colesterol_ldl(self):
        '''Función para actualizar el colesterol LDL en función de la dieta'''
        
        # 1. Guardamos el colesterol con el que parte el paciente
        if not hasattr(self, 'col_ldl_base'):
            self.col_ldl_base = self.col_ldl
            
        col_ldl_inicial = self.col_ldl_base

        # 2. Calcular % de energía aportada por cada grasa durante la dieta
        S_dieta = ((self.grasa_sat * 9.0) / self.calorias) * 100
        M_dieta = ((self.grasa_mono * 9.0) / self.calorias) * 100
        P_dieta = ((self.grasa_poli * 9.0) / self.calorias) * 100

        # 3. Calcular % de energía aportada por cada grasa en los hábitos base
        S_base = (self.pct_grasa_sat_base * self.pct_grasa_base) * 100
        M_base = (self.pct_grasa_mono_base * self.pct_grasa_base) * 100
        P_base = (self.pct_grasa_poli_base * self.pct_grasa_base) * 100

        # 4. Calcular los incrementos/decrementos (deltas)
        # 4.1 Tipos de grasa
        delta_S = S_dieta - S_base
        delta_M = M_dieta - M_base
        delta_P = P_dieta - P_base

        # 4.2 Añadimos el efecto de la fibra soluble
        delta_F = self.fibra_soluble - self.fibra_soluble_base

        # 4.3 Añadimos el efecto del colesterol dietético
        delta_C = self.col_dietetico - self.col_dietetico_base

        # 4.4 Añadimos el efecto del deficit calórico
        deficit = self.calorias_base - self.calorias

        # 5. Aplicar la ecuación matemática para bajada de Colesterol LDL
        # 5.1 Efecto de los tipos de grasa (Mensink and Katan, 2003)
        cambio_ldl_grasas = (0.036 * delta_S) - (0.009 * delta_M) - (0.022 * delta_P)

        # 5.2 Efecto de la fibra soluble (0.057 mmol/L por cada gramo adicional de fibra soluble)
        cambio_ldl_fibra = -0.057 * delta_F

        # 5.3 Efecto del colesterol dietético (Weggemans et al., 2001)
        cambio_ldl_colesterol = 0.012 * (delta_C / 100.0)

        # 5.4 Efecto del déficit calórico
        cambio_deficit = -0.08 * (deficit / 700.0)  # Beneficio máximo de -0.08 mmol/L por alcanzar un déficit de 700 kcal

        # # 5.2 Aplicar la ecuación matemática con ajuste de pesos para bajada de Colesterol LDL
        # # Le damos mayor importancia a las grasas monoinsaturadas por el factor AOVE
        # # cambio_ldl_grasas = (0.068 * delta_S) - (0.089 * delta_M) - (0.045 * delta_P) - (0.033 * delta_F) --> LA DE LOS BUENOS RESULTADOS
        # cambio_ldl_grasas = (0.036 * delta_S) - (0.009 * delta_M) - (0.022 * delta_P)

        # 6. Colesterol Total y LDL objetivo
        ldl_objetivo = col_ldl_inicial + cambio_ldl_grasas + cambio_ldl_fibra + cambio_ldl_colesterol + cambio_deficit

        # 7. Función asintótica
        # Si el paciente mejora, baja rápido al principio y luego se estabiliza
        # Si el paciente empeora, el aumento es más gradual
        if ldl_objetivo < self.col_ldl:
            k_ldl = 0.35
        else:
            k_ldl = 0.15
        
        self.col_ldl = self.col_ldl + (ldl_objetivo - self.col_ldl) * k_ldl


    def step(self):
        '''Función que se ejecuta en cada semana de la simulación'''

        # Simular ingesta semanal del paciente
        estado_paciente = self.comer()

        # Actualizar los biomarcadores de salud en función de la ingesta 
        self.actualizar_colesterol_total()
        self.actualizar_colesterol_ldl()