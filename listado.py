import os
import django
import fitz
import datetime

# 1. Le dices a Python dónde está tu archivo settings.py (cambia 'tuproyecto' por el nombre de tu carpeta de configuración)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TRAZABILIDAD_ESTERILIZACION.settings')

# 2. Inicializas Django para que cargue todo el entorno
django.setup()


from django.conf import settings

DIRECTORIO = settings.MEDIA_ROOT
print(DIRECTORIO)
registrosi=os.listdir(DIRECTORIO)  ## Lista todos los archivos en la carpeta
print(registrosi)
registros_validos = []             ## Lista para almacenar diccionarios {'pdf': nombre de archivo, 'nombre': nombre de archivo sin extension, 'fecha': fecha de creacion de archivo}
    
for archivo in registrosi:
    if archivo.lower().endswith(".pdf"):
        ruta_completa = os.path.join(DIRECTORIO, archivo)
        try:
            doc = fitz.open(ruta_completa)
            metadata = doc.metadata
            # Use current time as fallback if creationDate is missing or malformed
            try:
                fecha_raw = metadata.get('creationDate', '')
                if fecha_raw and len(fecha_raw) >= 16:
                    fecha = datetime.datetime.strptime(fecha_raw[2:16], "%Y%m%d%H%M%S")
                else:
                    fecha = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_completa))
            except Exception:
                fecha = datetime.datetime.fromtimestamp(os.path.getmtime(ruta_completa))
            
            registros_validos.append({
                'pdf': archivo,
                'nombre': archivo[:-4],
                'fecha': fecha
            })
            doc.close()
        except Exception as e:
            print(f"Error procesando {archivo}: {e}")

# Sort by date descending
            
print(registros_validos)
registros_validos.sort(key=lambda x: x['fecha'], reverse=True)

# Re-structure for the template (it expects a zip of 3 elements)
# Actually, it's easier to change the template to use the dict list, 
# but to maintain compatibility without major template changes:
registros_fechas = [ (r['pdf'], r['nombre'], r['fecha']) for r in registros_validos ]

print(registros_fechas)

#    return render(request, "examinar/examinar.html", {'registros_fechas': registros_fechas})

