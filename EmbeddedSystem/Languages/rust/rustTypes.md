# Primitivas e Tipos de Variáveis em Rust

Rust possui um sistema de tipos forte e estático, o que significa que o tipo de uma variável deve ser conhecido em tempo de compilação. Abaixo estão as principais primitivas e tipos de variáveis em Rust.

## 1. Tipos Primitivos

### 1.1. Números Inteiros

Rust possui diversos tipos de números inteiros que variam em tamanho e sinal:

| Tipo            | Tamanho             | Intervalo                                               |
| --------------- | ------------------- | ------------------------------------------------------- |
| **i8**    | 8 bits              | −128 a 127                                             |
| **i16**   | 16 bits             | −32.768 a 32.767                                       |
| **i32**   | 32 bits             | −2.147.483.648 a 2.147.483.647                         |
| **i64**   | 64 bits             | −9.223.372.036.854.775.808 a 9.223.372.036.854.775.807 |
| **i128**  | 128 bits            | Não definido (depende do hardware)                     |
| **isize** | Tamanho do ponteiro | Depende da arquitetura (32 ou 64 bits)                  |
| **u8**    | 8 bits              | 0 a 255                                                 |
| **u16**   | 16 bits             | 0 a 65.535                                              |
| **u32**   | 32 bits             | 0 a 4.294.967.295                                       |
| **u64**   | 64 bits             | 0 a 18.446.744.073.709.551.615                          |
| **u128**  | 128 bits            | Não definido (depende do hardware)                     |
| **usize** | Tamanho do ponteiro | Depende da arquitetura (32 ou 64 bits)                  |

```rust
let a: i8 = 100;
let b: u32 = 300000;
let c: i64 = -50000;
let d: isize = 42; // depende da arquitetura
```

#### Uso do Substituto de Dígitos com `_`

O uso do sublinhado (`_`) permite que você agrupe os dígitos em números inteiros e de ponto flutuante, tornando-os mais fáceis de ler e interpretar. É especialmente útil quando se trabalha com números que possuem muitos dígitos.

```rust
fn main() {
    let numero_grande: i32 = 1_000_000; // Um milhão
    let pi: f64 = 3.141_592_653_589_793; // Valor de Pi
    let binario: u32 = 0b1111_1111; // 255 em binário
    let hexadecimal: u32 = 0xFF_FF_FF; // 16777215 em hexadecimal
    let octal: u32 = 0o77_77; // 511 em octal
}
```

- **Não pode começar ou terminar com `_`**: Um número não pode começar ou terminar com o sublinhado. Por exemplo, `_1000` e `1000_` não são válidos.
- **Não pode haver dois sublinhados consecutivos**: Você não pode usar `_` duas vezes seguidas. Por exemplo, `1__000` não é válido.

### 1.2. Números de Ponto Flutuante

- **f32**: número de ponto flutuante de 32 bits
- **f64**: número de ponto flutuante de 64 bits (padrão)

```rust
let pi: f32 = 3.14;
let e: f64 = 2.718281828459045;
```

### 1.3. Booleano

- **bool**: representa um valor booleano (`true` ou `false`).

```rust
let is_rust_fun: bool = true;
let is_sunny: bool = false;
```

### 1.4. Caractere

- **char**: representa um único caractere Unicode (ex.: `'a'`, `'α'`, `'1'`).
- Note o uso da aspas simples 

```rust
let letter: char = 'R';
let emoji: char = '😊';
let digit: char = '5';
```

## 2. Tipos Compostos

### 2.1. Tuplas

As tuplas permitem agrupar valores de diferentes tipos. Exemplo:

```rust
let tupla: (i32, f64, char) = (500, 6.4, 'a');
println!("{:?}", tupla);
let (x, y, z) = tupla; // Desestruturação
println!("x: {}, y: {}, z: {}", x, y, z);
```

### 2.2. Arrays

Os arrays são coleções de valores do mesmo tipo. Exemplo:

```rust
let array: [i32; 5] = [1, 2, 3, 4, 5];
let primeiro = array[0]; // Acessando o primeiro elemento
println!("O primeiro elemento é: {}", primeiro);
```

## 3. Variáveis

### 3.1. Declaração

Para declarar uma variável em Rust, utiliza-se a palavra-chave `let`:

```rust
let x: i32 = 5;
```

### 3.2. Imutabilidade

Por padrão, as variáveis em Rust são imutáveis. Para torná-las mutáveis, use a palavra-chave `mut`:

```rust
let mut y: i32 = 10;
y = 15; // Agora é permitido
```

### 3.3. Tipo Inferido

Rust pode inferir o tipo de uma variável:

```rust
let z = 20; // Rust infere que z é do tipo i32
```
