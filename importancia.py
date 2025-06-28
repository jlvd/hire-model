import joblib
import matplotlib.pyplot as plt

# Cargar modelo y columnas
model = joblib.load('modelo.pkl')
feature_names = joblib.load('columnas.pkl')

# Obtener importancias de características
importances = model.feature_importances_


# Ordenar
sorted_indices = importances.argsort()[::-1]
sorted_features = [feature_names[i] for i in sorted_indices]
sorted_importances = importances[sorted_indices]

# Mostrar top características
print("Top características más influyentes en la contratación (>50%):")
for i in range(len(sorted_features)):
    print(f"{sorted_features[i]}: {sorted_importances[i]:.4f}")

# Gráfico
plt.figure(figsize=(10, 6))
plt.bar(range(len(sorted_importances)), sorted_importances, align='center', color='skyblue')
plt.xticks(range(len(sorted_importances)), sorted_features, rotation=45, ha='right')
plt.title("Importancia de Características en el Modelo de Contratación")
plt.ylabel("Importancia relativa")
plt.tight_layout()
plt.show()
