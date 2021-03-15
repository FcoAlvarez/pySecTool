import os

# Probar -H para buscar el PID del programa
# Probar -s para mostrar el arbol de un ProcessLookupError
# -p para mostrar le PID
p = os.popen('pstree -p')
print(p.read())