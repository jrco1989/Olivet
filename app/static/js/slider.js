let slider = document.querySelector('.slider-contenedor');
let sliderInd = document.querySelectorAll('.slider-test');
let contador = 1;
let tamañoWidth = sliderInd[0].clientWidth;

let intervalo = 4000;

window.addEventListener('resize',function(){
    let tamañoWidth = sliderInd[0].clientWidth;
})

setInterval(function tiempo(){
    slides();
}, intervalo);

function slides(){
    slider.style.transform = 'translate('+(-tamañoWidth*contador) + 'px)' ;
    slider.style.transition = 'transform 1s';
    contador++;

     if(contador == sliderInd.length){
         contador = 0;
         setTimeout(function(){
            slider.style.transform = 'translate(0px)' ;
            slider.style.transition = 'transfom 0s';

         },intervalo)
     }
}
