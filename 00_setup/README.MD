# Día 1 — Fundamentos  
## Probabilidades que mienten

### Propósito del día
Este día sienta las bases conceptuales de todo el laboratorio.  
El objetivo no es solo ejecutar código, sino **construir el vocabulario técnico mínimo** para razonar correctamente sobre probabilidad, confianza e incertidumbre en sistemas de Machine Learning.

Cada concepto se introduce **cuando el experimento lo exige**, no de forma teórica aislada.

---

## Estructura del día

- `00_setup/00_environment_and_utils.ipynb`
- `01_fundamentos/01_scores_vs_probabilities.ipynb`

Ambos notebooks son complementarios y obligatorios.

---

## 1️⃣ Notebook de setup  
📓 `00_setup/00_environment_and_utils.ipynb`

### Qué se estudia aquí (conceptos)
- **Semillas globales**
  - Qué son.
  - Por qué importan para reproducibilidad.
- **Reproducibilidad experimental**
  - Por qué un experimento no reproducible no genera conocimiento confiable.

### Qué se implementa
- Fijar semillas globales (`numpy`, `random`).
- Configuración estándar de visualización.
- Implementación de funciones reutilizables:
  - **Brier Score** (error cuadrático de la probabilidad).
  - **Expected Calibration Error (ECE)**.
  - **Reliability Diagram** con bins fijos.

> Regla: aquí no se interpretan resultados, solo se preparan herramientas.

---

## 2️⃣ Notebook principal del día  
📓 `01_fundamentos/01_scores_vs_probabilities.ipynb`

Este notebook combina **código y definición progresiva de conceptos**.

---

### A. Definición del objetivo
**Conceptos introducidos**
- Predicción.
- Probabilidad.
- Estimación.

**Qué se estudia**
- Qué significa “predecir” en ML.
- Por qué una probabilidad es una **estimación**, no un hecho.
- Por qué una estimación puede ser incorrecta incluso cuando el modelo acierta.

---

### B. Generación de datos sintéticos
**Conceptos introducidos**
- Datos sintéticos.
- Control experimental.
- Ruido y solapamiento.

**Qué se estudia**
- Por qué se usan datos sintéticos en fases tempranas.
- Cómo el control del problema permite entender el comportamiento del modelo.

---

### C. Entrenamiento de modelos
**Conceptos introducidos**
- Modelo.
- Score.
- Función de decisión.

**Qué se estudia**
- Diferencia entre:
  - score crudo,
  - probabilidad transformada.
- Por qué los modelos no “razonan” en términos probabilísticos.

---

### D. Scores vs probabilidades
**Conceptos introducidos**
- Score.
- Logit.
- Función sigmoide / softmax.

**Qué se estudia**
- Cómo se transforma un score en probabilidad.
- Por qué esta transformación **impone certeza**.
- Origen del overconfidence.

---

### E. Casos de alta confianza errónea
**Conceptos introducidos**
- Overconfidence.
- Error con alta confianza.

**Qué se estudia**
- Identificación de predicciones con:
  - probabilidad alta,
  - resultado incorrecto.
- Por qué estos casos son los más peligrosos en sistemas automatizados.

---

### F. Visualización
**Conceptos introducidos**
- Distribución de probabilidades.
- Separación visual de aciertos vs errores.

**Qué se estudia**
- Cómo los gráficos revelan patrones que las métricas pueden ocultar.

---

### G. Métricas iniciales
**Conceptos introducidos**
- Accuracy.
- Brier Score.
- Expected Calibration Error (ECE).

**Qué se estudia**
- Qué mide cada métrica.
- Qué problemas no detecta la accuracy.
- Por qué el Brier empieza a capturar riesgo.

---

## 3️⃣ Análisis crítico
**Conceptos reforzados**
- Confiabilidad.
- Riesgo operacional.
- Decisiones automáticas vs intervención humana.

**Preguntas guía**
- ¿Por qué este modelo puede ser peligroso?
- ¿Qué error cometería una política de automatización ingenua?
- ¿Qué señales faltan para tomar decisiones responsables?

---

## 4️⃣ Cierre del día

### Lo que se consolida
- Una probabilidad puede ser incorrecta incluso con alta precisión.
- La precisión no es sinónimo de confiabilidad.
- La confianza debe medirse, no asumirse.

### Lo que queda pendiente
- Cómo **medir formalmente** la calibración.
- Cómo **corregir** probabilidades mal calibradas.

Eso será el foco del Día 2.

---

### Nota del tutor
Este día construye el **lenguaje mental** del resto del laboratorio.  
Avanzar sin dominar estos conceptos genera deuda técnica.
