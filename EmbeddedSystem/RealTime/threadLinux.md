# Mapeamento de Threads no Espaço do Kernel

Espaço de Usuário vs. Espaço do Kernel:

* O espaço de usuário é onde os aplicativos (como navegadores, editores de texto, etc.) rodam, com certas restrições de segurança para evitar danos ao sistema.
* O espaço do kernel é onde o núcleo do sistema operacional roda e gerencia recursos de baixo nível, como memória, processos, e dispositivos.

Quando um programa cria threads adicionais usando a API POSIX, o Linux usa o NPTL para mapear essas threads diretamente como tarefas no espaço do kernel. Isso oferece uma combinação de benefícios:

* **Proteção:** Como o código do aplicativo ainda roda no espaço de usuário, ele não pode corromper diretamente o kernel ou outros processos.
* **Eficiência:** Porque as threads são tratadas como tarefas do kernel, elas podem ser escalonadas e gerenciadas eficientemente pelo kernel, aproveitando o suporte para multitarefa do sistema operacional.

Em resumo, o Linux usa uma abordagem onde threads de espaço de usuário (criados por programas) são mapeadas diretamente para tarefas no espaço do kernel através da NPTL.
