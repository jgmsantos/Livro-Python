# Python para Geociências

Este livro tem como objetivo ensinar Python para o público de Geociência.

# Instalação

É preferível instalar as bibliotecas necessárias via Anaconda. Para instalar o Anaconda, faça a instalação usando o [Miniconda](https://docs.conda.io/en/latest/miniconda.html):

```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

[Conda-forge](https://conda.io/projects/conda-forge) é um repositório de pacotes adicionais que não estão no [Anaconda](https://www.anaconda.com/download/).

# Criação do ambiente virtual para executar os scripts

Será criado o ambiente virtual chamado `livro_python` para não danificar nada no seu ambiente de trabalho. **Isso é feito para não gerar conflitos de bibliotecas**.

```
conda create --name livro_python
```

# Acessando o ambiente virtual criado

```
conda activate livro_python
```

Nota-se a mudança do nome `(base)` para `(livro_python)` na linha do terminal Linux.

Mudou de:
```
(base) gui@DESKTOP-LD7TCRV:
```

Para:
```
(livro_python) gui@DESKTOP-LD7TCRV:
```

# Instalação do Python

Este documento utiliza a versão do Python [3.9.12](https://www.python.org/downloads/release/python-3912/).

```
conda install -c conda-forge python==3.9.12
```

# Lista de bibliotecas a serem instaladas

Os script são executados corretamente com as bibliotecas listadas abaixo. Para instalação, basta digitar os comandos no seu terminal.

```
pip install matplotlib==3.4.3
pip install pandas==1.4.2
pip install SkillMetrics==1.1.8
pip install proplot==0.9.4
pip install xarray==2022.3.0
pip install netcdf4==1.5.8
pip install esmtools==1.1.3
pip install cartopy==0.20.2
pip install yellowbrick==1.4
pip install seaborn==0.11.2
pip install windrose==1.6.8
pip install climate-indices==1.0.10
pip install salem==0.3.7
pip install geopandas==0.10.2
pip install rasterio==1.2.10
pip install siphon==0.9
pip install metpy==1.3.0
```
## Conteúdo

O livro está estruturado da seguinte forma:

* Capítulo 1:
* Capítulo 2:
* Capítulo 3:
* Capítulo 4:
* Capítulo 5:
* Capítulo 6:
* Capítulo 7:
* Capítulo 8:
* Capítulo 9:
* Capítulo 10:
* Capítulo 11:
* Capítulo 12: