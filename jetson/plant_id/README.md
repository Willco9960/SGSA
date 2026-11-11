# Plant Identification

I'm training YOLO11 to identify herbs for KitchenSprout, starting with mint and basil. I'll train the model on a Windows computer with an RTX 3080 and run it on the Jetson.

## Training

1. Install CUDA-enabled PyTorch using the [PyTorch setup guide](https://pytorch.org/get-started/locally/), then install Ultralytics:

   ```bash
   python -m pip install ultralytics
   ```

2. Download the herb dataset from Teams and extract it. Keep the images, labels, and `data.yaml` together.

3. From this folder, run training with the path to the extracted `data.yaml`:

   ```bash
   python train.py path/to/data.yaml
   ```

The script downloads the pretrained YOLO11n weights on its first run. The trained model is saved as `best.pt` in the training results folder. The dataset and model weights are stored separately from Git.

The current dataset has 12 herb classes, but few mint and basil test images. I plan to add more images before relying on the results.
