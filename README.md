![Zomato](images/zomato.jpg)

# 1. Problema de negócio
  A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
  O CEO da empresa, que foi recém contratado, precisa entender melhor o negócio para conseguir tomar as melhores   decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:
## 1. Visão Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?
## 2. Visão Pais
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?
## 3. Visão Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
## 4. Visão Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de um prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
## 5. Visão Tipos culinários
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?
# 2. Premissas assumidas para a análise
1. Marketplace foi o modelo de negócio assumido.
2. As 4 principais visões de negócio foram: Visão Geral, Visão Países, Visão Cidades e Visão Tipos culinários.
# 3. Estratégia da solução
  O painel estratégico foi desenvolvido utilizando as respectivas métricas que refletem as 4 principais visões do modelo de negócio da empresa:
  Visão Geral
1.	Países cadastrados;
2.	Cidades cadastradas;
3.	Restaurantes cadastrados;
4.	Avaliações feitas na plataforma;
5.	Mapa interativo dos restaurantes distribuídos por país.
  Visão Países
6.	Gráfico interativo com os 6 países com mais restaurantes cadastrados;
7.	Gráfico interativo com os 6 países com mais restaurantes cadastrados por cidade;
8.	Gráfico interativo com a média de avaliações feitas por país;
9.	Gráfico interativo com a média de preço de uma refeição para 2 pessoas por país.
  Visão Cidades
10.	Gráfico interativo com as 10 cidades com mais restaurantes cadastrados;
11.	Gráfico interativo com as cidades que possuem restaurantes com avaliação média acima de 4, das 5 possíveis;
12.	Gráfico interativo com as cidades que possuem restaurantes com avaliação média abaixo de 2.5, das 5 possíveis;
13.	Gráfico interativo com as 10 cidades com mais tipos culinários distintos.
  Visão Tipos culinários
14.	Os 5 melhores restaurantes conforme avaliações dos usuários;
15.	Tabela contendo as informações destes restaurantes;
16.	Gráfico interativo com os 10 melhores tipos de culinárias;
17.	Gráfico interativo com os 10 piores tipos de culinárias.
# 4. Top 3 Insights de dados
1.	O país Indonésia tem a maior quantidade de avaliações feitas, mais até que o país Índia, porém valor médio da refeição para 2 pessoas é o mais alto entre os países observados;
2.	O país Índia possui 60% do total de restaurantes da base de dados, porém aproximadamente 54% destes restaurantes receberam avaliações inferiores a 2,5 das 5 possíveis;
3.	A cidade no país Índia que tem mais restaurantes cadastrados não é a capital e sim a cidade de Nagpur. 
# 5. O produto final do projeto
  Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado através desse link: https://leonardo-projetos-fome-zero.streamlit.app//
# 6. Conclusão
  O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.
Da visão de Países, podemos concluir que além de ser um dos países mais populosos do globo, também possui a maior quantidade de restaurantes por cidade.
# 7. Próximo passos
1.  Reduzir o número de métricas;
2.	Criar novos filtros;
3.	Adicionar novas visões de negócio.
