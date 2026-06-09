import os

# Caminhos dos dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "dataset")

DATASET_FILES = {
    "dataset01": os.path.join(DATA_PATH, "dataset01_parcerioA.csv"),
    "dataset02": os.path.join(DATA_PATH, "dataset02_parcerioB.csv"),
    'dataset03': os.path.join(DATA_PATH, "dataset03_parcerioC.csv"),
}


# Configuração da IA
LLM_MODEL = "gpt-4o-mini"
LLM_TEMPERATURE = 0.2

# Regras de negócio
DEFAULT_CASHBACK_LIMIT = 0.10
MIN_COMMISSION = 0.0

# Configurações do dashboard
APP_TITLE = "Dashboard Méliuz - Growth Analysis"
APP_LAYOUT = "wide"

# UI
PRIMARY_COLOR = "#2E86C1"

# Debug
DEBUG_MODE = True

print(f"Configurações carregadas: {DATASET_FILES}, LLM_MODEL={LLM_MODEL}, DEBUG_MODE={DEBUG_MODE}")
