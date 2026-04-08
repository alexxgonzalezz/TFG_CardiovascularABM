import mesa

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, grupo_dieta, es_mujer, es_fumador, edad, imc, col_total, ldl, trigliceridos, glucosa, insulina, pas):
        super().__init__(model)

        # Perfil del paciente
        self.unique_id = unique_id
        self.grupo_dieta = grupo_dieta
        self.sexo = "Mujer" if es_mujer else "Hombre"
        self.fumador = "Sí" if es_fumador else "No"
        
        # Biomarcadores de salud
        self.edad = edad
        self.imc = imc
        self.col_total = col_total
        self.ldl = ldl
        self.trigliceridos = trigliceridos
        self.glucosa = glucosa
        self.insulina = insulina
        self.pas = pas

    def step(self):
        '''
        Función que se ejecuta en cada paso de la simulación.
        Programar cómo la dieta afecta a los factores de riesgo del paciente.
        '''

        # Prueba imprimir los factores de riesgo del paciente en cada paso
        print(f'Paciente {self.unique_id} -> Dieta: {self.grupo_dieta} | Sexo: {self.sexo} | Edad: {self.edad} | ¿Fumador?: {self.fumador} | IMC: {self.imc:.2f} | Colesterol total: {self.col_total:.2f} | Colesterol LDL: {self.ldl:.2f} | Trigliceridos: {self.trigliceridos:.2f} | Glucosa: {self.glucosa:.2f} | Insulina: {self.insulina:.2f} | Presión Arterial Sistólica: {self.pas:.2f}')