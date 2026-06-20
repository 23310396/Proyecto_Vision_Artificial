# Sistema YOLOv8 para detección de logotipos automotrices

**IMPORTANTE: LAS EVIDENCIAS DEL MODELO ESTÁN EN `runs/detect/ -> evidencias/detecciones/`, CON IMÁGENES PROCESADAS Y BOUNDING BOXES GENERADOS POR YOLOv8.**

## Descripción general

Este proyecto utiliza visión artificial con YOLOv8 para detectar logotipos de marcas automotrices en imágenes de vehículos.

El dataset original tenía 36 clases, pero varias marcas tenían muy pocas imágenes. Para mejorar la calidad del entrenamiento, se generó una versión limpia conservando únicamente las clases con al menos 10 anotaciones.

## Integrantes

- Saulo Jaziel Tejeda Valle
- Integrante 2: agregar nombre aquí

## Estructura del repositorio

```text
Proyecto_YOLO_Logos_Automotrices/
├── README.md
├── requirements.txt
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
├── src/
│   ├── train.py
│   ├── predict.py
│   └── check_dataset.py
├── models/
├── evidencias/
└── docs/
    ├── CLASES_FINALES.md
    └── CLASES_ELIMINADAS.md
```

## Dataset limpio

Resumen del dataset final:

| Split | Imágenes | Labels | Anotaciones |
|---|---:|---:|---:|
| Train | 344 | 344 | 344 |
| Valid | 41 | 41 | 41 |
| Test | 42 | 42 | 42 |
| Total | 427 | 427 | 427 |

Clases finales: 15

| ID | Marca | Anotaciones |
|---:|---|---:|
| 0 | audi | 15 |
| 1 | chevrolet | 14 |
| 2 | citroen | 17 |
| 3 | dacia | 20 |
| 4 | ford | 16 |
| 5 | hyundai | 24 |
| 6 | mercedes | 10 |
| 7 | nissan | 14 |
| 8 | peugeot | 63 |
| 9 | renault | 90 |
| 10 | seat | 24 |
| 11 | skoda | 16 |
| 12 | suzuki | 32 |
| 13 | toyota | 10 |
| 14 | volkswagen | 62 |


## Instalación

Se recomienda usar un entorno virtual de Python.

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Verificar el dataset

```bash
python src/check_dataset.py
```

Este comando muestra el conteo de clases por cada división del dataset.

## Entrenar el modelo

```bash
python src/train.py
```

El entrenamiento usa `yolov8n.pt` como modelo base. Al terminar, YOLO genera una carpeta dentro de `runs/train/` con los resultados y pesos entrenados.

El archivo más importante es:

```text
runs/train/logos_automotrices_yolov8/weights/best.pt
```

## Probar el modelo

Primero copia el archivo `best.pt` a la carpeta `models/`:

```text
models/best.pt
```

Después ejecuta:

```bash
python src/predict.py
```

Las imágenes con bounding boxes se guardarán en:

```text
evidencias/detecciones/
```

## Caso de estudio industrial

### Problema a resolver

En talleres, estacionamientos inteligentes, agencias automotrices o zonas de inspección vehicular, puede ser necesario identificar la marca de un vehículo de forma automática. Hacerlo manualmente consume tiempo y depende del operador.

Este sistema propone usar visión artificial para detectar el logotipo automotriz y clasificar la marca del vehículo mediante YOLOv8.

### Hardware propuesto

- Cámara industrial colocada frente al vehículo.
- Iluminación LED para reducir sombras y reflejos.
- Computadora industrial o tarjeta NVIDIA Jetson para ejecutar el modelo.
- PLC o controlador industrial para recibir la decisión del sistema.
- Base de datos para registrar marca, fecha, hora e imagen capturada.
- Semáforo industrial, barrera automática o actuador, según la aplicación.

### Flujo de funcionamiento

1. El vehículo llega a la zona de inspección.
2. Un sensor detecta presencia y activa la captura de imagen.
3. La cámara toma una fotografía frontal o trasera del vehículo.
4. La imagen se envía al procesador donde corre YOLOv8.
5. El modelo detecta el logotipo y calcula la confianza de la predicción.
6. Si la confianza es aceptable, el sistema registra la marca detectada.
7. Si la confianza es baja, el vehículo se manda a revisión manual.
8. El PLC puede activar una barrera, semáforo, alarma o ruta de clasificación.

### Aplicación real propuesta

Un estacionamiento inteligente puede usar este sistema para registrar automáticamente la marca de los vehículos que entran. También puede servir en una agencia automotriz para clasificar unidades por marca o en un taller para validar que el vehículo atendido coincida con el registro de servicio.

## Notas de limpieza del dataset

- El dataset original tenía 36 clases.
- Se conservaron 15 clases.
- Se eliminaron las marcas con menos de 10 anotaciones.
- La clase original `cheverolet` fue corregida a `chevrolet`.
- Las etiquetas fueron reindexadas desde cero para mantener compatibilidad con YOLOv8.

Consulta también:

- `docs/CLASES_FINALES.md`
- `docs/CLASES_ELIMINADAS.md`
