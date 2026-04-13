# Ruby in einem Multilanguage-Repository

## Ausgangsproblem

Ruby lag nur in einem Unterordner des Repos. Dadurch war das Ruby-Projekt unvollstandig eingerichtet:

- kein `Gemfile`
- `bundle install` schlug fehl
- kein funktionierendes Autoformat
- Ruby LSP in VS Code hing bei 0 % Indexierung

## Umgebung

- Ruby via RubyInstaller
- Ruby-Version: `ruby 4.0.2`
- VS Code mit Ruby LSP Extension

## Losungsschritte


### 1. Bundler initialisieren und wichtige Gems installieren

```bash
gem install bundler
gem install byebug
gem install minitest
gem install sqlite3
bundle init
```

Ergebnis: Ein `Gemfile` wird im Ruby-Projekt angelegt.

### 2. Benotigte Gems eintragen


In `ruby/Gemfile`:

```ruby
gem "rubocop"
gem "ruby-lsp"
gem "byebug"
gem "minitest"
gem "sqlite3"
```


- `rubocop`: Stilregeln und Formatierung
- `ruby-lsp`: Language Server für VS Code
- `byebug`: Debugging-Tool für Ruby
- `minitest`: Test-Framework für Ruby
- `sqlite3`: SQLite-Anbindung für Ruby

Hinweis zu SQLite unter Windows:

- Wenn `gem install sqlite3` wie bei dir erfolgreich durchlaeuft (z. B. `sqlite3-2.9.2-x64-mingw-ucrt`), ist fuer Ruby-Projekte in der Regel keine manuelle SQLite-Installation noetig.
- Eine manuelle Installation von der offiziellen SQLite-Seite brauchst du nur zusaetzlich, wenn du auch die `sqlite3`-Kommandozeile separat nutzen willst.

### 3. Gems lokal installieren

```bash
bundle config set --local path 'vendor/bundle'
bundle install
```

Ergebnis:

- Abhangigkeiten landen lokal in `vendor/bundle`
- keine Vermischung mit globalen Gems

## VS Code korrekt konfigurieren

### Root-Konfiguration

In `.vscode/settings.json` im Repo-Root:

```json
{
  "rubyLsp.bundleGemfile": "ruby/Gemfile",
  "rubyLsp.rubyVersionManager": {
    "identifier": "none"
  }
}
```

Wichtig: Damit kennt VS Code das Ruby-Projekt im Unterordner und nutzt RubyInstaller statt `rbenv`/`rvm`.

### Ruby-spezifische Editor-Konfiguration

In `ruby/.vscode/settings.json`:

```json
{
  "[ruby]": {
    "editor.defaultFormatter": "Shopify.ruby-lsp",
    "editor.formatOnSave": true,
    "editor.formatOnType": true,
    "editor.insertSpaces": true,
    "editor.tabSize": 2
  }
}
```

Damit sind globale und sprachspezifische Einstellungen sauber getrennt.

## Ursachenanalyse

Die Probleme waren keine Ruby-Sprachprobleme, sondern Setup-/Tooling-Themen:

- fehlendes Projekt-Setup (`Gemfile`)
- falscher Ruby-LSP-Pfad im Multilanguage-Repo
- keine lokale Gem-Verwaltung

## Ergebnis

- Ruby LSP erkennt das Projekt korrekt
- Indexierung funktioniert
- Autoformat mit RuboCop lauft beim Speichern
- saubere Struktur fur ein Multilanguage-Repository

## Offener Punkt

Aktuell konnen unterschiedliche `rubyLsp.rubyVersionManager`-Werte zwischen Root und Unterordner zu Uberschreibungen fuhren.

Empfehlung: Einen einheitlichen Wert an genau einer Stelle definieren (bevorzugt im Root), um Konflikte zu vermeiden.

## Kurzfazit

Lokale Gems plus explizite VS-Code-Konfiguration machen Ruby in einem Multilanguage-Repo stabil und wartbar.