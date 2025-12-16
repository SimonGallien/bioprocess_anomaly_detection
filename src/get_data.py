import kagglehub
import shutil
from pathlib import Path
import glob
import os

def download_data():

    """Télécharge le dataset depuis KaggleHub et copie les CSV dans data/"""

    # Télécharge depuis Kaggle (va dans le cache)
    path = kagglehub.dataset_download("stephengoldie/big-databiopharmaceutical-manufacturing")
    print(f"✅ Données téléchargées dans le cache : {path}")

    csv_files = glob.glob(pathname=f"{path}/**/*.csv", recursive=True)
    if not csv_files:
        print("⚠️ Aucun fichier CSV trouvé dans le dataset.")
        return

    print(f"🎯 {len(csv_files)} fichiers CSV trouvés. Copie en cours...")
    # Dossier data/ à la racine du projet
    project_root = Path(__file__).resolve().parent.parent
    data_dir = os.path.join(project_root, "data")
    os.makedirs(data_dir, exist_ok=True)

    for csv_file in csv_files:
        name = os.path.basename(csv_file)
        destination = os.path.join(data_dir, name)
        shutil.copy2(csv_file, destination)
        print(f"   └─ 📁 Copié : {name}")

    print("\n🎉 Initialisation terminée ! Les données sont dans :", data_dir)

if __name__ == "__main__":
    download_data()
