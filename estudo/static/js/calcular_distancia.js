async function calculardistancia(){
    // console.log('Funcao chamada');
    // console.log(document.getElementById("rua"))
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
        console.log(`Distância calculada: ${data.distancia}`);
    const distancia_km = parseFloat(data.distancia.replace('KM', ''));
    const distancia_metros = distancia_km * 1000;
        console.log(`Distância em metros: ${distancia_metros}`);

    const resultado = document.getElementById('resultado');

    if (resposta.ok){
        resultado.innerText=`Distancia: ${data.distancia}, Tempo estimado: ${data.duracao}`;
        return data;
    } else{
        resultado.innerText="Erro:" + (data.erro|| "Não foi possível calcular a distância.");
        return null;
    }

    // transforma distancia em metros


    // inicio calcular taxa de entrega 
    // function calcular_frete(distancia_metro) {
    // if (distancia_metro <= 2000) {
    //     return 6.00;
    // } else if (distancia_metro <= 3000) {
    //     return 7.00;
    // } else if (distancia_metro <= 4000) { 
    //     return 8.00
    // }
    // else if (distancia_metro <= 5000){
    //     return 9.00
    // }
    // else if (distancia_metro <= 6000){
    //     return 10.00
    // }
    // else if  (distancia_metro <= 7000){
    //     return 11.00
    // }
    // excedente = distancia_metro - 7000
    // return round(10 + (excedente * 0.0016), 2)
    // }
    // fim  calcular taxa de entrega 
        
}

