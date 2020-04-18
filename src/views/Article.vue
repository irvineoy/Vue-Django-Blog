<template>
  <div class="Article" style="background: #eee;">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div class="pure-g">
      <!-- 左侧的空白 -->
      <div class="pure-u-3-24" style="background: #eee;"></div>
      <!-- 正文 -->
      <div class="pure-u-15-24" style="background: #f7f7f7; padding: 0 2em;">
        <div style="background: #f7f7f7; margin: 1em 0 1em 0;">
          <h1>{{article_content.title}}</h1>
          <p class="time">更新于：{{article_content.updataTime.slice(0,10)}} | 回复：{{article_content.timesOfReply}} | 阅读次数：{{article_content.timesOfRead}}</p>
          <p style="text-align: left;">{{article_content.content}}</p>
          <!-- <button class="button-large pure-button" style="margin: 1em 0 1em 0;">阅读全文</button> -->
        </div>


        <hr/>
        <!-- 展示评论 -->
        <div v-for="(v,i) in comments_content" :key="i" class="commentWrapper">
          <p class="byline">
            <strong>{{v.name}}</strong>
            说：
          </p>
          <div class="comment-content">
            <p>{{v.comment}}</p>
          </div>
          <div class="comment-footer" style="text-align: right;">
            <p>
              <abbr class="published">{{v.commentTime.slice(0,10)}}</abbr>
            </p>
          </div>
        </div>
        <!-- 输入评论 -->

        <div class="inputComment">
          <form class="pure-form">
            <fieldset class="pure-group">
              <textarea class placeholder="请输入您的评论..." style="width: 100%; height: 10em;" v-model="comment"></textarea>
            </fieldset>

            <fieldset class="pure-group">
              <input type="text" class="pure-input-1-2" placeholder="您的大名" v-model="name" />
              <input type="email" class="pure-input-1-2" placeholder="Email" v-model="email"/>
            </fieldset>
            <button
              type="submit"
              class="pure-button pure-input-1-2 pure-button-primary"
              style="float: left;"
              @click.prevent="addComment"
            >提交评论</button>
          </form>
        </div>
      </div>

      <!-- <div class="pure-u-1-24" style="background:;"><p>Thirds</p></div> -->
      <!-- 侧边栏 -->
      <div class="pure-u-4-24" style=" margin: 0 0 0 1em;">
        <sidebar></sidebar>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import sidebar from "@/components/sidebar.vue";
export default {
  name: "Article",
  components: {
    sidebar
  },
  data() {
    return {
      // id: 0,
      comment: '',
      name: '',
      email: '',
      blogid: Number,
      article_content: {
        title: "",
        updataTime: "",
        timesOfReply: "",
        timesOfRead: "",
        content: ""
      },
      comments_content:[]
    };
  },
  // props:["blogid"],
  created() {
    this.blogid = this.$router.history.current.params.id;
    this.$http.get("/article/" + this.blogid, {params:{'id':this.blogid}}).then(response => {
      // console.log(JSON.stringify(response.data['list'])); // TODO
      this.article_content = response.data;
    });
    this.$http.get("/comments/" + this.blogid, {params:{'blogid':this.blogid}}).then(response => {
      // console.log(JSON.stringify(response.data['list'])); // TODO
      this.comments_content = response.data['list'];
    });
  },
  methods:{
    addComment(){
      if(!this.comment) return;
      if(!this.name) return;
      if(!this.email) return;
      // this.$router.push({name:'addcomment/'+this.blogid, params:{id:1}}); // TODO
      var params = new URLSearchParams();
      params.append('comment', this.comment);
      params.append('name', this.name);
      params.append('email', this.email);
      params.append('blogid', this.blogid);
      this.$http.post('/addcomment/'+this.blogid, params);
      this.comment = '';
      this.name = '';
      this.email = '';
      location.reload();
    }
  }
};
</script>

<style>
/* .byline {
  text-align: left;
  width: 100%;
}
.comment-content{
  text-align: left;
  width: 100%;
} */
.time{
  font-size: 10px;
  color: gray;
}
.commentWrapper{
  width: 100%;
  margin-top: 3em;
}
.byline{
  text-align: left;
  margin: 0;
  width: 100%;
}
.comment-content{
  text-align: left;
}
.inputComment{
  margin: 4em 0;
}
</style>