# Documento de Requisitos — Sistema Bancário Funcional

## Papéis
- **Usuário (Cliente):** Interage com o sistema para criar contas, realizar depósitos, saques e consultar extratos.  
- **Sistema:** Processa as requisições do usuário e mantém histórico das transações.  

---

## 👥 Papeis da equipe

|   Integrantes     |Matrícula  |           Papeis           |
|-------------------|-----------|----------------------------|
| Rafael            |2318845    |documentação dos requisitos | 
| Felipe Paixão     |2318845    |implementação do código     | 
| Alexandre Oliveira|2318845    |implementação do código     | 
| Regison           |2318845    |testes unitários            | 
| Elton             |2318845    |testes de integração        | 



---

## Como rodar

### Cria ambiente virtual para rodar dependências 
```bash
poetry shell
```

### Instala dependências
```bash
poetry install
```

### Executa o código
```bash
task run
```

### Executa os testes
```bash
task run_tests
```


---

## Requisitos Funcionais
1. O sistema deve permitir criar clientes.  
   - Implementado em `criar_cliente`.  

2. O sistema deve permitir criar contas vinculadas a clientes.  
   - Implementado em `criar_conta` e closure `gerador_conta`.  

3. O sistema deve permitir depósitos em conta.  
   - Implementado em `depositar`.  

4. O sistema deve permitir saques respeitando limite de valor e quantidade.  
   - Implementado em `sacar`.  

5. O sistema deve registrar cada transação no histórico.  
   - Implementado em `registrar_transacao`.  

6. O sistema deve permitir consulta do extrato.  
   - Implementado em `extrato` (usa list comprehension).  

7. O sistema deve permitir filtrar clientes por CPF.  
   - Implementado em `filtrar_cliente` (lambda).  

8. O sistema deve permitir execução genérica de transações.  
   - Implementado em `executar_transacao` (função de alta ordem).  

---

## Requisitos Não Funcionais
1. O sistema deve executar sem erros.  
   - Validado pelos testes unitários (`pytest`).  

2. O sistema deve ser implementado utilizando conceitos de Programação Funcional.  
   - **Função lambda:** `filtrar_cliente`.  
   - **List comprehension:** `extrato`.  
   - **Closure:** `gerar_numero_conta`.  
   - **Função de alta ordem:** `executar_transacao`.  

---

## Cobertura dos requisitos
- Todos os requisitos funcionais e não funcionais foram mapeados para funções existentes no código.  
- Casos de testes em `testes.py` garantem a execução sem erros.  
