<template>
  <el-container>
  <el-aside width="20%" height="100vh">
      <img src="../../../img/Tic Moklogo.png" alt="">
    <div class="aside">
      <!-- ファイル数　-->
      <file-app :form1="form1"></file-app>
      <!-- ファイル数-->
      <el-form 
        :inline="true" 
        label-position="top"  
        :model="form1" 
        ref="form1" 
        class="demo-dynamic">
        <!-- ヘッダー -->
        <header-app :flag="flag"></header-app>
        <!-- ヘッダー -->
        <!-- ドラッグ＆ドロップ -->
        <el-draggable :form1="form1" :options="options"></el-draggable>
        <!-- ドラッグ＆ドロップ -->
        <!-- フッター -->
        <footer-app :flag="flag"></footer-app>
        <!-- フッター -->
        <el-form-item 
             :maxFiles="maxFiles"
             :form1="form1"
             :flag="flag"
             :refForm="getForm"
             >
        </el-form-item>
      </el-form>
    </div>
     </el-aside>
    <el-container>
       <div style="height: 22vh">
      <img src="../../../img/header.png" alt="">
    </div>
    <el-header style="height: 8vh; border-bottom: 3px solid #000; border-top: 2px solid #000;">
      <div>
          <img src="../../../img/tikmoklogo.png" style="width: 15%;margin-left: 30px;">
          <nav>
            <ul>
              <li><a href="/">HOME</a></li>
              <li><a href="/random">RANDOM</a></li>
              <li><a href="/manual">MANUAL</a></li>
              <li><a href="/manual">DEVELOPER</a></li>
            </ul>
          </nav>
      </div>
    </el-header>

 <el-main v-if="main">
　 <el-row>
    <div class="wrapper">
    <div class="one">
      <el-col>
        <el-card :body-style="{ padding: '0px' }">
        <img src="../../../img/header01.png" class="image">
        <img src="../../../img/header02.png" class="image">
        <img src="../../../img/header03.png" class="image">
        <img src="../../../img/header04.png" class="image">
        <img src="../../../img/header05.png" class="image">
        <img src="../../../img/header06.png" class="image">
        <div style="padding: 10px;">
          <span>ヘッダー <br>上記のようなヘッダー部分のHTMLテキスト。</span>
          <div class="bottom clearfix">
            <el-button type="text" class="button">Operating button</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    </div>
    <div class="two">
      <el-col>
        <el-card :body-style="{ padding: '0px' }" style="padding-top: 30px;padding-bottom: 30px;">
          <img src="../../../img/service01.png" class="image">
          <img src="../../../img/service02.png" class="image">
          <img src="../../../img/service03.png" class="image">
          <img src="../../../img/service04.png" class="image">
          <div style="padding: 10px;">
            <span>サービス<br>上記のような特徴や機能のポイントを説明するためのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <div class="three">
   <el-col>
    <el-card :body-style="{ padding: '0px' }" style="padding-top: 30px;">
      <img src="../../../img/content01.png" class="image">
      <img src="../../../img/content02.png" class="image">
      <img src="../../../img/content03.png" class="image">
      <img src="../../../img/content04.png" class="image">
      <div style="padding: 10px;">
        <span>コンテンツ<br>上記のような汎用的に扱えるHTMLテキスト。</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">Operating button</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
    </div>
    <div class="four">
        <el-col>
        <el-card :body-style="{ padding: '0px' }">
          <!-- <img src="../../../img/footer01.png" class="image"> -->
          <img src="../../../img/footer02.png" class="image">
          <img src="../../../img/footer03.png" class="image">
          <div style="padding: 10px;">
            <span>フッター <br>上記のようなユーザーに対して行動を促すためのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <div class="five">
       <el-col>
        <el-card :body-style="{ padding: '0px' }">
          <img src="../../../img/action01.png" class="image">
          <img src="../../../img/action02.png" class="image">
          <img src="../../../img/action03.png" class="image">
          <div style="padding: 10px;">
            <span>Call To Action <br>上記のようなユーザーに対して行動を促すためのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <div class="six">
      <el-col>
        <el-card :body-style="{ padding: '0px' }" style="padding-top: 30px;padding-bottom: 30px;">
          <img src="../../../img/customer01.png" class="image">
          <img src="../../../img/customer02.png" class="image">
          <img src="../../../img/customer03.png" class="image">
          <div style="padding: 10px;">
            <span>お客様の声<br>上記のようなお客様からの感想を表示するためのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <div class="seven">
   <el-col>
    <el-card :body-style="{ padding: '0px' }">
      <img src="../../../img/staff01.png" class="image">
      <img src="../../../img/staff02.png" class="image">
      <div style="padding: 10px;">
        <span>スタッフ<br>上記のようなスタッフのカード・リスト表示のHTMLテキスト。</span>
        <div class="bottom clearfix">
          <el-button type="text" class="button">Operating button</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
    </div>
    <div class="eito">
       <el-col>
        <el-card :body-style="{ padding: '0px' }" style="padding-top: 45px;padding-bottom: 30px;">
          <img src="../../../img/price01.png" class="image">
          <img src="../../../img/price02.png" class="image">
          <img src="../../../img/price03.png" class="image">
          <img src="../../../img/price04.png" class="image">
          <div style="padding: 10px;">
            <span>価格表<br>上記のような価格の一覧を表示するためのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <div class="Nain">
      <el-col>
        <el-card :body-style="{ padding: '0px' }">
          <img src="../../../img/form01.png" class="image">
          <img src="../../../img/form02.png" class="image">
          <div style="padding: 10px;">
            <span>フォーム<br>上記のような登録フォームのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
    <div class="Ten">
      <el-col>
        <el-card :body-style="{ padding: '0px' }" style="padding-top: 35px;">
          <img src="../../../img/contact01.png" class="image">
          <img src="../../../img/contact02.png" class="image">
          <div style="padding: 10px;">
            <span>お問い合わせ<br>上記のような登録フォームのHTMLテキスト。</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">Operating button</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </div>
