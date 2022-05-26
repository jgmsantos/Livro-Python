# Python para Geociências

## 1. Introdução

Este livro tem como objetivo ensinar Python para o público de Geociências. 

A partir de dados dos principais centro mundiais de meteorologia são fornecidas dicas de como realizar a manipulação desses dados, bem como a sua visualização.

Este documento foi redigido pensando no usuário que está iniciando nesta linguagem fascinante que o Python.

Os scripts fornecidos são comentados para facilitar o entendimento.

Este documento contou com a colaboração de excelentes profissionais (listados abaixo) que possuem uma vasta experiência em Python e na manipulação e visualização de dados ambientais.

* Guilherme Martins: [CV Lattes](http://lattes.cnpq.br/5997657584785803)
* Jonatas Leon: [CV Lattes](http://lattes.cnpq.br/6707812894667096) | [Github](https://github.com/jonatasleon)
* Diogo Ramos: [CV Lattes](http://lattes.cnpq.br/1800868291881642)
* Cristiano Eichholz: [CV Lattes](http://lattes.cnpq.br/3933039769920991)

## 2. Fonte dos dados utilizados

Os dados utilizados são de diferente fontes, por exemplo:
* INPE (Instituto Nacional de Pesquisas Espaciais)
    * Programa Queimadas: [https://queimadas.dgi.inpe.br/queimadas/portal](https://queimadas.dgi.inpe.br/queimadas/portal)
    * Produto MERGE: [http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY](http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY)
* ERA5/ECMWF (European Centre for Medium-Range Weather Forecasts)
    * ERA5/ECMWF: [https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset)
* NCEP (National Centers for Environmental Prediction)
    * [https://psl.noaa.gov/data/gridded](https://psl.noaa.gov/data/gridded)
* NASA (National Aeronautics and Space Administration)
    * GRACE: [https://nasagrace.unl.edu](https://nasagrace.unl.edu)


Os passos a seguir devem ser digitados no terminal, pois eles instalam o miniconda (item 3) para criar o ambiente virtual (item 4) para instalar o Pyhton (item 5) e suas bibliotecas (item 6).

## 3. Instalação do Miniconda

É preferível instalar as bibliotecas necessárias via Anaconda. Para instalar o Anaconda, faça a instalação usando o [Miniconda](https://docs.conda.io/en/latest/miniconda.html):

```bash
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

[Conda-forge](https://conda.io/projects/conda-forge) é um repositório de pacotes adicionais que não estão no [Anaconda](https://www.anaconda.com/download/).

**Importante:** Uma vez a instalação concluída, deve-se reiniciar o terminal para que a instalação seja finalizada corretamente.

Para mais informações sobre criação de ambiente virtual, basta clicar [aqui](https://guilherme.readthedocs.io/en/latest/pages/tutoriais/miniconda.html).

## 4. Criação do ambiente virtual para executar os scripts

Será criado o ambiente virtual chamado `livro_python` para não danificar nada no seu ambiente de trabalho. **Isso é feito para não gerar conflitos de bibliotecas**.

```
conda create --name livro_python
```

### 4.1 Habilitando o ambiente virtual criado

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

## 5. Instalação do Python

Este documento utiliza a versão do Python [3.9.12](https://www.python.org/downloads/release/python-3912/).

```
conda install -c conda-forge python==3.9.12
```

## 6. Lista de bibliotecas a serem instaladas

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
