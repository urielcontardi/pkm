# Padrões de Teste

Test patterns (ou padrões de teste) são sequências predefinidas de sinais de entrada aplicadas a um sistema ou circuito para verificar seu comportamento e garantir que ele funcione corretamente sob diferentes condições. Esses padrões são usados em testes de hardware e software para detectar defeitos, falhas ou mau funcionamento no sistema sob teste (SUT).

* **No Contexto de Hardware:**
  Em circuitos digitais, como circuitos integrados e máquinas de estados finitos, os test patterns são conjuntos de sinais de entrada que são aplicados para estimular o circuito e observar as saídas. O objetivo é garantir que o circuito responda corretamente a todas as entradas possíveis, detectando assim qualquer defeito presente.
* **No Contexto de Software:**
  Test patterns em software envolvem conjuntos de dados de entrada usados para verificar a funcionalidade de um programa ou sistema. Eles ajudam a assegurar que o software funcione corretamente em diferentes cenários, incluindo casos extremos e situações de falha.

### Importância dos Test Patterns:

* **Cobertura de Falhas:** Os test patterns são usados para garantir uma alta cobertura de falhas, ou seja, a capacidade de detectar a maior quantidade possível de falhas potenciais em um sistema.
* **Eficiência de Teste:** Com padrões de teste bem projetados, é possível detectar rapidamente defeitos no sistema, economizando tempo e recursos.
* **Verificação de Robustez:** Além de detectar falhas, os padrões de teste podem ser usados para verificar a robustez de um sistema, ou seja, sua capacidade de operar corretamente sob condições adversas ou inesperadas.

## Cobertura de Falhas (Fault Coverage)

**Fault coverage** (cobertura de falhas) é uma métrica usada para avaliar a eficácia de um conjunto de padrões de teste em detectar possíveis falhas em um sistema, especialmente em circuitos digitais. Ela é expressa como uma porcentagem que indica a proporção de falhas detectáveis em relação ao número total de falhas possíveis, com base em um modelo de falhas específico. A qualidade dos conjuntos de padrões de teste pode ser avaliada usando a cobertura de falhas como uma métrica importante.

$$
\text{Cobertura} = \frac{\text{Número de falhas detectáveis para um dado conjunto de padrões de teste}}{\text{Número de falhas possíveis de acordo com o modelo de falhas}}
$$

### Importância da Cobertura de Falhas:

1. **Qualidade do Produto:** Uma alta cobertura de falhas é essencial para garantir que o sistema ou produto seja de alta qualidade e confiável. Em indústrias críticas, como a aeroespacial ou automotiva, onde a falha de um sistema pode ter consequências graves, a cobertura de falhas deve ser muito alta (geralmente 98-99% ou mais).
2. **Verificação de Testes:** A cobertura de falhas ajuda a avaliar a qualidade do conjunto de testes. Se a cobertura é baixa, pode ser necessário gerar padrões de teste adicionais ou revisar o modelo de falhas utilizado.
3. **Eficiência:** Ao medir a cobertura de falhas, é possível identificar quais áreas do sistema estão mais suscetíveis a falhas não detectadas e concentrar esforços adicionais nessas áreas.

### Desafios na Cobertura de Falhas:

* **Modelos de Falhas:** A cobertura de falhas depende do modelo de falhas usado. Modelos diferentes podem resultar em diferentes estimativas de cobertura. Por exemplo, um modelo de falhas pode considerar apenas falhas simples em portas lógicas, enquanto outro pode incluir falhas mais complexas, como falhas temporais.
* **Equívocos de 100% de Cobertura:** Alcançar 100% de cobertura de falhas não garante que o sistema esteja completamente livre de falhas. Isso porque a cobertura de falhas se baseia em um modelo de falhas específico, e algumas falhas fora desse modelo podem não ser detectadas.
* **Redundância:** Algumas falhas podem ser "redundantes," significando que elas não afetam o comportamento observável do sistema e, portanto, não são detectáveis. Mesmo assim, essas falhas precisam ser consideradas ao calcular a cobertura de falhas.

