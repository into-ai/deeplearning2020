#### Lokale Installation unter MacOS

##### Grafisches Installationsprogramm
1. Zuallererst müsst ihr euch das grafische Installationsprogramm von [Anaconda][1] herunter laden. Hierbei wollen wir die neuere Python Version und wählen somit Python 3.7.

2. Dieses Installationsprogramm muss anschließend ausgeführt werden, um die Installation von Anaconda abzuschließen.

##### Homebrew Packet Manager

1. Solltet ihr kein Homebrew auf eurem Rechner installiert haben, müsst ihr dies als aller Erstes tun. Geht hierfür auf die [offizielle Webseite][2] und kopiert den Befehl zu "Install Homebrew" in euer Terminal und führt ihn aus.

2. `brew cask install anaconda` installiert euch die aktuelle Anaconda Version mit dem Homebrew Packet Manager.

**Im Terminal:**

3. `conda` verrät uns, ob wir den Befehl conda überall im Terminal verwenden können

4. **Grafisches Installationsprogramm:**
`echo 'export PATH=“/Users/<USER_NAME>/anaconda3/bin:$PATH"' >> <SHELL_KONFIGURATIONSDATEI>` **Homebrew:**
`echo 'export PATH="/usr/local/anaconda3/bin:$PATH"' >> <SHELL_KONFIGURATIONSDATEI>`  schreibt den Pfad zu dem conda Befehl in eure Konfigurationsdatei.
Bei mir handelt es sich bei der Shell Konfigurationsdatei um `.zshrc`, da ich die zsh Shell verwende. Ihr habt höchstwahrscheinlich die bash Shell und somit die Konfigurationsdatei `.bash_profile`. Wenn ihr euch sicher sein wollt, erfahrt ihr den Namen eurer Shell unter dem Befehl: `echo “$SHELL”`. Der USER_NAME muss ebenfalls in dem Pfad zur Installation mit dem grafischen Installationsprogramm angepasst werden. Mit welchem User ihr angemeldet seid, könnt ihr mit dem Befehl: `echo “$USER”` herausfinden.

5. `source <SHELL_KONFIGURATIONSDATEI>` führt die Konfigurationsdatei aus, sodass der Pfad nicht nur in die Datei geschrieben, sondern ebenfalls exportiert wird, um conda anschließend überall im Terminal ausführen zu können.

6. `conda` sollte jetzt den Hilfstext mit einer Liste der verfügbaren Befehle ausgeben.

7. `conda create -n neuralnets2020` erstellt eine Anaconda (virtuelle) Umgebung mit dem Namen neuralnets2020. In diesem können wir jetzt alle notwedigen Pakete installieren ohne andere Umgebungen zu beeinflussen und das Projekt somit von allen anderen Projekten und deren Abhängigkeiten zu isolieren.

8. `conda init <SHELL_NAME>` initialisiert die Shell, um anschließend Anaconda Umgebungen zu aktivieren (z.B.: `conda init zsh` oder `conda init bash`).

9. `conda activate neuralnets2020` aktiviert die virtuelle Umgebung (befinden uns anschließend in dieser), was durch das Kürzel vor dem User erkennbar ist.

10. `conda install tensorflow nb_conda` installiert alle benötigten Pakete in der aktiven Umgebung.

11. `jupyter notebook` startet einen Notebook Server, sodass ihr lokal in eurem Browser Jupyter Notebooks erstellen könnt und die gleiche Funktionalitäten habt, wie sonst in Google Colab (kann mit CTRL-C beendet werden).

12. `conda deactivate` deaktiviert die aktuell aktive, virtuelle Umgebung, um z.B. eine andere Umgebung zu öffnen.

13. `conda activate neuralnets2020` aktiviert erneut eine erstellte virtuelle Umgebung, um die Arbeit an dem Projekt fortzusetzen.



[1]: https://www.anaconda.com/distribution/
[2]: https://brew.sh/
