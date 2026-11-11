"""Train a plant detector on an existing YOLO-format dataset."""
import argparse

from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="Path to the dataset's data.yaml")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=float, default=-1)
    parser.add_argument("--device", default="0", help="CUDA device, e.g. 0; use cpu for a smoke test")
    args = parser.parse_args()

    YOLO(args.model).train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=int(args.batch) if args.batch.is_integer() else args.batch,
        device=args.device,
        project="runs/detect",
        name="plant_id",
    )


if __name__ == "__main__":
    main()
