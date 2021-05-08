

const Readmorebtn = document.querySelector('.Read-more-btn');
const text = document.querySelector('.text');

Readmorebtn.addEventListener('click',(e)=>{
    if(e.target.className='Read-more-btn'){
       
        text.classList.toggle('showmore');

    }
}

)












