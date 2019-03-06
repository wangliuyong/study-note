/*全局注册*/

// Vue.component('alert', {
//     template: `<a @click="on_click($event)"><slot></slot></a>`,
//     methods: {
//         on_click: function (e) {
//             console.log(e)
//         }
//     }
// })


/*局部注册*/

// const alert = {
//     template: `<button  @click="on_click"><slot></slot>{{count}}</button>`,
//     data:function(){
//         return {
//             count:100,
//             liked:false
//         }
//     },
//     methods: {
//         on_click: function (e) {
//             console.log(this.count)
//             if(!this.liked){
//                 this.count++;
//                 this.liked=!this.liked;
//
//                 console.log(this.count)
//             }else {
//                 this.count--;
//                 this.liked=!this.liked;
//                 console.log(this.count)
//             }
//         }
//     }
// }



/*组件之间的通信*/

let EventBus=new Vue()

EventBus.$emit('toPater',data)
EventBus.$on('toPater',(data)=>{

})



Vue.component('son1',{
    props:['message'],
    template:`<button>son1:{{message}}</button>`,
})


let app = new Vue({
    el: "#app"
})
