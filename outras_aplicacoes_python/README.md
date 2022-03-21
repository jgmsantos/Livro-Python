# Preparação do ambiente para plot da previsão do modelo WRF operacional do CPTEC/INPE

Os procedimentos a seguir foram testados em um sistema operacional Ubuntu 20.04 LTS. Portanto, a aplicação destes passos em outros sistemas podem ser parcial ou totalmente diferentes. 

O exemplo a seguir considera apenas os produtos relacionados com a variável precipitação acumulada. 

O catálogo completo pode ser acessado em:

[http://ftp.cptec.inpe.br/modelos/tempo/WRF/ams_05km](http://ftp.cptec.inpe.br/modelos/tempo/WRF/ams_05km)

Vá para o seu diretório no seu computador onde ficarão as simulações de interesse.
 
É importante ressaltar que o acervo histórico das previsões numéricas geradas pelo CPTEC/INPE retém apenas os últimos 30 dias. Portanto, dependendo do momento que você esteja reproduzido os exemplos que consultam a base das previsões do WRF, a data considerada no script pode não estar mais disponível na base de dados. 

Por exemplo, o tutorial abaixo considera os dados WRF da previsão iniciada em **00 UTC 17/fev/2022**, que ainda estava disponível durante a preparação deste tutorial.

Digite o comando abaixo:

```
wget -r -np -A "WRF_*" http://ftp.cptec.inpe.br/modelos/tempo/WRF/ams_05km/recortes/prec/2022/02/17/00/ -q --show-progress
```

>Não esqueça de alterar a data da simulação, neste exemplo, utiliza-se o ano 2022, mês, 02 e dia, 17 referente a simulação das 00 UTC.

## Organizando arquivos baixados

Após realizar o download dos dados com o comando `wget` acima, cria-se o diretório `wrf2022021700` para organizar as simulações.

```
mkdir wrf2022021700
```

```
mv ftp.cptec.inpe.br/modelos/tempo/WRF/ams_05km/recortes/prec/2022/02/17/00/* wrf2022021700/
```

```
rm -rf ftp.cptec.inpe.br
```

## Instalação e download do OpenGrADS

O OpenGrADS é necessário para o `py3grads`. Caso a instalação já tenha sido feita, pode-se ignorar os passos a seguir.

```
wget'https://sourceforge.net/projects/opengrads/files/grads2/2.2.1.oga.1/Linux%20%2864%20Bits%29/opengrads-2.2.1.oga.1-bundle-x86_64-pc-linux-gnu-glibc_2.17.tar.gz'
```

```
tar -zxf opengrads-2.2.1.oga.1-bundle-x86_64-pc-linux-gnu-glibc_2.17.tar.gz
export PATH=$PATH:"opengrads-2.2.1.oga.1/Contents/"
```

```
export PATH=$PATH:"opengrads-2.2.1.oga.1/Contents/"
```


## Instalando o git

O git é necessário para clonar o repositório do `py3grads`. Caso o git já tenha sido instalado, ignore essa etapa.

```
sudo apt install git
```

## Instalando o PyGrADS

Clonado o repositório do py3grads.

```
git clone https://github.com/meridionaljet/py3grads
```

Entre no diretório `py3grads`:

```
cd py3grads
```

Caso seja utilizado um ambiente virtual instalado via Conda ou virtualenv, ative-o para depois instalar o `py3grads` nele.

Para ativar um ambiente virtual:

```
conda activate <Nome_Ambiente_Virtual>
```

Instalando o `py3grads`.

```
python py3grads/setup.py install
```
