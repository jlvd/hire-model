import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import joblib

model= joblib.load('modelo.pkl')

def predict():
    if not(model):
        messagebox.showerror("Error", "Modelo no cargado.")
        return
    try:
        age = int(entry_age.get())
        experience = int(entry_experience.get())
        certifications = int(certifications_var.get())
        gender = gender_var.get()
        education = education_var.get()
        languages = languages_var.get()

        data={
            'Age': [age],
            'Experience': [experience],
            'Certifications': [certifications],
            'Gender_Male': [1 if gender == 'Male' else 0],
            'Education_HighSchool': [1 if education == 'HighSchool' else 0],
            'Education_Master': [1 if education == 'Master' else 0],
            'Languages_English': [1 if languages == 'English' else 0],
            'Languages_French': [1 if languages == 'French' else 0],
        }

        allColumns = ['Age', 'Experience', 'Certifications', 'Gender_Male', 'Education_HighSchool', 'Education_Master', 
                      'Languages_English', 'Languages_French']
        
        print(f"Edad: {age}, Experiencia: {experience}, Género: {gender}, Educación: {education} Languages: {languages}, Certificaciones: {certifications}")
        input_df = pd.DataFrame(data, columns=allColumns)
        for col in allColumns:
            if col not in input_df.columns:
                input_df[col] = 0
        
        #prediction = model.predict(input_df)
        prob = model.predict_proba(input_df)[:,1][0]
        #result = "fue contratado" if prediction[0] == 1 else "no fue contratado"

        if prob >= 0.5:
            pred = "fue contratado"
            icon_type = "info"
        else:
            pred = "no fue contratado"
            icon_type = "warning"
                
        message = f"El candidato {pred} con una probabilidad de {prob*100:.2f}%"
        messagebox.showinfo("Resultado de Predicción", message, icon=icon_type)

        # Guardar el registro de la predicción para análisis posterior
        registro = {
            'Age': age,
            'Experience': experience,
            'gender': gender,
            'education': education,
            'certifications': certifications,
            'Languages': languages,
            'pred': pred,
            'probabilidad': prob
        }
        df_log = pd.DataFrame([registro])
        df_log.to_csv('registro_predicciones.csv', mode='a', header=not pd.io.common.file_exists('registro_predicciones.csv'), index=False)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos para Edad y Experiencia.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")    
    return

app = tk.Tk()
app.title("Modelo de Predicción de Contratación")
app.geometry("400x300")

ttk.Label(app, text="Edad:").grid(row=0, column=0, padx=5, pady=5)
entry_age = ttk.Entry(app)
entry_age.grid(row=0, column=1, padx=5, pady=5) 

ttk.Label(app, text="Experiencia:").grid(row=1, column=0, padx=5, pady=5)
entry_experience = ttk.Entry(app)
entry_experience.grid(row=1, column=1, padx=5, pady=5) 

ttk.Label(app, text="Género:").grid(row=2, column=0, padx=5, pady=5)
gender_var = tk.StringVar(value='Male')
ttk.OptionMenu(app, gender_var, "Male", "Female").grid(row=2, column=1, padx=5, pady=5)

ttk.Label(app, text="Educación:").grid(row=3, column=0, padx=5, pady=5)
education_var = tk.StringVar(value='HighSchool')   
ttk.OptionMenu(app, education_var, "HighSchool", "Bachelor", "Master").grid(row=3, column=1, padx=5, pady=5)

ttk.Label(app, text="Languages:").grid(row=4, column=0, padx=5, pady=5)
languages_var = tk.StringVar(value='HighSchool')   
ttk.OptionMenu(app, languages_var, "English", "French", "Eng. & Fr.").grid(row=4, column=1, padx=5, pady=5)

ttk.Label(app, text="Certifications:").grid(row=5, column=0, padx=5, pady=5)
certifications_var = tk.StringVar(value='HighSchool')   
ttk.OptionMenu(app, certifications_var, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10").grid(row=5, column=1, padx=5, pady=5)



ttk.Button(app, text="Predecir", command=predict).grid(row=6, column=0, columnspan=2, padx=5, pady=10)

app.mainloop()
