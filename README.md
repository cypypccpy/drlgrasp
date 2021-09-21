# drlgrasp: deep reinforcement learning grasp

![Image text](img-folder/1111.jpg)

[![Author](https://img.shields.io/badge/Author-cypypccpy-blue.svg "Author")](https://github.com/cypypccpy "Author")
[![license](https://img.shields.io/github/license/:user/:repo.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
<br></br>

## 内容列表

- [背景](#背景)
- [安装](#安装)
- [用法](#用法)
- [TODO](#TODO)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)
<br></br>

## 背景

- Train kuka robot reach a point with deep rl in pybullet.
<br></br>

## 安装 (Now only support linux and macos)
**I strongly recommend using Conda to install the env, because you will possible encounter the mpi4py error with pip.**

The spinningup rl library is the necessary lib.
first, you should install miniconda or anaconda.
second, install some dev dependencies.

```bash
sudo apt-get update && sudo apt-get install libopenmpi-dev
sudo apt install libgl1-mesa-glx
```
third, create a conda virtual environment
```bash
conda create -n spinningup python=3.6   #python 3.6 is recommended
```

```bash
#activate the env
conda activate spinningup
```

then, install spiningup,is contains almost dependencies
```bash
# clone my version, I made some changes.
git clone https://github.com/borninfreedom/spinningup.git
cd spinningup
pip install -e .
```

last, install torch and torchvision.

if you have a gpu, please run this (conda will install a correct version of cudatoolkit and cudnn in the virtual env, so don't care which version you have installed in your machine.)
```bash
# CUDA 10.1
conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=10.1 -c pytorch
```

if you only have a cpu, please run this,
```bash
# CPU Only
conda install pytorch==1.4.0 torchvision==0.5.0 cpuonly -c pytorch
```

## 用法

### view the train results through plot
```bash
python -m spinup.run plot ./logs
```
More detailed information please visit [plotting results](https://spinningup.openai.com/en/latest/user/plotting.html)
<br></br>

## TODO

<br></br>

## 如何贡献

See [the contributing file](CONTRIBUTING.md)!
<br></br>

## 使用许可

[MIT © Richard McRichface.](../LICENSE)



