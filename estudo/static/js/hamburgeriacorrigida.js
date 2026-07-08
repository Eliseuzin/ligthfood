// Seletores principais do DOM
const Menugeral = document.getElementById("menu");
const Meucarrinho = document.getElementById("meucarrinho");
const dentrodocarrinho = document.getElementById("dentrodocarrinho");
const submeucarrinho = document.getElementById("submeucarrinho");
const subdentrodocarrinho = document.getElementById("subdentrodocarrinho");
const Valortotal = document.getElementById("valortotal");
const Subtotal = document.getElementById("subtotal")
const TotalTaxa =  document.getElementById("taxaentrega")
const Fechar = document.getElementById("Fechar");
const Finalizar = document.getElementById("Finalizar");
const Quantidadecarinho = document.getElementById("quantidadecarinho");
const Addressinput = document.getElementById("address");
const addressnome = document.getElementById("addressnome");
const addressphone = document.getElementById("addressphone");
const Addresswarninput = document.getElementById("address-warn");
const Addresswarninputnome = document.getElementById("address-warnnome");
const Addresswarninputphone = document.getElementById("address-warnphone");
const itensaddnocarrinho = document.getElementById("itensadd");
const subbottom = document.getElementById("subbottom");
const out = document.getElementById("out");
const Finish = document.getElementById("Finish");

let listcar = [];
subbottom.style.display = "none";

// Eventos para abrir/fechar carrinho
Meucarrinho.addEventListener("click", () => {
  dentrodocarrinho.style.display = "block";
});

dentrodocarrinho.addEventListener("click", (event) => {
  if (event.target === dentrodocarrinho || event.target === Fechar) {
    dentrodocarrinho.style.display = "none";
  }
});

subbottom.addEventListener("click", (event) => {
  if (event.target === out) {
    dentrodocarrinho.style.display = "none";
  }
});

// Adicionar item ao carrinho
Menugeral.addEventListener("click", (event) => {
  const parentButtom = event.target.closest(".addcart");
  if (parentButtom) {
    const name = parentButtom.getAttribute("data-name");
    const price = parseFloat(parentButtom.getAttribute("data-price"));
    addinmycar(name, price);
  }
});
function addinmycar(name, price) {
  const checklistcar = listcar.find(item => item.name === name);
  if (checklistcar) {
    checklistcar.quantity += 1;
  } else {
    listcar.push({ name, price, quantity: 1 });
  }
  EsperarDistancia()
  subbottom.style.display = "block";

  // Envia para o backend Flask
  fetch('/adicionar-carrinho', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      nome_produto: name,
      preco: price,
      quantidade: 1 // sempre adicionando 1 por clique
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.mensagem); // opcional
  })
  .catch(error => {
    console.error('Erro ao enviar item para o backend:', error);
  });
}


fetch('/meu-carrinho')
  .then(response => {
    if (response.ok) return response.json();
    else throw new Error('Usuário não logado ou erro ao carregar');
  })
  .then(data => {
    if (Array.isArray(data)) {
      listcar = data; // <- substitui o carrinho local
      EsperarDistancia()
      subbottom.style.display = "block";
    }
  })
  .catch(err => {
    console.log('Carrinho não carregado:', err.message);
  });



// inicio esperar carregar distancia para depois atualizar carrinho
async function EsperarDistancia() {
   await calculardistancia();
   updatecarrinho();
  //  console.log(`valor em metros vindo de calcular_distancia: ${distancia_taxa_metros}`);

}
// fim esperar carregar distancia para depois atualizar carrinho


