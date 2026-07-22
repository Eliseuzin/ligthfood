//inicio eventos para abrir/fechar carrinho
const Meucarrinho = document.getElementById("meucarrinho");
const dentrodocarrinho = document.getElementById("dentrodocarrinho");
const FecharStep1 = document.getElementById("fecharstep1");
// document.querySelector(".ativo").classList.remove("ativo");


// inicio abrir meu carrinho
Meucarrinho.addEventListener("click", (event) => {
  dentrodocarrinho.style.display = "block";
});
// fim abrir meu carrinho


// Inicio eventos para abrir/fechar carrinho e com click fora dele
dentrodocarrinho.addEventListener("click", (event) => {
  if (event.target === dentrodocarrinho || event.target === FecharStep1) {
    dentrodocarrinho.style.display = "none";
  }
});
// fim eventos para abrir/fechar carrinho e com click fora dele

// inicio continuar passo 1 para o passso 2
const ContinuarStep1 = document.getElementById("continuar-step1");
const StepCarrinho1 = document.getElementById("step-carrinho");
const StepEntrega1 = document.getElementById("step-entrega");


// dentrodocarrinho.addEventListener("click", (event) =>{
//   if (event.target === dentrodocarrinho || event.target === ContinuarStep1){
//     StepCarrinho1.style.display = "none";
//   }
// })

ContinuarStep1.addEventListener("click", (event) =>{
  StepCarrinho1.style.display = "none";
   //inicio mostrar passso 2
  //  StepEntrega1.classList.add(".ativo");

  StepEntrega1.style.display = "block";
   // fim mostrar passo 2  


});

//  fim continuar passo 1 para o passso 2


// inicio voltar step2 para step1
const VoltarStep2 = document.getElementById("voltar-step2");

VoltarStep2.addEventListener("click", (event) =>{
  StepEntrega1.style.display = "none";
  StepCarrinho1.style.display = "block";
});
// fim voltar step2 para step1

// inicio continuar step2 para step3
const ContinuarStep2 = document.getElementById("continuar-step2");
const ResumoStep3 = document.getElementById("step-resumo");


ContinuarStep2.addEventListener("click", (event) =>{
  StepEntrega1.style.display = "none";
  ResumoStep3.style.display = "block";
});
// fim continuar step2 para step3

// inicio voltar step3 para step2
const VoltarStep3 = document.getElementById("voltar-step3");


VoltarStep3.addEventListener("click", (event) =>{
  ResumoStep3.style.display = "none";
  StepEntrega1.style.display = "block"
})
// fim voltar step3 para step2

// inicio mostrar subtotal
const SubTotalResumo = document.getElementById("subtotal-resumo");

// console.log(Subtotal);
// // Subtotal.textContent = `Subtotal: ${subtotal.toLocaleString("pt-BR", {
// //     style: "currency",
// //     currency: "BRL"
// // })}`;

// // subtotalResumo.textContent = subtotal.toLocaleString("pt-BR", {
// //     style: "currency",
// //     currency: "BRL"
// // });






















// SubTotalResumo.textContent = Subtotal.toLocaLString("pt-BR",{
//   style:"currency",
//   currency: "BRL"
// });

// SubTotalResumo.textContent = `Sub total: ${subtotal.toLocaleString("pt-BR", {
//   style: "currency",
//   currency: "BRL"
// })}`;
// fim mostrar subtotal
// console.log(Subtotal);