</div>
　 </el-row>
 </el-main>
 
 <div v-if="show" class="alert" id="modal-overlay">
        <div class="alertCenter css-fade2">
          <div class="alertImg">
            <img src="../../../img/Mockup.png">
          </div>
          <div class="alertcontent">
            <h2>RANDOM Generation</h2>
            <p>RANDOM Generationは、ランダムにHTMLファイルを生成することができます。<br>
              左のナビメニューから追加したい要素をドラックアンドドロップで適宜配置してください。<br>
            配置完了後Tic Mokボタンを押して生成してください。</p>
            <el-button type="primary" round @click="modal()">Close</el-button>
          </div>
       </div>
      </div>  
      <div v-if=" showcontent" class="alert" id="modal-overlay-contnet">
        <div class="alertCenter" style="margin-top: 15vh">
          <!-- <div class="alertcontent"> -->
           <div class="balloon2-left flash3">
            <img src="../../../img/randomgenerater.png" alt="">1
           </div>
            <el-button type="primary" round @click="modal2()">Close</el-button>
          <!-- </div> -->
       </div>
      </div>  
</el-container>
</el-container>
</template>

<script>
import VueGallery from 'vue-gallery'
import {v4} from 'uuid'
import File from './randomComponents/File.vue'
import Header from './randomComponents/Header.vue'
import ElementDraggable from './randomComponents/ElementDraggable.vue'
import Footer from './randomComponents/Footer.vue'
import ElementFormItem from './randomComponents/ElementFormItem.vue'
// import NaviHeader from './NaviHeader.vue'

  export default {
    mounted(){
       console.log('random',this.$refs['form1']);
       console.log(this.form1);
    },
    props: {
    },
      components: {
           'gallery': VueGallery,
           'file-app':File,
           'header-app':Header,
           'el-draggable':ElementDraggable,
           'footer-app':Footer,
           'el-form-item':ElementFormItem,
           // 'navi-header':NaviHeader
      },
    data() {
      return {
        show:true,
        showcontent:false,
        randomtitle:'RandomGeneration',
        randomlink:'https://youtu.be/UmaQF1v9My4',
        main:false,
        allList: {
            "call_to_action": 22,
            "contacts": 10,
            "contents": 34,
            "features": 33,
            "footers": 12,
            "forms": 12,
            "headers": 20,
            "pricings": 10,
            "teams": 8,
            "testimonials": 10
        },
        maxFiles: 3,
        flag: {
            header: true,
            footer: true,
        },
         options: [{
          value: 'features',
          label: 'サービス'
        }, {
          value: 'contents',
          label: 'コンテンツ'
        }, {
          value: 'teams',
          label: 'スタッフ'
        }, {
          value: 'pricings',
          label: '価格表'
        }, {
          value: 'call_to_action',
          label: 'Call To Action'
        }, {
          value: 'forms',
          label: 'フォーム'
        }, {
          value: 'testimonials',
          label: 'お客様の声'
        }, {
          value: 'contacts',
          label: 'お問い合わせ' 
        }],
        form1: {
          templates: [{
            key: 2,
            value1: 'contents',
            value2: 1,
          },{
            key: 3,
            value1: 'features',
            value2: 1,
          },{
            key: 4,
            value1: 'pricings',
            value2: 1,
          },{
            key: 5,
            value1: 'teams',
            value2: 1,
          },{
            key: 6,
            value1: 'forms',
            value2: 1,
          },{
            key: 7,
            value1: 'testimonials',
            value2: 1,
          },{
            key: 8,
            value1: 'contacts',
            value2: 1,
          },{
            key: 9,
            value1: 'call_to_action',
            value2: 1,
          }],
          file_numbers: 10
        }
      };
    },
    methods: {
      getForm(){
         return this.$refs['form1']
      },
      modal() {
        this.show = false
        this.showcontent = true
      },
      modal2() {
        this.showcontent=false
        this.main = true
      }
    }
  }
