#### Assignment Woche 2

EDIT: Die Lösung befindet sich unter diesem [Link](https://colab.research.google.com/drive/1LoKnlSpvVNF0NbVMHt58Ci45uBwjmu_o)

![Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist/raw/master/doc/img/embedding.gif)

**Errinnerung**: Durch die Bearbeitung der Übungen können insgesamt bis zu **40%** Prozent der Kurspunkte erhalten werden. Diese Summe setzt sich aus der Übung in dieser Woche (15%) und der Übung in der nächsten Woche (25%) zusammen.

#### Was sollt ihr in dieser Übung lernen?

Ihr habt in dieser Woche die wichtigsten Tools für das Trainieren von neuronalen Netzen kennegelernt und sollt nun einmal selbst ein Netz trainieren! Dabei ist es egal, ob ihr [Google Colab](https://colab.research.google.com/) oder eine lokale Installation verwendet.

Ziel ist es, ein Netz für den im folgenden vorgestellten Datensatz zu trainieren, das dessen Bilder so zuverlässig wie möglich klassifiziert.

#### Welchen Datensatz sollt ihr benutzen?

![Fashion MNIST](https://s3-eu-central-1.amazonaws.com/zalando-wp-zalando-research-production/2017/08/fashion-mnist-sprite.png)

Ein einfacher Datensatz, welcher sich ebenso gut für den Einstieg eignet, ist der [Fashion MNIST](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/) Datensatz von Zalando Research (ja genau, der Onlineshop :wink:), welcher aus Bildern des Modesortiments eben jenes Onlineshops besteht. Im Bild sehr ihr eine Auswahl der Trainingsbilder.

Der Datensatz besteht aus **60.000 Trainings-** und **10.000 Testdaten**. Genauso wie auch bei MNIST haben die Bildmatrizen eine Größe von **28x28**, wobei jeder Eintrag der Matrix einem Graustufen-Pixelwert entspricht.
Jedes Bild ist mit einer aus **10 Klassen** (*Trouser, Pullover, Dress, Coat....*) gelabeled, die genaue Liste an Klassen findet ihr [hier](https://github.com/zalandoresearch/fashion-mnist#labels).

Euer Netz soll also lernen, zwischen verschiedenen Kleidungsstücken zu unterscheiden.

Wie man unschwer erkennen kann, wurde dieser Datensatz von Zalando als modernere und etwas anspruchsvollere Alternative zum MNIST Datensatz entwickelt. Spielt an dieser Stelle gerne selbst einmal mit dem Datensatz herum, schaut euch die Bilder an und nutzt die Tools und Techniken die wir in dieser Woche vorgestellt haben.

#### Wie bekommt ihr den Datensatz?

Den Datensatz könnt ihr genau wie den MNIST Datensatz über Keras herunterladen und direkt loslegen:

```python
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
```

#### Ich weiß nicht wie ich anfangen soll?

Falls du nicht weißt wie du am Besten anfangen solltest, schau dir am Besten noch einmal das Video zum Laden und Bearbeiten des MNIST Datensatzes aus dieser Woche an und lies das [kommentierte Notebook zum Video](../notebooks/first-mnist-net/mnist-commented-solution.ipynb). *Spoiler*: Die praktische Übung *kann* sehr ähnlich gelöst werden.

Seid gerne ermutigt neue Techniken auszuprobieren und an Parametern zu schrauben!

#### Wie reicht ihr eure Lösung ein?

Nachdem ihr euer Keras Netz trainiert habt, könnt ihr es ganz einfach hochladen:

1. Gehe dazu auf [open.hpi.de](https://open.hpi.de/) auf die Übungsaufgabe und klicke auf *Aufgabe starten*.
2. Es sollte sich ein neuer Tab öffnen, welcher dir den Python Code anzeigt, den du zur Abgabe deines Keras Models benötigst. Alle benötigten Informationen findest du dort auch in der Beschreibung. Trotzdem an dieser Stelle noch einmal:
    1. Falls noch nicht getan, installiere das Python Package zu diesem Kurs mit `pip`:
        ```bash
        pip install --upgrade deeplearning2020
        ```
        In einem Jupyter Notebook (Google Colab oder lokal) geht das mit:
        ```bash
        !pip install --upgrade deeplearning2020
        ```
    2. Importieren des Package
        ```python
        from deeplearning2020 import Submission
        ```
    3. Submitte dein Model, wobei du den Token und die Assignment ID von der Webseite kopieren musst:
        ```python
        Submission('<your-token>', '<assignment-id>', model).submit()
        ```
        Falls du für dein Model einen anderen Variablennamen als `model` verwendest, musst du diese Variable entsprechend verwenden.

3. Mit dem Ausführen sollte das Model von uns validiert werden und du erhaeltst abschließend eine Accuracy und Benotung. **Unserer Accuracy kann sich von euer Accuracy unterscheiden, da wir euer Model mit Werten testen, die es eventuell noch nie gesehen hat. Das gilt aber gleichermaßen für alle Teilnehmer.**

**Ihr könnt euer trainiertes Model beliebig oft submitten und es wird automatisch das beste Ergebnis gewählt, ohne dass ihr etwas machen müsst.**

#### Wie werden wir eure Lösungen bewerten?

Uns geht es hauptsächlich darum, dass ihr selbst einmal praktisch arbeitet und mit den Tools vertraut werdet. Die Übung sollte für alle Teilnehmer gut zu meistern sein.

Wir haben uns daher für folgende Bewertungsgrundlage entschieden:

- Bei einer **Accuracy >= 0.8** (80%) gibt es volle Punktzahl
- Bei einer **Accuracy = 0.0** (0%) gibt es 0 Punkte
- Alles dazwischen wird entsprechend linear interpoliert

Wir wünschen euch viel Spaß und Erfolg bei der ersten Übung!
