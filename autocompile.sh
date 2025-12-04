UIC="./.venv/bin/pyside6-uic"

clear

echo "autocompiling is running. Waiting for file changes..."
echo "Press ctrl+c to stop."

while true; do
    find . -path "./.venv" -prune -o -name "*.ui" -print | while read ui_file; do
        ui_dir=$(dirname "$ui_file")
        filename_with_ext=$(basename "$ui_file")
        filename_no_ext="${filename_with_ext%.*}"
        py_file="$ui_dir/ui_$filename_no_ext.py"
        if [ ! -f "$py_file" ] || [ "$ui_file" -nt "$py_file" ]; then
            echo "🔄 Changes in $ui_file detected. Compiling..."
            $UIC "$ui_file" -o "$py_file"
            if [ $? -eq 0 ]; then
                echo "✅ Created: $py_file"
            else
                echo "❌ Compiling error $ui_file"
            fi
        fi
    done
    sleep 1
done
