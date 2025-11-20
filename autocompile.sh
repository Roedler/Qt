UIC="./.venv/bin/pyside6-uic"

OUTPUT_DIR="./compiled"

mkdir -p "$OUTPUT_DIR"

echo "👀 Beobachte alle .ui Dateien..."
echo "📂 Ziel-Ordner: $OUTPUT_DIR"
echo "Drücke [STRG+C] zum Beenden."

while true; do
    # Suche alle .ui Dateien, ignoriere aber den .venv Ordner (für Performance)
    find . -path "./.venv" -prune -o -name "*.ui" -print | while read ui_file; do

        # Dateinamen extrahieren
        # Aus "./examples/005/myFirstUi.ui" wird "myFirstUi.ui"
        filename_with_ext=$(basename "$ui_file")

        # Dateiendung entfernen -> "myFirstUi"
        filename_no_ext="${filename_with_ext%.*}"

        # Ziel definieren: ./compiled/myFirstUi.py
        # (Laut deinem Screenshot nutzt du kein "ui_" Präfix mehr)
        py_file="$OUTPUT_DIR/$filename_no_ext.py"

        # Check: Muss kompiliert werden? (Datei fehlt ODER .ui ist neuer)
        if [ ! -f "$py_file" ] || [ "$ui_file" -nt "$py_file" ]; then
            echo "🔄 Änderung in $filename_with_ext erkannt..."

            $UIC "$ui_file" -o "$py_file"

            if [ $? -eq 0 ]; then
                echo "✅ Erstellt: compiled/$filename_no_ext.py"
            else
                echo "❌ Fehler beim Kompilieren von $ui_file"
            fi
        fi
    done
    sleep 1
done
