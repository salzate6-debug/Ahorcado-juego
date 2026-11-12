import os
from words import obtener_palabra
from display import ETAPAS

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def jugar():
    palabra_oculta = obtener_palabra()
    letras_adivinadas = set()
    letras_usadas = set()
    vidas = 6
    mensaje_error = ""

    while vidas > 0:
        limpiar_pantalla()
        print("=== JUEGO DEL AHORCADO (hangman_1_0) ===")
        print(ETAPAS[6 - vidas])
        print(f"Vidas restantes: {vidas}")

        # Mostrar estado de la palabra oculta
        estado = [letra if letra in letras_adivinadas else "_" for letra in palabra_oculta]
        print("\nPalabra: " + " ".join(estado))
        print(f"Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else 'Ninguna'}")

        if mensaje_error:
            print(f"\n⚠️ {mensaje_error}")
            mensaje_error = ""

        # Verificar si ganó
        if set(palabra_oculta).issubset(letras_adivinadas):
            print("\n🎉 ¡Ganaste! Has adivinado la palabra.")
            break

        # Entrada del usuario
        entrada = input("\nIngrese una letra: ").strip().upper()

        # Validaciones solicitadas en las reglas
        if len(entrada) != 1 or not entrada.isalpha():
            mensaje_error = "Debe ingresar solo 1 letra [A-Z]."
            continue

        if entrada in letras_usadas:
            mensaje_error = f"Ya ha utilizado la letra {entrada}."
            continue

        letras_usadas.add(entrada)

        if entrada in palabra_oculta:
            letras_adivinadas.add(entrada)
        else:
            vidas -= 1

    # Verificar si perdió
    if vidas == 0:
        limpiar_pantalla()
        print("=== JUEGO DEL AHORCADO ===")
        print(ETAPAS[6])
        print("Vidas restantes: 0")
        print("\n❌ ¡Ha perdido!")
        print(f"La palabra oculta era: {palabra_oculta}")

def main():
    while True:
        jugar()
        print("\n" + "="*35)
        opcion = input("¿Desea jugar de nuevo? (S/N): ").strip().upper()
        if opcion != 'S':
            print("¡Gracias por jugar! Finalizando programa.")
            break

if __name__ == "__main__":
    main()