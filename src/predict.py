from pathlib import Path
from ultralytics import YOLO


def main():
    """Genera detecciones usando el modelo entrenado."""
    model_path = Path("models/best.pt")

    if not model_path.exists():
        raise FileNotFoundError(
            "No se encontró models/best.pt. "
            "Copia ahí el best.pt generado después del entrenamiento."
        )

    model = YOLO(str(model_path))

    results = model.predict(
        source="test/images",
        conf=0.25,
        save=True,
        project="evidencias",
        name="detecciones",
        exist_ok=True
    )

    print("Predicción terminada.")
    print("Las imágenes con bounding boxes quedan en evidencias/detecciones")
    return results


if __name__ == "__main__":
    main()
