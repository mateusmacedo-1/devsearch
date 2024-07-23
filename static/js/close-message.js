function closeMessage(){
    document.querySelectorAll('.alert').forEach((el) => {
        el.style.display = 'none'
    })
}