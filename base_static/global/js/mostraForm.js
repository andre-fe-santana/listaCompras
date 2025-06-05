function mostraForm(){
    let formCadastro = document.getElementById('formCadastro');

    formCadastro.style.display = "flex";
}

function fechaForm(){
    let formCadastro = document.getElementById('formCadastro');

    formCadastro.style.display = "none";
}

// mostrar a imagem que o usuário colocou no form como preview
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('id_imagem'); // input da imagem
    const imagePreview = document.getElementById('imagePreview'); // img em si

    //toda vez que o usuário alterar a imagem, ele vai acionar esse evento
    fileInput.addEventListener('change', function(event){
        if(event.target.files && event.target.files[0]){
            const reader = new FileReader(); //utulizando a API FileReader pra processar essa imagem
            //quando terminar de ler o arquivo
            reader.onload = function(e){
                imagePreview.src = e.target.result; //troca o atributo src da imagem original por essa

                //faz a imagem preencher toda a label
                imagePreview.style.position = 'absolute';
                imagePreview.style.top = '0';
                imagePreview.style.left = '0';
                imagePreview.style.width = '100%';
                imagePreview.style.height = '100%';
                imagePreview.style.objectFit = 'cover';
                imagePreview.style.display = 'block';    
                
            }

            reader.readAsDataURL(event.target.files[0])
        };
    });
});