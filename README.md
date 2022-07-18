# ufmg-iia-tp2

Este repositório contém o código do trabalho prático 2 da disciplina Introdução à Inteligência Artificial do Departamento de Ciência da Computação da Universidade Federal de Minas Gerais. Neste trabalho, deve-se implementar os algoritmos _K Nearest Neighbors_ e _K Means_ para classificar dados. Os dados utilizados nos testes são do dataset iris, tambem incluso neste repositório.

### Dependências

É necessário ter Python instalado na máquina, versão >= 3.9.12.

### Execução

Para executar o projeto com o algoritmo _KNN_ utilizando 3 vizinhos, execute da raíz do projeto:
```bash
python3 src/main.py --algo knn -k 3
```

Para executar o projeto com o algoritmo _K Means_ distinguindo 3 grupos, execute na raíz do projeto:
```bash
python3 src/main.py --algo kmeans -k 3
```

Outros argumentos podem ser passados na execução. Para o algoritmo _KNN_, é possível utilizar:
```bash
--accuracy # para ver acurácia
--precision # para ver a precisão
--recall # para revocação
--f1 # para score f1
```
Ao utilizar qualquer um destes argumentos a matriz de confusão será impressa.

Para os dois algoritmos, também é possível utilizar:
```bash
--print-predictions # para imprimir as predições feitas em todos os dados no arquivo de testes
--train-dataset <arquivo.csv> # para alterar o arquivo utilizado no treino
--test-dataset <arquivo.csv> # para alterar o arquivo de testes
```
