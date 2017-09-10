### Relatório do projeto de WEB APIs utilizando o Django REST framework

* **A API deve possuir pelo menos 4 entidades relevantes e relacionadas via
mapeamento objeto relacional;**
    * As entidades escolhidas são referentes a um sistema de gerenciamento de projeto, que integra Gerenciamento de Tempo/Atividades, Gerenciamento de Risco, e Gerenciamento de Aquisições
    * Respectivamente: Task (Tarefa), Category (Categoria de uma tarefa), Risk (Risco) e Purchase (Aquisição)
    * Uma Task pode conter vários riscos e várias aquisições, assim como riscos e aquisições podem ser associados à várias tarefas
    * Todas estão definidas em ```core.models```
* **Pelo menos uma entidade deve ser integrada ao esquema de autenticação do
Django;**
    * Profile (Perfil) foi a entidade escolhida para integração, ela é relacionada com todas as acima no atributo "created_by", que indica qual usuário criou o determinado objeto
    * Além disso, também tem as listas dos respectivos objetos criados
    * Arquivo: ```core.models```
* **Parte da API deve ser somente leitura e parte deve ser acessível apenas para
usuários autenticados;**
    * Os perfis, as categorias e as tarefas podem ser listadas mas os respectivos riscos e aquisições precisam de autenticação
    * Todas as operações de criação, edição e remoção precisam de autenticação para serem realizadas
    * Pacote com todos os arquivos: ```api.core```
* **A API deve ser documentada com Swagger;**
    * A integração foi feita como explicado no README do [repositório](https://github.com/marcgibbons/django-rest-swagger)
    * Arquivo: ```api.urls```
* **Definir e usar critérios de paginação e throttling. Esse último deve diferenciar
usuários autenticados de não atenticados;**
    * Arquivos: ```consili.settings```, ```api.mixins```
* **Implementar para pelo menos 2 entidades: filtros, busca e ordenação;**
    * Como é um processo simples, foi feito um Mixin para tais critérios e os respectivos atributos nos ViewSets e Views, encontrado em ```api.mixins```, e as configurações em ```api.core.viewsets``` e ```api.core.views```
* **Criar testes unitários e de cobertura;**
    * Foram feitos testes simples para integridade de rotas e suas respectivas permissões, além de verificar autenticação em ```api.tests```, as instruções para executá-los está no cabeçalho da classe principal