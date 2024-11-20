import mlx.core as mx

def test_mlx():
    print("🔄 Probando MLX en tu Mac M3...")
    
    try:
        # Crear algunos tensores simples
        x = mx.array([[1, 2, 3], [4, 5, 6]])
        y = mx.array([[7, 8, 9], [10, 11, 12]])
        
        # Realizar algunas operaciones
        z = mx.add(x, y)
        
        print("\n✅ MLX está funcionando correctamente!")
        print("\nPrueba simple:")
        print(f"x = \n{x}")
        print(f"y = \n{y}")
        print(f"x + y = \n{z}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    test_mlx()