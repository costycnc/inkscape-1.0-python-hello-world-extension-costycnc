
# Inkscape G-code Generator - Esempio Didattico

![Inkscape](https://img.shields.io/badge/Inkscape-1.0+-blue.svg) ![Python](https://img.shields.io/badge/Python-3.x-green.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Descrizione

Questo è un **esempio pratico** per chi vuole imparare le basi delle **estensioni di Inkscape** e trasformare un'immagine vettoriale in **G-code** per macchine a 3 assi (X, Y, Z).

> **⚠️ IMPORTANTE:** Non è un programma finito e solido... è solo un **esempio didattico** con il minimo indispensabile di codice!

## 🎯 Cosa fa

- Converte un percorso (path) selezionato in Inkscape in **G-code**
- Genera codice per macchine a **3 assi (X, Y, Z)**
- Supporta comandi G-code di base (G01, G21, G90, G92)
- Il file G-code viene salvato automaticamente

## 📋 Prerequisiti

Prima di usare l'estensione, assicurati che il tuo oggetto sia un **percorso (path)**. Se non lo è, convertilo usando:

```
Menu > Path > Object to Path
```
(opzioni alternative: `Stroke to Path` o `Bitmap to Path`)

## 🚀 Installazione

### Metodo 1 (consigliato - estensioni utente)
Copia i file `gcode.inx` e `gcode.py` in:

```
C:\Users\IL_TUO_NOME_ADMIN\AppData\Roaming\inkscape\extensions
```

### Metodo 2 (sistema - richiede permessi admin)
Copia i file in:

```
C:\Program Files\Inkscape\share\inkscape\extensions
```

> **Nota:** Questo metodo potrebbe dare errore di permessi di scrittura.

### Dopo l'installazione
1. **Riavvia Inkscape**
2. L'estensione apparirà in: `Menu > Estensioni > helloworld > gcode`

> 🔍 **Se non trovi l'estensione nel menu... significa che qualcosa è andato storto!**

## 💻 Come si usa

1. **Disegna o importa** un vettoriale in Inkscape
2. **Converti in path** se necessario (vedi Prerequisiti)
3. **Seleziona il percorso** che vuoi convertire
4. Vai su `Menu > Estensioni > helloworld > gcode`
5. **Esegui l'estensione**

## 📁 Output

Dopo l'esecuzione, troverai il file `gcode.nc` nella cartella:

```
C:\Users\IL_TUO_NOME_ADMIN\AppData\Roaming\inkscape\extensions\gcode.nc
```

> **Nota:** Il file `gcode.nc` viene **sovrascritto** ogni volta che esegui l'estensione.

## 🔧 Spiegazione del codice

Ecco cosa fa il tuo script passo passo:

```python
import inkex
from inkex import bezier
from inkex.elements import Group, Line
```

**Import** dei moduli necessari di Inkscape.

```python
class hello(inkex.EffectExtension):
```
Classe principale che eredita da `EffectExtension`.

```python
def effect(self):
```
Metodo principale eseguito dall'estensione.

```python
g = "G21 F500 G90\nG92 X0 Y0\n"
```
Inizializza il G-code con:
- `G21` = unità millimetriche
- `F500` = feed rate 500 mm/min
- `G90` = posizionamento assoluto
- `G92 X0 Y0` = imposta origine corrente

```python
current_layer = self.svg.get_current_layer()
path_list = current_layer.xpath('./svg:path')
```
Ottiene il layer corrente e trova tutti i percorsi (path) al suo interno.

```python
for path in path_list:
    csp_list = path.path.to_superpath()
    bezier.cspsubdiv(csp_list, 1)
```
Per ogni path, lo converte in formato CSP (Curve Super Path) e lo suddivide per approssimare le curve.

```python
for cord in csp:
    g += "G01 X" + "{:.2f}".format(cord[0][0]) + " Y" + "{:.2f}".format(cord[0][1]) + "\n"
```
Genera un comando `G01` per ogni punto del percorso, formattando le coordinate con 2 decimali.

```python
with open("gcode.nc", "w") as f:
    f.write(g)
```
Salva il G-code generato nel file `gcode.nc`.

## 🎨 Personalizzazione - Aggiungere comandi personalizzati

Il codice è **molto semplice e facile da modificare** per aggiungere comandi come:

```python
# Aggiungi all'inizio del codice G, dopo l'inizializzazione:
g += "M03 S1000\n"  # Accendi mandrino a 1000 RPM
g += "G04 P2\n"      # Pausa 2 secondi

# Aggiungi alla fine, prima di G01 X0 Y0:
g += "M05\n"         # Spegni mandrino
g += "M30\n"         # Fine programma
```

### Esempi di comandi che puoi aggiungere:

| Comando | Funzione |
|---------|----------|
| `M03 S1000` | Accendi mandrino a 1000 RPM |
| `M05` | Spegni mandrino |
| `M08` | Attiva liquido refrigerante |
| `M09` | Disattiva liquido refrigerante |
| `G04 P1` | Pausa 1 secondo |
| `M30` | Fine programma e reset |

## 📊 Output G-code di esempio

Ecco un esempio di cosa produce l'estensione:

```gcode
G21 F500 G90
G92 X0 Y0
G01 X10.50 Y15.20
G01 Z5
G01 Z0
G01 X20.30 Y25.40
G01 X30.10 Y10.80
G01 Y0
G01 X0
```

## ❗ Possibili problemi e soluzioni

| Problema | Soluzione |
|----------|-----------|
| "No path found!" | Assicurati di avere selezionato un path (converti l'oggetto con `Object to Path`) |
| Estensione non appare nel menu | Riavvia Inkscape o controlla la cartella di installazione |
| Errore di permessi | Usa la cartella estensioni utente (AppData/Roaming) |
| File gcode.nc non viene creato | Verifica i permessi di scrittura nella cartella estensioni |
| Coordinate strane o troppo grandi | Ricontrolla che il percorso non sia in scala errata |

## 🔄 Limitazioni attuali

- ❌ Non gestisce curve di Bezier (le approssima con linee rette)
- ❌ Non supporta più layer
- ❌ Non chiede all'utente impostazioni (feed rate, profondità Z, ecc.)
- ❌ Non supporta movimenti ad arco (G02/G03)

## 📈 Prossimi miglioramenti possibili

- [ ] Aggiungere interfaccia utente per parametri (profondità Z, feed rate)
- [ ] Migliorare la gestione delle curve
- [ ] Supportare archi con G02/G03
- [ ] Aggiungere opzione per il nome del file di output
- [ ] Gestire più path su layer diversi

## 📝 Licenza

Questo progetto è puramente **didattico** - sentiti libero di usarlo, modificarlo e condividerlo!

## 🙏 Ringraziamenti

Creato come esempio per la community di Inkscape e appassionati di CNC.

---

**Buon coding e buon taglio CNC!** 🎯⚙️
