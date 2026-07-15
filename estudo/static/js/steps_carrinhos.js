//inicio eventos para abrir/fechar carrinho
const dentrodocarrinho = document.getElementById("dentrodocarrinho");
const FecharStep1 = document.getElementById("fecharstep1");

Meucarrinho.addEventListener("click", () => {
  dentrodocarrinho.style.display = "block";
});

dentrodocarrinho.addEventListener("click", (event) => {
  if (event.target === dentrodocarrinho || event.target === FecharStep1) {
    dentrodocarrinho.style.display = "none";
  }
});
// fim eventos para abrir/fechar carrinho

// inicio continuar passo 1 para o passso 2
const ContinuarStep1 = document.getElementById("continuar-step1");
const StepCarrinho1 = document.getElementById("step-carrinho");


dentrodocarrinho.addEventListener("click", (event) =>{
  if (event.target === dentrodocarrinho || event.target === ContinuarStep1){
    StepCarrinho1.style.display = "none";
  }
})
//  fim continuar passo 1 para o passso 2

//inicio mostrar passso 2
const StepEntrega1 = document.getElementById("step-entrega");


dentrodocarrinho.addEventListener("click", (event) =>{
  if (event.target === dentrodocarrinho || event.target === ContinuarStep1){
    StepEntrega1.style.display = "block";
  }
})
// fim mostrar passo 2  

// inicio voltar step2 para step1
const VoltarStep2 = document.getElementById("voltar-step2");


dentrodocarrinho.addEventListener("click", (event) =>{
  if (event.target === dentrodocarrinho || event.target === VoltarStep2){
  StepEntrega1.style.display = "none";
  StepCarrinho1.style.display = "block";
}
})
// fim voltar step2 para step1

// inicio continuar step2 para step3
const ContinuarStep2 = document.getElementById("continar-step2");
const ResumoStep3 = document.getElementById("step-resumo");


dentrodocarrinho.addEventListener("click", (event) =>{
  if(event.target === dentrodocarrinho || event.target === ContinuarStep2){
    StepEntrega1.style.display = "none";
    ResumoStep3.style.display = "block";
  }
})
// fim continuar step2 para step3

// inicio voltar step3 para step2
const VoltarStep3 = document.getElementById("voltar-step3");


dentrodocarrinho.addEventListener("click", (event) =>{
  if(event.target === dentrodocarrinho || event.target === VoltarStep3){
    ResumoStep3.style.display = "none";
    StepEntrega1.style.display = "block";
  }
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