</script>


<style scoped>

body {
  font-family:-apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", sans-serif;
}

body:before{
  content: '';
  background: inherit;
  -webkit-filter: blur(5px);
  -moz-filter: blur(5px);
  -o-filter: blur(5px);
  -ms-filter: blur(5px);
  filter: blur(5px);
  position: absolute;
  top: -5px;
  left: -5px;
  right: -5px;
  bottom: -5px;
  z-index: -1;
}



h2 {
  margin-left: 20px;
  margin-bottom: 20px;
}

h3 {
  font-size: 25px;
}

#left {
  float: right;
}

#left a {
  margin-right: 30px;
  font-weight: bold;
}

.displayblock img {
  max-width: 100%;
  max-height: 100%;
}

.Operatingprocedure,
.specification {
   margin-top: 20px;
}

.operation_video {
  text-align: center;
}

.handle:active { 
    cursor: grabbing;
    cursor: -moz-grabbing;
    cursor: -webkit-grabbing;
}

#blueimp-gallery > a.close,
#blueimp-gallery > a.next,
#blueimp-gallery > a.prev {
  color: #fff;
}

.split-box{
  overflow: auto;
  background-size:cover;
  position:absolute;
  width:50%;
  height:100%;
}
 
.el-aside {
  background-color: white;
  height: 100vh;
}

.el-header {
  padding: 0;
  margin: 0;
}


#modal-overlay{
  z-index:1;
  position:fixed;
  top: -50px;
  left:0;
  width:100%;
  height:120%;
  background-color:rgba(0,0,0,0.75);
}

#modal-overlay-contnet{
  z-index:1;
  position:fixed;
  top: -50px;
  right:0;
  width:80%;
  height:120%;
  background-color:rgba(0,0,0,0.75);
}

