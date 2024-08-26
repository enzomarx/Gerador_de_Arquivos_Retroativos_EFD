# Gerador de Arquivos Retroativos EFD

![demointerface](https://github.com/user-attachments/assets/7028df03-c27c-4f2e-b9fe-30df4f41c73e)

## Visão Geral
O Aplicativo de Arquivos Retroativos EFD é um aplicativo desenvolvido para auxiliar empresas e contadores na criação de arquivos TXT de Escrituração Fiscal Digital (EFD). Este aplicativo permite a importação de dados a partir de um arquivo CSV e gera automáticamente os arquivos TXT formatados de acordo com os layouts exigidos pelo guia prático da EFD. Além disso, os arquivos gerados são automáticamente compactados em um arquivo ZIP para facilitar o armazenamento e envio.

## Funcionalidades
- Importação de CSV: Carregue um arquivo CSV contendo as colunas obrigatórias "cnpj" e "nome diretamente na interface do aplicativo.
- Visualização de Dados: Veja os dados carregados do CSV na interface antes de gerar os arquivos.
- Definição de Período: Insira as datas de início e fim para a geração dos arquivos retroativos.
- Geração Automática de Arquivos TXT: Cria arquivos TXT para cada linha do CSV, substituindo as variáveis de acordo com os dados inseridos pelo usuário.
- COmpactação Automática: Todos os arquivos TXT gerados são automáticamente compactados em um arquivo ZIP.
- Interface Amigável: Interface de usuário intuitiva e moderna utilizando a biblioteca CustomTkinter.
