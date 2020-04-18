<template>
  <div class="sidebar" style="height:100%; background: #eee">
    <!-- <div class="pure-u-4-24" style=" margin: 0 0 0 1em;"> -->
    <!-- <div> -->
      <div class="sidebarTop">
        <p style="font-size:16px; font-weight:bolder;">OUYANG</p>
        <p style="margin-top: 1em; color: #bbb;">给时光以生命</p>
      </div>

      <div class="pure-menu" style="background: #f7f7f7">
        <ul class="pure-menu-list">
            <a id="menu-heading" class="pure-menu-heading" href="#">我的博客</a>

            <!-- <li class="pure-menu-item pure-menu-selected"><a href="http://localhost:8080/" class="pure-menu-link">首页</a></li> -->
            <li class="pure-menu-item"><a href="http://localhost:8080/" id="menu-item" class="pure-menu-link">首页</a></li>
            <!-- <li class="pure-menu-item"><a href="#" class="pure-menu-link">文章分类</a></li> -->
            <!-- <li class="pure-menu-item menu-item-divided"><a href="#" class="pure-menu-link">请我喝咖啡</a></li> -->
            <li class="pure-menu-item"><a href="#" id="menu-item" class="pure-menu-link">关于我</a></li>
            <br>
            <a id="menu-heading" class="pure-menu-heading" href="#">一些小工具</a>
            <li class="pure-menu-item"><a href="#" id="menu-item" class="pure-menu-link">GRE 背单词</a></li>
            <li class="pure-menu-item"><a href="/todo/index.html" id="menu-item" class="pure-menu-link">TODO List</a></li>
        </ul>
      <!-- </div> -->

      <div style="margin: 1em 0; padding:1em 0; height: 100%; background: #f7f7f7" >
        <div style="height: 1em; background: #eee"></div>
        <!-- <hr/> -->

        <img id="profile" src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1297131345,3641620732&fm=26&gp=0.jpg">
        <p style="font-weight: bolder;">Ouyang Wenwen</p>
        <a href=mailto:irvineoy@gmail.com class="button-xsmall pure-button">Email</a>
        <a href="https://github.com/irvineoy" class="button-xsmall pure-button">Github</a>
        <p style="font-size:10px; color:gray;">分享自己的知识</p>

        <!-- <p style="font-size:10px; color:gray;">Email: irvineoy@gmail.com</p> -->
        <!-- <p style="font-size:10px; color:gray;"> Github: https://github.com/irvineoy</p> -->
        <!-- <p>日志|分类</p> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'sidebar',
  props: {
    // msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  margin: 0px;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  text-align: left;
  margin: 0 0px;
  width: 100%;
  color: black;
}
a {
  color: #42b983;
}

#profile {
  margin: 5%;
  width: 90%; 
  padding: 0;
  border-radius: 10%;
  
}
.sidebarTop{
  height: 9em;
  padding-top: 3em;
  margin:0;
  color:white;
  background: black;
  font-size: 8px;
}

#menu-heading{
  color:black;
  text-align: left;
  font-weight: bold;
}

#menu-item{
  margin: 0px;
  color: #222;
  font-size: 14px;
  line-height: 1em;
}

.button-xsmall{
  font-size: 75%;
  background-color: #eee;
  width: 40%;
  color: gray;
}
</style>
