# PSL (Property Specification Language)

A verificação PSL (Property Specification Language) refere-se ao uso de uma linguagem formal para especificar propriedades que um sistema de hardware ou software deve satisfazer. 

PSL é comumente usada na verificação de circuitos digitais e design de hardware para assegurar que o comportamento de um circuito esteja conforme as especificações.

A verificação PSL é uma parte crítica do fluxo de design e verificação de sistemas eletrônicos complexos, garantindo que o design final esteja livre de erros e opere conforme esperado em diferentes condições.

## Origem

O PSL foi criado pela Comissão Técnica de Verificação Funcional da Accellera. Após um processo em que foram avaliadas doações de diversas fontes, a linguagem Sugar da IBM foi escolhida como base para o PSL. O Manual de Referência de Idioma para PSL versão 1.01 foi lançado em abril de 2003. A versão 1.1 do PSL estava em desenvolvimento em fevereiro de 2004 e se tornou um padrão IEEE em 2005 (IEEE 1850-2005).

## Principais Pontos

1. **Linguagem Formal**: PSL é uma linguagem formal que permite a especificação precisa de propriedades e comportamentos desejados de um sistema.
2. **Verificação de Hardware**: É frequentemente usada na verificação de designs de hardware, especialmente em circuitos digitais, para verificar se o circuito funciona conforme especificado.
3. **Propriedades Temporal**: PSL é baseada em lógica temporal, o que permite a especificação de propriedades que dependem de sequências de eventos ao longo do tempo.
4. **Abordagens**: PSL suporta diferentes abordagens de verificação, incluindo simulação baseada em propriedade, verificação formal, e checagem estática.

## Estrutura e Sintaxe

1. Base Lógica: PSL é baseada em lógica temporal, permitindo a especificação de propriedades que envolvem sequências de eventos ao longo do tempo.
2. Componentes: PSL inclui operadores lógicos e temporais, como "always", "never", "next", "until", entre outros.
3. Linguagens Suportadas: Pode ser usada com várias linguagens de descrição de hardware, incluindo VHDL, Verilog, e SystemVerilog.

### Linguagem

Trata-se de uma linguagem baseada em asserção (assertions), isto é, o programador deve inserir afirmações que serão verificadas pela ferramenta de verificação.

To Do: Descrever a linguagem

## Ferramentas

### Pagas

### OpenSource

- Yosys (GHDL)

## Exemplo Prático

## Referência

1. https://vhdlwhiz.com/formal-verification-in-vhdl-using-psl/
