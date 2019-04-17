//模块:第三方（npm install） 引入不用 ‘./’；自定义的要用‘./’

//使用解构赋值获取导入的内容
//import会变量提升，但一般开发都会写在最上面
// import {name,age} from  './module2.js'
// //一次性导入所有
// import * as obj from './module2.js'
//或者使用  export default {} 导出，也可以使用import一次性导入
let box=document.getElementById('box')
let button=document.getElementById('Button')
let text=document.createElement('div')

let observer = new MutationObserver(function (mutations, observer) {
    mutations.forEach(function(mutation) {
      console.log(mutation);
    });
  });

  
var  options = {
    'class': true,
    'attributes':true
  } ;
  
observer.observe(box, options);

button.addEventListener('click',(e)=>{
    console.log(e)
    box.className='box1'
    box.appendChild(text)
})
// console.log(name);
// console.log(obj);

