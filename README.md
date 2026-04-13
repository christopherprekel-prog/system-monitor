# System Monitor 
---

### Beschreibung
Ein kleines Python Projekt zur Erfassung der CPU und RAM Daten. Über den Zeitraum von einer Minute wird die RAM und CPU Auslastung aufgenommen, in eine CSV Datei geschrieben. Dann wird diese wieder eingelesen und ein Diagramm über die Zeit erstellt, welches als pdf abgespeichert wird

### Voraussetzungen
- Python3
- psutil
- matplotlib

### Installationen
```bash
source venv/bin/activate
pip install psutil matplotlib
