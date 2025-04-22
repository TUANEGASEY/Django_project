# Types of data
# 1. Integers
int = 0
# 2. Floats
float = 1.5
# 3. Strings
str = "Sou lindo"
# 4. Booleans
bool = False
# 5. Lists
list = ["um", 2, True, 4.5, [1, 2, 3], {"um": 1, "dois": 2}, (1, 2, 3), {1, 2, 3}, None]
# 6. Tuples
tuple = (1, 2, 3, 4, 5, 5, 7, 8, 9, 10) #não pode ser modificado, mas pode ter valores duplicados
# 7. Dictionaries
dict = {"um": 1,
        "dois": 2, 
        "três": 3, 
        "quatro": 4, 
        "cinco": 5, 
        "seis": 6}
# 8. Sets
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} #não pode ter valores duplicados, ou elementos que podem ser modificados
# 9. None
none = None
# 10. Bytes
bytes = b"Sou lindo" or bytes("Sou lindo")
                    # bytes são imutáveise, ou seja, não podem ser alterados após a criação. Eles são usados para armazenar dados binários, como imagens ou arquivos de áudio.
                    # bytes são representados por uma sequência de números inteiros entre 0 e 255, onde cada número representa um byte. Eles podem ser criados usando a função bytes() ou prefixando uma string com b, como no exemplo acima.
                    # bytes são úteis quando precisamos trabalhar com dados binários, como arquivos de imagem ou áudio, ou quando precisamos enviar dados pela rede. Eles também podem ser usados para representar strings em codificações específicas, como UTF-8 ou ASCII.
print(bytes)

# 11. Bytearrays
bytearray = bytearray(b"Sou lindo") # bytearrays são bytes mutáveis.

# 12. Memoryviews
memoryview = memoryview(b"Sou lindo") # memoryviews são uma maneira de acessar os dados de um objeto bytes ou bytearray sem fazer uma cópia dos dados. Eles permitem que você trabalhe com partes específicas dos dados, em vez de ter que copiar todo o objeto.
# memoryviews são úteis quando você precisa trabalhar com grandes quantidades de dados e não quer desperdiçar memória fazendo cópias desnecessárias. Eles também podem ser usados para compartilhar dados entre diferentes partes do seu código sem precisar fazer cópias.
# memoryviews são criados usando a função memoryview() e podem ser usados para acessar partes específicas dos dados, como no exemplo acima. Eles também podem ser usados para modificar os dados subjacentes, se o objeto original for mutável.

# 13. Complex numbers
complex = 1 + 2j # números complexos são representados por uma parte real e uma parte imaginária, separadas por um sinal de adição ou subtração. Eles podem ser criados usando a função complex() ou usando a notação a + bj, onde a é a parte real e b é a parte imaginária.
# números complexos são úteis em matemática, física e engenharia, onde muitos problemas envolvem números complexos. Eles também podem ser usados em gráficos e visualizações, onde a parte real e a parte imaginária podem ser usadas para representar coordenadas em um plano complexo.

# 14. Functions
def funcao():
    return "Sou lindo" # funções são blocos de código que podem ser chamados para executar uma tarefa específica. Elas podem ter parâmetros de entrada e retornar valores de saída. As funções são úteis para organizar o código, reutilizar código e tornar o código mais legível.

# 15. Classes
class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome # classes são modelos para criar objetos. Elas podem ter atributos (variáveis) e métodos (funções) associados a elas. As classes são úteis para organizar o código, encapsular dados e comportamentos e criar objetos que representam entidades do mundo real.

# 16. Modules
# módulos são arquivos que contêm código Python. Eles podem conter funções, classes e variáveis que podem ser importadas e usadas em outros arquivos. Os módulos são úteis para organizar o código, reutilizar código e compartilhar código entre diferentes partes do seu projeto.
import math  # módulo matemático embutido

# 17. Exceptions
# exceções são erros que ocorrem durante a execução do código. Elas podem ser tratadas usando blocos try/except, que permitem capturar e lidar com erros de forma controlada. As exceções são úteis para lidar com erros inesperados e garantir que o código continue funcionando mesmo quando ocorrem erros.
try:
    1 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")
