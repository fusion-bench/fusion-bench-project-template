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

## Introduction

FusionBench Project Template is designed to help researchers and developers quickly set up a new project for deep model fusion using PyTorch and FusionBench. This template provides a well-organized project structure, pre-configured settings, and essential tools to streamline the development process. Key features include:

- **Hydra Configuration**: Simplifies the management of complex configurations.
- **PyTorch Lightning**: Facilitates the training and evaluation of models.
- **Pre-configured Linters**: Ensures code quality with tools like Black and isort.
- **Jupyter Notebooks**: Supports interactive development and experimentation.
- **Modular Design**: Encourages clean and maintainable code with a clear separation of concerns.

By using this template, you can focus on developing and experimenting with your fusion models without worrying about the initial setup and configuration.

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
├── notebooks              <- Jupyter notebooks. Here you can place 
|                             some example code and notebooks.
|
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


## The FusionBench Workflow

FusionBench follows a three-component architecture to perform model fusion experiments:

```mermaid
graph LR
    CLI[fusion_bench CLI] --> Hydra[Hydra Config]
    Hydra --> Program[Program]
    
    Program --> MP[ModelPool<br/>Manages Models<br/>& Datasets]
    Program --> Method[Method<br/>Fusion Algorithm]
    Program --> TP[TaskPool<br/>Evaluation Tasks]
    
    MP --> Method
    Method --> Merged[Merged Model]
    Merged --> TP
    TP --> Report[Evaluation Report]
    
    style CLI fill:#e1f5e1
    style Hydra fill:#f0e1ff
    style Method fill:#ffe1f0
    style Merged fill:#fff4e1
    style Report fill:#e1f0ff
```

**Key Components:**

1. **CLI**: Entry point using Hydra for configuration management
2. **Program**: Orchestrates the fusion workflow (e.g., `FabricModelFusionProgram`)
3. **ModelPool**: Manages task-specific models and their datasets
4. **Method**: Implements the fusion algorithm (e.g., Simple Average, Task Arithmetic, AdaMerging)
5. **TaskPool**: Evaluates the merged model on benchmark tasks

**Workflow Steps:**

1. User runs `fusion_bench` with config overrides
2. Hydra loads YAML configs for method, modelpool, and taskpool
3. Program instantiates all three components
4. Method executes fusion algorithm on ModelPool
5. TaskPool evaluates the merged model
6. Results are saved and reported

## Acknowledgement

This template is motivated by [Lightning-Hydra-Template](https://github.com/ashleve/lightning-hydra-template).

<br/>
<br/>
<br/>


> [!NOTE]
> **DELETE EVERYTHING ABOVE FOR YOUR PROJECT**

______________________________________________________________________

<div align="center">

# Your Project Name

<a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-ee4c2c?logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning-792ee5?logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: Hydra" src="https://img.shields.io/badge/Config-Hydra-89b8cd"></a>
<a href="https://github.com/fusion-bench/fusion-bench-project-template"><img alt="Template" src="https://img.shields.io/badge/-FusionBench--Project--Template-017F2F?style=flat&logo=github&labelColor=gray"></a><br>

</div>

## Description

What it does

## Installation

#### Pip

```bash
# clone project
git clone https://github.com/YourGithubName/your-repo-name
cd your-repo-name

# [OPTIONAL] create conda environment
conda create -n myenv python=3.12 # recommend python 3.12+
conda activate myenv

# install pytorch according to instructions
# https://pytorch.org/get-started/

# install requirements
pip install -r requirements.txt
# install project as editable package (edit pyproject.toml as needed)
pip install -e .
```

#### Conda

```bash
# clone project
git clone https://github.com/YourGithubName/your-repo-name
cd your-repo-name

# create conda environment and install dependencies
conda env create -n myenv python=3.12

# activate conda environment
conda activate myenv
```

## How to run

run my method

```shell
fusion_bench \
    --config-name main \
    # method=...
    # method.option_1=...
    # modelpool=...
    # ...
```

or

```shell
bash scripts/run_experiments.sh
```

## Acknowledgement

This project is based on [FusionBench](https://github.com/tanganke/fusion_bench) and created using [FusionBench Project Template](https://github.com/fusion-bench/fusion-bench-project-template).
