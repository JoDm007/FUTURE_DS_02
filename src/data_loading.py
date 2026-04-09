import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def load_data(input_path: str) -> pd.DataFrame:
    """Charge les données depuis un fichier CSV."""
    input_path = Path(input_path)
    if not input_path.exists():
        logger.error(f"❌ Fichier non trouvé : {input_path}")
        raise FileNotFoundError(f"{input_path} n'existe pas")
    logger.info(f"|==> Chargement des données depuis {input_path}")
    return pd.read_csv(input_path)