# 18. Files
# arquivos são usados para armazenar dados de forma persistente. Eles podem ser lidos e escritos usando funções embutidas, como open(), read() e write(). Os arquivos são úteis para armazenar dados que precisam ser acessados em diferentes execuções do programa, como configurações, logs ou dados de entrada/saída.
with open("meuarquivo.txt", "w") as f:
    f.write("Sou lindo") # o comando with é usado para abrir um arquivo e garantir que ele seja fechado corretamente após o uso. O modo "w" indica que o arquivo será aberto para escrita, e se o arquivo já existir, seu conteúdo será sobrescrito. O método write() é usado para escrever dados no arquivo.
        # 18.1 File objects
        # file objects são objetos que representam arquivos abertos. Eles têm métodos para ler e escrever dados no arquivo, como read(), write() e close(). Os file objects são úteis para trabalhar com arquivos de forma eficiente e garantir que os arquivos sejam fechados corretamente após o uso.
        # 18.2 File descriptors
        # file descriptors são números inteiros que representam arquivos abertos no sistema operacional. Eles são usados para identificar arquivos abertos e podem ser usados em operações de baixo nível, como leitura e escrita em arquivos. Os file descriptors são úteis para trabalhar com arquivos de forma eficiente e garantir que os arquivos sejam fechados corretamente após o uso.
        # 18.3 File-like objects
        # file-like objects são objetos que se comportam como arquivos, mas não são necessariamente arquivos físicos no sistema de arquivos. Eles podem ser usados para ler e escrever dados em memória ou em outros tipos de armazenamento. Os file-like objects são úteis para trabalhar com dados de forma eficiente e garantir que os dados sejam manipulados corretamente.
        # 18.4 File systems
        # sistemas de arquivos são estruturas que organizam e armazenam arquivos em um dispositivo de armazenamento, como um disco rígido ou uma unidade flash. Eles permitem que os usuários criem, leiam, escrevam e excluam arquivos, além de organizar os arquivos em diretórios e pastas. Os sistemas de arquivos são essenciais para o funcionamento do sistema operacional e para o gerenciamento de dados.
        # 18.5 File paths
        # caminhos de arquivo são strings que representam a localização de um arquivo em um sistema de arquivos. Eles podem ser absolutos (começando do diretório raiz) ou relativos (começando do diretório atual). Os caminhos de arquivo são úteis para localizar e acessar arquivos em um sistema de arquivos.
        # 18.6 File names
        # nomes de arquivo são strings que representam o nome de um arquivo em um sistema de arquivos. Eles podem incluir a extensão do arquivo (como .txt ou .jpg) e podem ser usados para identificar e acessar arquivos em um sistema de arquivos. Os nomes de arquivo são úteis para organizar e localizar arquivos em um sistema de arquivos.
        # 18.7 File types
        # tipos de arquivo são categorias que descrevem o formato e o conteúdo de um arquivo. Eles podem incluir texto, imagem, áudio, vídeo e outros tipos de dados. Os tipos de arquivo são úteis para identificar e acessar arquivos em um sistema de arquivos e para determinar como os arquivos devem ser manipulados.
        # 18.8 File encodings
        # codificações de arquivo são métodos usados para representar dados em um arquivo. Elas podem incluir ASCII, UTF-8, UTF-16 e outros formatos de codificação. As codificações de arquivo são úteis para garantir que os dados sejam armazenados e lidos corretamente em diferentes sistemas e plataformas.
        # 18.9 File permissions
        # permissões de arquivo são configurações que determinam quem pode acessar e modificar um arquivo em um sistema de arquivos. Elas podem incluir permissões de leitura, gravação e execução para diferentes usuários e grupos. As permissões de arquivo são úteis para garantir a segurança e a privacidade dos dados em um sistema de arquivos.
        # 18.10 File ownership
        # propriedade de arquivo é a configuração que determina quem é o proprietário de um arquivo em um sistema de arquivos. O proprietário de um arquivo tem permissões especiais para acessar e modificar o arquivo. A propriedade de arquivo é útil para garantir a segurança e a privacidade dos dados em um sistema de arquivos.
        # 18.11 File attributes
        # atributos de arquivo são configurações que descrevem as características de um arquivo em um sistema de arquivos. Eles podem incluir o tamanho do arquivo, a data de criação, a data de modificação e outros metadados. Os atributos de arquivo são úteis para identificar e acessar arquivos em um sistema de arquivos e para determinar como os arquivos devem ser manipulados.
        # 18.12 File metadata
        # metadados de arquivo são informações adicionais sobre um arquivo em um sistema de arquivos. Eles podem incluir o tamanho do arquivo, a data de criação, a data de modificação e outros atributos. Os metadados de arquivo são úteis para identificar e acessar arquivos em um sistema de arquivos e para determinar como os arquivos devem ser manipulados.
        # 18.13 File streams
        # fluxos de arquivo são sequências de dados que podem ser lidas ou escritas em um arquivo. Eles podem incluir dados de texto, imagem, áudio, vídeo e outros tipos de dados. Os fluxos de arquivo são úteis para trabalhar com dados de forma eficiente e garantir que os dados sejam manipulados corretamente.
        # 18.14 File buffers
        # buffers de arquivo são áreas de memória usadas para armazenar temporariamente dados lidos ou escritos em um arquivo. Eles são usados para melhorar o desempenho das operações de leitura e escrita em arquivos, permitindo que os dados sejam processados em blocos em vez de byte a byte. Os buffers de arquivo são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 18.15 File locks
        # bloqueios de arquivo são mecanismos usados para controlar o acesso a um arquivo em um sistema de arquivos. Eles podem ser usados para garantir que apenas um processo possa acessar um arquivo de cada vez, evitando conflitos e corrupção de dados. Os bloqueios de arquivo são úteis para garantir a segurança e a integridade dos dados em um sistema de arquivos.
        # 18.16 File handles
        # manipuladores de arquivo são objetos que representam um arquivo aberto em um sistema de arquivos. Eles podem ser usados para ler e escrever dados no arquivo, além de controlar o acesso ao arquivo. Os manipuladores de arquivo são úteis para trabalhar com arquivos de forma eficiente e garantir que os arquivos sejam fechados corretamente após o uso.

