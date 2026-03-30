// const Menugeral = document.getElementById("menu");
// // console.log(Menugeral);
// const Meucarrinho = document.getElementById("meucarrinho");
// const dentrodocarrinho = document.getElementById("dentrodocarrinho");
// const submeucarrinho = document.getElementById("submeucarrinho");
// const subdentrodocarrinho = document.getElementById("subdentrodocarrinho");
// const Valortotal = document.getElementById("valortotal");
// const Fechar = document.getElementById("Fechar");
// const Finalizar = document.getElementById("Finalizar");
// const Quantidadecarinho = document.getElementById("quantidadecarinho");
// //fazer a busca do endereço de entrega utilizando api do google maps
// const Addressinput = document.getElementById("address");
// const addressnome=document.getElementById("addressnome")
// const addressphone=document.getElementById("addressphone");
// const Addresswarninput = document.getElementById("address-warn");
// const Addresswarninputnome = document.getElementById("address-warnnome");
// const Addresswarninputphone = document.getElementById("address-warnphone");
// const itensaddnocarrinho = document.getElementById("itensadd");
// const subbottom = document.getElementById("subbottom");
// const out = document.getElementById("out");
// const Finish = document.getElementById("Finish");
// // const error = document.getElementById("error");
// // const success = document.getElementById("success");

// var listcar = [];
// subbottom.style.display = "none";

// // abrir o carrinho

// Meucarrinho.addEventListener("click", function () {
//   // updatecarrinho();
//   dentrodocarrinho.style.display = "block";
//   // updatecarrinho();
// });

// //fechar o carrinho, click fora
// dentrodocarrinho.addEventListener("click", function (event) {
//   if (event.target === dentrodocarrinho) {
//     dentrodocarrinho.style.display = "none";
//   }
// });
// //fim de outro teste

// subbottom.addEventListener("click", function (event) {
//   if (event.target === out) {
//     dentrodocarrinho.style.display = "none";
//   }
// });
// // updatecarrinho();

// //fechar carrinho no click em fechar

// dentrodocarrinho.addEventListener("click", function (event) {
//   if (event.target === Fechar) {
//     dentrodocarrinho.style.display = "none";
//   }
// });

// Menugeral.addEventListener("click", function (event) {
//   // console.log(event.target);

//   var parentButtom = event.target.closest(".addcart");

//   // console.log(parentButtom);

//   if (parentButtom) {
//     const name = parentButtom.getAttribute("data-name");
//     const price = parseFloat(parentButtom.getAttribute("data-price"));


//     // console.log(name);
//     // console.log(price);

//     //adicionar no carrinho

//     addinmycar(name, price);
//     // remoitenscarrinho(name);
//   }
// });

// // função para adicionar no carrinho
// function addinmycar(name, price) {
//   // alert(` item is ${name} and  price is ${price}`);

//   const checklistcar = listcar.find((item) => item.name === name);

//   if (checklistcar) {
//     //se o item já existe aumenta a quantidade +1
//     // console.log(checklistcar);
//     checklistcar.quantity += 1;

//     // return;
//   } else {
//     listcar.push({
//       name,
//       price,
//       quantity: 1,
//     });
//   }
//   updatecarrinho();
//   subbottom.style.display = "block";
// }

// //atualizar o carrinho

// function updatecarrinho() {
//   submeucarrinho.innerHTML = "";
//   let total = 0;

//   listcar.forEach((item) => {
//     const incluirosprodutos = document.createElement("div");
//     incluirosprodutos.setAttribute("class", "estilizarprodutos");

//     incluirosprodutos.innerHTML = `<div>
//         <div>
//             <p>${item.name}</p>
//             <p> Qtds:${item.quantity}</p>
//             <p>R$:${item.price.toFixed(2)}</p>

//         </div>

//            <button  class='removeritem' data-name="${
//              item.name
//            }">Remover</button>
      
//     </div>`;
//     total += item.price * item.quantity;
//     submeucarrinho.appendChild(incluirosprodutos);
//   });

//   //valor total do carrinho
//   Valortotal.textContent = `Total a Pagar: ${total.toLocaleString("pt-BR", {
//     style: "currency",
//     currency: "BRL",
//   })}`;

//   Quantidadecarinho.innerHTML = listcar.length;
// }

// // funçao para remover item
// submeucarrinho.addEventListener("click", function (event) {
//   if (event.target.classList.contains("removeritem")) {
//     const name = event.target.getAttribute("data-name");
//     console.log(name);
//     //chamar funçao
//     removeritens(name);
//   }
// });

// function removeritens(name) {
//   const index = listcar.findIndex((item) => item.name === name);

//   if (index !== -1) {
//     const item = listcar[index];
//     // console.log(item);

//     if (item.quantity > 1) {
//       item.quantity -= 1;
//       updatecarrinho();
//       return;
//     } else {
//       listcar.splice(index, 1);
//       updatecarrinho();
//     }
//   }
// }

// Addressinput.addEventListener("input", function (event) {
//   var inputValue = event.target.value;
//   // if (inputValue !== "") {
//   //   Addresswarninput.style.visibility = "hidden";
//   // }
// });

