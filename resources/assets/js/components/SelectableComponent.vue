<template>
 <el-container>
  <el-aside width="20%">
     <section-app
       :options="options"
       :allList="allList"
       :sectionList="sectionList"
       >
    </section-app>
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
    <el-main>
       <el-draggable :sectionList="sectionList" :labels="labels" z></el-draggable>
            <div v-if="0 < progressValue && progressValue < 100">
              <div class="row">
                <div class="col-12 pt-3">
                  <el-progress :percentage="progressValue"></el-progress>
                </div>
              </div>
            </div>
        <div class="container">
         <div class="row pt-3" v-if="0 < sectionList.length">
            <el-button type="primary" round @click="submitForm()" class="outline-none">Tic Mok</el-button>
            <el-button class="download" type="primary" round v-if="100 <= progressValue">
              <a :href="`/download/${creatingFile.filename}`" download></a>
                DownLoad<i class="el-icon-download"></i>
            </el-button>
          </div>
         </div>
  </el-main>
      <div v-if="show" class="alert" id="modal-overlay">
        <div class="alertCenter css-fade2">
          <div class="alertImg">
            <img src="../../../img/Mockup.png">
          </div>
          <div class="alertcontent">
            <h2>MANUAL Generation</h2>
            <p>MANUAL Generationは、任意にHTMLファイルを生成することができます。<br>左のナビメニューから追加したい要素を選択しカスタマイズしてください。<br>
            カスタマイズ完了後Tic Mokボタンを押して生成してください。</p>
            <el-button type="primary" round @click="modal()">Close</el-button>
          </div>
       </div>
      </div>  
      <div v-if=" showcontent" class="alert" id="modal-overlay-contnet">
        <div class="alertCenter">
           <div class="balloon2-left flash3">
            <img src="../../../img/manualdescription.png" alt="">
           </div>
            <el-button type="primary" round @click=" showcontent = false">Close</el-button>
          <!-- </div> -->
       </div>
      </div>  
  </el-container>
</el-container>
</template>

<script>
import * as utils from '../utils'
import Chance from 'chance'
import {v4} from 'uuid';
import Elementdraggable from './selectableComponents/Elementdraggable.vue'
import SectionAdd from './selectableComponents/SectionAdd.vue'
// import NaviHeader from './NaviHeader.vue'

  export default {
    mounted() {
      this.loadStorage()
      this.sectionList = []
    },
    watch: {
      sectionList: function (val) {
        if (100 <= this.progressValue) {
          this.progressValue = 0
        }
      }
    },
    components: {
        'el-draggable':Elementdraggable,
        'section-app':SectionAdd,
        // 'navi-header':NaviHeader
    },
    data() {
      return {
        show:true,
        showcontent:false,
        activeIndex: '1',
        manualtitle:'ManualGeneration',
        manuallink:'https://youtu.be/P3uG6HYEj2w',
        sectionList: [],
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
        uuid: null,
        creatingFile: {isProgress: false},
        maxFiles: 3,
        progressValue: 0,
        tableData: [],
        labels: {
        'contents': 'コンテンツ',
        'features': 'サービス',
        'teams': 'スタッフ',
        'pricings': '価格表',
        'call_to_action': 'Call To Action' ,
        'contacts':'お問い合わせ'
        },
        options: [{
          value: 'headers',
          label: 'ヘッダー'
        }, {
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
        }, {
          value: 'footers',
          label: 'フッター'
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
            value1: 'contents',
            value2: 1,
          },{
            key: 7,
            value1: 'call_to_action',
            value2: 1,
          }]
        }
      };
    },
    methods: {
      loadStorage() {
            const data = utils.loadStorage(Vue)
            this.uuid = v4()
      },
      storeStorage() {
            utils.storeStorage(Vue, 'uuid', this.uuid)
      },
      updateProgress() {
      // Simulate loading
        const timer = setInterval(() => {
          this.progressValue += 1;

              if (this.progressValue > 100) {

                this.$message({
                    message: `ファイルを作成しました`,
                    type: 'success'
                });
                this.creatingFile = {...this.creatingFile, isProgress: false}
                this.storeStorage()
                clearInterval(timer);            
              }
        }, 100);
      },
      modal() {
        this.show = false
        this. showcontent = true
      },
      submitForm() {
          const uuid = this.uuid;
          const templates = this.sectionList.map(o => {
            return { 
                key: o.key, 
                value: parseInt(o.value.find(e => e.isSelected).number, 10)
            }
          })

          this.creatingFile = {isProgress: true}
          this.progressValue = 0
          this.updateProgress()

          axios.post('/api/generate2', {templates, uuid}).then((e) => {

          // console.log(e)
          const data = e.data.data
          const labelName = 'サンプル' + data.filename.substring(0,3)
          
          this.creatingFile = {
              isProgress: false,
              filename: data.filename, 
              name: labelName,
              isEdit: false
          }
          this.tableData.push(this.creatingFile)
          console.log(this.tableData)
          }).catch((e) => {
              console.log('error')
              console.log(e)
          })
      }
    }
  }
 

</script>



<style>

body {
  /* background-image: url(../../../img/img05.png); */
  background-size: cover;
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

#header {
  height: 100px;
  margin-bottom: 20px;
  line-height: 100px;
  background-color:  white;
}

