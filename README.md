# Projeto de Iniciação Científica — Aprendizado de Máquina e Redes Neurais

Este repositório contém o pipeline completo de tratamento de dados, análise exploratória, técnicas de balanceamento de classes (SMOTE) e treinamento de arquiteturas de redes neurais. O projeto foi desenvolvido como parte da Iniciação Científica do curso de Sistemas de Informação da Pontifícia Universidade Católica de Minas Gerais (PUC Minas - Campus São Gabriel).


> **Aviso Importante sobre o Código:**
> Foram realizados diversos testes experimentais continuados neste repositório mesmo após a obtenção dos resultados principais desejados. Por conta disso, é possível que alguns detalhes ou "melindres" no código atual (como, por exemplo, a configuração exata dos hiperparâmetros das redes neurais dentro dos notebooks) estejam ligeiramente diferentes da versão final documentada nos relatórios ou artigos do projeto.

---

## Estrutura do Repositório

A estrutura de diretórios e arquivos do projeto está organizada da seguinte forma:

| Caminho / Arquivo | Descrição |
| :--- | :--- |
| `Datasets/` | Diretório para armazenamento dos conjuntos de dados brutos e processados. |
| `Generate_datasets/` | Scripts e módulos dedicados à geração e construção de datasets. |
| `Imgs/` | Gráficos, visualizações e figuras exportadas das análises. |
| `Pentagon_stages/` | Módulos e etapas da metodologia aplicada no projeto de pesquisa anterior. |
| `IC-data-organizer.ipynb` | Limpeza, padronização e estruturação dos dados brutos. |
| `IC-MS-data-organizer.ipynb` | Organização de dados de múltiplos cenários/fontes. |
| `IC-reasons-data-organizer.ipynb` | Processamento e categorização de razões/atributos dos dados. |
| `IC-data-analysis.ipynb` | Análise exploratória de dados (EDA). |
| `IC-boxplot.ipynb` | Análise estatística visual para identificação de variação e outliers. |
| `IC-SMOTE-oversampling-data.ipynb` | Aplicação da técnica SMOTE para sobreamostragem e balanceamento de classes. |
| `IC-SMOTE-balanced-data-division.ipynb` | Divisão e amostragem estratificada dos dados balanceados. |
| `IC-SMOTE-histogram.ipynb` | Análise de distribuição de frequências pós-balanceamento. |
| `IC-neural-network-M1.ipynb` | Implementação e avaliação da Rede Neural — Modelo 1. |
| `IC-neural-network-M2.ipynb` | Implementação e avaliação da Rede Neural — Modelo 2. |
| `IC-neural-network-M3.ipynb` | Implementação e avaliação da Rede Neural — Modelo 3. |
| `requirements.txt` | Lista de dependências do ambiente Python. |

---

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Análise e Processamento de Dados:** Pandas, NumPy
* **Balanceamento de Dados:** (SMOTE)
* **Modelagem e Redes Neurais:** Scikit-learn, TensorFlow 
* **Visualização:** Matplotlib, Seaborn

