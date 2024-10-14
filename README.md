# mtfjet

[![Actions Status][actions-badge]][actions-link]
[![PyPI version][pypi-version]][pypi-link]
[![PyPI platforms][pypi-platforms]][pypi-link]


# MTFJet

**MTFJet** is a lightweight and powerful tool designed to calculate the Modulation Transfer Function (MTF) for neutron imaging stacks (TIFF) as a function of Time-of-Flight (TOF) neutron energy. With support for both ImageJ/Fiji scripts and a Python API, MTFJet makes it easy to analyze the sharpness and resolution of neutron images in both experimental and simulation environments.

## Why "MTFJet"?

The name **MTFJet** is all about speed, precision, and power! Just like a jet engine, it propels your MTF analysis to new heights—fast and sharp. "MTF" stands for **Modulation Transfer Function**, and "Jet" captures the boost we aim to give your neutron image analysis. It's short, fun, and packs a punch, just like the tool itself.

## Features

- **MTF Calculation**: Extract and compute the MTF from neutron image stacks to evaluate image sharpness and system resolution.
- **TOF Energy Support**: Analyze MTF as a function of Time-of-Flight neutron energy for a comprehensive view of system performance.
- **ImageJ/Fiji Script**: Easily integrate with ImageJ or Fiji workflows using the included script.
- **Python API**: Take advantage of a flexible and easy-to-use Python API for advanced automation and integration into larger pipelines.
- **Neutron Imaging Compatibility**: Optimized for working with neutron image TIFF stacks from neutron detectors.

## Installation

```bash
python -m pip install mtfjet
```

From source:
```bash
git clone https://github.com/TsvikiHirsh/mtfjet
cd mtfjet
python -m pip install .
```

### ImageJ/Fiji Script

1. Download the `MTFJet.ijm` script from the repository.
2. Place it in the `macros` folder of your ImageJ/Fiji installation.
3. Run the script from the ImageJ/Fiji GUI.

## Usage

### Python API

```python
import mtfjet

# Example: Load a TIFF stack and calculate MTF
stack = mtfjet.load_tiff_stack("path/to/stack.tiff")
mtf_results = mtfjet.calculate_mtf(stack, tof_data="path/to/tof_data.txt")

# Analyze MTF as a function of TOF neutron energy
mtfjet.plot_mtf_vs_energy(mtf_results)
```

### ImageJ/Fiji Script

1. Open your neutron image stack in ImageJ/Fiji.
2. Run the MTFJet macro from the `Plugins` > `Macros` menu.
3. Follow the prompts to input your TOF data and calculate the MTF.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to contribute.

## License

Distributed under the terms of the [MIT license](LICENSE).


<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/TsvikiHirsh/mtfjet/workflows/CI/badge.svg
[actions-link]:             https://github.com/TsvikiHirsh/mtfjet/actions
[pypi-link]:                https://pypi.org/project/mtfjet/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/mtfjet
[pypi-version]:             https://img.shields.io/pypi/v/mtfjet
<!-- prettier-ignore-end -->
