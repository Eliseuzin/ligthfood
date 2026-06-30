async function calculardistancia(){
    console.log('Funcao chamada');
    console.log(document.getElementById("cep"));
    const endereco_rua_cliente = document.getElementById("rua").value;
    const resposta = await fetch ("/calcular_distancia",{
        method: "POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify({
            endereco_rua_cliente:endereco_rua_cliente
        })
    });
    console.log('resposta recebida');

    const data = await resposta.json();
    const resultado = document.getElementById('resultado');

    if (resposta.ok){
        resultado.innerText=`Distancia: ${data.distancia}, Tempo estimado: ${data.duracao}`;
    } else{
        resultado.innerText="Erro:" + (data.erro|| "Não foi possível calcular a distância.");
    }
}