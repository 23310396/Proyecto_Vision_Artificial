from ultralytics import YOLO


def main():
    """Entrena un modelo YOLOv8 con el dataset limpio de logotipos automotrices."""
    model = YOLO("yolov8n.pt")

    results = model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        name="logos_automotrices_yolov8",
        project="runs/train"
    )

    print("Entrenamiento terminado.")
    print("Revisa la carpeta runs/train/logos_automotrices_yolov8")
    return results


if __name__ == "__main__":
    main()
