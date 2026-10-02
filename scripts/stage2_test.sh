#!/bin/bash
# этап 2: проверка параметров командной строки
cd "$(dirname "$0")/.."
echo "=== 1. Только --vfs ==="
echo "exit" | python3 emulator.py --vfs ./vfs/test.csv
echo "=== 2. --vfs и --script ==="
echo "exit" | python3 emulator.py --vfs ./vfs/test.csv --script scripts/start.emu
echo "=== 3. Несуществующий скрипт ==="
echo "exit" | python3 emulator.py --vfs ./vfs/test.csv --script scripts/no_such.emu
echo "=== 4. Без обязательного --vfs ==="
python3 emulator.py --script scripts/start.emu
