**Diese Übung ist für Woche 3 und Woche 4 gedacht. In den nächsten beiden Kurswochen werdet ihr vielfältige Möglichkeiten kennenlernen die Genauigkeit eures Netzes zu verbessern.**

EDIT: Die Lösungen zu dieser Übung befinden sich unter den folgenden Links:
- [Lösung nach Woche 3](https://colab.research.google.com/drive/1Oqdv-ldz4WZJqhMbcjQJ24fBh2km4xIb)
- [Lösung nach Woche 3 mit weniger Parametern](https://colab.research.google.com/drive/1C0YDbJb7qug0ibum4Ox8MI3l2vHSSi_G)
- [Lösung nach Woche 4 mit Transferlearning](https://colab.research.google.com/drive/1JSgk_njvRxCl5njT1pQ1WuSKOnwzen9T)

![ImageWoof](https://drive.google.com/uc?id=1UVjiie92RMAcsmSgRpNugANX2m7nJOIx)

**Errinnerung**: Durch die Bearbeitung der Übungen können insgesamt bis zu **40%** Prozent der Kurspunkte erhalten werden. Diese Summe setzt sich aus der Übung in dieser Woche (25%) und der Übung aus Woche 2 (15%) zusammen.

#### Was sollt ihr in dieser Übung lernen?

In dieser Kurswoche habt ihr gelernt, wie komplexere neuronale Netze aufgebaut werden und wie ihr diese auf eure Trainingsdaten anpassen könnt. Die Aufgabe in dieser Woche besteht darin, ein neuronales Netz für einen komplexen Datensatz zu trainieren und damit selbst durch Ausprobieren der verschiedenen Parameter weitere Einblicke in die Entwicklung neuronaler Netze zu erhalten. Dabei ist es egal, ob ihr [Google Colab](https://colab.research.google.com/) oder eine lokale Installation verwendet. Wir würden jedoch den Einsatz von Google Colab empfehlen, da ihr dort meist leistungsfähigere Hardware einsetzen könnt, die den Trainigsprozess stark beschleunigt.

**Ziel ist es, ein Netz für den im folgenden vorgestellten Datensatz zu trainieren, das dessen Bilder so zuverlässig wie möglich klassifiziert.**

#### Welchen Datensatz sollt ihr benutzen?

Es wird wieder ein Teildatensatz des Imagenets benutzt. Dieser wird von Fast.ai zur Verfügung gestellt und kann [hier](https://github.com/fastai/imagenette) heruntergeladen werden.

Die sehr genaue Klassifizierung ist hier nicht einfach und soll euch anregen, mit verschiedenen Parametern herumzuspielen.

Der Datensatz besteht aus **10.000 Trainings-** und **3000 Testdaten**. Genauso wie beim Imagenette Datensatz, der in dieser Woche verwendet wurde, sind die Bilder in einer Dimension 320px groß und können wie in dieser Woche vorgestellt, verarbeitet werden.

Jedes Bild ist mit je einer der **10 Klassen** klassifiziert, welche verschiedene Hunderassen darstellen. Dabei handelt es sich um Australian Terrier, Border Terrier, Samoyed, Beagle, Shih-Tzu, English Foxhound, Rhodesian Ridgeback, Dingo, Golden Retriever und Old English Sheepdog. Die genaue Liste an Klassen findet ihr [hier](https://github.com/fastai/imagenette).

Euer Netz soll also lernen, zwischen verschiedenen Hunderassen zu unterscheiden.

#### Wie bekommt ihr den Datensatz?

Wir haben euch über unser `deeplearning2020` python package eine Funktion bereitgestellt, mit der ihr die Daten laden könnt. Diese kann folgendermaßen verwendet werden:

```python
# ohne Ausrufezeichen bei Ausführung im lokalen Notebook
!pip install --upgrade deeplearning2020
from deeplearning2020.datasets import ImageWoof

train_data, test_data, classes = ImageWoof.load_data()
```
Der Datensatz ist in einen `train_data` (Trainigsdaten) und einen `test_data` (Validierungdaten) Datensatz aufgeteilt, welche ihr wie oben gezeigt laden könnt.

Die `load_data()` Funktion liefert sowohl einen Datensatz zurück, mit dem ihr genauso arbeiten könnt, wie mit den den aus `tfds.load` geladenen Datensets.

Der Unterschied ist, dass wir euch mit diesem Befehl Trainigsdaten (Bilder und Label), Testdaten (Bilder und Label) und auch die Klassennamen über `classes` bereitstellen. Damit könnt ihr dann weiterarbeiten.

Um einen Eindruck über die Klassen zu bekommen, könnt ihr folgendes ausführen:
Wie im Notebook in dieser Woche gezeigt,könnt ihr über `helpers.plot_images(train_data.take(9), classes)` Bilder des Datensatzes anzeigen, um einen Eindruck zu bekommen, wie diese aussehen.


Hier noch ein paar weitere Informationen zum Datensatz:
- Die Bildpunkte sind als Floats zwischen 0 und 1 gespeichert. Das heißt für euch, dass die im Notebook 3.5.2 genutzte `preprocessing` Funktion genutzt werden kann, wobei das Teilen durch 255 weggelassen werden muss.
- Die Labels der Daten liegen in sparse Form vor. Das heißt für euch, dass ihr die `sparse_categorical_crossentropy` Fehlerfunktion nutzen solltet.

Somit sieht die preprocessing Funktion dieser Woche so aus:
```python
def preprocess(image, label):
    resized_image = tf.image.resize(image, [300, 300])
    return resized_image, label
```
Dies ist notwendig, da die Bilder nicht in der gleichen Bildgröße vorkommen und somit vorher auf eine einheitliche Größe resized werden müssen.

Um auf dem Netz trainieren zu können orientiert ihr euch am besten am [Notebook zum Video `3.5.2`](https://colab.research.google.com/drive/18BGSjiQ9h7-XJ45HNV0iK2coaRTd8AQk), so das preprocessing der Daten im Abschnitt **Preprocessing der Daten zur schnelleren Verarbeitung** vorgestellt ist.

#### Ich weiß nicht, wie ich anfangen soll

Falls du nicht weißt, wie du am Besten anfangen solltest, orientiere dich am [Praxisvideo zum komplexen Aufbau neuronaler Netze](https://colab.research.google.com/drive/18BGSjiQ9h7-XJ45HNV0iK2coaRTd8AQk). Schau dir dazu am besten das kommentierte Notebook an, welches du unter Lehrmaterialien zu diesem Video findest.

Realistische Werte für die Validation Accuracy für diesen Datensatz mit den gelernten Methoden aus Woche 3 sind um die 50% mit starken Overfitting. In der nächsten Kurswoche werdet ihr diese schrittweise verbessern können.

Seid gerne ermutigt, neue Techniken auszuprobieren und an Parametern zu schrauben!

#### Wie reicht ihr eure Lösung ein?

Nachdem ihr euer Keras Netz trainiert habt, könnt ihr es ganz einfach hochladen:

1. Gehe dazu auf [open.hpi.de](https://open.hpi.de/) auf die Übungsaufgabe und klicke auf *Aufgabe starten*.
2. Es sollte sich ein neuer Tab öffnen, welcher dir den Python Code anzeigt, den du zur Abgabe deines Keras Models benötigst. Alle benötigten Informationen findest du dort auch in der Beschreibung. Trotzdem an dieser Stelle noch einmal:
    1. Falls noch nicht getan, installiere das Python Package zu diesem Kurs mit Hilfe von pip:
        ```
        pip install --upgrade deeplearning2020
        ```

        In einem Jupyter Notebook (Google Colab oder lokal) geht das mit:
        ```
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

3. Mit dem Ausführen sollte das Model von uns validiert werden und du erhältst abschließend eine Accuracy und Benotung. **Unsere Accuracy kann sich von euer Accuracy unterscheiden, da wir euer Model mit Werten testen, die es eventuell noch nie gesehen hat. Das gilt aber gleichermaßen für alle Teilnehmer.**

**Ihr könnt euer trainiertes Model beliebig oft submitten und es wird automatisch das beste Ergebnis gewählt, ohne dass ihr etwas machen müsst.**

#### Wie werden wir eure Lösungen bewerten?

In dieser Übung wird mit einem komplexeren Datensatz gearbeitet. Seid daher nicht frustriert, wenn ihr keine perfekte Accuracy erhaltet. In der nächsten Kurswoche werden Techniken vorgestellt, mit denen ihr dieses Netz verbessern könnt, sodass ihr eine höhere Genauigkeit erzielt und damit auch eine bessere Bewertung für die Übung. Sie ist also bewusst darauf ausgelegt, über beide Kurswochen gestreckt zu sein. Fangt also diese Woche mit der Bearbeitung der Aufgabe an und verbessert euer Netz in der nächsten Kurswoche.

Eure Abgabe bewerten wir nach folgender Bewertungsgrundlage:

- Bei einer **Accuracy >= 0.95** (95%) gibt es volle Punktzahl
- Bei einer **Accuracy = 0.0** (0%) gibt es 0 Punkte
- Alles dazwischen wird entsprechend linear interpoliert

### Schwierigkeit der Übung

Wie ihr bei der Arbeit mit dem Datensatz vielleicht feststellen werdet, ist eine sehr gute Accuracy mit dem Wissen aus Woche 3 noch nicht machbar. Aus diesem Grund habt ihr auch in Woche 4 genügend Zeit, die Übung dann weiter zu bearbeiten. Wir würden euch trotzdem darum bitten, auch in dieser Woche schon herumzuprobieren, um das Wissen aus dieser Woche praktisch anzuwenden.

Falls ihr mit einem anderen Datensatz arbeiten möchtet, könnt ihr gerne, die von uns zusätzlich bereitgestellte Möglichkeit der extra Übung nutzen. Weitere Informationen findet ihr [hier](https://open.hpi.de/courses/neuralnets2020/items/3vh2FG4fjjKKNPA2GnoQ8r).

Wir wünschen euch viel Spaß und Erfolg bei der Übung!
