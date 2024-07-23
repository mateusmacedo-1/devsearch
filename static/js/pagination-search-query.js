
let searchForm = document.getElementById('search-form')
let pageLinks = document.getElementsByClassName('page-link')

if(searchForm){
Array.from(pageLinks).forEach((element) => {
    element.addEventListener('click', (e)=>{
    e.preventDefault()
    const page = e.currentTarget.dataset.page
    searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
    searchForm.submit()
    })
});
}
