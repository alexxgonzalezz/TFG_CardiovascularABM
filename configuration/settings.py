# ==============================================================
# PARÁMETROS POBLACIONALES
# ==============================================================
NUM_PACIENTES = 212
PROPORCION_MED = 102 / NUM_PACIENTES
PROPORCION_LOW_FAT = 110 / NUM_PACIENTES

# Edad (años)
EDAD_MEDIA = 51.0
EDAD_STD = 10.5

# Probabilidades género y tabaquismo
PROPORCION_MUJERES_MED = 0.58
PROPORCION_MUJERES_LOW_FAT = 0.605

# PROPORCION_FUMADORES_MED = 0.273
# PROPORCION_FUMADORES_LOW_FAT = 0.173

# Tasas de abandono
TASA_ABANDONO_MED = 0.159
TASA_ABANDONO_LOW_FAT = 0.358

# Factor de conversión de Kj a Kcal
KJ_TO_KCAL = 4.184


# ==============================================================
# PORCENTAJES DE MACRONUTRIENTES ESENCIALES INICIALES / BASELINE
# ==============================================================
# Base Dieta Mediterránea
PROT_PCT_MEDIA_MED_INICIAL = 0.184      
PROT_PCT_STD_MED_INICIAL = 0.035        
CARB_PCT_MEDIA_MED_INICIAL = 0.426      
CARB_PCT_STD_MED_INICIAL = 0.061        
GRASA_PCT_MEDIA_MED_INICIAL = 0.390     
GRASA_PCT_STD_MED_INICIAL = 0.061       

# Base Dieta Baja en Grasas
PROT_PCT_MEDIA_LOW_FAT_INICIAL = 0.194  
PROT_PCT_STD_LOW_FAT_INICIAL = 0.040    
CARB_PCT_MEDIA_LOW_FAT_INICIAL = 0.416  
CARB_PCT_STD_LOW_FAT_INICIAL = 0.071    
GRASA_PCT_MEDIA_LOW_FAT_INICIAL = 0.390 
GRASA_PCT_STD_LOW_FAT_INICIAL = 0.069 


# ==============================================================
# DESGLOSE DE TIPOS DE GRASAS INICIALES / BASELINE (% of energy)
# ==============================================================
# Dieta Mediterránea
GRASA_SAT_PCT_MEDIA_MED_INICIAL = 0.144
GRASA_SAT_PCT_STD_MED_INICIAL = 0.037
GRASA_MONO_PCT_MEDIA_MED_INICIAL = 0.143
GRASA_MONO_PCT_STD_MED_INICIAL = 0.033
GRASA_POLI_PCT_MEDIA_MED_INICIAL = 0.054
GRASA_POLI_PCT_STD_MED_INICIAL = 0.022

# Dieta Baja en Grasas
GRASA_SAT_PCT_MEDIA_LOW_FAT_INICIAL = 0.143
GRASA_SAT_PCT_STD_LOW_FAT_INICIAL = 0.037
GRASA_MONO_PCT_MEDIA_LOW_FAT_INICIAL = 0.144
GRASA_MONO_PCT_STD_LOW_FAT_INICIAL = 0.032
GRASA_POLI_PCT_MEDIA_LOW_FAT_INICIAL = 0.054
GRASA_POLI_PCT_STD_LOW_FAT_INICIAL = 0.019

# ==============================================================
# DESGLOSE DE TIPOS DE GRASAS A LOS 3 MESES (% of energy)
# ==============================================================
# Dieta Mediterránea
GRASA_SAT_PCT_MEDIA_MED = 0.100
GRASA_SAT_PCT_STD_MED = 0.026
GRASA_MONO_PCT_MEDIA_MED = 0.156
GRASA_MONO_PCT_STD_MED = 0.039
GRASA_POLI_PCT_MEDIA_MED = 0.058
GRASA_POLI_PCT_STD_MED = 0.022

# Dieta Baja en Grasas
GRASA_SAT_PCT_MEDIA_LOW_FAT = 0.103
GRASA_SAT_PCT_STD_LOW_FAT = 0.031
GRASA_MONO_PCT_MEDIA_LOW_FAT = 0.134
GRASA_MONO_PCT_STD_LOW_FAT = 0.032
GRASA_POLI_PCT_MEDIA_LOW_FAT = 0.063
GRASA_POLI_PCT_STD_LOW_FAT = 0.027


# ==============================================================
# DIETA MEDITERRÁNEA
# ==============================================================

# 1. Ingesta nutricional DIARIA (medias y desviaciones estándar)

# Energía total diaria (Kcal)
ENERGIA_MEDIA_MED_INICIAL = 8471.2 / KJ_TO_KCAL
ENERGIA_STD_MED_INICIAL = 2406.8 / KJ_TO_KCAL

