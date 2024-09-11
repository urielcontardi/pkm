
# AXI (Advanced eXtensible Interface)
O AXI é parte do conjunto de barramentos da AMBA (Advanced Microcontroller Bus Architecture) da ARM. Ele é amplamente utilizado em SoCs (Systems on Chip) para comunicação de alta velocidade entre componentes. Algumas de suas características incluem:

- **Transações independentes de leitura e escrita**, permitindo operações simultâneas.
- **Transferências de dados não alinhadas** são permitidas, o que oferece flexibilidade para diferentes larguras de dados.
- **Suporte a bursts longos** de dados, o que melhora a eficiência em operações de memória.
- **Arbitragem avançada** e gerenciamento de prioridade, permitindo alta performance e baixa latência.
- **Pipeline**: as operações podem ser processadas em etapas, aumentando o throughput.

# AHB (Advanced High-performance Bus)
O AHB é um barramento de alta performance também parte da arquitetura AMBA, mas geralmente utilizado para componentes que requerem uma comunicação rápida, mas menos complexa que o AXI. Ele é frequentemente usado para conectar o processador central, memória e periféricos de alta largura de banda.

- **Barramento de largura fixa**: normalmente 32 ou 64 bits.
- **Transferências burst** e **single-cycle** para acesso rápido à memória.
- Não suporta transações independentes de leitura e escrita, como o AXI.
- **Árbitro central**: há um controlador que define qual mestre tem acesso ao barramento.

# APB (Advanced Peripheral Bus)
O APB é otimizado para periféricos de baixa largura de banda e baixa complexidade. Ele é usado em componentes onde a performance não é crítica, como timers, controladores de GPIO e interfaces de controle.

- **Operação simples**: projetado para ser um barramento com baixa complexidade, ideal para periféricos que não exigem alta performance.
- **Baixa latência** e overhead reduzido.
- Não suporta bursts e não possui suporte para transações pipelined, tornando-o mais simples, mas menos eficiente para grandes volumes de dados.