# 19. Generators
# geradores são funções que podem ser usadas para criar iteradores. Eles permitem que você crie sequências de dados de forma eficiente, gerando os dados sob demanda em vez de armazená-los todos na memória. Os geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
def gerador():
    yield 1
    yield 2
    yield 3
        # gerador é uma função que usa a palavra-chave yield para gerar valores sob demanda. Quando a função é chamada, ela retorna um objeto gerador que pode ser iterado para obter os valores gerados. Os geradores são úteis para criar sequências de dados de forma eficiente e garantir que os dados sejam manipulados corretamente.
        # 19.1 Generator expressions
        # expressões geradoras são uma forma concisa de criar geradores usando uma sintaxe semelhante a listas. Elas permitem que você crie sequências de dados de forma eficiente, gerando os dados sob demanda em vez de armazená-los todos na memória. As expressões geradoras são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
gerador_expressao = (x for x in range(10)) # expressão geradora que gera números de 0 a 9
        # 19.2 Generator functions
        # funções geradoras são funções que usam a palavra-chave yield para gerar valores sob demanda. Elas permitem que você crie sequências de dados de forma eficiente, gerando os dados sob demanda em vez de armazená-los todos na memória. As funções geradoras são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.3 Generator objects
        # objetos geradores são instâncias de funções geradoras que podem ser iteradas para obter os valores gerados. Eles permitem que você crie sequências de dados de forma eficiente, gerando os dados sob demanda em vez de armazená-los todos na memória. Os objetos geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.4 Generator iterators
        # iteradores geradores são objetos que implementam o protocolo de iteração, permitindo que você itere sobre os valores gerados. Eles permitem que você crie sequências de dados de forma eficiente, gerando os dados sob demanda em vez de armazená-los todos na memória. Os iteradores geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.5 Generator protocols
        # protocolos de geradores são regras que definem como os geradores devem se comportar. Eles incluem métodos como __iter__() e __next__(), que permitem que os geradores sejam iterados e usados em loops for. Os protocolos de geradores são úteis para garantir que os geradores funcionem corretamente e sejam compatíveis com outras partes do código.
        # 19.6 Generator methods
        # métodos de geradores são funções que podem ser chamadas em objetos geradores para controlar seu comportamento. Eles incluem métodos como send(), throw() e close(), que permitem que você interaja com os geradores de forma mais avançada. Os métodos de geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.7 Generator expressions vs. generator functions
        # expressões geradoras são uma forma concisa de criar geradores usando uma sintaxe semelhante a listas, enquanto funções geradoras usam a palavra-chave yield para gerar valores sob demanda. Ambas as abordagens permitem que você crie sequências de dados de forma eficiente, mas as expressões geradoras são mais concisas e fáceis de ler.
        # 19.8 Generator performance
        # desempenho de geradores é geralmente melhor do que o desempenho de listas, pois os geradores geram os dados sob demanda em vez de armazená-los todos na memória. Isso significa que os geradores podem ser usados para trabalhar com grandes quantidades de dados sem consumir muita memória. No entanto, o desempenho dos geradores pode variar dependendo do tipo de dados e da complexidade do código.
        # 19.9 Generator use cases
        # casos de uso de geradores incluem processamento de grandes quantidades de dados, criação de sequências de dados sob demanda e otimização do uso da memória. Os geradores são úteis para trabalhar com dados em tempo real, como streaming de vídeo ou áudio, e para criar algoritmos eficientes que podem lidar com grandes quantidades de dados sem consumir muita memória.
        # 19.10 Generator libraries
        # bibliotecas de geradores são bibliotecas que fornecem funções e classes para trabalhar com geradores. Elas podem incluir funções para criar geradores, manipular geradores e otimizar o desempenho dos geradores. As bibliotecas de geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.11 Generator frameworks
        # frameworks de geradores são estruturas que fornecem suporte para trabalhar com geradores em projetos maiores. Eles podem incluir ferramentas para otimizar o desempenho dos geradores, manipular geradores e integrar geradores com outras partes do código. Os frameworks de geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.12 Generator patterns
        # padrões de geradores são abordagens comuns para trabalhar com geradores em projetos. Eles podem incluir padrões de design, como o padrão produtor-consumidor, que descreve como os geradores podem ser usados para produzir e consumir dados de forma eficiente. Os padrões de geradores são úteis para trabalhar com grandes quantidades de dados e garantir que os dados sejam manipulados corretamente.
        # 19.13 Generator best practices
        # melhores práticas para trabalhar com geradores incluem otimizar o desempenho dos geradores, garantir que os geradores sejam fechados corretamente após o uso e usar expressões geradoras quando apropriado. As melhores práticas para trabalhar com geradores são úteis para garantir que os dados sejam manipulados corretamente e que o código seja eficiente e legível.
        # 19.14 Generator debugging
        # depuração de geradores é o processo de identificar e corrigir erros em geradores. Isso pode incluir o uso de ferramentas de depuração, como o pdb, para inspecionar o estado dos geradores e identificar problemas. A depuração de geradores é útil para garantir que os dados sejam manipulados corretamente e que o código funcione conforme o esperado.
        # 19.15 Generator testing
        # testes de geradores são o processo de verificar se os geradores funcionam conforme o esperado. Isso pode incluir a criação de testes automatizados para verificar o comportamento dos geradores e garantir que eles produzam os resultados corretos. Os testes de geradores são úteis para garantir que os dados sejam manipulados corretamente e que o código funcione conforme o esperado.
        # 19.16 Generator debugging tools
        # ferramentas de depuração de geradores são ferramentas que ajudam a identificar e corrigir erros em geradores. Elas podem incluir ferramentas de depuração, como o pdb, que permitem inspecionar o estado dos geradores e identificar problemas. As ferramentas de depuração de geradores são úteis para garantir que os dados sejam manipulados corretamente e que o código funcione conforme o esperado.
        # 19.17 Generator debugging techniques
        # técnicas de depuração de geradores são abordagens comuns para identificar e corrigir erros em geradores. Elas podem incluir o uso de ferramentas de depuração, como o pdb, para inspecionar o estado dos geradores e identificar problemas. As técnicas de depuração de geradores são úteis para garantir que os dados sejam manipulados corretamente e que o código funcione conforme o esperado.
        # 19.18 Generator debugging best practices
        # melhores práticas de depuração de geradores incluem o uso de ferramentas de depuração, como o pdb, para inspecionar o estado dos geradores e identificar problemas. As melhores práticas de depuração de geradores são úteis para garantir que os dados sejam manipulados corretamente e que o código funcione conforme o esperado.


