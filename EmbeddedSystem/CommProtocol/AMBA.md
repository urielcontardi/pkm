# AMBA (Advanced Microcontroller Bus Architecture)

AMBA (Advanced Microcontroller Bus Architecture) é um padrão aberto e livre de royalties para a conexão e gerenciamento de blocos funcionais em um System-on-Chip (SoC). Ele é independente de plataforma e suporta a integração de designs multiprocessadores, garantindo compatibilidade e escalabilidade entre componentes de diversos fornecedores. O AMBA facilita o design eficiente de SoCs ao fornecer uma arquitetura de interconexão padronizada.

---

## Principais Características do AMBA

- **Padrão aberto e livre de royalties**: Incentiva ampla adoção.
- **Independente de plataforma**: Compatível com qualquer arquitetura de processador.
- **Escalável e modular**: Suporta uma ampla variedade de aplicações, de dispositivos móveis a data centers.
- **Ecossistema robusto**: Garante compatibilidade e interoperabilidade entre componentes IP.

---

## Especificações do AMBA

### 1. **AMBA CHI (Coherent Hub Interface)**

- Define interfaces para processadores totalmente coerentes.
- Separa camadas de protocolo e transporte para otimizar desempenho, consumo de energia e área.
- Aplicações: Dispositivos móveis, redes, automotivo e data centers.

### 2. **AMBA CHI C2C (Chip-to-Chip)**

- Extensão do CHI para transportar protocolos em formato de pacotes entre chips.
- Alvo: Sistemas heterogêneos avançados e sistemas SMP coerentes.
- Proporciona uma interface unificada para máxima interoperabilidade.

### 3. **[AMBA AXI](AMBA_AXI.md) (Advanced eXtensible Interface)**

- Projetado para interconexões de alta frequência e alta largura de banda.
- Suporta diversas aplicações: Dispositivos móveis, redes, automotivo e sistemas embarcados.

### 4. **AMBA ACE (AXI Coherency Extension)**

- Extensão do AXI para coerência em sistemas multicore.
- Substituído pelo CHI em novos projetos.

### 5. **[AMBA AHB](AMBA_AHB.md) (Advanced High-performance Bus)**

- Usado com processadores Cortex-M para sistemas embarcados.
- Otimizado para SoCs de baixa latência.

### 6. **[AMBA APB](AMBA_APB.md) (Advanced Peripheral Bus)**

- Barramento compacto e de baixo consumo de energia para tráfego de baixa largura de banda.
- Isola transações de baixa largura de banda das interconexões de alto desempenho.

### 7. **AMBA AXI-Stream**

- Define transferências de dados unidirecionais com redução de sinais de roteamento.
- Ideal para implementações em FPGA.

### 8. **AMBA CXS (Credited eXternal Streaming)**

- Interface não bloqueante e pacotizada para transporte de CCIX e CXL.
- Otimizada para interfaces largas e altas taxas de dados.

### 9. **AMBA DTI (Distributed Translation Interface)**

- Protocolo ponto a ponto para serviços de tradução alinhados à arquitetura Arm System MMU.

### 10. **AMBA LTI (Local Translation Interface)**

- Complementa o AMBA DTI para maior desempenho em serviços de tradução.
- Proporciona comunicação entre dispositivos de I/O e TBUs.

### 11. **AMBA ATB (Advanced Trace Bus)**

- Interface agnóstica de dados para transferência de informações de rastreamento para depuração.

### 12. **AMBA LPI (Low Power Interface)**

- Define interfaces para gerenciamento de recursos de clock e energia em componentes de SoC.

### 13. **AMBA ATP (Adaptive Traffic Profiles)**

- Estrutura para modelar comportamentos de acesso à memória em alto nível.
- Auxilia no design e verificação de SoCs complexos.

### 14. **AMBA GFB (Generic Flash Bus)**

- Padrão para desenvolvimento de controladores de memória para Memória Não Volátil (NVM).
- Facilita a migração entre processos de fabricação de diferentes foundries.

---

## Referencias

https://developer.arm.com/Architectures/AMBA
