const ContinuarStep1 = document.getElementById("continuar-step1");
const dentrodocarrinho = document.getElementById("dentrodocarrinho")
const Fechar = document.getElementById("fecharstep1");

Meucarrinho.addEventListener("click", () => {
  dentrodocarrinho.style.display = "block";
});

dentrodocarrinho.addEventListener("click", (event) => {
  if (event.target === dentrodocarrinho || event.target === Fechar) {
    dentrodocarrinho.style.display = "none";
  }
});