# 20. Coroutines
# corrotinas são funções que podem ser usadas para criar concorrência em Python. Elas permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam executadas enquanto a corrotina está pausada. As corrotinas são úteis para trabalhar com tarefas assíncronas e garantir que o código seja eficiente e responsivo.
def corrotina():
    yield 1
    yield 2
    yield 3
        # corrotinas são funções que usam a palavra-chave yield para gerar valores sob demanda. Elas permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam executadas enquanto a corrotina está pausada. As corrotinas são úteis para trabalhar com tarefas assíncronas e garantir que o código seja eficiente e responsivo.
        # 20.1 Coroutine functions
        # funções de corrotina são funções que usam a palavra-chave yield para gerar valores sob demanda. Elas permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam executadas enquanto a corrotina está pausada. As funções de corrotina são úteis para trabalhar com tarefas assíncronas e garantir que o código seja eficiente e responsivo.
        # 20.2 Coroutine objects
        # objetos de corrotina são instâncias de funções de corrotina que podem ser iteradas para obter os valores gerados. Eles permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam executadas enquanto a corrotina está pausada. Os objetos de corrotina são úteis para trabalhar com tarefas assíncronas e garantir que o código seja eficiente e responsivo.
        # 20.3 Coroutine protocols
        # protocolos de corrotina são regras que definem como as corrotinas devem se comportar. Eles incluem métodos como __iter__() e __next__(), que permitem que as corrotinas sejam iteradas e usadas em loops for. Os protocolos de corrotina são úteis para garantir que as corrotinas funcionem corretamente e sejam compatíveis com outras partes do código.
        # 20.4 Coroutine methods
        # métodos de corrotina são funções que podem ser chamadas em objetos de corrotina para controlar seu comportamento. Eles incluem métodos como send(), throw() e close(), que permitem que você interaja com as corrotinas de forma mais avançada. Os métodos de corrotina são úteis para trabalhar com tarefas assíncronas e garantir que o código seja eficiente e responsivo.
        # 20.5 Coroutine expressions
        # expressões de corrotina são uma forma concisa de criar corrotinas usando uma sintaxe semelhante a listas. Elas permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam
        # 20.6 Coroutine iterators
        # iteradores de corrotina são objetos que implementam o protocolo de iteração, permitindo que você itere sobre os valores gerados. Eles permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam
        # 20.7 Coroutine performance
        # desempenho de corrotinas é geralmente melhor do que o desempenho de funções normais, pois as corrotinas permitem que você pause e retome a execução de uma função, permitindo que outras funções sejam executadas enquanto a corrotina está pausada. Isso significa que as corrotinas podem ser usadas para trabalhar com tarefas assíncronas e garantir que o código seja eficiente e responsivo.

