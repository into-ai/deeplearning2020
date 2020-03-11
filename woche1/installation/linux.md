#### Lokale Installation unter Linux

1. Download des Installationsskriptes unter [anaconda.com/distribution](https://www.anaconda.com/distribution/). Als Download sollte unter dem Reiter **Linux** die Version für **Python 3.7** und **64-Bit (x86)** (außer es handelt sich um einen Computer mit Power8/9 Architektur) gewählt werden.

2. Ausführen des Installationsskriptes im Terminal:
    ```bash
    bash ~/Downloads/Anaconda3-2019.10-Linux-x86_64.sh
    ```
    Bestätigen der Installation mit *ENTER*. Anschließend Akzeptieren der Lizenzbedingungen mit *yes*. Der Installationsort kann beliebig gewählt werden. Am Ende noch einmal die Bestätigung von `conda init` ebenfalls mit *yes*.

3. Terminal schließen und neu öffnen, damit die änderungen aktiv werden.

4. Überprüfen der Installation mit `conda list`.

5. Erstellen eines neuen *conda environment* mit
    ```bash
    conda create -n deeplearning2020 python=3.7 tensorflow keras nb_conda numpy matplotlib notebook
    ```
    Die Frage, ob die Transaktion durchgeführt werden soll mit *yes* bestätigen.

6. Aktivieren des conda environments mit
    ```bash
    conda activate deeplearning2020
    ```

7. Starten eines lokalen `jupyter notebook` server mit
   ```bash
   jupyter notebook
   ```
   Dies sollte automatisch einen neuen Browser Tab mit dem notebook *dashboard* öffnen. Falls das nicht passiert findet ihr eine URL mit einem Token in der Ausgabe auf der Kommandozeile.

8. Erstellen eines neuen `jupyter notebook` in einem beliebigen Ordner durch Klick auf **New** im Dashboard oben rechts und dann auf **[conda env:deeplearning2020]**.

9.  Testen ob alle Pakete fehlerfrei importiert und benutzt werden können, indem eine Codezelle des notebooks mit folgendem Code ausgeführt wird (**Run**):
    ```python
    import tensorflow as tf
    from tensorflow import keras
    import numpy as np
    import matplotlib.pyplot as plt
    print(tf.__version__)
    ```

10. Speichern des notebooks durch Klick auf **File>Save** oder den *Save* Button links oben. Wenn das Speichern erfolgreich war sollte ein neuer Checkpoint erstellt worden sein.

11. (Optional) Nach dem Speichern kann die Seite mit dem **Logout** Button oben rechts verlassen werden und der  `jupyter notebook` Server mit `Ctrl-C` gestoppt werden. Zum erneuten Starten siehe Schritt 7.

12. (Optional) Conda erlaubt es beliebig viele environments zu erstellen. Mit `conda deactivate` kann das `deeplearning2020` environment deaktiviert werden und weitere environments erstellt und aktiviert werden falls gewünscht. Für die erneute Aktivierung des `deeplearning2020` environments siehe Schritt 6.