ENERGIA_MEDIA_MED = 6280.4 / KJ_TO_KCAL
ENERGIA_STD_MED = 1714.6 / KJ_TO_KCAL

DEFICIT_MEDIA_MED = 2190 / KJ_TO_KCAL

# Alcohol (kcal)
ALCOHOL_MEDIA_MED_INICIAL = 264.5 / KJ_TO_KCAL
ALCOHOL_STD_MED_INICIAL = 377.6 / KJ_TO_KCAL

ALCOHOL_MEDIA_MED = 187.5 / KJ_TO_KCAL
ALCOHOL_STD_MED = 359.8 / KJ_TO_KCAL

# Proteínas (g)
PROT_MEDIA_MED_INICIAL = 88.3
PROT_STD_MED_INICIAL = 23.1

PROT_MEDIA_MED = 70.5
PROT_STD_MED = 19.8

PROT_PCT_MEDIA_MED = 19.6
PROT_PCT_STD_MED = 3.2

# Carbohidratos (g)
CARB_MEDIA_MED_INICIAL = 208.9
CARB_STD_MED_INICIAL = 63.6

CARB_MEDIA_MED = 166.5
CARB_STD_MED = 45.3

CARB_PCT_MEDIA_MED = 45.8
CARB_PCT_STD_MED = 5.1

# Grasa total (g)
GRASA_MEDIA_MED_INICIAL = 86.3
GRASA_STD_MED_INICIAL = 32.0

GRASA_MEDIA_MED = 56.2
GRASA_STD_MED = 17.3

GRASA_PCT_MEDIA_MED = 34.6
GRASA_PCT_STD_MED = 6.9

# Grasa saturada (g)
GRASA_SAT_MEDIA_MED_INICIAL = 32.4
GRASA_SAT_STD_MED_INICIAL = 15.6

GRASA_SAT_MEDIA_MED = 16.3
GRASA_SAT_STD_MED = 6.3

# Grasa monoinsaturada (g)
GRASA_MONO_MEDIA_MED_INICIAL = 31.3
GRASA_MONO_STD_MED_INICIAL = 11.7

GRASA_MONO_MEDIA_MED = 25.3
GRASA_MONO_STD_MED = 8.8

# Grasa poliinsaturada (g)
GRASA_POLI_MEDIA_MED_INICIAL = 11.5
GRASA_POLI_STD_MED_INICIAL = 5.3

GRASA_POLI_MEDIA_MED = 9.4
GRASA_POLI_STD_MED = 4.2


# 2. Biomarcadores inciales: Medias y desviaciones estándar
# Colesterol total (mmol/L)
COL_TOTAL_MEDIA_MED = 6.6
COL_TOTAL_STD_MED = 1.0

# Colesterol LDL "malo" (mmol/L)
COL_LDL_MEDIA_MED = 4.4
COL_LDL_STD_MED = 1.0


# ==============================================================
# DIETA BAJA EN GRASAS
# ==============================================================

# 1. Ingesta nutricional DIARIA (medias y desviaciones estándar)
# Energía total diaria (Kcal)
ENERGIA_MEDIA_LOW_FAT_INICIAL = 8489.5 / KJ_TO_KCAL
ENERGIA_STD_LOW_FAT_INICIAL = 2875.4 / KJ_TO_KCAL

ENERGIA_MEDIA_LOW_FAT = 6408.2 / KJ_TO_KCAL
ENERGIA_STD_LOW_FAT = 2060.5 / KJ_TO_KCAL

DEFICIT_MEDIA_LOW_FAT = 2081 / KJ_TO_KCAL

# Alcohol (kcal)
ALCOHOL_MEDIA_LOW_FAT_INICIAL = 330.3 / KJ_TO_KCAL
ALCOHOL_STD_LOW_FAT_INICIAL = 412.9 / KJ_TO_KCAL

ALCOHOL_MEDIA_LOW_FAT = 141.9 / KJ_TO_KCAL
ALCOHOL_STD_LOW_FAT = 192.6 / KJ_TO_KCAL

# Proteínas (g)
PROT_MEDIA_LOW_FAT_INICIAL = 92.5
PROT_STD_LOW_FAT_INICIAL = 27.3

PROT_MEDIA_LOW_FAT = 77.8
PROT_STD_LOW_FAT = 19.3

PROT_PCT_MEDIA_LOW_FAT = 21.3
PROT_PCT_STD_LOW_FAT = 3.6

# Carbohidratos (g)
CARB_MEDIA_LOW_FAT_INICIAL = 203.5
CARB_STD_LOW_FAT_INICIAL = 74.6

CARB_MEDIA_LOW_FAT = 168.3
CARB_STD_LOW_FAT = 58.7

