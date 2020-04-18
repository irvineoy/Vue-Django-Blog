<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div class="pure-g" style="background: #F0F0F0;">
        <div class="pure-u-3-24" style="background: #eee;"><p></p></div>
        <div class="pure-u-15-24" style="background: #f7f7f7; padding: 0em 2em;">
            <div v-for="(v,i) in blogList" :key="i" style="background: ; margin: 1em 0 1em 0;"> 
              <router-link :to="'/article/'+v.pk" class="title">{{v.fields.title}}</router-link>
              <!-- <h1>{{v.fields.title}}</h1> -->
              <p class="time">更新于：{{v.fields.updataTime.slice(0,10)}} | 回复：{{v.fields.timesOfReply}} | 阅读次数：{{v.fields.timesOfRead}}</p>
              <p class="content">
                {{v.fields.content.slice(0,150)}}
              </p>
              <button class="button-large pure-button" style="margin: 1em 0 1em 0;" @click="$router.push('/article/'+v.pk)">阅读全文</button>

              <hr class="hr1" /> 
            </div>
          </div>
        <!-- <div class="pure-u-1-24" style="background:;"><p>Thirds</p></div> -->
        <div class="pure-u-4-24" style=" margin: 0 0 0 1em; background:#f7f7f7;">
          <sidebar></sidebar>
        </div>
    </div>
  </div>

</template>


<script>
// @ is an alias to /src
import sidebar from '@/components/sidebar.vue'
export default {
  name: 'Home',
  components: {
    sidebar
  },
  data(){
    return{
      blogList: []
    }
  },
  methods:{
    // jump(){
    //   this.$router.push('')
    // }
  },
  created(){
    this.$http.get('/showbloglist').then(response =>{
      // console.log(JSON.stringify(response.data['list'])); // TODO
      this.blogList = response.data['list'];
      console.log(this.blogList)
      
    })
  }
}
</script>

<style scoped>

.content{
  text-align: left;
}
.title{
  color: black;
  font-size: 20px;
  text-decoration: none;
  font-weight: bold;
  
}
.time{
  font-size: 10px;
  color: gray;
}
.hr1{ 
  height:1px;
  width: 6em;
  border:none;
  border-top:1px solid #ccc;
  margin-top: 4em;
  margin-bottom: 3em;
}  

</style>