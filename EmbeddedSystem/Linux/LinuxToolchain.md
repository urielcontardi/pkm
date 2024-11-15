# Toolchain

A **toolchain** do Linux é um conjunto de ferramentas que permite o desenvolvimento de software, especialmente para sistemas embarcados ou para compilação de programas para diferentes arquiteturas de hardware. Uma toolchain típica inclui os seguintes componentes principais:

1. **Compilador**: O compilador (como o GCC - GNU Compiler Collection) transforma o código-fonte escrito em linguagens como C ou C++ em código de máquina que pode ser executado pelo processador. O GCC é amplamente utilizado no desenvolvimento de software para Linux e suporta várias arquiteturas de hardware.
2. **Linker**: O linker (como o GNU ld) é responsável por combinar vários arquivos de objeto gerados pelo compilador em um único executável. Ele resolve referências entre diferentes partes do código e também pode incluir bibliotecas externas.
3. **Assemblador**: O assembler converte o código de montagem em código de máquina. Embora muitos desenvolvedores não precisem interagir diretamente com o assembler, ele desempenha um papel importante na construção de executáveis.
4. **Bibliotecas**: As bibliotecas (como a glibc - GNU C Library) fornecem funções e rotinas que podem ser reutilizadas em diferentes programas, facilitando o desenvolvimento. Elas incluem funções para manipulação de strings, operações de entrada/saída, manipulação de arquivos e muito mais.
5. **Utilitários de Desenvolvimento**: A toolchain pode incluir uma variedade de utilitários que ajudam no desenvolvimento, depuração e teste de software, como `make` (para automação de compilação), `gdb` (para depuração), e ferramentas de análise estática de código.
6. **Ambiente de Desenvolvimento**: Algumas toolchains vêm com um ambiente de desenvolvimento integrado (IDE) que facilita a escrita, compilação e depuração de código, embora muitos desenvolvedores optem por usar editores de texto e ferramentas de linha de comando.

### Exemplo de Toolchain para Desenvolvimento em Linux

Uma toolchain típica para desenvolvimento em Linux pode incluir:

- **GCC** (compilador)
- **GNU Binutils** (linker e utilitários)
- **glibc** (biblioteca padrão C)
- **Make** (ferramenta de automação)
- **GDB** (depurador)

### Uso em Sistemas Embarcados

Em sistemas embarcados, as toolchains são frequentemente cruzadas, ou seja, são usadas em um ambiente de desenvolvimento (geralmente x86) para compilar software que será executado em uma arquitetura diferente (como ARM ou MIPS). Isso é feito utilizando toolchains cruzadas, que incluem todos os componentes necessários para compilar, linkar e gerar executáveis para o sistema de destino.

### Tipos de Toolchain

- Toolchain Nativo
  - Roda no mesmo sistema que o programa foi gerado
  
- Cross Toolchain
  - Roda em uma arquitetura diferente que o do host
  

# GCC Toolchain Components

- Binutils - utilzaitio binario incluindo assembler e linker
- GCC (GNU Compiler Collection)
- C Library - API baseada no padrao POSIX


## Configurando Toolchain

- Manualmente: Downloading/building/installing componentes Manualmente
- Build System: utilizando um buildsystem como Buildroot ou Yocto