// //INÍCIO TESTE PARA DIRECIONAMENTO DE PAGAMENTO MERCADO PAGO

// document.getElementById("pagarPedido").addEventListener("click", function () {
//   // Pegue o valor total do pedido (já mostrado na tela)
//   const Valortotal = parseFloat(document.querySelector("#valortotal").textContent.replace(/[^\d.,]/g, '').replace(',', '.'));
//   // const Valortotal = parseFloat(document.querySelector("valortotal").textContent);

//   // Envie para o backend Flask para gerar o link de pagamento
//   fetch("https://0c37-2804-540-153-2d00-c187-5c88-abfe-fac3.ngrok-free.app/criar_pagamento", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json"
//     },
//     body: JSON.stringify({
//       titulo: "Pedido Hamburgueria",
//       preco: total.toFixed(2)
//     })
//   })
//     .then(response => response.json())
//     .then(data => {
//       if (data && data.init_point) {
//         window.location.href = data.init_point; // redireciona para o Mercado Pago
//       } else {
//         alert("Erro ao iniciar pagamento.");
//       }
//     })
//     .catch(err => {
//       console.error("Erro ao comunicar com servidor:", err);
//       alert("Erro ao processar pagamento.");
//     });
// });
  
// //FIM TESTE PARA DIRECIONAMENTO DE PAGAMENTO MERCADO PAGO

// Finish.addEventListener("click", function () {
//   const isOpen = verificaropen();
//   if (!isOpen) {
//     //importaçao mensagem loja fechada
//     Toastify({
//       text: "Desculpe, a pizzaria está fechada!",
//       duration: 4000,
//       close: true,
//       gravity: "top", // `top` or `bottom`
//       position: "left", // `left`, `center` or `right`
//       stopOnFocus: true, // Prevents dismissing of toast on hover
//       style: {
//         background: "linear-gradient(to right,rgba(255, 0, 0, 0.13),rgb(255, 0, 0))",
//       },
//     }).showToast();
//     return;
//   }

//   if (listcar.length === 0) return;

//     if(addressnome.value===""){
//     Addresswarninputnome.style.display="block"
//     Addresswarninputnome.innerText="Um nome, por favor!!!"
//     return;
//   }else if(addressnome.value.length<=3){
//     Addresswarninputnome.style.display="block"
//     Addresswarninputnome.innerText="Nome precisa ter mais de 3 caracteres! "
//     return;
//   }else{
//     Addresswarninputnome.style.display="none"
//   }

//   if (Addressinput.value === "") {
//     Addresswarninput.style.display = "block";
//     Addresswarninput.innerText = "Endereço completo, por favor!!!";
//     return;
//   } else if (Addressinput.value.length <= 3) {
//     Addresswarninput.style.display = "block";
//     Addresswarninput.innerText =
//       "O endereço precisa ter no minimo 3 caracteres";
//     return;
//   } else {
//     Addresswarninput.style.display = "none";
//   }

//   if(addressphone.value===""){
//     Addresswarninputphone.style.display="block"
//     Addresswarninputphone.innerText="Numero para contato, por favor!"
//     return;
//   } 
//   else if (addressphone.value.length<=10){
//     Addresswarninputphone.style.display="block"
//     Addresswarninputphone.innerText="Precisa ter 11 numeros "
//     Addresswarninputphone.innerText="Ex.:31999990000 "
//     return;
//   }else if (addressphone.value.length>11){
//     Addresswarninputphone.style.display="block"
//     Addresswarninputphone.innerText="Precisa ter 11 numeros "
//     return;
//   }else{
//     Addresswarninputphone.style.display="none"
//   }


//   //ENVIAR PARA O WHATSAPP
//   // console.log(listcar);

//   const listcaritens = listcar
//     .map((item) => {
//       return `${item.name}, Quantidade:(${item.quantity}), Preço R$:(${item.price})|***|`;
//     })
//     .join("");

//   const messagem = encodeURIComponent(listcaritens);
//   const celular = "31994174975";

//   window.open(
//     `https://wa.me/${celular}?text=${messagem}, ${Valortotal.textContent},// Nome: ${addressnome.value},// Endereço: ${Addressinput.value},// Celular: ${addressphone.value}`,
//     "_blank"
//   );
//   // listcar.length = [];
//     listcar.length =0 ;

//   updatecarrinho();
//   // console.log(listcaritens);
// });

// // Addresswarninputnome.addEventListener('keyup',() =>{
// // const AddresswarninputnomeValue=Addresswarninputnome.value;
// // })

// // FUNÇÃO PARA VERIFICAR SE A LOJA ESTA ABERTA OU FECHADA
// function verificaropen() {
//   const data = new Date();
//   // const hora = data.getHours();
//   const hora = 20 ;
//   // return hora >= 16 || hora <= 23;
//   return hora >= 16 && hora <24;

// }
// const spanhorario = document.getElementById("horario");
// const isOpen = verificaropen();
// if (isOpen) {
//   spanhorario.style.background = "green";
//   spanhorario.style.color = "antiquewhite";
// } else {
//   spanhorario.style.background = "red";
//   spanhorario.style.color = "antiquewhite";
// }

// console.log(Valortotal);
