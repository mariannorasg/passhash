# passhash 

Herramienta simple en Python para hashear y verificar contraseñas usando PBKDF2-HMAC con SHA-256.  
No requiere librerías externas (usa solo la biblioteca estándar de Python).

---

## Uso

### Generar un hash
```bash
python passhash.py hash
```
### Verificar un hash
```
python passhash.py verify
```

# Por qué hashear contraseñas y no encriptarlas ?

Hash ≠ cifrado: el hash es unidireccional (es decir que no se puede revertir). En autenticación no necesitás recuperar la contraseña del usuario; solo comprobar si coincide.

Menor impacto ante fugas: si un atacante roba tu base de datos, encontrará hashes, lo que hace mucho más costoso adivinar contraseñas por fuerza bruta, la cantidad de iteraciones es absurda para descifrar los hashes.

Estándar de la industria: PBKDF2-HMAC (SHA-256) es aceptado, interoperable y está disponible en la biblioteca estándar de Python.

# Cómo funciona ? Explicado simple

PBKDF2-HMAC: algoritmo que toma una contraseña y la “estira” aplicando muchas iteraciones de SHA-256 combinadas con HMAC para resistir intentos masivos de adivinación.

Salt: bytes aleatorios únicos por contraseña. Evita rainbow tables y que dos usuarios con la misma contraseña tengan el mismo hash.

Iteraciones: aumentan el costo computacional por intento. Cuantas más, más caro es para un atacante.

compare_digest: comparación en tiempo constante (evita filtrar información por diferencias de tiempo de ejecución).
