"""
ml-uncertainty-lab — Setup del entorno y utilidades comunes
==========================================================

OBJETIVO
--------
Este módulo prepara el entorno base para todo el laboratorio.
Su propósito es garantizar:

- Reproducibilidad (semillas globales).
- Consistencia visual (configuración estándar de plots).
- Reutilización de métricas (funciones comunes para calibración).

Aquí NO se entrenan modelos ni se analizan resultados.
Solo se definen configuraciones y funciones que serán usadas de forma
transversal a lo largo del repositorio.

REGLA
-----
Este módulo se importa; no se modifica sin justificación.
Cualquier cambio aquí impacta todo el laboratorio.
"""

from __future__ import annotations

# Librerías base
import random
from typing import Iterable, Union

import numpy as np
import matplotlib.pyplot as plt

# Nota: pandas no es necesario para estas utilidades.
# Si lo necesitas en el futuro para helpers adicionales, puedes importarlo
# en los notebooks o agregarlo explícitamente aquí.
# import pandas as pd


# ---------------------------------------------------------------------
# 1) Semillas globales (reproducibilidad)
# ---------------------------------------------------------------------
"""
¿QUÉ HACEMOS?
Fijamos semillas globales para que los experimentos sean reproducibles:
si ejecutas el mismo notebook hoy o en semanas, deberías obtener resultados
consistentes (dentro de lo razonable).

¿POR QUÉ IMPORTA?
Sin semillas fijas, pequeñas variaciones aleatorias pueden cambiar métricas
y gráficos. Eso genera ruido, dificulta comparar modelos y debilita conclusiones.
"""

SEED: int = 42

random.seed(SEED)
np.random.seed(SEED)


def set_global_seed(seed: int = 42) -> None:
    """
    Fija la semilla global del laboratorio.

    Nota:
    - Esta función es útil si deseas cambiar la semilla desde un notebook,
      manteniendo una única fuente de verdad.
    """
    global SEED
    SEED = int(seed)
    random.seed(SEED)
    np.random.seed(SEED)


# ---------------------------------------------------------------------
# 2) Configuración de visualización
# ---------------------------------------------------------------------
"""
¿QUÉ HACEMOS?
Definimos una configuración básica y consistente para los gráficos.

¿POR QUÉ IMPORTA?
La visualización es una herramienta de análisis, no decoración.
Usar siempre el mismo tamaño y estilo evita interpretaciones erróneas y
facilita comparar resultados entre notebooks.
"""

plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["axes.grid"] = True
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["axes.labelsize"] = 10
plt.rcParams["legend.fontsize"] = 9


# ---------------------------------------------------------------------
# 3) Funciones reutilizables
# ---------------------------------------------------------------------
"""
¿QUÉ HACEMOS?
Implementamos funciones básicas que se reutilizarán en todo el laboratorio
para evaluar calidad de probabilidades.

Estas funciones NO entrenan modelos ni toman decisiones.
Solo miden y visualizan.

¿POR QUÉ IMPORTA?
- Evita reescribir código en cada notebook.
- Garantiza comparaciones consistentes (mismas definiciones).
- Reduce errores conceptuales al evaluar confianza.
"""

ArrayLike = Union[np.ndarray, Iterable[float]]


def brier_score(y_true: ArrayLike, y_prob: ArrayLike) -> float:
    """
    Calcula el Brier Score para clasificación binaria.

    Parámetros
    ----------
    y_true : array-like
        Valores reales (0 o 1).
    y_prob : array-like
        Probabilidades predichas para la clase positiva.

    Retorna
    -------
    float
        Brier score (menor es mejor).
    """
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.asarray(y_prob, dtype=float)
    return float(np.mean((y_prob - y_true) ** 2))


def expected_calibration_error(
    y_true: ArrayLike, y_prob: ArrayLike, n_bins: int = 10
) -> float:
    """
    Calcula el Expected Calibration Error (ECE).

    Divide las probabilidades en bins y mide la diferencia promedio
    entre confianza (probabilidad promedio) y precisión empírica por bin.

    Parámetros
    ----------
    y_true : array-like
        Valores reales (0 o 1).
    y_prob : array-like
        Probabilidades predichas para la clase positiva.
    n_bins : int
        Número de bins para discretizar el rango [0, 1].

    Retorna
    -------
    float
        ECE (menor es mejor).
    """
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.asarray(y_prob, dtype=float)

    bins = np.linspace(0.0, 1.0, n_bins + 1)
    # digitize devuelve [1..n_bins], restamos 1 para [0..n_bins-1]
    bin_ids = np.digitize(y_prob, bins) - 1

    ece = 0.0
    for i in range(n_bins):
        mask = bin_ids == i
        if np.any(mask):
            bin_confidence = float(np.mean(y_prob[mask]))
            bin_accuracy = float(np.mean(y_true[mask]))
            bin_weight = float(np.mean(mask))  # proporción de muestras en el bin
            ece += abs(bin_confidence - bin_accuracy) * bin_weight

    return float(ece)


def plot_reliability_diagram(
    y_true: ArrayLike,
    y_prob: ArrayLike,
    n_bins: int = 10,
    title: str = "Reliability Diagram",
) -> None:
    """
    Grafica un reliability diagram (calibration curve) para clasificación binaria.

    Parámetros
    ----------
    y_true : array-like
        Valores reales (0 o 1).
    y_prob : array-like
        Probabilidades predichas para la clase positiva.
    n_bins : int
        Número de bins para discretizar el rango [0, 1].
    title : str
        Título del gráfico.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_prob = np.asarray(y_prob, dtype=float)

    bins = np.linspace(0.0, 1.0, n_bins + 1)
    bin_ids = np.digitize(y_prob, bins) - 1

    accuracies = []
    confidences = []

    for i in range(n_bins):
        mask = bin_ids == i
        if np.any(mask):
            accuracies.append(float(np.mean(y_true[mask])))
            confidences.append(float(np.mean(y_prob[mask])))
        else:
            # Mantener longitud fija para visualizar todos los bins
            accuracies.append(0.0)
            confidences.append(0.0)

    plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Perfect calibration")
    plt.plot(confidences, accuracies, marker="o", label="Model")
    plt.xlabel("Predicted probability")
    plt.ylabel("Empirical accuracy")
    plt.title(title)
    plt.legend()
    plt.show()


# ---------------------------------------------------------------------
# 4) Cierre
# ---------------------------------------------------------------------
"""
¿QUÉ QUEDA LISTO?
- Reproducibilidad mediante semillas globales.
- Estándar visual consistente para gráficos.
- Funciones reutilizables para evaluar calibración y confiabilidad.

A partir de aquí, los notebooks siguientes pueden centrarse en experimentos,
análisis y toma de decisiones sin preocuparse por infraestructura.

REGLA PARA EL LABORATORIO
Este módulo se importa, no se modifica. Cambios aquí deben estar justificados.
"""
