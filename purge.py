import os
import sys
import subprocess

def uninstall_all_packages():
    """Desinstala todos os pacotes Python instalados."""    
    print("Iniciando a desinstalação de todos os pacotes...")
    """Desinstala todos os pacotes Python instalados."""
    try:
        installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Erro ao listar pacotes instalados: {e}")
        return
    
    for package in installed_packages:
        if package:
            package_name = package.split('==')[0]
            try:
                subprocess.call([sys.executable, '-m', 'pip', 'uninstall', package_name, '-y'])
                print(f"Pacote {package_name} desinstalado com sucesso.")
            except Exception as e:
                print(f"Erro ao desinstalar o pacote {package_name}: {e}")

def clear_pip_cache():
    """Limpa o cache do pip."""
    try:
        subprocess.call([sys.executable, '-m', 'pip', 'cache', 'purge'])
        print("Cache do pip limpo com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar o cache do pip: {e}")

if __name__ == "__main__":
    uninstall_all_packages()
    clear_pip_cache()
    print("Todos os pacotes desinstalados e cache limpo.")
