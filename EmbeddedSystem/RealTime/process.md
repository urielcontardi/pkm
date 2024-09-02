# Process

Um **processo** é uma unidade de execução que representa um programa em execução. No contexto de sistemas embarcados, que frequentemente possuem recursos limitados (como memória, processamento, e energia), o conceito de processo pode variar um pouco em comparação com sistemas operacionais de propósito geral.

### Isolamento e Proteção

Em muitos sistemas embarcados, um processo possui seu próprio espaço de memória isolado. Isso significa que ele não pode acessar diretamente a memória de outros processos, o que ajuda a evitar falhas e corrupção de dados entre diferentes partes do sistema. Cada processo possui seu próprio espaço de memória independente. Isso significa que a memória alocada para um processo não é acessível por outro processo sem mecanismos explícitos de comunicação (como pipes, sockets, ou memória compartilhada). Isso proporciona isolamento e proteção entre processos.

### Prioridades e Escalonamento

Sistemas embarcados geralmente utilizam um escalonador para gerenciar a execução de processos com base em suas prioridades. Isso é especialmente importante em sistemas de tempo real, onde algumas tarefas devem ser executadas dentro de um certo prazo.

### Comunicação entre Processos

Como os processos são isolados uns dos outros, é necessário usar mecanismos de comunicação entre processos (IPC - Inter-Process Communication) para que eles possam trocar dados ou sinalizar eventos. Em sistemas embarcados, isso pode ser feito através de filas de mensagens, semáforos, eventos, ou buffers circulares.

### Overhead

A criação e o gerenciamento de processos geralmente requerem mais recursos (overhead) do sistema, pois cada processo possui seu próprio contexto de execução completo, incluindo memória, espaço de endereço e recursos do sistema.
