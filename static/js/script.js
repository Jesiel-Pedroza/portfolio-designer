// Função para adicionar um novo projeto ao portfólio
function adicionarProjeto(titulo, descricao, urlImagem) {
    // 1. Encontra o container onde os projetos serão adicionados
    const portfolioContainer = document.getElementById('portfolio-container');

    // 2. Cria um novo elemento <section> para o cartão do projeto
    const projectCard = document.createElement('section');
    projectCard.classList.add('project-card'); // Adiciona a classe CSS para estilização

    // 3. Define o conteúdo HTML interno do novo cartão de projeto
    projectCard.innerHTML = `
        <img src="${urlImagem}" alt="Imagem do Projeto: ${titulo}">
        <h2>${titulo}</h2>
        <p>${descricao}</p>
    `;

    // 4. Adiciona o novo cartão de projeto ao container do portfólio
    portfolioContainer.appendChild(projectCard);
}

// --- Exemplo de como você pode usar a função ---
// Você pode chamar esta função para adicionar seus projetos.
// Por enquanto, vamos adicionar alguns projetos de exemplo ao carregar a página.

document.addEventListener('DOMContentLoaded', () => {
    // Adicionando projetos de exemplo ao carregar a página
    adicionarProjeto(
        "Identidade Visual para Cafeteria",
        "Desenvolvimento completo da identidade visual, incluindo logotipo, paleta de cores e tipografia, para uma nova cafeteria moderna.",
        "https://via.placeholder.com/400x300?text=Logo+Cafeteria"
    );

    adicionarProjeto(
        "Website Responsivo de E-commerce",
        "Criação de um website de e-commerce com foco em experiência do usuário e design responsivo para dispositivos móveis e desktop.",
        "https://via.placeholder.com/400x300?text=Web+E-commerce"
    );

    adicionarProjeto(
        "Ilustração Digital para Livro Infantil",
        "Série de ilustrações digitais vibrantes e cativantes para um livro infantil com tema de aventura espacial.",
        "https://via.placeholder.com/400x300?text=Ilustracao+Livro"
    );

    // Você pode remover os projetos estáticos do seu index.html agora,
    // pois eles serão adicionados via JavaScript.
    // Ou pode mantê-los e adicionar novos por JS.
});


// --- Opcional: Adicionar um formulário para cadastrar novos projetos no próprio app ---
// Para um app de portfólio simples, é mais comum o designer editar o código
// ou ter um sistema de gerenciamento de conteúdo.
// Mas se você quiser um formulário no próprio app, podemos fazer isso!

/*
// Se você quiser adicionar um formulário no HTML para permitir que o usuário adicione projetos:
// 1. Adicione um formulário no seu index.html dentro da tag <main> ou em uma nova <section>.
// Exemplo de HTML para o formulário:
// <section class="add-project-form">
//     <h2>Adicionar Novo Projeto</h2>
//     <form id="projectForm">
//         <label for="titulo">Título:</label>
//         <input type="text" id="titulo" required><br><br>
//
//         <label for="descricao">Descrição:</label>
//         <textarea id="descricao" rows="4" required></textarea><br><br>
//
//         <label for="imagem">URL da Imagem:</label>
//         <input type="url" id="imagem" required><br><br>
//
//         <button type="submit">Adicionar Projeto</button>
//     </form>
// </section>

// 2. E no seu script.js, você adicionaria o seguinte código para lidar com o formulário:
// const projectForm = document.getElementById('projectForm');
// if (projectForm) {
//     projectForm.addEventListener('submit', function(event) {
//         event.preventDefault(); // Impede o envio padrão do formulário
//
//         const titulo = document.getElementById('titulo').value;
//         const descricao = document.getElementById('descricao').value;
//         const imagem = document.getElementById('imagem').value;
//
//         adicionarProjeto(titulo, descricao, imagem);
//
//         // Limpa o formulário após adicionar
//         projectForm.reset();
//     });
// }
*/