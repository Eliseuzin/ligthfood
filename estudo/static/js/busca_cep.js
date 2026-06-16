async function buscarCep(){
    console.log("Função buscarCep executada");
    //Todos os caracteres que não são números foram removidos .replace(/\D/g,''). 
    const cep = document.getElementById("cep").value.replace(/\D/g,'');
    if (cep.length !==8){
        alert("CEP inválido!");
        return;
    }

    try {
        // fetch() é uma função do JavaScript que faz uma requisição para um servidor.

        // É como se o navegador perguntasse:

        // "ViaCEP, você pode me enviar os dados do CEP 33825470?"
        const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        const dados = await resposta.json();


            //        Quando você faz uma consulta na internet, a resposta não chega instantaneamente.

            //O JavaScript precisa esperar.

            //const resposta = await fetch(...);

            //significa:

            //"Espere o ViaCEP responder antes de continuar."

            //Sem o await, o código continuaria executando antes da resposta chegar.

        if (dados.erro){
            alert("CEP não encontrado!");
            return;
        }

        document.getElementById("endereco").value = dados.logradouro || '';
        document.getElementById("rua").value = dados.logradouro || '';
        document.getElementById("bairro").value = dados.bairro || '';
        document.getElementById("cidade").value = dados.localidade || '';
        document.getElementById("estado").value = dados.uf || '';
    
      
    } catch (erro){
        console.error(erro);
        alert("Erro ao consultar o CEP.")
    }
    




}