// inicio calcular subtotal e total 
function updatecarrinho() {
  submeucarrinho.innerHTML = "";
  let subtotal = 0;
  let total= 0;
  let taxa=0;

  listcar.forEach((item) => {
    const incluirosprodutos = document.createElement("div");
    incluirosprodutos.className = "estilizarprodutos";
    incluirosprodutos.innerHTML = `
      <div>
        <p>${item.name}</p>
        <p>Qtds: ${item.quantity}</p>
        <p>R$: ${item.price.toFixed(2)}</p>
        <button class='removeritem' data-name="${item.name}">Remover</button>
      </div>`;

    subtotal += item.price * item.quantity;
    submeucarrinho.appendChild(incluirosprodutos);
  });


  Subtotal.textContent = `Sub total: ${subtotal.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL"
  })}`;

  //inicio calcular taxa de entrega 
  function calcular_frete(distancia_taxa_metros) {
  if (distancia_taxa_metros <= 2000) {
      return 6.00;
  } else if (distancia_taxa_metros <= 3000) {
      return 7.00;
  } else if (distancia_taxa_metros <= 4000) { 
      return 8.00;
  }
  else if (distancia_taxa_metros <= 5000){
      return 9.00;
  }
  else if (distancia_taxa_metros <= 6000){
      return 10.00;
  }
  else if  (distancia_taxa_metros <= 7000){
      return 11.00;
  }
  const excedente = distancia_taxa_metros - 7000;
  return Number((11 + (excedente * 0.0016)).toFixed (2));
  }
  // console.log("Distância:", distancia_taxa_metros);
  taxa= calcular_frete(distancia_taxa_metros);
  // console.log("Taxa:", calcular_frete(distancia_metros));
  TotalTaxa.textContent = `Taxa de entrega: ${taxa.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL"
  })}`;

  //fim  calcular taxa de entrega 

  total+=subtotal + taxa ;
  Valortotal.textContent = `Total:${total.toLocaleString("pt-BR",{
    style:"currency",
    currency: "BRL"
  })}`;


  Quantidadecarinho.textContent = listcar.length;
}
// fim calcular subtotal e total 

submeucarrinho.addEventListener("click", (event) => {
  if (event.target.classList.contains("removeritem")) {
    const name = event.target.getAttribute("data-name");
    removeritens(name);
  }
});

function removeritens(name) {
  const index = listcar.findIndex(item => item.name === name);
  if (index !== -1) {
    if (listcar[index].quantity > 1) {
      listcar[index].quantity -= 1;
    } else {
      listcar.splice(index, 1);
    }
    EsperarDistancia()
  }
}

// Verifica se a loja está aberta
function verificarOpen() {
  const data = new Date();
  // const hora = data.getHours();
  const hora=20;
  return hora >= 16 && hora < 24;
}

