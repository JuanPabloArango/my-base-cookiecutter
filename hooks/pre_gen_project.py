"""Módulo para realizar validaciones del Cookie Cutter."""

import re
import sys


def validate():
    """Función para hacer unas validaciones previas antes de ejecutar el cookie cutter."""

    repo_name = "{{cookiecutter.repo_name}}"
    project_folder = "{{cookiecutter.project_folder}}"

    if not re.match(r"ci_\d+_[a-z]+", repo_name) or \
       not repo_name.islower() or \
       repo_name.count("-") > 0 or \
       repo_name.count(" ") > 0:
        
        print(f"{repo_name} no se adhiere a la nomenclatura 'ci_000_nombre_repositorio'.")

        sys.exit(1)

    if not re.match(r"[a-z]+_([a-z]+_)*", project_folder) or \
       not project_folder.islower() or \
       project_folder.count("-") > 0 or \
       project_folder.count(" ") > 0:
        
        print(f"{project_folder} no se adhiere a la nomenclatura 'nombre_repositorio'.")

        sys.exit(1)

    sys.exit(0)
