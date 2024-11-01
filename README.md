<div align="center">

# FusionBench Project Template


[![python](https://img.shields.io/badge/-Python_3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_2.0+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra-89b8cd)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

FusionBench is a PyTorch-based comprehensive benchmark/toolkit for deep model fusion. This repository serves as a template for creating new projects based on FusionBench. It includes all the necessary configurations and boilerplate code to get started quickly.

Click on [<kbd>Use this template</kbd>](https://github.com/fusion-bench/fusion-bench-project-template/generate) to initialize new repository.

</div>

## Project Structure

The directory structure of new project looks like this:

```plaintext
├── .github                   <- Github Actions workflows
├── .vscode                   <- VSCode settings
├── config                    <- Hydra configs
│   ├── hydra                    <- Hydra configs
│   ├── fabric                   <- Fabric configs
│   ├── fabric_logger            <- Fabric logger configs
│   ├── method                   <- Method configs
│   ├── modelpool                <- Model pool configs
│   ├── taskpool                 <- Task pool configs
│   │
│   └── main.yaml            <- Main config for training
│
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials, and a short `-` delimited description,
│                             e.g. `1.0-jqp-initial-data-exploration.ipynb`.
│
├── scripts                <- Shell scripts
│
├── src                    <- Source code
│   ├── data                     <- Data classes
│   ├── models                   <- Model classes
│   ├── method                   <- Method classes
│   ├── modelpool                <- Model pool classes
|   ├── taskpool                 <- Task pool classes
│   └── utils                    <- Utility functions
|
├── tests                  <- Tests of any kind
│
├── .gitignore                <- List of files ignored by git
├── requirements.txt          <- File for installing python dependencies
├── setup.py                  <- File for installing project as a package
└── README.md
```
