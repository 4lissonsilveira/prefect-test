# Passos para gerar o token do SalesForce

 - Pegue o nome do seu dominio
 - Pegue a chave do client e a senha do client
 - Siga esses passos: https://developer.salesforce.com/docs/atlas.en-us.chatterapi.meta/chatterapi/quickstart_connecting.htm
 - ex: curl -X POST https://orgfarm-fa4f9b8218-dev-ed.develop.my.salesforce.com/services/oauth2/token -d 'grant_type=client_credentials' -d 'client_id=3MVG9rZjd7MXFdLhb._HMnhm1AWRnoV0BYmerX0NeniOwjGnCpLB5V63WpobYGesT7kU.6xZTzWo5FDqHLNs4' -d 'client_secret=86B4D3A674F80344FEDE761EEC0DD0DE6073D47736E7F0A4E179553DC172BE30'


 # Rodar prefect locally:
 - PREFECT_API_URL="http://localhost:4200/api"  prefect worker start --pool my-docker-pool --type docker

 # Observacoes sobre o Prefect
 - A Api URL do deployment, é a url onde esse deployment vai chamar o admin, como o prefect roda cada tarefa de maneira isolada em containers, quando o container é executado ele vai acessar a api como se fosse um componente externo, logo, usamos localhost inves de prefect-server ou o nome do container onde o servidor está sendo executado.