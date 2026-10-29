"""
build_exe.py - Compilador automatizado a ejecutable único .EXE portable
Empaqueta todo (código, imágenes de Pooh, audio de caja de música, motor de sabiduría)
en un único archivo independiente: dist/Winnie_Pooh_Para_Ti.exe
"""

import os
import subprocess
import sys

def build():
    project_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir(project_dir)
    
    icon_path = os.path.join(project_dir, "assets", "icon.ico")
    assets_dir = os.path.join(project_dir, "assets")
    main_script = os.path.join(project_dir, "main_app.py")
    
    cmd = [
        sys.executable,
        "-m", "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--windowed",
        "--name", "Winnie_Pooh_Para_Ti",
        f"--icon={icon_path}",
        f"--add-data={assets_dir};assets",
        main_script
    ]
    
    print("Compilando ejecutable con PyInstaller...")
    print("Comando:", " ".join(cmd))
    res = subprocess.run(cmd, check=True)
    
    dist_exe = os.path.join(project_dir, "dist", "Winnie_Pooh_Para_Ti.exe")
    if os.path.exists(dist_exe):
        size_mb = os.path.getsize(dist_exe) / (1024 * 1024)
        print(f"\n=======================================================")
        print(f"¡COMPILACIÓN EXITOSA!")
        print(f"Ejecutable generado: {dist_exe}")
        print(f"Tamaño: {size_mb:.2f} MB")
        print(f"=======================================================")
    else:
        print("Error: No se encontró el ejecutable generado en dist/")

if __name__ == "__main__":
    build()
