// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')
console.log('aaaaaaaaaaaaaaaaa');
if (alertWrapper) {
  console.log('Elemento alertWrapper encontrado');
  alertClose.addEventListener('click', () => {
    alertWrapper.style.display = 'none'
    console.log('fechandooooo');
    }
  )
}