#header h1 {
  float: left;
  line-height: 100px;
  font-weight: bold;
  font-size: 30px;
}

.handle:active { 
    cursor: grabbing;
    cursor: -moz-grabbing;
    cursor: -webkit-grabbing;
}
.non-selectable {
    padding-left: 14px;
}

.displayblock h2,
.Operatingprocedure h2 {
  text-align: center;
}

.displayblock img {
  width: 100%;
  height: 100%;
}

.text {
  padding: 20px;
}

#blueimp-gallery > a.close,
#blueimp-gallery > a.next,
#blueimp-gallery > a.prev {
  color: #fff;
}

.ribbon_box2 {    
    display: block;
    position: relative;
    margin: 15px auto;
    padding: 0;
    box-sizing: border-box;
  }


.ribbon13-2 {    
    display: inline-block;
    position: absolute;
    top: -6px;
    right: 10px;
    margin: 0;
    padding: 5px 0 3px;
    z-index: 2;
    width: 40px;
    text-align: center;
    color: white;
    font-size: 13px;
    background: #fa8383;
    border-radius: 2px 0 0 0;
  }

.ribbon13-2 > i {
  font-size: 26px;
}

.ribbon13-2:before{
    position: absolute;
    content: '';
    top: 0;
    right: -5px;
    border: none;
    border-bottom: solid 6px #d07676;
    border-right: solid 5px transparent;
}

.ribbon13-2:after{
    content: '';
    position: absolute;
    left: 0;
    top: 100%;
    height: 0;
    width: 0;
    border-left: 20px solid transparent;
    border-right: 20px solid transparent;
    border-top: 10px solid #fa8383;
}

.download > span  {
  position: relative;
  display: block;
}

#header h1 {
  float: left;
  line-height: 100px;
  font-size: 30px;
  text-align: center;
  width: 100%;
  margin: 0 auto;
}
.generation h1{
  background-color: #fffaf0 
}

.download > span > a {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    color: #fff;
    width: 100%;
    height: 100%;
    text-align: center;
}

button.outline-none:focus {
  outline: none;
}

.img-responsive {
  max-width: 100%;
  height: auto;
}

.selectedImage {
  position: relative;
  min-height: 40px;
  cursor: pointer;
}

.selection-border {
  border: 1px solid #dcdfe6;
  border-bottom: none;
}

.selectedImage > .title {
    position: absolute;
    top: 0;
    left: 0;
    font-size: 18px;
    background: #000;
    padding: 10px;
    opacity: 0.45;
    color: #aaa;
}

.selectedImage > .number {
    position: absolute;
    top: 0;
    right: 0;
    font-size: 18px;
    background: #000;
    padding: 10px;
    opacity: 0.45;
    color: #aaa;
}

.move-trash {
    position: absolute;
    bottom: 0;
    right: 0;
    font-size: 18px;
    background: #000;
    padding: 10px;
    opacity: 0.45;
    color: #aaa;
}

.el-button--text:focus, .el-button--text:hover {
    background-color: #000;
    opacity: 0.45;
    color: #aaa;
    cursor: pointer;
}

.card-body {
  width: 70%;
}

.listItem {
  margin-left: 30px; 
  margin-top: 100px; /* 変更 */
  background-color: white;
  height: 650px;
  border-radius: 20px;
}

.el-header{
    background-color: #ffffff;
    filter: drop-shadow(1px 1px 1px rgba(0,0,0,0.6));
  }

.el-header img{
  float: left;
}

.el-header li {
  line-height: 8vh;
  font-size: 20px;
  margin-right: 30px;
}

.el-header a {
  color: black;
}

.el-header ul {
  float: right;
}

.el-aside {
  background-color: #fff;
  height: 100vh;
  filter: drop-shadow(1px 1px 1px rgba(0,0,0,0.6));
}

.el-main {
  padding: 100px;
  overflow: auto;
  height: 70vh;
  overflow: scroll;

}

.mockup {
  color: blue;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

img {
  width: 100%;
}

.alertImg {
   box-shadow: 0 0 8px gray;
   width: 75%;
   margin: 0 auto;
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

.alert {
  margin-top: 50px;
}

#modal-content{
  background:#fff;
  z-index:2;
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
  width: 80%;
  height:120%;
  background-color:rgba(0,0,0,0.75);
}

.alertCenter {
  margin-top: 15vh;  /* 変更 */
}

.css-fade2{
  animation-name:fade-in2;
  animation-duration:1s; 
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

footer {
  text-align: center;
  height: 80px;
}


.items-leave-active,
.items-enter-active {
    transition: opacity .5s, transform .5s ease;
}
.items-leave-to,
.items-enter {
    opacity: 0;
    transform: translateX(50px);
}
.items-leave,
.items-enter-to {
    opacity: 1;
}
.items-move {
    transition: transform .5s;
}

.el-menu-demo {
  background-color: #00000073;
}

.el-header li {
  display: inline;
}

.balloon2-left {
  width: 40%;
}

.balloon2-left {
  margin-top: 35vh;
}

@keyframes fade-in2 {
  0% {opacity: 0; transform: translate3d(0,-20px,0);}
  100% {opacity: 1; transform: translate3d(0,0,0);}
}

span {
  font-weight: 700;
}

</style>

