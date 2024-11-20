# tests/test_mlx_model.py
from mlx_lm import load, generate
from transformers import AutoTokenizer
import mlx.core as mx
from pathlib import Path
import time
from dotenv import load_dotenv
import os

def test_complete_generation():
    print("🚀 Iniciando prueba de Mistral con MLX-LM...")
    
    start_time = time.time()
    
    try:
        model_id = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"
        
        print("\n🔄 Cargando modelo y tokenizer...")
        model, tokenizer = load(model_id)
        print("✅ Modelo cargado exitosamente")
        
        # Preparar prompt
        prompt = """<s>[INST] Actúa como un historiador y responde en español:
        ¿Quién fue Julio César? Responde en dos oraciones. [/INST]"""
        
        print("\n📝 Generando respuesta para prompt:", prompt)
        
        # Generar respuesta
        response = generate(
            model,
            tokenizer,
            prompt=prompt,
            max_tokens=100,
            temp=0.7
        )
        
        print("\n✨ Respuesta generada:")
        print(response)
        
        print(f"\n⏱️ Tiempo total: {time.time() - start_time:.2f}s")
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_complete_generation()