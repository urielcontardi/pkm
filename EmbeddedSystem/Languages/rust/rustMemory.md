# Memória em Rust: Stack, Heap e Static

A gestão de memória em Rust envolve três conceitos principais: *stack* (pilha), *heap* (montão) e *static* (memória estática). Cada um tem suas características, vantagens e desvantagens. Vamos explorar cada um deles.

## 1. Stack (Pilha)

### 1.1. O que é Stack?

A pilha é uma área de memória que armazena dados de forma estruturada, seguindo a ordem LIFO (Last In, First Out). É usada para armazenar variáveis de tamanho fixo e estruturas de dados que têm um tempo de vida conhecido e limitado, como exemplo:

* Argumentos de funcoes
* Variáveis locais
* Cada Thread possui uma stack isolada

### 1.2. Características da Stack

- **Rápido acesso**: A alocação e desalocação de memória na pilha são rápidas, pois ocorre através do ajuste do ponteiro da pilha.
- **Tamanho fixo**: Os dados armazenados na pilha devem ter um tamanho conhecido em tempo de compilação.
- **Escopo limitado**: As variáveis na pilha são liberadas automaticamente quando saem do escopo.

### 1.3. Exemplo de Stack

```rust
fn main() {
    let x: i32 = 10; // x é armazenado na pilha
    {
        let y: i32 = 20; // y é também armazenado na pilha
        println!("Dentro do escopo: x = {}, y = {}", x, y);
    } // y é liberado aqui
    println!("Fora do escopo: x = {}", x); // y não está mais disponível
}
```

## 2. Heap 

### 2.1. O que é Heap?

A Heap é uma área de memória usada para armazenar dados que precisam ter um tamanho dinâmico ou que têm um tempo de vida que não é conhecido em tempo de compilação. A alocação de memória na heap é feita de forma manual, utilizando o sistema de gerenciamento de memória.

### 2.2. Características do Heap

- **Tamanho dinâmico**: Permite armazenar dados de tamanho variável, como vetores e strings.
- **Acesso mais lento**: O acesso à memória na heap é mais lento em comparação com a pilha, pois envolve a alocação e desalocação de memória, além de acessos indiretos através de ponteiros.
- **Gerenciamento manual**: O programador deve gerenciar a memória, utilizando os conceitos de *ownership* e *borrowing*.

### 2.3. Exemplo de Heap

```rust
fn main() {
    let s: String = String::from("Olá"); // s é armazenado na heap
    let tamanho: usize = s.len();
    println!("O tamanho da string é: {}", tamanho);
} // s é liberado aqui
```

## 3. Static (Memória Estática)

### 3.1. O que é Static?

A memória estática é uma área de memória que contém dados que têm um tempo de vida equivalente ao da aplicação. Esses dados são alocados em tempo de compilação e permanecem disponíveis durante toda a execução do programa.

### 3.2. Características da Memória Estática

- **Tempo de vida constante**: Os dados estão disponíveis durante toda a execução do programa.
- **Acesso rápido**: O acesso à memória estática é rápido, semelhante ao da pilha.
- **Não mutável**: Geralmente, os dados estáticos são imutáveis, mas você pode ter referências mutáveis a eles em contextos específicos.

### 3.3. Exemplo de Static

```rust
static NOME: &str = "Rust"; // NOME é armazenado na memória estática

fn main() {
    println!("A linguagem é: {}", NOME);
}
```

## 4. Comparação entre Stack, Heap e Static

| Característica | Stack                | Heap                        | Static                    |
| --------------- | -------------------- | --------------------------- | ------------------------- |
| Alocação      | Automática, rápida | Manual, mais lenta          | Compilação, constante   |
| Tamanho         | Fixos                | Dinâmico                   | Fixo                      |
| Tempo de vida   | Escopo limitado      | Controlado pelo programador | Durante toda a execução |
| Acesso          | Rápido              | Mais lento                  | Rápido                   |
