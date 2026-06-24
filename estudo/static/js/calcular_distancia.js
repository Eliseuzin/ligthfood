async function calcular_distanci(){
    console.log('Funcao chamada')
    const endereco_rua_cliente = document.getElementById('rua').value
    const resposta = await fetch ("/calcular_distancia",{
        method: "POST",
        headers:{"Content-Type": "application/json"},
        body: JSON.stringify({
            endereco_rua_cliente:endereco_rua_cliente
        })
    });

    const data = await resposta.json();
    const resultado = document.getElementById('resultado')

    if (resposta.ok){
        resultado.innerText=`Distancia: ${data.distancia}, Tempo estimado: ${data.duracao}`;
    } else{
        resultado.innerText="Erro:" + (data.erro|| "Não foi possível calcular a distância.");
    }
}