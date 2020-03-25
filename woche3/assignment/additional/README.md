## Informationen zu weiteren Übungsmöglichkeiten

Im Internet und vor allem direkt in [Tensorflow](https://www.tensorflow.org/datasets/catalog/overview) gibt es einige Datensätze mit denen das erlernte Wissen ganz einfach auf die Probe gestellt werden kann. Seid also neugierig und spielt gerne so viel ihr wollt mit diesen Datensätzen herum. Solange ihr es während der Kurslaufzeit tut, können eventuell aufkommende Fragen noch im Forum geklärt werden.

Da ihr in der aktuellen Übung in dieser Woche noch keine optimalen Ergebnisse erzielen werdet und durch die Inhalte der nächsten Woche euer Netz stark verbessern könnt, wollten wir euch an dieser Stelle nochmal speziell die Möglichkeit geben, eine bessere Genauigkeit mit den bis jetzt erlernten Methoden zu erzielen.

Der  Datensatz, den wir euch hierfür vorstellen wollen, nennt sich `deep_weeds` und enthält Bilder von 9 verschiedenen Gräsern. Ebenso steht er ganz unkompliziert unter den Tensorflow Datasätzen zur Verfügbar. Weitere Informationen findet ihr [hier](https://www.tensorflow.org/datasets/catalog/deep_weeds).

Diese weitere Übungsmöglichkeit ist **komplett freiwillig** und es wird somit **keine Punkte** geben.

### Einbindung des Datensatzes

Über folgenden Befehl kann der Datensatz genauso wie der in Woche 3 behandelte Datensatz eingebunden werden:

```python
train_data_weed = tfds.load(
    'deep_weeds',
    split='train[:80%]',
    as_supervised=True,
    with_info=True
)

test_data_weed = tfds.load(
    'deep_weeds',
    split='train[80%:]',
    as_supervised=True,
    with_info=True
)
```

Viel Erfolg bei der Bearbeitung.