CARB_PCT_MEDIA_LOW_FAT = 44.8
CARB_PCT_STD_LOW_FAT = 6.7

# Grasa total (g)
GRASA_MEDIA_LOW_FAT_INICIAL = 86.5
GRASA_STD_LOW_FAT_INICIAL = 38.7

GRASA_MEDIA_LOW_FAT = 56.7
GRASA_STD_LOW_FAT = 20.5

GRASA_PCT_MEDIA_LOW_FAT = 33.9
GRASA_PCT_STD_LOW_FAT = 6.4

# Grasa saturada (g) --> Aumentan los niveles de colesterol LDL "malo"
GRASA_SAT_MEDIA_LOW_FAT_INICIAL = 31.6
GRASA_SAT_STD_LOW_FAT_INICIAL = 15.7

GRASA_SAT_MEDIA_LOW_FAT = 17.2
GRASA_SAT_STD_LOW_FAT = 7.7

# Grasa monoinsaturada (g) --> Aumentan los niveles de colesterol HDL "bueno"
GRASA_MONO_MEDIA_LOW_FAT_INICIAL = 31.8
GRASA_MONO_STD_LOW_FAT_INICIAL = 14.3

GRASA_MONO_MEDIA_LOW_FAT = 22.4
GRASA_MONO_STD_LOW_FAT = 8.8

# Grasa poliinsaturada (g) --> Aumentan los niveles de colesterol HDL "bueno" y reducen los niveles de colesterol LDL "malo"
GRASA_POLI_MEDIA_LOW_FAT_INICIAL = 12.0
GRASA_POLI_STD_LOW_FAT_INICIAL = 6.7

GRASA_POLI_MEDIA_LOW_FAT = 10.5
GRASA_POLI_STD_LOW_FAT = 5.6


# 2. Biomarcadores inciales: Medias y desviaciones estándar
# Colesterol total (mmol/L)
COL_TOTAL_MEDIA_LOW_FAT = 6.4
COL_TOTAL_STD_LOW_FAT = 0.9

# Colesterol LDL "malo" (mmol/L)
COL_LDL_MEDIA_LOW_FAT = 4.1
COL_LDL_STD_LOW_FAT = 0.9














# ========================================================================================================================
# ========================================================================================================================
# ========================================================================================================================

# ANTIGUO

# ========================================================================================================================
# ========================================================================================================================
# ========================================================================================================================


# ==============================================================
# BIOMARCADORES INCIALES: Medias y desviaciones estándar
# ==============================================================
# IMC (kg/m^2)
# IMC_MEDIA = 28.7
# IMC_STD_MED = 4.6
# IMC_STD_LOW_FAT = 5.4

# # Triglicéridos (mmol/L)
# TRIGLICERIDOS_MEDIA_MED = 1.6
# TRIGLICERIDOS_STD_MED = 1.0

# TRIGLICERIDOS_MEDIA_LOW_FAT = 1.5
# TRIGLICERIDOS_STD_LOW_FAT = 1.0

# # Glucosa en sangre (mmol/L)
# GLUCOSA_MEDIA_MED = 5.3
# GLUCOSA_STD_MED = 0.6

# GLUCOSA_MEDIA_LOW_FAT = 5.2
# GLUCOSA_STD_LOW_FAT = 0.7

# # Insulina (mmol/L)
# INSULINA_MEDIA_MED = 10.6
# INSULINA_STD_MED = 5.8

# INSULINA_MEDIA_LOW_FAT = 10.6
# INSULINA_STD_LOW_FAT = 7.8

# # Presión Arterial Sistólica (mmHg)
# PAS_MEDIA_MED = 128.0
# PAS_STD_MED = 17.0

# PAS_MEDIA_LOW_FAT = 126.0
# PAS_STD_LOW_FAT = 17.0

# ==============================================================
# HÁBITOS NUTRICIONALES INCIALES: Medias y desviaciones estándar
# ==============================================================

# # Ácido fólico (ug)
# FOLICO_MEDIA_MED = 302.9
# FOLICO_STD_MED = 110.6
# FOLICO_MEDIA_LOW_FAT = 316.3
# FOLICO_STD_LOW_FAT = 144.8

# # Calcio (mg)
# CALCIO_MEDIA_MED = 967.2
# CALCIO_STD_MED = 333.3
# CALCIO_MEDIA_LOW_FAT = 981.4
# CALCIO_STD_LOW_FAT = 381.1

# # Hierro (mg)
# HIERRO_MEDIA_MED = 12.2
# HIERRO_STD_MED = 3.9
# HIERRO_MEDIA_LOW_FAT = 12.7
# HIERRO_STD_LOW_FAT = 4.2