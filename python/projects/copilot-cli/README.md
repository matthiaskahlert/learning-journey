# Copilot CLI – Python SDK Experiment

Mein Plan war es die copilot cli auf meiner gitbash meines windowssystems zum laufen zu kriegen.

## Probleme auf dem Weg

1. **`copilot: command not found`** – die CLI war gar nicht installiert, nur das Python SDK per pip.
2. **Node.js zu alt** – nach dem npm-Install kam `GitHub Copilot CLI requires Node.js v24 or higher. Currently using v18.16.0.` → Node musste erst auf v25 geupdated werden.
3. **`on_permission_request` fehlt** – das Python SDK wirft einen `ValueError`, wenn beim `create_session`-Aufruf kein Permission-Handler angegeben wird.
4. **Timeout nach 60s / 120s** – das SDK konnte nicht rechtzeitig eine Antwort empfangen, weil der CLI-Prozess nicht eingeloggt war.
5. **Auth nur in PowerShell möglich** – der interaktive Login (`copilot` + `/login`) funktionierte nicht in Git Bash ohne `winpty`, aber in PowerShell problemlos.
6. **SDK spawnt eigenen CLI-Prozess** – ohne `COPILOT_CLI_URL` startet das SDK selbst eine CLI-Instanz, die nicht eingeloggt ist und deshalb hängt.

## Lösung

Zusammenfassung was gebraucht hat um es zum Laufen zu bringen:

- Node.js v24+ installieren → `copilot --version` funktioniert
- Login via `copilot` + `/login` (in PowerShell) → Credentials systemweit gespeichert
- Headless-Server in einem separaten Terminal: `copilot --headless --port 4321`
- `COPILOT_CLI_URL=localhost:4321` setzen → SDK verbindet sich mit dem laufenden Server statt selbst spawning

```bash
# Terminal A (einmal starten, offen lassen)
copilot --headless --port 4321

# Terminal B
export COPILOT_CLI_URL=localhost:4321
python main.py
```

## Ergebnis

Nach all diesen Schritten hat es funktioniert. Die erste erfolgreiche Antwort vom Modell war:

> *Why did the scarecrow win an award? Because he was outstanding in his field!*
