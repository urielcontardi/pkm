# Structs em Rust

## 1. Definição de Struct

As **structs** permitem agrupar dados relacionados em um único tipo composto. Existem três tipos:

- **Struct Clássica**: Campos nomeados.

  ```rust
  struct Pessoa {
      nome: String,
      idade: u32,
  }
  ```
- **Tuple Struct**: Campos sem nome.

  ```rust
  struct Ponto(i32, i32);
  ```
- **Unit Struct**: Não possui campos, usada como marcador.

  ```rust
  struct Marcador;
  ```

## 2. Bloco `impl`

Usado para definir **métodos** e **funções associadas** para uma struct.

- **Método** (função associada à instância):

```rust
impl Pessoa {
    fn descricao(&self) -> String {
        format!("{} tem {} anos.", self.nome, self.idade)
    }
}
```

Aqui está um exemplo de uma `struct` com sua implementação (`impl`) e como utilizá-la na função `main`:

```rust
// Definindo a struct Pessoa
struct Pessoa {
    nome: String,
    idade: u32,
}

// Implementando métodos para a struct Pessoa
impl Pessoa {
    // Função associada para criar uma nova instância de Pessoa
    fn nova(nome: String, idade: u32) -> Pessoa {
        Pessoa { nome, idade }
    }

    // Método para retornar uma descrição da pessoa
    fn descricao(&self) -> String {
        format!("{} tem {} anos.", self.nome, self.idade)
    }

    // Método para modificar a idade
    fn set_idade(&mut self, nova_idade: u32) {
        self.idade = nova_idade;
    }
}

fn main() {
    // Criando uma nova instância de Pessoa
    let mut pessoa = Pessoa::nova(String::from("Alice"), 30);

    // Exibindo a descrição da pessoa
    println!("{}", pessoa.descricao());

    // Alterando a idade da pessoa
    pessoa.set_idade(35);
    
    // Exibindo a descrição atualizada
    println!("{}", pessoa.descricao());
}
```
