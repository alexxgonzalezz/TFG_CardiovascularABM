from model.cardioModel import CardioModel
from configuration import settings

if __name__ == "__main__":
    print("Iniciando simulación semanal de ingesta nutricional y evolución de biomarcadores...")
    model = CardioModel(num_pacientes = settings.NUM_PACIENTES)

    # Ejecutar la simulación durante 12 semanas (3 meses)
    for _ in range(12):
        model.step()