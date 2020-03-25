![Fashion MNIST](https://cs.stanford.edu/people/karpathy/cnnembed/cnn_embed_full_1k.jpg)

**Errinnerung**: Durch die Bearbeitung der Übungen können insgesamt bis zu **40%** Prozent der Kurspunkte erhalten werden. Diese Summe setzt sich aus der Übung in dieser Woche (25%) und der Übung aus Woche 2 (15%) zusammen.

#### Was sollt ihr in dieser Übung lernen?

In dieser Kurswoche habt ihr gelernt, wie komplexere neuronale Netze aufgebaut werden und wie ihr diese auf eure Trainingsdaten anpassen könnt. Die Aufgabe in dieser Woche besteht darin, ein neuronales Netz für einen komplexen Datensatz zu trainieren und damit selbst durch Ausprobieren der verschiedenen Parameter weitere Einblicke in die Entwicklung neuronaler Netze zu erhalten. Dabei ist es egal, ob ihr [Google Colab](https://colab.research.google.com/) oder eine lokale Installation verwendet. Wir würden jedoch den Einsatz von Google Colab empfehlen, da ihr dort meist leistungsfähigere Hardware einsetzen könnt, die den Trainigsprozess stark beschleunigt.

**Ziel ist es, ein Netz für den im folgenden vorgestellten Datensatz zu trainieren, das dessen Bilder so zuverlässig wie möglich klassifiziert.**

#### Welchen Datensatz sollt ihr benutzen?

Es wird wieder ein Teildatensatz des Imagenets benutzt. Dieses wird von Fast.ai zur Verfügung gestellt und kann [hier](https://github.com/fastai/imagenette) heruntergeladen werden.

Die sehr genaue Klassifizierung ist hier nicht einfach und soll euch anregen mit verschiedenen Parameter herumzuspielen.

Der Datensatz besteht aus **12000 Trainings-** und **500 Testdaten**. Genauso wie beim Imagenette Datensatz, der in dieser Woche verwendet wurde, sind die Bilder in einer Dimension 320px groß und können wie in dieser Woche vorgestellt, verarbeitet werden.

Jedes Bild ist klassifiziert mit je eine der **10 Klassen**, welche verschiedene Hunderassen darstellen. Dabei handelt es sich um Australian Terrier, Border Terrier, Samoyed, Beagle, Shih-Tzu, English Foxhound, Rhodesian Ridgeback, Dingo, Golden Retriever und Old English Sheepdog. Die genaue Liste an Klassen findet ihr [hier](https://github.com/fastai/imagenette).

Euer Netz soll also lernen, zwischen verschiedenen Hunderassen zu unterscheiden.

#### Wie bekommt ihr den Datensatz?

Wir haben euch über unser `deeplearning2020` python package eine Funktion bereitgestellt, mit der ihr die Daten lade könnt. Diese kann folgendermaßen verwendet werden:

```python
# ohne Ausrufezeichen bei Ausführung im lokalen Notebook
!pip install --upgrade deeplearning2020
from deeplearning2020 import helper
train_data, test_data = helper.load_imagewoof()
```

#### Ich weiß nicht wie ich anfangen soll?

Falls du nicht weißt, wie du am Besten anfangen solltest, orientiere dich am Praxisvideo zum komplexen Aufbau neuronaler Netze. Schau dir dazu am besten das kommentierte Notebook an, welches du unter Lehrmaterialien zu diesem Video findest.

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

3. Mit dem Ausführen sollte das Model von uns validiert werden und du erhältst abschließend eine Accuracy und Benotung. **Unserer Accuracy kann sich von euer Accuracy unterscheiden, da wir euer Model mit Werten testen, die es eventuell noch nie gesehen hat. Das gilt aber gleichermaßen für alle Teilnehmer.**

**Ihr könnt euer trainiertes Model beliebig oft submitten und es wird automatisch das beste Ergebnis gewählt, ohne dass ihr etwas machen müsst.**

#### Wie werden wir eure Lösungen bewerten?

In dieser Übung wird mit einem komplexeren Datensatz gearbeitet. Seid daher nicht frustriert, wenn ihr keine perfekte Accuracy erhaltet. In der nächsten Kurswoche werden Techniken vorgestellt, mit denen ihr dieses Netz verbessern könnt, sodass ihr eine höhere Genauigkeit erzielt und damit auch eine bessere Bewertung für die Übung. Sie ist also bewusst darauf ausgelegt über beide Kurswochen gestreckt zu sein.

Wir haben uns daher für folgende Bewertungsgrundlage entschieden:

- Bei einer **Accuracy >= 0.95** (95%) gibt es volle Punktzahl
- Bei einer **Accuracy = 0.0** (0%) gibt es 0 Punkte
- Alles dazwischen wird entsprechend linear interpoliert

### Schwierigkeit der Übung

Wie ihr bei der Arbeit mit dem Datensatz vielleicht feststellen werdet, ist eine sehr gute Accuracy mit dem Wissen aus Woche 3 noch nicht machbar. Aus diesem Grund habt ihr auch in Woche 4 genügend Zeit, die Übung dann weiter zu bearbeiten. Wir würden euch trotzdem darum bitten, auch in dieser Woche schon herumzuprobieren, um das Wissen aus dieser Woche praktisch anzuwenden.

Falls ihr mit einem anderen Datensatz arbeiten möchtet, könnt ihr gerne, die von uns zusätzlich bereitgestellte Möglichkeit der extra Übung nutzen. Weitere Informationen findet ihr [hier](https://open.hpi.de/courses/neuralnets2020/items/3vh2FG4fjjKKNPA2GnoQ8r).

Wir wünschen euch viel Spaß und Erfolg bei der Übung!
