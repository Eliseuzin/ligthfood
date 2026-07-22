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