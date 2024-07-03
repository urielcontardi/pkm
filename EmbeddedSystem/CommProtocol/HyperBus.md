## Tecnologia HyperBus

A tecnologia HyperBus foi introduzida pela primeira vez pela Cypress em 2014. Ela se baseia nos recursos legados das memórias de interface paralela e serial, ao mesmo tempo em que melhora o desempenho do sistema.

### Características Principais

1. **Alta Taxa de Transferência de Dados**:
   - A primeira geração do HyperBus oferece uma taxa de transferência de até 333 MB/s.
   - O HyperRAM 2.0 aumenta essa taxa de transferência para até 400 MB/s.

2. **Design Eficiente**:
   - Utiliza uma interface DDR (Double Data Rate) com uma largura de dados de 8 bits tanto para endereço quanto para dados.
   - Normalmente utilizado com interface xSPI (Octal) ou HyperBus
   - Possui pinos para sinalização para operações de leitura/gravação e inclui um chip select para cada dispositivo de memória.

3. **Integração Flexível**:
   - Permite que microcontroladores suportem flash externo e RAM no mesmo barramento.
   - Compatível com qualquer dispositivo de memória que tenha uma interface HyperBus.
   - Oferece uma interface eficaz e fácil de usar para expansão de memória em aplicativos com restrição de espaço.
