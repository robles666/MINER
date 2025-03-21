import hashlib # Importamos la librería hashlib

def mine(block_number, transactions, previous_hash, difficulty): # Definimos la función mine
    nonce = 0 # Inicializamos el nonce en 0
    # Mientras sea verdadero
    while True:
        data = f"{block_number}{transactions}{previous_hash}{nonce}" # Concatenamos los datos
        # Calculamos el hash de los datos concatenados y lo convertimos a hexadecimal
        hash_result = hashlib.sha256(data.encode()).hexdigest() # Calculamos el hash de los datos concatenados
        # Si el hash resultante empieza con el número de ceros indicado por la dificultad
        if hash_result.startswith('0' * difficulty): # Si el hash resultante empieza con el número de ceros indicado por la dificultad
            # Imprimimos el nonce encontrado, el hash resultante y retornamos el nonce y el hash resultante
            print(f"Nonce encontrado: {nonce}") # Imprimimos el nonce encontrado
            print(f"Hash: {hash_result}") # Imprimimos el hash resultante
            return nonce, hash_result # Retornamos el nonce y el hash resultante
        nonce += 1 # Incrementamos el nonce

# Ejemplo de uso
block_number = 1
transactions = "Alice->Bob->100BTC"
previous_hash = "00000000000000000000000000000000"
difficulty = 4  # Número de ceros al inicio del hash

block_number = 12 # Número de bloque
transactions = "Alice->Bob->100BTC" # Transacciones
previous_hash = "00000000000000010000000000000000" # Hash del bloque anterior
difficulty = 4  # Número de ceros al inicio del hash

mine(block_number, transactions, previous_hash, difficulty) # Llamada a la función