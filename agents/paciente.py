import mesa

class Paciente(mesa.Agent):
    '''Agente que representa a un paciente con factores de riesgo cardiovascular.'''

    def __init__(self, unique_id, model, edad, colesterol, presion_arterial):
        super().__init__(model)

        # Atributos de salud iniciales del paciente
        self.unique_id = unique_id
        self.age = edad
        self.colesterol = colesterol
        self.presion_arterial = presion_arterial

        # Tipo de dieta

    def step(self):
        '''
        Función que se ejecuta en cada paso de la simulación.
        Programar cómo la dieta afecta a los factores de riesgo del paciente.
        '''

        # Prueba imprimir los factores de riesgo del paciente en cada paso
        print(f'Paciente {self.unique_id} -> Edad: {self.age} | Colesterol: {self.colesterol} | Presión Arterial: {self.presion_arterial}')