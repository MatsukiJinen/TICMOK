<template>
    <el-container>
      <el-container >
       <el-aside width="53%">
        <div class="aside">
          <h1><span>Tic Mock</span></h1>
          <h2><span>Mock</span>Up <br> Automa<span>tic</span> <br>Generation Site</h2>
          <h3><img src="../../../img/icons8-checkmark.svg" class="icon">
          Tic Mock ー HTMLファイルを自動生成するためのサービスです。</h3>
          <h3><img src="../../../img/icons8-checkmark.svg" class="icon">
          RANDOM ー HTMLファイルをランダムに生成します。</h3>
          <h3><img src="../../../img/icons8-checkmark.svg" class="icon">
          MANUAL ー HTMLファイルを任意に生成します。</h3>
          <a href="/random" class="cp_btn"><span>RANDOM</span></a>
          <a href="/manual" class="cp_btn"><span>MANUAL</span></a>
       </div> 
       </el-aside>
       <el-main>
        <el-carousel  arrow="always" class="carousel">
          <el-carousel-item style="height: 300px;">
           <div class="carousel_mac" style="width: 65%; margin:0 auto">
            <img src="../../../img/mac.png" style="width: 85%; margin-left: 50px;">
            </div>
          </el-carousel-item>
           <el-carousel-item>
           <div class="carousel_tablet">
            <img src="../../../img/tablet.png" style="width: 80%;margin-left: 50px;">
          </div>
          </el-carousel-item>
            <el-carousel-item >
           <div class="carousel_iphone">
           <div class="iphoneContainer">
            <img src="../../../img/iphone.png" style="width: 30%;margin-left: 220px;">
           </div>
           </div>
          </el-carousel-item>
        </el-carousel>
       </el-main>
      </el-container>
    </el-container>
</template>

<script>
  import { Carousel, Slide } from 'vue-carousel';

export default {
  components: {
    Carousel,
    Slide
  }
}
</script>

<style scoped>

 h1,h2,h3 {
  font-family: Graphik Web,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Fira Sans,Droid Sans,Helvetica Neue,sans-serif;
 }

  a {
     margin-top: 20px;
  }

  .el-container {
    background-color: #FFBF00;
  }

  .el-aside {
    background-color: white;
    height: 100vh;
    border-radius:  0 60px 60px 0;
     box-shadow: 3px 3px 6px -2px #555,3px 3px 8px rgba(255,255,255,0.8) inset;
  }

  .el-main {
    height: 100vh;
  }

.aside {
  width: 75%;
  margin: 0 auto;
  height: auto;
  margin-top: 250px;
}

h1 {
  font-weight: 900;
  margin-bottom: 30px;
  font-size: 5vw;
  line-height: 50px;
}

h2 span {
  color: blue;
}

h2 {
  font-size: 3vw;
  font-weight: bold;
  margin-bottom: 20px;
  padding-left: 20px;
}

h3 {
  font-size: 1.2vw;
  font-weight: bold;
  line-height: 25px;
  margin-bottom: 10px;
}

a.cp_btn {
  display: inline-block;
  text-decoration:none;
  width: 200px;
  padding: 0.8em;
  text-align: center;
  color: #FFF;
  border-radius: 100px;
  background: blue;
  overflow: hidden;
  margin-right: 30px;
}

a.cp_btn span {
  display:inline-block;
  transition: .5s;
  font-size: 20px;
  font-weight: bold;
}

a.cp_btn:hover span {
  transform: rotateX(360deg);
}
/* 
img {
  width: 90%;
} */

.icon {
  width: 3%;
}

.el-main {
  position: relative;
}

.carousel {
  height: 38vh;
  position: absolute;
  top: 0px;
  right: 0px;
  bottom: 0px;
  left: 0px;
  margin: auto;
}

.el-carousel__container  {
  height: 400px;
}

.carousel_tablet,
.carousel_iphone {
  width: 70%;
  margin: 0 auto;
}

.el-carousel__arrow i {
  margin-top: 200px;
}

. {
  width: 50%;
  margin: 0 auto;
}

.carousel_iphone img {
  width: 45%;
  margin-left: 140px
}

.el-carousel__item {
  height: 700px;
}


</style>