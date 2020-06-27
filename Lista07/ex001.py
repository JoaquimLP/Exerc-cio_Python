"""
1. Explique quando podemos tratar erros do tipo NameError, SyntaxError, TypeError e
SystemError:
"""
"""
Reposta: 

*** exceção NameError ***
Gerado quando um nome local ou global não é encontrado. Isso se aplica apenas a nomes não qualificados. 
O valor associado é uma mensagem de erro que inclui o nome que não pôde ser encontrado.
***** exceção SyntaxError ****
Gerado quando o analisador encontra um erro de sintaxe. Isso pode ocorrer em uma importdeclaração, 
em uma chamada para as funções internas exec() ou eval(), ou ao ler o script inicial ou a entrada padrão 
(também interativamente). Instâncias desta classe têm atributos filename, lineno, offsete textpara facilitar 
o acesso aos detalhes. str() da instância de exceção retorna apenas a mensagem.
**** exceção TypeError ***
Gerado quando uma operação ou função é aplicada a um objeto do tipo inadequado. 
valor associado é uma sequência que fornece detalhes sobre a incompatibilidade de tipos. 
Essa exceção pode ser gerada pelo código do usuário para indicar que uma tentativa de operação em um objeto não 
é suportada e não deve ser. Se um objeto é destinado a suportar uma determinada operação, mas ainda não forneceu 
uma implementação, NotImplementedErroré a exceção apropriada a ser lançada. Passar argumentos do tipo errado 
(por exemplo, passar a listquando um inté esperado) deve resultar em a TypeError, mas passar argumentos com o 
valor errado (por exemplo, um número fora dos limites esperados) deve resultar em a ValueError.
****** exceção SystemError ****** 
Criado quando o intérprete encontra um erro interno, mas a situação não parece tão séria para fazer com que ele 
abandone toda a esperança. O valor associado é uma sequência que indica o que deu errado (em termos de baixo nível). 
Você deve relatar isso ao autor ou mantenedor do seu intérprete Python. Certifique-se de relatar a versão do interpretador 
Python ( sys.version; também é impressa no início de uma sessão interativa do Python), a mensagem de erro exata (o valor 
associado à exceção) e, se possível, a origem do programa que acionou o erro.
"""