## Cobertura de correção

 garante que um sistema sem falhas seja corretamente reconhecido como tal. Sem isso, teoricamente, seria possível alcançar 100% de cobertura de falhas classificando todos os sistemas como defeituosos, o que seria enganoso e ineficaz. É importante não apenas alcançar uma alta cobertura de falhas, mas também uma alta cobertura de correção.

Para aumentar as opções de validação dos sistemas, muitas vezes é vantajoso aplicar métodos de teste já na fase de design. Por exemplo, conjuntos de padrões de teste podem ser aplicados a modelos de software para verificar se vários modelos se comportam de maneira consistente. Esse teste inicial pode reduzir a necessidade de métodos formais mais demorados, que podem ser reservados para casos em que o sistema tenha passado na verificação de equivalência baseada em testes.

## Simulação de Falhas

Prever o comportamento dos sistemas na presença de falhas, ou calcular analiticamente a cobertura de falhas, não é totalmente viável com a tecnologia atual. Como resultado, a simulação de falhas é frequentemente usada para avaliar o comportamento do sistema sob condições de falha. Na simulação de falhas, os modelos de sistema são alterados para refletir o impacto de falhas específicas.

**Os objetivos da simulação de falhas incluem:**

- Compreender os efeitos das falhas dos componentes no nível do sistema (por exemplo, determinar se as falhas são redundantes).
- Avaliar a eficácia dos mecanismos de tolerância a falhas.

**Uma falha é considerada redundante se não afetar o comportamento observável do sistema.**

A simulação de falhas exige simular o sistema para todas as falhas viáveis sob o modelo de falhas, muitas vezes em um grande número de padrões de entrada diferentes. Consequentemente, a simulação de falhas pode ser extremamente demorada. Várias técnicas foram desenvolvidas para acelerar esse processo.

Uma dessas técnicas é a simulação de falhas em paralelo no nível de portas lógicas. Nesse contexto, os sinais internos são tratados como sinais de um único bit, permitindo o mapeamento eficiente dos sinais para a palavra de máquina de um computador hospedeiro durante a simulação. Redes Booleanas podem ser simuladas usando instruções de máquina AND e OR, onde cada bit da palavra de máquina representa um padrão de teste diferente.

## Injeção de Falhas

A simulação de falhas pode ser proibitivamente demorada para sistemas reais. Se sistemas reais estiverem disponíveis, a injeção de falhas pode ser usada como uma alternativa. A injeção de falhas envolve a modificação de sistemas reais e a observação do comportamento resultante. Ao contrário da simulação de falhas, a injeção de falhas não depende estritamente de modelos de falhas, o que significa que pode, potencialmente, descobrir falhas que não foram previstas pelos modelos existentes.

**Podemos distinguir dois tipos de injeção de falhas:**

1. **Falhas locais dentro do sistema**: Essas ocorrem devido a falhas ou defeitos internos nos componentes do sistema.
2. **Falhas no ambiente**: Essas são condições externas ou comportamentos que não estão alinhados com as especificações do sistema, como operar o sistema fora dos limites de temperatura ou radiação especificados.

**Métodos de injeção de falhas incluem:**

- **Injeção de falhas em nível de hardware**: Técnicas como manipulação de pinos, interferência eletromagnética e radiação nuclear são usadas para induzir falhas.
- **Injeção de falhas em nível de software**: Métodos como alternância de bits de memória são empregados para simular falhas no software do sistema.

A eficácia da injeção de falhas é influenciada pelo “efeito de sondagem”, que se refere à possibilidade de que o ato de sondagem (ou injeção de falhas) possa alterar o comportamento do sistema. Idealmente, esse impacto deve ser mínimo e negligenciável.

Experimentos realizados por Kopetz indicam que a injeção de falhas baseada em software pode ser tão eficaz quanto os métodos baseados em hardware. No entanto, a radiação nuclear foi encontrada gerando erros únicos que outros métodos não produziram, destacando a importância de selecionar o método adequado de injeção de falhas com base nos requisitos específicos do sistema em teste.
