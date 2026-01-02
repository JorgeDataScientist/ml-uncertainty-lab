# ml-uncertainty-lab

Laboratorio práctico para aprender **calibración y estimación de incertidumbre** en modelos de Machine Learning.  
Enfoque **100% hands-on**: la teoría se introduce solo cuando el código la exige.

El objetivo es desarrollar criterio técnico y capacidades prácticas para evaluar, corregir y **operacionalizar la confianza** de modelos, con foco en escenarios reales y aplicación futura en **PRISMA**.

---

## 🎯 Objetivo del repositorio

Construir, paso a paso, un **prototipo de autovalidación estadística** que:
- reciba outputs de modelos,
- evalúe su confiabilidad,
- estime incertidumbre,
- y decida cuándo automatizar o escalar a revisión humana.

---

## 🧠 Metodología

- *Learning by doing*: primero código, luego teoría.
- Experimentos controlados y reproducibles.
- Métricas, gráficos y decisiones operativas en cada notebook.
- Nada de optimizar accuracy sin entender riesgo.

> Si no produce una métrica, un gráfico o una decisión, no sirve.

---

## 🗂️ Estructura del repositorio

```text
ml-uncertainty-lab/
│
├── 00_setup/                  # entorno, helpers, métricas comunes
├── 01_fundamentos/            # scores vs probabilidades
├── 02_evaluacion_confianza/   # Brier, ECE, calibration curves
├── 03_calibracion/            # Platt, Isotonic, Temperature Scaling
├── 04_variabilidad/           # Ensembles, MC-style uncertainty
├── 05_entropia/               # Entropía como señal de duda
├── 06_structured_outputs/     # Confianza por campo (PRISMA-like)
├── 07_certs_like/             # Top-2 delta y CeRTS simplificado
├── 08_alternatives/           # Alternativas actuales y fiables a CeRTS
│   ├── 08_01_conformal/        # Conformal Prediction (cobertura/intervalos)
│   ├── 08_02_ensembles/        # Deep ensembles como señal robusta
│   ├── 08_03_logit_gap/        # Top-k margin / logit gap (baseline fuerte)
│   └── 08_04_comparison/       # Matriz comparativa orientada a PRISMA
│
└── reports/                   # conclusiones cortas por bloque


