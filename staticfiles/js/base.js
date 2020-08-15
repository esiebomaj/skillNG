const showCourses = () => {
  const coursesHead = document.querySelector(".page-title");
  coursesHead.scrollIntoView({ behavior: "smooth" });
};

window.addEventListener("scroll", () => {
  const nav = document.querySelector("#main-nav");
  const content = document.querySelector(".content");
  if (window.scrollY > 50) {
    nav.classList.add("box-shadow");
    nav.classList.add("fixed");
    nav.classList.add("animated");
    nav.classList.add("fadeInDown");
  } else {
    nav.classList.remove("box-shadow");
    nav.classList.remove("fixed");
    nav.classList.remove("animated");
    nav.classList.remove("fadeInDown");
  }
});

// const animateShowText=()=>{
//     const object= document.querySelector('.hero-head');
//     object.classList.add('hero-head-show')
//     console.log(object.classList)
// }
