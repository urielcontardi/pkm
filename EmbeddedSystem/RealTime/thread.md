# Thread

Uma **thread** (ou "linha de execução") é a menor unidade de processamento que pode ser executada de forma independente por um sistema operacional. Em sistemas embarcados, que geralmente possuem recursos limitados de processamento e memória, o uso de threads permite a execução de múltiplas tarefas de maneira "concorrente" (aparentemente ao mesmo tempo) dentro de um único processo.

### Espaço de Memória

Todas as threads de um processo compartilham o mesmo espaço de memória. Isso significa que variáveis globais e recursos alocados pelo processo são acessíveis a todas as threads dentro daquele processo. Isso facilita a comunicação entre threads, mas também aumenta o risco de condições de corrida e corrupção de dados se não houver sincronização adequada.

### Isolamento e Proteção

Como as threads compartilham o mesmo espaço de memória e outros recursos do processo pai, um problema em uma thread (como uma violação de segmentação ou uma falha de sincronização) pode potencialmente afetar outras threads dentro do mesmo processo.

### Overhead

 A criação e a troca de contexto entre threads são mais rápidas e exigem menos overhead do que processos. Como todas as threads compartilham o mesmo espaço de memória, não é necessário duplicar os dados e o contexto do sistema.

### Comunicação e Sincronização

A comunicação entre threads dentro do mesmo processo é mais direta e eficiente, pois todas as threads compartilham o mesmo espaço de memória. No entanto, isso requer mecanismos de sincronização (como mutexes, semáforos, ou variáveis de condição) para evitar condições de corrida e garantir a integridade dos dados.

Essa tabela resume as principais diferenças entre processos e threads no contexto de sistemas operacionais e programação.

| **Processo** | **Thread** |
| --- | --- |
| "pesado" (heavyweight) | "processo leve" (lightweight) |
| memória independente | memória compartilhada |
| comunicação lenta | comunicação rápida |
| troca de contexto custosa | troca de contexto eficiente |
| boa para gerenciar memória | não gerencia memória |
