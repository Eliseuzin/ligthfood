// Este código externo vai usar a variável definida no template
if (typeof usuarioLogado !== "undefined") {
  if (usuarioLogado) {
    console.log("Exibir botão de logout");
  } else {
    console.log("Exibir formulário de login");
  }
} else {
  console.error("Variável usuarioLogado não foi definida");
}
