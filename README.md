# Locust Load Test  

## Introdução  
Este é um projeto que disponibiliza a ferramenta **Locust** para teste de carga de forma simples e rápida usando o Docker.

## Pré-requisitos:  
1. git
2. docker
3. docker-compose

## Como usar:  
1. Clone este projeto  
`git clone git@github.com:Delermando/locust-load-test.git`  

2. Entre na pasta do projeto  
    `cd locust-load-test`  

3. Defina o comportamento do testw, editando o arquivo **src/load_test_definition.py** nele você irá especificar o host para o teste, mudando o valor da propriedade **host**. Caso queira definir outras configurações acesse [locust.io](http://docs.locust.io/en/latest/).  
![arquivo de defição do teste]
(https://s32.postimg.org/fww94rmat/image.png)

4. Inicie o container  
    `make run`  

5. Acesse a interface para iniciar o teste de carga `localhost:8089`  
![Interface Web Locust]
(https://s32.postimg.org/uu4q5rzj9/image.png)

6. Defina a quantidade de requisições, numero usuarios simultâneos e clique em **start swarming**  
![Definição de requestes]
(https://s32.postimg.org/morq4qhlx/image.png)

7. Agora acompanhe os resultados do teste  
![Tela final]
(https://s32.postimg.org/4zzzd45ut/image.png)

## Comandos
- make run  
- make kill  
- make rm  
- make restart  