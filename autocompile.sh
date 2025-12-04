UIC="./.venv/bin/pyside6-uic"

echo "👀 Beobachte alle .ui Dateien..."
echo "📂 Ziel-Format: ui_<DATEINAME>.py (im selben Ordner wie die .ui Datei)"
echo "Drücke [STRG+C] zum Beenden."

while true; do
    # Suche alle .ui Dateien, ignoriere aber den .venv Ordner (für Performance)
    find . -path "./.venv" -prune -o -name "*.ui" -print | while read ui_file; do

        # Das Verzeichnis der .ui Datei extrahieren
        # Aus "./examples/005/myFirstUi.ui" wird "./examples/005"
        ui_dir=$(dirname "$ui_file")

        # Dateinamen extrahieren
        # Aus "./examples/005/myFirstUi.ui" wird "myFirstUi.ui"
        filename_with_ext=$(basename "$ui_file")

        # Dateiendung entfernen -> "myFirstUi"
        filename_no_ext="${filename_with_ext%.*}"

        # Ziel definieren: ui_Verzeichnis/ui_Dateiname.py
        # Beispiel: ./examples/005/ui_myFirstUi.py
        py_file="$ui_dir/ui_$filename_no_ext.py"

        # Check: Muss kompiliert werden? (Datei fehlt ODER .ui ist neuer)
        if [ ! -f "$py_file" ] || [ "$ui_file" -nt "$py_file" ]; then
            echo "🔄 Änderung in $ui_file erkannt..."

            $UIC "$ui_file" -o "$py_file"

            if [ $? -eq 0 ]; then
                # Ausgabe angepasst, um den vollständigen Pfad zu zeigen
                echo "✅ Erstellt: $py_file"
            else
                echo "❌ Fehler beim Kompilieren von $ui_file"
            fi
        fi
    done
    sleep 1
done
