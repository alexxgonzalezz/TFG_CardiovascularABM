<div align="center">

## Diseño y Desarrollo de un Modelo Basado en Agentes para Evaluar la Eficacia de las Intervenciones Dietéticas en la Salud Cardiovascular

*Trabajo de Fin de Grado — Grado en Ingeniería y Sistemas de Datos (Calificación: 10/10)*  
**Universidad Politécnica de Madrid (ETSIT - UPM)**

<p>
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Mesa-ABM_Framework-00A98F?style=for-the-badge" alt="Mesa" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge" alt="Seaborn" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter" />
</p>

</div>

---

## 🎯 ¿Qué busca este proyecto?

Las enfermedades cardiovasculares son una de las principales causas de mortalidad en el mundo y la alimentación juega un papel clave en su prevención. Sin embargo, evaluar el impacto real de distintas dietas mediante ensayos clínicos tradicionales con pacientes es un proceso extremadamente costoso, lento y complejo.

El objetivo de este Trabajo de Fin de Grado es ofrecer una alternativa computacional: diseñar y validar un **simulador basado en agentes** capaz de predecir cómo evolucionan los niveles de **colesterol total y colesterol LDL** de una población a lo largo de **12 semanas** al someterse a cuatro tipos de dieta: **Mediterránea, Baja en grasas, Vegetariana y Cetogénica (Keto)**.

---

## ⚙️ ¿Cómo se ha abordado?

Para construir un entorno virtual que refleje fielmente la realidad clínica, el proyecto se ha desarrollado en `Python` combinando tres pilares:

* **Modelado Basado en Agentes (Framework `Mesa`):** En lugar de tratar a la población como un promedio estadístico, se crean pacientes virtuales individuales y heterogéneos, cada uno con su propio perfil clínico, niveles iniciales de colesterol y hábitos alimenticios.
* **Motor Biológico y Comportamiento Humano:** El metabolismo de cada paciente actualiza su colesterol semana a semana mediante ecuaciones médicas validadas científicamente (evaluando el impacto de las grasas, colesterol dietético, fibra soluble, fitoesteroles y pérdida de peso). Además, el modelo simula el comportamiento humano real introduciendo variaciones diarias en la comida y la probabilidad de abandonar la dieta.
* **Simulaciones de Montecarlo y Ciencia de Datos:** Para eliminar el factor azar y obtener datos estadísticamente sólidos, el simulador ejecuta **1.000 iteraciones independientes**. Todos los datos generados se procesan, unifican y visualizan utilizando `Numpy`, `Pandas`, `Matplotlib` y `Seaborn`.

---

## 📊 Resultados y Conclusiones

Tras contrastar el simulador y analizar la evolución de los pacientes virtuales, se alcanzaron las siguientes conclusiones principales:

* **Validación clínica de alta precisión:** Al comparar los resultados del simulador con los datos reales del ensayo clínico de referencia **Medi-RIVAGE**, el modelo demostró una gran fiabilidad, registrando un margen de error **inferior al 2%**.
* **La Dieta Vegetariana como opción más eficaz:** Demostró ser la mejor intervención para reducir el riesgo cardiovascular, logrando las mayores bajadas en colesterol total y colesterol LDL gracias a su alto aporte de fibra soluble y fitoesteroles y a la ausencia de colesterol dietético.
* **Eficacia intermedia (Mediterránea y Baja en grasas):** Ambas dietas lograron reducciones notables y sostenidas en el perfil lipídico al mantener bajo control el consumo de grasas saturadas.
* **El riesgo de la Dieta Cetogénica (Keto):** Se posicionó como el escenario más perjudicial para la salud cardiovascular, provocando un aumento notable de los niveles de colesterol total y LDL debido a la elevada ingesta de grasas saturadas.
* **Potencial en medicina preventiva:** Este trabajo demuestra que los modelos basados en agentes son herramientas precisas, rápidas y económicas para experimentar con estrategias nutricionales sin poner en riesgo la salud de pacientes reales.
