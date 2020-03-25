## OpenHPI Deeplearning 2020

[![Build Status](https://travis-ci.com/into-ai/deeplearning2020.svg?branch=master)](https://travis-ci.com/into-ai/deeplearning2020)
[![PyPI version](https://img.shields.io/pypi/v/deeplearning2020.svg)](https://pypi.python.org/pypi/deeplearning2020)

------------------------------

Materialien zum Kurs [Eine praktische Einführung in Deep Learning für Computer Vision](https://open.hpi.de/courses/neuralnets2020) auf [OpenHPI](https://open.hpi.de/).

### Inhaltsverzeichnis

- [Wie nutze ich das GitHub Repository?](#wie-nutze-ich-dieses-github-repository)
- Woche 1
  - [Bonusaufgabe: Backpropagation selber nachvollziehen](woche1/bonus.md)
  - [Exkurs: Lokale Installation ](woche1/installation/)
    - [Linux](woche1/installation/linux.md)
    - [macOS](woche1/installation/mac.md)
    - [Windows](woche1/installation/windows.md)
- Woche 2
  - [Notebooks](woche2/notebooks/)
    - [Einführung in Numpy](woche2/notebooks/intro-numpy/)
    - [Einführung in Matplotlib](woche2/notebooks/intro-matplotlib/)
    - [Laden und Bearbeiten des MNIST Datensatz](woche2/notebooks/exploring-mnist)
    - [MNIST Vergleich Aktivierungsfunktionen](woche2/notebooks/mnist-activation-functions/)
    - [Einführung in Tensorflow / Keras](woche2/notebooks/intro-tensorflow-keras/)
    - [Beispiel: Trainieren eines Netzes für MNIST](woche2/notebooks/first-mnist-net/)
  - [Praktische Übung](woche2/assignment/)
- Woche 3
  - [Notebooks](woche3/notebooks/)
    - [Komplexe Layerstruktur](woche3/notebooks/komplex-layer-structure/)
    - [Loss Functions](woche3/notebooks/loss-functions/)
    - [Optimizer](woche3/notebooks/optimizer/)
    - [Hyperparameter](woche3/notebooks/hyperparameter/)
  - [Exkurs: Neuronale Netze von Scratch](woche3/scratch-net)
  - [Praktische Übung](woche3/assignment/)
    - [Bewertete Übung](woche3/assignment/week3&4/)
    - [Zusätzliche Übung](woche3/assignment/additional/)
- Woche 4
  - t.b.a

### Wie nutze ich dieses GitHub Repository?

Dieses Repository dient als Ort für Materialien zu diesem Kurs. Du benötigst kein GitHub Account und musst das Repository auch nicht verwenden, da sich die wichtigen Materialien auch auf [OpenHPI](https://open.hpi.de/) finden lassen.

Du kannst das Repository auf zwei verschiedene Arten verwenden:
1. Du kannst dir die Materialien, die du oben im Inhaltsverzeichnis findest online anschauen, daraus kopieren oder Dateien herunterladen. Du kannst auch das gesamte Repository als ZIP herunterladen. Falls du `.ipynb`-Notebooks herunterlädst kannst du diese dann mit deinem `jupyter notebook` Server öffnen, indem du im Browserfenster des Server zu dieser Datei navigierst und sie öffnest.

2. Du kannst das Repository mit
    ```bash
    git clone https://github.com/into-ai/deeplearning2020.git
    ```
    *klonen*. Damit hast du das Repository ebenfalls lokal, aber kannst es außerdem mit
    ```bash
    git pull origin master
    ```
    aktualisieren, sobald neue Inhalte verfügbar werden. Das Öffnen von Notebooks funktioniert genauso wie in Variante 1. Wir empfehlen diesen Workflow aber nur denjenigen, die sich bereits ein bisschen mit `git` auskennen oder sich [hier](https://git-scm.com/doc) einlesen wollen.
