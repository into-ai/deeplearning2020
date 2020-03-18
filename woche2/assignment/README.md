#### Assignment Woche 2

![Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist/raw/master/doc/img/embedding.gif)

**Errinnerung**: Durch die Bearbeitung der Assignments koennen ingesamt bis zu **40%** Prozent der Kurspunkte erhalten werden. Diese Summe setzt sich aus der Uebung in dieser Woche (15%) und der Uebung in der naechsten Woche (25%) zusammen.

#### Was sollt ihr in dieser Uebung lernen?

Ihr habt in dieser Woche die wichtigsten Tools fuer das Trainieren von neuronalen Netzen kennegelernt und sollt nun einmal selbst ein Netz trainieren! Dabei ist es egal ob ihr [Google Colab](https://colab.research.google.com/) oder eine lokale Installation verwendet.

Ziel ist es, ein Netz fuer den im folgenden vorgestellten Datensatz zu trainieren, das dessen Bilder so zuverlaessig wie moeglich korrekt klassifiziert.

#### Welchen Datensatz sollt ihr benutzen?

![Fashion MNIST](https://s3-eu-central-1.amazonaws.com/zalando-wp-zalando-research-production/2017/08/fashion-mnist-sprite.png)

Ein einfacher Datensatz, welcher sich ebenso gut fuer den Einstieg eignet, ist der [Fashion MNIST](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/) Datensatz von Zalando Research (ja genau, der Onlineshop :wink:), welcher aus Bildern des Modesortiments eben jenes Onlineshops besteht. Im Bild sehr ihr eine Auswahl der Trainingsbilder.

Der Datensatz besteht aus **60.000 Trainings-** und **10.000 Testdaten**. Genauso wie auch bei MNIST haben die Bildmatrizen eine Groesse von **28x28**, wobei jeder Eintrag der Matrix einem Graustufen-Pixelwert entspricht.
Jedes Bild ist mit einer aus **10 Klassen** (*Trouser, Pullover, Dress, Coat....*) gelabeled, die genaue Liste an Klassen findet ihr [hier](https://github.com/zalandoresearch/fashion-mnist#labels).

Euer Netz soll also lernen, zwischen verschiedenen Kleidungsstuecken zu unterscheiden. 

Wie man unschwer erkennen kann, wurde dieser Datensatz von Zalando als modernere und etwas anspruchsvollere Alternative zum MNIST Datensatz entwickelt. Spielt an dieser Stelle gerne selbst einmal mit dem Datensatz herum, schaut euch die Bilder an und nutzt die Tools und Techniken die wir in dieser Woche vorgestellt haben.

#### Wie bekommt ihr den Datensatz?

Den Datensatz koennt ihr genau wie den MNIST Datensatz ueber Keras herunterladen und direkt loslegen:

```python
import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

#### Ich weiss nicht wie ich anfangen soll?

Falls du nicht weisst wie du am Besten anfangen solltest, schaue dir am Besten noch einmal das Video zum Laden und Trainieren des MNIST Datensatzes aus dieser Woche an und lies das [kommentierte Notebook zum Video](../notebooks/first-mnist-net/mnist-commented-solution.ipynb). *Spoiler*: Die praktische Uebung *kann* sehr aehnlich geloest werden.

Seid gerne ermutigt neue Techniken auszuprobieren und an Parametern zu schrauben!

#### Wie reicht ihr eure Loesung ein?

Nachdem ihr euer Keras Netz trainiert habt koennt ihr es ganz einfach submitten:

1. Gehe dazu auf [open.hpi.de](https://open.hpi.de/) auf die Uebungsaufgabe und klicke auf *Aufgabe starten*.
2. Es sollte sich einer neuer Tab oeffnen, welcher euch den Python Code anzeigt, den du zur Abgabe deines Keras Models benoetigst. Alle benotigten Informationen findest du dort auch in der Beschreibung. Trotzdem an dieser Stelle noch einmal:
    1. Falls noch nicht getan, installiere das Python Package zu diesem Kurs mit `pip`:
        ```bash
        pip install deeplearning2020
        ```
        In einem Jupyter Notebook (Google Colab oder lokal) geht das mit:
        ```bash
        !pip install deeplearning2020
        ```
    2. Importiertien des Package
        ```python
        from deeplearning2020 import Submission
        ```
    3. Submitte dein Model, wobei du den Token und die Assignment ID von der Webseite kopieren musst:
        ```python
        Submission('<your-token>', '<assignment-id>', model).submit()
        ```
        Falls du fuer dein Model einen anderen Variablennamne als `model` verwendest, musst du diese Variable entsprechend verwenden.
    
3. Mit dem Ausfuehren sollte das Model von uns validiert werden und ihr erhaltet abschliessend eine Accuracy und Benotung. **Die Accuracy kann sich von euer Accuracy unterscheiden, da wir euer Model mit Werten testen, die es eventuell noch nie gesehen hat. Das gilt aber gleichermassen fuer alle Teilnehmer.**

**Ihr koennt euer trainiertes Model beliebig oft submitten und es wird automatisch das Beste Ergebnis gewaehlt, ohne dass ihr etwas machen muesst.**

#### Wie werden wir eure Loesungen bewerten?

Uns geht es hauptsaechlich darum, dass ihr selbst einmal praktisch arbeitet und mit den Tools vertraut werdet. Die Uebung sollte fuer alle Teilnehmer gut zu meistern sein.

Wir haben uns daher fuer folgende Bewertungsgrundlage entschieden:

- Bei einer **Accuracy >=0.8** (80%) gibt es volle Punktzahl
- Bei einer **Accuracy =0.0** (0%) gibt es 0 Punkte
- Alles dazwischen wird entsprechend linear interpoliert

Wir wuenschen euch viel Spass und Erfolg bei der ersten Uebung!