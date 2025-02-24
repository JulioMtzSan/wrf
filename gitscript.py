import os
from git import Repo, GitCommandError

# Obtén tus credenciales desde las variables de entorno
token = os.environ.get('GITHUB_TOKEN')
username = "JulioMtzSan"
remote_url = f"https://{username}:{token}@github.com/{username}/wrf.git"

repo_path = "/home/sig07/website_nuevo"  # Ajusta la ruta a tu repositorio

try:
    # Inicializa (o abre) el repositorio
    repo = Repo(repo_path)
    
    # Asegúrate de estar en la rama main
    if 'main' not in repo.heads:
        repo.git.checkout('-b', 'main')
    else:
        repo.git.checkout('main')
    
    # Agrega todos los archivos y haz commit
    repo.git.add(A=True)
    repo.index.commit("Agregar WRF")
    
    # Configura el remoto
    try:
        repo.create_remote('origin', remote_url)
    except GitCommandError:
        repo.git.remote('set-url', 'origin', remote_url)
    
    # Realiza un push forzado
    repo.git.push('--force', '-u', 'origin', 'main')
    print("Push realizado correctamente.")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")

