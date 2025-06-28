import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

#Constantes para Calculo y cantidad de datos
RANDOM_STATE = 50
n = 5000

np.random.seed(RANDOM_STATE)
data = {
    "Gender": np.random.choice(['Male', 'Female'], n, p=[0.7, 0.3]),
    "Age": np.random.randint(21, 50, n),
    'Education': np.random.choice(['HighSchool', 'Bachelor', 'Master'], n, p=[0.5, 0.3, 0.2]),
    'Experience': np.random.randint(0, 20, n),
    "Languages": np.random.choice(['English', 'French', 'Both'], n, p=[0.5, 0.35, 0.15]),
    "Certifications": np.random.randint(0, 10, n),
    'Hired': np.random.choice([0, 1], n, p=[0.6, 0.4])
}
df = pd.DataFrame(data)
#print(df.head())

df_encoded = pd.get_dummies(df, columns=['Gender', 'Education', 'Languages'], drop_first=True)
print("Datos codificados:")
print(df_encoded.head())

X = df_encoded.drop('Hired', axis=1)
y = df_encoded['Hired']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE)
model = RandomForestClassifier(random_state=RANDOM_STATE)
model.fit(X_train, y_train)

#Agrego las columnas al modelo
joblib.dump(X.columns.tolist(), 'columnas.pkl')

print("Modelo entrenado y guardado como 'modelo.pkl'")

y_pred = model.predict(X_test)

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['No Hired', 'Hired']))

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Métricas específicas
precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average=None)

plt.figure(figsize=(8,5))
labels = ['No Hired', 'Hired']
x = range(len(labels))
plt.bar(x, precision, width=0.25, label='Precision', align='center')
plt.bar(x, recall, width=0.25, label='Recall', align='edge')
plt.bar(x, f1, width=0.25, label='F1-Score', align='edge', alpha=0.7)
plt.xticks(x, labels)
plt.title('Precision, Recall y F1-Score por clase')
plt.legend()
plt.show()