// Estiliza o span de horário com base no funcionamento
const spanhorario = document.getElementById("horario");
if (spanhorario) {
  if (verificarOpen()) {
    spanhorario.style.background = "green";
    spanhorario.style.color = "antiquewhite";
  } else {
    spanhorario.style.background = "red";
    spanhorario.style.color = "antiquewhite";
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const statusDiv = document.getElementById("status");
  const usuarioLogado = statusDiv.dataset.usuarioLogado === "true";

  if (Finish) {
    Finish.addEventListener("click", function () {
      if (!usuarioLogado) {
        Toastify({
          text: "⚠️ Você precisa estar logado para finalizar o pedido!",
          duration: 4000,
          close: true,
          gravity: "top",
          position: "right",
          style: {
            background: "linear-gradient(to right, #ff5f6d, #ffc371)",
            color: "#000",
            fontWeight: "bold",
          },
        }).showToast();
        return;
      }

      const isOpen = verificarOpen();
      if (!isOpen) {
        Toastify({
          text: "Desculpe, a pizzaria está fechada!",
          duration: 4000,
          close: true,
          gravity: "top",
          position: "left",
          stopOnFocus: true,
          style: {
            background: "linear-gradient(to right,rgba(255, 0, 0, 0.13),rgb(255, 0, 0))"
          },
        }).showToast();
        return;
      }

      if (listcar.length === 0) return;

      if (addressnome.value === "") {
        Addresswarninputnome.style.display = "block";
        Addresswarninputnome.innerText = "Um nome, por favor!!!";
        return;
      } else if (addressnome.value.length <= 3) {
        Addresswarninputnome.style.display = "block";
        Addresswarninputnome.innerText = "Nome precisa ter mais de 3 caracteres!";
        return;
      } else {
        Addresswarninputnome.style.display = "none";
      }

      if (Addressinput.value === "") {
        Addresswarninput.style.display = "block";
        Addresswarninput.innerText = "Endereço completo, por favor!!!";
        return;
      } else if (Addressinput.value.length <= 3) {
        Addresswarninput.style.display = "block";
        Addresswarninput.innerText = "O endereço precisa ter no mínimo 3 caracteres";
        return;
      } else {
        Addresswarninput.style.display = "none";
      }

      if (addressphone.value === "") {
        Addresswarninputphone.style.display = "block";
        Addresswarninputphone.innerText = "Número para contato, por favor!";
        return;
      } else if (addressphone.value.length !== 11) {
        Addresswarninputphone.style.display = "block";
        Addresswarninputphone.innerText = "Número inválido. Ex.: 31999990000";
        return;
      } else {
        Addresswarninputphone.style.display = "none";
      }

      const listcaritens = listcar.map((item) => {
        return `${item.name}, Quantidade:(${item.quantity}), Preço R$:(${item.price}) |***|`;
      }).join("");

      const mensagem = encodeURIComponent(listcaritens);
      const celular = "31994174975";

       //abrir o whtasapp com a mensagem formatada
      // window.open(
      //   `https://wa.me/${celular}?text=${mensagem}, ${Valortotal.textContent},// Nome: ${addressnome.value},// Endereço: ${Addressinput.value},// Celular: ${addressphone.value}`,
      //   "_blank"
      // );


      //este e o codigo que esta funcionando para enviar os dados para o whatsapp, mas quero mandar para o flask primeiro e depois redirecionar para o whatsapp, entao vou comentar esta parte e usar a parte do fetch para mandar os dados para o flask e depois abrir o whatsapp
      //iremos mandar os dados para o flask para criar o pedido e depois redirecionar para o whatsapp
      const wpp = window.open(
          `https://wa.me/${celular}?text=${mensagem}, ${Valortotal.textContent},// Nome: ${addressnome.value},// Endereço: ${Addressinput.value},// Celular: ${addressphone.value}`,
          "_blank"
        );

      // 🔥 ENVIA PARA O FLASK PRIMEIRO
          // fetch("/finalizar_pedido", {
          //   method: "POST",
          //   headers: {
          //     "Content-Type": "application/json"
          //   },
          //   body: JSON.stringify({
          //     nome: addressnome.value,
          //     telefone: addressphone.value,
          //     endereco: Addressinput.value,
          //     total: Valortotal.textContent,
          //     carrinho: listcar
          //   })
          // })
          // .then(response => response.json())
          // .then(data => {

          //   // 🔥 AGORA abre o WhatsApp
          //   const wpp = window.open(data.link, "_blank");

          //   if (wpp) {
          //     listcar.length = 0;
          //     updatecarrinho();
          //   } else {
          //     Toastify({
          //       text: "⚠️ Pop-up bloqueado. Permita o navegador abrir o WhatsApp!",
          //       duration: 4000,
          //       gravity: "top",
          //       position: "right",
          //     }).showToast();
          //   }

          // })
          // .catch(err => {
          //   console.error("Erro ao salvar pedido:", err);
          //   alert("Erro ao finalizar pedido.");
          // });
          
        //here finish the send date for flask


       //quando add para enviar para o flask, posso comentar esta parte
        if (wpp) {
          // wpp foi aberta com sucesso
          listcar.length = 0;
          EsperarDistancia()
        } else {
          //  Pop-up foi bloqueado
          Toastify({
            text: "⚠️ Pop-up bloqueado. Permita o navegador abrir o WhatsApp!",
            duration: 4000,
            close: true,
            gravity: "top",
            position: "right",
            style: {
              background: "linear-gradient(to right, #ffc371, #ff5f6d)",
              color: "#000",
              fontWeight: "bold",
            },
          }).showToast();
        }
    });
  }
});

// Botão "Pagar Pedido" com integração ao Flask
const botaoPagamento = document.getElementById("pagarPedido");
if (botaoPagamento) {
  botaoPagamento.addEventListener("click", function () {
    let totalPedido = 0;
    listcar.forEach(item => {
      totalPedido += item.price * item.quantity;
    });

    if (totalPedido === 0) {
      alert("Seu carrinho está vazio!");
      return;
    }

    fetch("https://0c37-2804-540-153-2d00-c187-5c88-abfe-fac3.ngrok-free.app/criar_pagamento", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        titulo: "Pedido Hamburgueria",
        preco: totalPedido.toFixed(2)
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data && data.init_point) {
        window.location.href = data.init_point;
      } else {
        alert("Erro ao iniciar pagamento.");
      }
    })
    .catch(err => {
      console.error("Erro ao comunicar com servidor:", err);
      alert("Erro ao processar pagamento.");
    });
  });
}
