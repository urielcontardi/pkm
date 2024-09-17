## Principais Comandos do Linux

- **`cd`**: Muda o diretório atual de trabalho. Exemplos:

  - `cd /home/user`: Acessa o diretório `/home/user`.
  - `cd ..`: Sobe um nível no diretório.
- **`mkdir`**: Cria novos diretórios. Exemplo:

  - `mkdir projetos`: Cria um diretório chamado `projetos`.
- **`mv`**: Move ou renomeia arquivos e diretórios. Exemplos:

  - `mv arquivo.txt /home/user`: Move `arquivo.txt` para o diretório `/home/user`.
  - `mv arquivo.txt novo_nome.txt`: Renomeia o arquivo `arquivo.txt` para `novo_nome.txt`.
- **`echo`**: Exibe uma mensagem ou o conteúdo de uma variável. Exemplo:

  - `echo "Olá, Mundo!"`: Exibe a mensagem "Olá, Mundo!" no terminal.
- **`cat`**: Exibe o conteúdo de arquivos no terminal. Exemplo:

  - `cat arquivo.txt`: Mostra o conteúdo de `arquivo.txt`.
- **`pwd`**: Mostra o diretório atual de trabalho. Exemplo:

  - `pwd`: Exibe o caminho completo do diretório atual.
- **`ls`**: Lista arquivos e diretórios no diretório atual. Exemplos:

  - `ls`: Lista os arquivos e pastas.
  - `ls -la`: Lista arquivos e pastas com detalhes, incluindo ocultos.
- **`rm`**: Remove arquivos ou diretórios. Exemplo:

  - `rm arquivo.txt`: Remove o arquivo `arquivo.txt`.
  - `rm -r pasta`: Remove a pasta `pasta` e seu conteúdo recursivamente.
- **`cp`**: Copia arquivos ou diretórios. Exemplos:

  - `cp arquivo.txt /home/user`: Copia `arquivo.txt` para o diretório `/home/user`.
  - `cp -r pasta /home/user`: Copia a pasta `pasta` e seu conteúdo para `/home/user`.
- **`touch`**: Cria um arquivo vazio ou atualiza a data de modificação de um arquivo. Exemplo:

  - `touch novo_arquivo.txt`: Cria um arquivo vazio chamado `novo_arquivo.txt`.
- **`man`**: Exibe o manual de um comando. Exemplo:

  - `man ls`: Mostra o manual completo do comando `ls`, com detalhes sobre suas opções e uso.

## O Comando `grep`

- **`grep`**: O `grep` é um dos comandos mais úteis no Linux para buscar texto dentro de arquivos ou na saída de outros comandos. Ele procura por padrões específicos usando expressões regulares.

### Exemplos:

- **Buscar uma palavra em um arquivo**:

  - `grep "palavra" arquivo.txt`: Procura pela string "palavra" dentro de `arquivo.txt`.
- **Buscar de forma insensível ao caso**:

  - `grep -i "palavra" arquivo.txt`: Ignora diferenças entre maiúsculas e minúsculas durante a busca.
- **Buscar em vários arquivos**:

  - `grep "palavra" *.txt`: Procura pela string "palavra" em todos os arquivos `.txt` no diretório atual.
- **Buscar linhas que não contenham o padrão**:

  - `grep -v "palavra" arquivo.txt`: Mostra todas as linhas que **não** contêm "palavra".
- **Mostrar o número das linhas**:

  - `grep -n "palavra" arquivo.txt`: Mostra o número das linhas onde o padrão foi encontrado.

O `grep` é bastante poderoso e oferece várias opções para buscas avançadas, incluindo suporte para expressões regulares e combinações de padrões.

## Permissões de Arquivos no Linux

No Linux, cada arquivo ou diretório tem permissões associadas, que controlam quem pode ler, escrever ou executar o arquivo. As permissões são atribuídas a três tipos de usuários:

- **Usuário**: O dono do arquivo.
- **Grupo**: Um grupo de usuários que têm permissões específicas para o arquivo.
- **Outros**: Todos os outros usuários no sistema.

### Tipos de Permissões

Cada arquivo ou diretório pode ter três tipos de permissões:

- **Leitura (`r`)**: Permite ler o conteúdo do arquivo ou listar o conteúdo de um diretório.
- **Escrita (`w`)**: Permite modificar o arquivo ou adicionar/remover arquivos de um diretório.
- **Execução (`x`)**: Permite executar o arquivo (se for um script ou programa) ou acessar um diretório.

### Visualizando Permissões

Para visualizar as permissões de um arquivo ou diretório, use o comando `ls -l`

Aqui está uma explicação da saída:

- O primeiro caractere indica o tipo do arquivo (`-` para arquivos regulares, `d` para diretórios).
- Os próximos três caracteres (`rwx`) são as permissões do **usuário** (leitura, escrita e execução).
- Os próximos três caracteres (`r-x`) são as permissões do **grupo**.
- Os últimos três caracteres (`r--`) são as permissões para **outros**.

### Alterando Permissões

Para alterar permissões, use o comando `chmod`. Existem duas formas principais de usar o `chmod`:

- **Modo simbólico**:

  - `chmod u+x arquivo.sh`: Adiciona permissão de execução para o **usuário** (dono do arquivo).
  - `chmod g-w arquivo.sh`: Remove permissão de escrita do **grupo**.
- **Modo numérico**:
  Cada permissão tem um valor numérico associado:

  - `r = 4`
  - `w = 2`
  - `x = 1`

  Para definir as permissões diretamente, você pode usar uma combinação desses valores. Exemplo:

  - `chmod 755 arquivo.sh`: Define permissões como `rwxr-xr-x`, o que significa que o **usuário** tem todas as permissões, enquanto o **grupo** e **outros** têm apenas leitura e execução.

### Alterando Proprietário e Grupo

- **`chown`**: Altera o dono do arquivo. Exemplo:

  - `chown novo_usuario arquivo.txt`: Muda o proprietário de `arquivo.txt` para `novo_usuario`.
- **`chgrp`**: Altera o grupo associado ao arquivo. Exemplo:

  - `chgrp novo_grupo arquivo.txt`: Muda o grupo de `arquivo.txt` para `novo_grupo`.

Entender as permissões de arquivos é essencial para manter a segurança e o controle no sistema Linux.

## Condicionais no Bash

No Bash, estruturas condicionais permitem executar comandos com base em condições. O comando mais comum para isso é o `if`, mas também existem outras construções como `case` e operadores lógicos. A sintaxe básica para um condicional `if` no Bash é:

```bash
if [ condição ]; then
    # comandos se a condição for verdadeira
else
    # comandos se a condição for falsa
fi
```
