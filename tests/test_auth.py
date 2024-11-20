# tests/test_auth.py
from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

def test_auth():
    print("🔄 Probando autenticación con Hugging Face...")
    
    # Cargar token
    load_dotenv()
    token = os.getenv("HUGGINGFACE_TOKEN")
    
    if not token:
        print("❌ No se encontró HUGGINGFACE_TOKEN en .env")
        return False
        
    try:
        # Crear cliente API
        api = HfApi(token=token)
        
        # Probar autenticación
        user = api.whoami()
        print(f"\n✅ Autenticación exitosa!")
        print(f"Usuario: {user['name']}")
        print(f"Email: {user['email']}")
        
        # Listar modelos disponibles
        print("\n📚 Buscando modelos MLX disponibles...")
        models = api.list_models(author="mlx-community", search="Mistral")
        
        print("\nModelos encontrados:")
        for model in models:
            print(f"- {model.modelId}")
            
        return True
        
    except Exception as e:
        print(f"\n❌ Error durante la autenticación: {str(e)}")
        return False

if __name__ == "__main__":
    test_auth()