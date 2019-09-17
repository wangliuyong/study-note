参考阮一峰ts教程:https://ts.xcatliu.com/basics

# ts简介
什么是ts：ts是js的超集
特点：提供类型系统和es6的支持
优点：
增加代码的可读性和可维护性
类型系统是最好的文档
在编译阶段就发现错误，比运行时发现错误好
增加了编辑器和ide的功能，代码不全、接口提示、跳转到定义、重构
包容性
.js文件可重命名为.ts文件
不显式的定义类型，也能自动作出类型推论
可定义一切类型
即使typescript编译报错，也可生成js文件
兼容第三方库，即使第三方库不是用ts写的，也可编写单独的类型文件供ts读取
缺点：集成到构建流程需要工作量，可能和一些库结合的不是很完美
安装：npm i -g typescript 执行tsc ts文件来编译会生成js文件或者ide支持
# ts基础
定义类型
ts中，使用:指定变量的类型，:的前后有没有空格都可以
定义：let isDone:boolean = false

检查
ts只会进行静态检查，如果发现有错误，编译的时候就会报错

数据类型

原始数据类型
构造函数Boolean、String、Number创建的对象是对象，不是基本类型
注意：undefined和null是所有类型的子类型，undefined和null类型的变量可以赋值给其他类型的变量

let num:number = undefined;//正确
let u:void;
let num:number  = u;//错误

void
js没有空值的概念，在ts中，可用void表示没有任何返回值的函数

function alertName():void{
  alert("name");
}

用void声明变量的时候，只能赋值为undefined和null

let name:void = undefined;

any任意值
用来表示允许赋值为任意类型
普通类型，在赋值过程中改变类型是不被允许的
任意值的属性和方法:

在任意值上访问任何属性和方法都是允许的
声明一个变量为任意值后，对它的操作，返回的内容的类型都是任意值
变量在声明的时候，未指定其类型，那么他会被识别为任意值类型

类型推论
ts会在没有明确的指定类型的时候推出一个类型，这就是类型推论

let name = "";
name = 3;//错误

联合类型
联合类型：取值可以为多种类型种的一种
联合类型使用|分隔每个类型

let favoriteNumber:string|number;
favoriteNumber = 'one';
favoriteNumber = 1;//正确

访问联合类型的属性或方法:只能访问此类型的所有类型里共有的属性或方法

类型断言

#  用来手动指定一个值的类型
语法
<类型>值
值 as 类型：react中的jsx语法的ts版必须是用这种
例子1：获取something.length会报错
```
        function getLength(something:string|number):number{
        if(something.length){
                return something.length;
        }
        }
```

例子2：类型断言，将something断言成string

```
        function getLength(something:string|number):number{
        if(<string>something.length){
                return (<string>something).length;
        }
        }
```

类型断言的用法如上，在需要断言的变量前加上 即可
类型断言不是类型转换，断言成一个联合类型中不存在的类型是不允许的

声明文件
```
        declare var 声明全局变量
        declare function 声明全局方法
        declare class 声明全局类
        declare enum 声明全局枚举类型
        declare namespace 声明（含有子属性的）全局对象
        interface 和 type 声明全局类型
        export 导出变量
        export namespace 导出（含有子属性的）对象
        export default ES6 默认导出
        export = commonjs 导出模块
        export as namespace UMD 库声明全局变量
        declare global 扩展全局变量
        declare module 扩展模块
```

## 应用总结
 1.函数参数的类型使用联合类型时，在ts类型推断错误的情况下，可以使用断言来解决 
 ```
 <type>参数
 ```
 2.会用到的内置对象
 Document、HTMLElement、Event、NodeList、Boolean、Error、Date、RegExp
 
 内置对象大全：https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects
 
 3.如果一个变量声明未赋值，类型会被推断为any；赋值了就会被推断为值得类型；
 
 4.在angular的组件中可以使用get,set来监听属性的变化来在属性更改时去调用相应的函数
 
  5.接口的继承使用implements
  ```
    interface Alarm {
    alert();
    }

    interface Light {
        lightOn();
        lightOff();
    }

    class Car implements Alarm, Light {
        alert() {
            console.log('Car alert');
        }
        lightOn() {
            console.log('Car light on');
        }
        lightOff() {
            console.log('Car light off');
        }
    }
  ```
