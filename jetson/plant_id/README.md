# KitchenSprout plant identification

Fine-tune a YOLO detector on a labeled mint and basil dataset, then run the resulting model on the Jetson. Training can happen on a separate NVIDIA GPU computer.

## 1. Get the code

On the RTX 3080 computer, install Git and Python 3.10 or 3.11, then open a terminal:

```bash
git clone https://github.com/Willco9960/SGSA.git
cd SGSA
git switch plant-id-training-setup
cd jetson/plant_id
```

If you already cloned the repository, fetch the branch first with `git fetch origin`. If these changes have been merged to main, use `git switch main` and `git pull` instead.

## 2. Set up Python and the GPU

Create an environment with `python -m venv .venv`, then activate it:

- Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
- Linux: `source .venv/bin/activate`

Install a CUDA-enabled PyTorch build using the official selector at https://pytorch.org/get-started/locally/ (choose the OS and supported CUDA version). Then:

```bash
python -m pip install ultralytics
python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'not detected')"
```

Confirm the output identifies the 3080 before training. A working NVIDIA driver is required. The Jetson needs its own JetPack-compatible setup; do not reuse desktop CUDA install instructions there.

## 3. Prepare a dataset

Export a labeled object-detection dataset in Ultralytics YOLO format. It needs mint and basil boxes, training and validation splits, and a `data.yaml`; use a held-out test split for final evaluation. Inspect labels and class names before training. Keep photos of the same plants or capture sessions together in one split to limit leakage. The dataset is not included and the code does not download one.

Example layout:
```
datasets/herbs/
  data.yaml
  train/images/  train/labels/
  valid/images/  valid/labels/
  test/images/   test/labels/
```

Use the dataset's own YAML paths and class IDs; don't relabel classes by editing names alone. The local `datasets/` directory, model weights, and training results are ignored by Git. Transfer the dataset separately to the training machine and check its license before use.

## 4. Train on the 3080

Replace the example path with your dataset's actual YAML path:

```bash
python train.py datasets/herbs/data.yaml
```

The first run downloads the pretrained `yolo11n.pt` model. Defaults are 100 epochs, image size 640, automatic batch sizing, and CUDA device 0. Example options:

```bash
python train.py datasets/herbs/data.yaml --model yolo11s.pt --epochs 100 --imgsz 640
```

Training prints the output path. Typically the best weights are `runs/detect/plant_id/weights/best.pt`; subsequent runs may have numbered folders.

## 5. Evaluate and transfer

Use the held-out test split if the YAML defines it:

```bash
yolo detect val model=runs/detect/plant_id/weights/best.pt data=datasets/herbs/data.yaml split=test
```

Review mint and basil results separately, including misses and mix-ups, and test new images captured from the intended camera angle. Copy the chosen `best.pt` to the Jetson separately; it is ignored by Git. If you need faster Jetson inference, consider exporting to TensorRT on the target after the PyTorch model works.
