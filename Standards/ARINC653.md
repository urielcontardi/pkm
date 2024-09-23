# ARINC 653

O ARINC 653 é um padrão de software utilizado em sistemas de aviação para gerenciar a execução de aplicativos em ambientes de tempo real críticos. Ele define uma interface entre o sistema operacional em tempo real (RTOS) e os aplicativos, permitindo a execução segura e separada de diferentes funções em um único hardware, usando um esquema de particionamento.

### Estrutura do ARINC 653

O ARINC 653 é dividido em várias partes:

- **Parte 0**: Introdução ao padrão, incluindo conceitos e objetivos.
- **Parte 1**: Define os serviços obrigatórios, como gerenciamento de partições e processos, além do gerenciamento de modos de operação (por exemplo, COLD_START e NORMAL).
- **Parte 2**: Serviços estendidos opcionais, como acesso a sistemas de arquivos e logging de dados.
- **Parte 3A e 3B**: Especificações de teste de conformidade para os serviços obrigatórios e estendidos, respectivamente.
- **Parte 4**: Serviços de subconjunto, oferecendo uma versão reduzida do padrão.
- **Parte 5**: Capacidades recomendadas de software central, sugerindo funcionalidades adicionais para implementações de RTOS baseadas no ARINC 653.

### Principais Funcionalidades

- **Gerenciamento de Partições**: Cada partição funciona de maneira independente e isolada, permitindo que diferentes aplicativos ou funções de sistemas críticos operem sem interferência.
- **Gerenciamento de Processos**: Dentro de cada partição, os processos são gerenciados por um escalonador, e as operações podem ser preemptivas ou baseadas em prioridades definidas.
- **Suporte Multicore**: O ARINC 653 foi atualizado para suportar arquiteturas de múltiplos núcleos, permitindo que uma partição use vários núcleos ou que múltiplas partições compartilhem recursos de múltiplos núcleos.

### Utilização e Certificação

O ARINC 653 é usado principalmente em sistemas de aviônicos integrados modulares (IMA), onde é essencial garantir a segurança e a confiabilidade das operações. A certificação é baseada em conformidade com padrões como o DO-178C e requer a adesão a requisitos rigorosos, especialmente para uso em processadores multicore, conforme especificado pelo CAST-32A e documentos regulatórios equivalentes da FAA e EASA.
