# tests/test_interactive_memory.py
from mlx_lm import load, generate
import mlx.core as mx
import time
from typing import List, Tuple

class RomanHistoryBot:
    def __init__(self, memory_limit: int = 3):
        self.model = None
        self.tokenizer = None
        self.model_id = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"
        self.conversation_history: List[Tuple[str, str]] = []
        self.memory_limit = memory_limit
    
    def load_model(self):
        if self.model is None:
            print("🔄 Cargando modelo y tokenizer (esto puede tomar un minuto)...")
            load_start = time.time()
            self.model, self.tokenizer = load(self.model_id)
            print(f"✅ Modelo cargado en {time.time() - load_start:.2f}s")
    
    def generate_response(self, question: str, temp: float = 0.7):
        if self.model is None:
            self.load_model()
        
        # Prompt más específico y restrictivo
        prompt = f"""<s>[INST] Sistema: Eres un historiador experto del Imperio Romano. 
        Responde directamente a la pregunta sin saludos ni formalidades.
        Mantén un tono académico y profesional.
        
        Contexto previo: {self._format_history() if self.conversation_history else 'Ninguno'}
        
        Pregunta: {question}
        [/INST]"""
        
        gen_start = time.time()
        response = generate(
            self.model,
            self.tokenizer,
            prompt=prompt,
            temp=temp,
            max_tokens=500
        )
        gen_time = time.time() - gen_start
        
        self.conversation_history.append((question, response))
        return response, gen_time
    
    def show_history(self):
        if not self.conversation_history:
            print("\n📝 No hay historial de conversación.")
            return
            
        print("\n📝 Historial de la conversación:")
        for i, (q, a) in enumerate(self.conversation_history, 1):
            print(f"\n=== Interacción {i} ===")
            print(f"👤 Pregunta: {q}")
            print(f"🤖 Respuesta: {a}")
            print("=" * 50)

    def _format_history(self) -> str:
        """Formatea el historial de conversación de manera concisa"""
        if not self.conversation_history:
            return ""
        
        history = []
        for q, a in self.conversation_history[-self.memory_limit:]:
            history.append(f"P: {q}\nR: {a}")
    
        return "\n".join(history)

    
def interactive_session():
    print("🏛️ Bot de Historia Romana - Sesión Interactiva")
    print("=" * 50)
    print("Comandos disponibles:")
    print("- 'historia': muestra el historial de la conversación")
    print("- 'creativo': aumenta la creatividad de las respuestas")
    print("- 'preciso': hace las respuestas más precisas")
    print("- 'salir': termina la sesión")
    print("=" * 50)
    
    bot = RomanHistoryBot(memory_limit=3)
    temperature = 0.7  # Temperatura por defecto
    
    while True:
        try:
            question = input("\n👤 Tu pregunta: ").strip().lower()
            
            if question == 'salir':
                print("\n¡Vale! ¡Hasta luego!")
                break
                
            if question == 'historia':
                bot.show_history()
                continue
                
            if question == 'creativo':
                temperature = min(temperature + 0.1, 1.0)
                print(f"\n🎨 Aumentando creatividad (temperatura: {temperature:.1f})")
                continue
                
            if question == 'preciso':
                temperature = max(temperature - 0.1, 0.1)
                print(f"\n🎯 Aumentando precisión (temperatura: {temperature:.1f})")
                continue
            
            if not question:
                print("Por favor, escribe una pregunta.")
                continue
            
            print("\n🤖 Generando respuesta...")
            response, gen_time = bot.generate_response(question, temp=temperature)
            
            print("\n✨ Respuesta:")
            print(response)
            print(f"\n⏱️ Tiempo de generación: {gen_time:.2f}s")
            print(f"🎨 Temperatura actual: {temperature:.1f}")
            print(f"📚 Conversaciones en memoria: {len(bot.conversation_history)}")
            
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    interactive_session()