# 21. Async functions
    # A programação assíncrona parece com o paralelismo, mas nela você não vai rodar dois processos ao mesmo tempo. Você vai rodar 1 processo e a medida que ele estiver rodando pode acontecer de ele travar ou ficar em espera por algum motivo. Quando isso acontece se inicia um segundo processo assíncrono.

# 22. Async generators
    # São geradores assíncronos

# 23. Context managers
    # Gerencia o contexto de execução de um bloco de código. O exemplo mais comum é o uso do with para abrir arquivos. O with garante que o arquivo seja fechado corretamente após o uso, mesmo que ocorra um erro durante a leitura ou gravação.
    # O with é usado para abrir um arquivo e garantir que ele seja fechado corretamente após o uso. O modo "w" indica que o arquivo será aberto para escrita, e se o arquivo já existir, seu conteúdo será sobrescrito. O método write() é usado para escrever dados no arquivo.

# 24. Iterators
# 25. Iterables
# 26. Itertools

# 25. Mappings
    # São objetos que associam chaves a valores. O exemplo mais comum é o dicionário, onde as chaves são usadas para acessar os valores correspondentes.

# 26. Sequences
    # São objetos que podem ser indexados e fatiados. O exemplo mais comum é a lista, onde os elementos podem ser acessados por seus índices.

# 28. Views
    # São objetos que fornecem uma visão de um objeto, permitindo acessar e modificar os dados subjacentes. O exemplo mais comum é a view de um dicionário, onde as chaves e valores podem ser acessados e modificados.
