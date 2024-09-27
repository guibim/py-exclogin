# py-exclogin
## Teste simples de login e logout no site para testes The Internet
Arquivo teste-headless feito para executar sem a necessidade da interface gráfica do navegador.

## Ferramentas utilizadas
Vscode <br /> 
Python <br /> 
Selenium <br /> 
ChromeDriver <br /> 

## GHERKIN - BDD

### Funcionalidade: Testar a funcionalidade de login no site "The Internet" <br /> 
  Como usuário do sistema <br /> 
  Quero testar o login com credenciais válidas e inválidas <br /> 
  Para verificar se o sistema responde corretamente e realiza o logout  <br /> 

 ### Cenário 1: Login com credenciais inválidas
    Given que estou na página de login 
    When eu insiro um nome de usuário inválido "usuarioteste" 
    And eu insiro uma senha inválida "senhateste" 
    And eu clico no botão de login 
    Then vejo uma mensagem de erro informando "Seu nome de usuário é inválido!" 

 ### Cenário 2: Login com credenciais válidas
    Given que estou na página de login 
    When eu insiro um nome de usuário válido "tomsmith" 
    And eu insiro uma senha válida "SuperSecretPassword!" 
    And eu clico no botão de login 
    Then vejo uma mensagem de sucesso informando "Você fez login com sucesso!" 
    And eu clico no botão de logout 
    Then sou redirecionado para a página de login 
