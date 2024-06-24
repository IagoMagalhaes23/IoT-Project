// FUNÇÃO DA PÁGINA INDEX

		//função submitForm que envia e armazena os DADOS DO USUÁRIO
  		 function submitInfo() {
            const name = document.getElementById('name').value; // variável que armazena o nome da pessoa
            const age = document.getElementById('age').value;  // variável que armazena a idade da pessoa
            const resultDiv = document.getElementById('result'); // variável que armazena a div
            const startButton = document.getElementById('startButton'); // variável botão

            if (name === '' || age === '') { // critica de entrada caso estiver vazio
                resultDiv.textContent = 'Informe seus dados para iniciarmos!';
                resultDiv.style.color = 'red';
                startButton.classList.add('hidden');
            } else {
                resultDiv.textContent = 'Cadastro realizado com sucesso! NOME: '  + name + ', IDADE: ' + age;
                resultDiv.style.color = 'black';
                startButton.classList.remove('hidden');
            }
        }

        function paginaPergunta() {
            // Redireciona para a página do quiz
            window.location.href = "pergunta.html";

        }

//---------------------------------------------------------------------------------------------------------------------

// FUNÇÃO DA PÁGINA PERGUNTA

  		//função submitForm que envia e armazena pergunta quando o botão enviar for pressionado
        function submitForm() {

            const Pergunta = document.getElementById('pergunta').value; // variável que armazena a pergunta
            const resultDiv = document.getElementById('feedback'); // variável que armazena a div

        //aqui ele informa ou não se a pergunta foi enviada
             if (Pergunta === '') { // condição que critica entrada de dados 
               
                resultDiv.textContent = 'INFORME A PERGUNTA'; // texto
                resultDiv.style.color = 'red'; // cor do texto
            
            } else {
               
                resultDiv.textContent = 'PERGUNTA ENVIADA'; // texto
                resultDiv.style.color = 'green'; // cor do texto
            
            }
        }
        // função que volta para página anterior quando o o botão voltar for pressionado
        function voltaPagina(){
        	// Redireciona para a página do index
            window.location ="index.html";

        }





