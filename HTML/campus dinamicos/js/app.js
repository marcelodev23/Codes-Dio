var btn_add = document.getElementById('add');
var btn_buy = document.getElementById('buy');
var form1   = document.getElementById('form1');
var box = document.getElementById('box');
var cont=1;


btn_add.addEventListener('click',function(){
    cont++;
    createLabel();
    createInput();
});
// <label for="nome">Produto: </label>

function createLabel(){
    var elemento = document.createElement('label');
    elemento.setAttribute('for','nome_'+cont);
    elemento.textContent = 'Produto'; 
    box.appendChild(elemento);
}
//<input type="text" name="nome" id="nome" autocomplete="off">
function createInput(){
    var elemento = document.createElement('input');
    elemento.setAttribute('type','text');
    elemento.setAttribute('name','nome_'+cont);
    elemento.setAttribute('id','nome_'+cont);
    elemento.setAttribute('autocomplete','off');
    box.appendChild(elemento);
}

btn_buy.addEventListener('click',function(){
    form1.submit();
});