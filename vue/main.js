/*注册组件*/

/*全局注册*/
Vue.component('todo-item', {
  props: ['todo'],
  template: `
    <div class="todo-item">
      <li>{{todo.num}}</li>
      <button v-on:click="$emit('test','33333333')">click</button>
    </div>
`
})


let app=new Vue({
  el:"#app",
  data:{
    message:'hello vue',
    seen:true,
    list:[{title:'wang',num:1},{title:"liu",num:2}],
    buttonText:'button',
    backColor:false,
    checkbox:false
  },
  watch:{
    message:function(){
      console.log('0000000')
    },
    seen:function(){
      console.log('0000000')
    },
    buttonText:function(){
      console.log('0000000')
    }
  }
  ,
  methods:{
    onClick(){
      console.log('button click')
      this.buttonText = this.buttonText.split('').reverse().join('')
    },
    changeColor(){
      this.backColor = !this.backColor
    },
    xxx(data){
      console.log(data)
    }
  },
  created:function(){
    console.log('app created')
  },
  computed:{
    textChange:function(){
      return this.message.split('').reverse().join('')
    }
  }
})

app.message=`wangliuyong`

app.$watch('buttonText',function(newV ,oldV){
  console.log('message 被修改了')
})


console.log(Vue)
