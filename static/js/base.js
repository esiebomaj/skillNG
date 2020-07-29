

const showCourses=()=>{
    const coursesHead=document.querySelector('.module')
    coursesHead.scrollIntoView({behavior:'smooth'})
}

window.addEventListener('scroll',()=>{
    const nav= document.querySelector('#main-nav')
    if(window.scrollY>200){
        nav.classList.add('box-shadow')
        nav.classList.add('fixed')
    }
    else{
        nav.classList.remove('box-shadow')
        nav.classList.remove('fixed')
    }
    
})


// const animateShowText=()=>{
//     const object= document.querySelector('.hero-head');
//     object.classList.add('hero-head-show')
//     console.log(object.classList)
// }