# KitchenSprout

KitchenSprout is a smart countertop growing system developed as a senior design project. This repository organizes the software for its proof of concept (PoC).

## Proof-of-concept objectives

1. Identify two plant species live using a camera connected to an NVIDIA Jetson Orin Nano.
2. Read physical sensors with an STM32 Nucleo L4RG and reliably communicate their measurements to the Jetson.
3. Produce a rough preliminary enclosure mockup.

## Repository structure

```text
SCSG/
├── README.md
├── .gitignore
├── jetson/
│   ├── plant_id/
│   └── sensor_receiver/
└── stm32/
    └── sensor_transmitter/
```

- `jetson/plant_id/`: camera capture, plant identification inference, and predicted plant output.
- `jetson/sensor_receiver/`: serial reception, sensor measurement parsing and display, and basic communication logging.
- `stm32/sensor_transmitter/`: STM32CubeIDE firmware project for sensor readings and serial transmission.

Engineering documents and CAD files are stored separately in Microsoft Teams. The software directories are starting points; implementation will be added as the PoC is developed.