.css-fade2 {
  margin-top: 200px;
}

.balloon2-left {
  position: relative;
  display: inline-block;
  margin: 1.5em 0 1.5em 15px;
  min-width: 120px;
  max-width: 100%;
  color: #555;
  font-size: 16px;
  background: #FFF;
  border: solid 3px #555;
  box-sizing: border-box;
  width: 40%;
  margin-top: 35vh;
}

.balloon2-left:before {
  content: "";
  position: absolute;
  top: 50%;
  left: -24px;
  margin-top: -12px;
  border: 12px solid transparent;
  border-right: 12px solid #FFF;
  z-index: 2;
}

.balloon2-left:after {
  content: "";
  position: absolute;
  top: 50%;
  left: -30px;
  margin-top: -14px;
  border: 14px solid transparent ;
  border-right: 14px solid #555;
  z-index: 1;
}

.balloon2-left img{
  padding: 5px;
}

.flash3{
  display: inline-block;
  white-space: nowrap;
  animation-name: Flash1;
  animation-duration: 1.7s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  animation-play-state: running;
}


.alertcontent {
  position: relative;
  background-color: white;
  width: 65%;
  height: 200px;
  box-shadow: 0 0 8px gray;
  background-color: #FAFAFA;
  text-align: center;
  margin: 0 auto;
  color: #000;
}

.alertcontent h2 {
  font-weight: bold;
  font-size: 20px;
  padding-top: 20px;
}

.alertcontent p{
  opacity: 0.5;
}


.alertImg {
   box-shadow: 0 0 8px gray;
   width: 75%;
   margin: 0 auto;
}


.css-fade2{
  animation-name:fade-in2;
  animation-duration:1s; 
}


@keyframes fade-in2 {
  0% {opacity: 0; transform: translate3d(0,-20px,0);}
  100% {opacity: 1; transform: translate3d(0,0,0);}
}

img {
  width: 100%;
}

h1 {
  padding-left: 30%; /* 変更 */
  font-weight: 900;
  padding-top: 30px;
  letter-spacing: 1.5px;
  opacity: 0.8;
 }

.mockup {
  color: blue;
}

h2 {
  font-size: 20px;
  opacity: 0.5;
  padding-left: 50px;
  letter-spacing: 1px;
}

.aside {
  width: 65%;
  margin: 0 auto;
}

.aside-title {
  width: 100%;
  margin:  0 auto;
}

 .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .wrapper {
  margin: 0 auto;
}
/* 
.wrapper > div {
  border: 2px solid rgb(233,171,88);
  background-color: rgba(233,171,88,.5);
  color: #d9480f;
} */
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 20px;
  grid-auto-rows: minmax(250px, auto);
}
.one {
  grid-column: 1 / 3;
  grid-row: 1
}
.two { 
  /* grid-column: 2 / 4; */
  grid-row: 1 / 3;
}
.three {
  grid-column: 1;
  grid-row: 2 / 4;
}
.four {
  grid-column: 2 / 4;
  grid-row: 5;
}
.five {
  /* grid-column: 2; */
  grid-row: 4;
}
.six {
  grid-column: 3;
  grid-row: 4;
}

.el-header a {
  color: black;
}

.el-header{
  background-color: #ffffff;
  filter: drop-shadow(1px 1px 1px rgba(0,0,0,0.6));
}

.eito {
  grid-column: 2;
  grid-row: 3 / 5;
}

.el-main {
  overflow: auto;
  height: 70vh;
  overflow: scroll;
}

.el-header li {
  display: inline;
}

.el-header img{
  float: left;
}

.el-header li {
  line-height: 8vh;
  font-size: 20px;
  margin-right: 30px;
}

.el-header ul {
  float: right;
}

@keyframes fadeIn {
    0% {opacity: 0}
    100% {opacity: 1}
}

@-webkit-keyframes fadeIn {
    0% {opacity: 0}
    100% {opacity: 1}
}

</style>
