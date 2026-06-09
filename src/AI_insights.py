
# src/ai_insights.py

from config import LLM_MODEL, LLM_TEMPERATURE
import json

# Se estiver usando OpenAI (ou similar)
from openai import OpenAI

client = OpenAI()


def generate_ai_insights(kpis: dict) -> str:
    """
    Gera insights de growth baseados em KPIs do Méliuz.
    """

    prompt = f"""
Você é um analista de Growth de uma fintech de cashback (Méliuz).

Analise os dados abaixo e gere insights objetivos e acionáveis:

KPIs:
{json.dumps(kpis, indent=2)}

Responda com:
1. Principais padrões observados
2. Oportunidades de otimização
3. Possíveis hipóteses para testes A/B

Seja direto, focado em negócio e evite explicações longas.
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        temperature=LLM_TEMPERATURE,
        messages=[
            {"role": "system", "content": "Você é um analista de Growth altamente objetivo."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content