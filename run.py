from model.cardioModel import CardioModel
from configuration import settings

if __name__ == "__main__":
    print("Iniciando simulación de pacientes con factores de riesgo cardiovascular...")
    model = CardioModel(num_pacientes=settings.NUM_PACIENTES)
    for _ in range(5):  # Ejecutar la simulación durante 5 pasos
        model.step()