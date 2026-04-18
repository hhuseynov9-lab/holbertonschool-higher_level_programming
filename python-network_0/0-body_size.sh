#!/bin/bash
# Bu skript daxil edilən URL-in body ölçüsünü baytla göstərir

# 1. İstifadəçinin bir URL daxil edib-etmədiyini yoxlayırıq
if [ -z "$1" ]; then
    echo "İstifadə qaydası: ./script.sh <URL>"
    exit 1
fi

# 2. curl əmrini işlədirik
# -s: Proqres barı gizlədir (artıq bilirsən!)
# -o /dev/null: Cavabın özünü (məs. HTML-i) ekrana çıxarmır, "zibil qutusuna" atır
# -w: Spesifik məlumatları (metadata) çıxarmaq üçün işlədilir
curl -s "$1" -o /dev/null -w "%{size_download}\n"
