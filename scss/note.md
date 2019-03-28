# scss
----
## 1.npm初始化
    npm init -y
## 2.安装parcel
    npm i -D parcel
## 3.启动服务
    npx parcel index.html
## scss语法用法大全

    /*1.使用变量*/
    $them:#ccc;
    
    /*2混入，类似于函数*/
    @mixin border-1px($amount) {
      border: $amount solid red;
    }
    
    /*2.1也可默认变量的值*/
    @mixin border-2px($amount:2px) {
      border: $amount solid red;
    }
    
    body{
      h1{
        color: green;
        background: $them;
        @include border-1px(0.5px);
      }
    }



- css命名法--BEM

普通：user-card__name
激活状态时：user-card--active/user-card--hover
