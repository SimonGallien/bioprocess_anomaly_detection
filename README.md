# Bioprocess Anomaly Detection

## À propos du projet

Ce projet analyse un ensemble de données généré par **IndPenSim**, une simulation mathématique avancée d'un système de fermentation de pénicilline de 100 000 litres. IndPenSim est la première simulation à inclure un dispositif de spectroscopie Raman simulé de manière réaliste pour le développement, l'évaluation et la mise en œuvre de solutions de contrôle avancées et innovantes applicables aux installations de biotechnologie.

## Dataset

Le dataset contient **100 batches** avec toutes les mesures disponibles de processus et de spectroscopie Raman (~2,5 GB), représentant le plus grand ensemble de données disponible pour l'analyse de données avancée dans l'industrie biopharmaceutique.

### Structure des batches

- **Batches 1-30** : Contrôlés par une approche pilotée par recette
- **Batches 31-60** : Contrôlés par des opérateurs
- **Batches 61-90** : Contrôlés par une solution de contrôle de processus avancé (APC) utilisant la spectroscopie Raman
- **Batches 91-100** : Contiennent des défauts entraînant des déviations de processus

Ce dataset est particulièrement adapté au développement d'algorithmes de big data analytics, machine learning (ML) ou intelligence artificielle (IA) applicables à l'industrie biopharmaceutique.

## Source des données

- **Kaggle** : [Big Data Biopharmaceutical Manufacturing](https://www.kaggle.com/datasets/stephengoldie/big-databiopharmaceutical-manufacturing)
- **Site web** : [http://www.industrialpenicillinsimulation.com/](http://www.industrialpenicillinsimulation.com/)
- **Notebook de référence** : [https://github.com/StephenGoldie/indpensim-notebook.git](https://github.com/StephenGoldie/indpensim-notebook.git)

## Installation

```bash
uv sync
```

## Utilisation

Pour télécharger les données depuis Kaggle :

```python
from src.get_data import download_data

# Télécharge et copie les données dans data/
download_data()
```

## Références

Merci de citer les travaux suivants lors de l'utilisation de ces données :

- Goldrick S., Stefan, A., Lovett D., Montague G., Lennox B. (2015) *The development of an industrial-scale fed-batch fermentation simulation* Journal of Biotechnology, 193:70-82.

- Goldrick S., Duran-Villalobos C., K. Jankauskas, Lovett D., Farid S. S, Lennox B., (2019) *Modern day control challenges for industrial-scale fermentation processes*. Computers and Chemical Engineering.

## Contact

- **Twitter** : [@Stephen_Goldric](https://twitter.com/Stephen_Goldric)
- **GitHub** : [StephenGoldie](https://github.com/StephenGoldie)
- **LinkedIn** : Stephen Goldrick - Post Doc @UCL Biochemical Society