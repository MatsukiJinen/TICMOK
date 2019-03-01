<template>
	<div id="header">
       <div class="navs">
        <ul class="nav">
          <li class="nav-item">
            <a class="nav-link active" href="/">Top</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/random">Random</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/manual">Manual</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" :href="link">Movie</a>
          </li>
        </ul>   
      </div>
  <div class="title">
		<h1>MockUpAutomatic Generation Site</h1>
    <div id="left">
        <a href="/"><span data-text="リンクテキスト-link text-">TOP</span></a>
        <a href="/manual"><span data-text="リンクテキスト-link text-">Manual</span></a>
        <a href="/random"><span data-text="リンクテキスト-link text-">Random</span></a>
     </div>
       <div class="subtitle">
        <div class="generation">
         <h2>{{ title }}</h2>
        </div>
       </div>
      </div>
	</div>
</template>

<script>
    export default {
        props:['title','link']
    }
</script>

<style scoped>

#left {
  float: right;
  margin-right: 30px;
}

#left a {
  margin-right: 30px;
  font-weight: bold;
  line-height: 100px;
}

#header h1 {
	float: left;
	line-height: 100px;
	font-weight: bold;
  font-size: 30px;
  text-align: center;
  width: 60%;
  margin: 0 auto;
}

.generation {
    display: none;
}

#header {
	background-color:  white;
    height: 100px;
}

#header h2 {
    font-size: 18px;
    font-weight: bold;
    text-align: center;
}

#header {
  background-color: #35424a;
  color: white;
  border-bottom: #e8491d 3px solid;
}

.nav {
    display: none;
}

#header a {
    color: white;
}

@media(max-width: 1024px) {
   #header h1 {
    font-size: 20px;
    line-height: 50px;
    animation:fadeIn 0.1s 0.5s; 
    animation-fill-mode: both;
    float: none;
    width: 100%;
  }

  #header h1 span {
    font-size: 12px;
  }

  #header h2 {
    animation:fadeIn 0.1s 0.5s; 
    animation-fill-mode: both;
  }

  #header {
    height: 150px
  }

  .generation {
    display: block;
  }

  #left {
    display: none;
  }

  .nav {
    display:block;
    background-color: #e8491d;
    height: 60px;
    line-height: 60px;
    text-align: center;
    color: white;
    border-bottom: #35424a 3px solid;
  }

  .nav li {
    display: inline-block;
    animation:fadeIn 0.1s 0.5s; 
    animation-fill-mode: both;
  }

   a {
    font-weight: bold;
    color: black;
    display: inline-block;
    transition: .3s;
  }

    a:hover {
      transform: rotate(5deg);
    }

    .generation h2 {
     animation-name: RightToLeft;
     animation-duration: 2s;
    }

    .navs {
      overflow:hidden;
      position:relative;
    }
    .navs:after{  
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      background-color: #fffaf0;
      animation: 
      secondaryImageOverlayIn 0.6s 0s cubic-bezier(.77,0,.175,1), 
      secondaryImageOverlayOut 0.6s 0.6s cubic-bezier(.77,0,.175,1);
      animation-fill-mode: both;
    }

    .title {
      overflow:hidden;
      position:relative;
      background-color: #fffaf0;
      color: black;
    }
    
    .title:after{  
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      background-color: #e8491d;
      animation: 
      secondaryImageOverlayIn 0.6s 0s cubic-bezier(.77,0,.175,1),
      secondaryImageOverlayOut2 0.6s 0.6s cubic-bezier(.77,0,.175,1);
      animation-fill-mode: both;
    }
}

@media(max-width: 769px) {
 #header h1 {
    font-size: 20px;
    line-height: 50px;
    animation:fadeIn 0.1s 0.5s; 
    animation-fill-mode: both;
    float: none;
    width: 100%;
  }

  #header h1 span {
    font-size: 12px;
  }

  #header h2 {
    animation:fadeIn 0.1s 0.5s; 
    animation-fill-mode: both;
  }

  #header {
    height: 150px
  }

  .generation {
    display: block;
  }

  #left {
    display: none;
  }

  .nav {
    display:block;
    background-color: #e8491d;
    height: 60px;
    line-height: 60px;
    text-align: center;
    color: white;
    border-bottom: #35424a 3px solid;
  }

  .nav li {
    display: inline-block;
    animation:fadeIn 0.1s 0.5s; 
    animation-fill-mode: both;
  }

   a {
    font-weight: bold;
    color: black;
    display: inline-block;
    transition: .3s;
  }

    a:hover {
      transform: rotate(5deg);
    }

    .generation h2 {
     animation-name: RightToLeft;
     animation-duration: 2s;
    }

    .navs {
      overflow:hidden;
      position:relative;
    }
    .navs:after{  
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      background-color: #fffaf0;
      animation: 
      secondaryImageOverlayIn 0.6s 0s cubic-bezier(.77,0,.175,1), 
      secondaryImageOverlayOut 0.6s 0.6s cubic-bezier(.77,0,.175,1);
      animation-fill-mode: both;
    }

    .title {
      overflow:hidden;
      position:relative;
      background-color: #fffaf0;
      color: black;
    }
    
    .title:after{  
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      height: 100%;
      background-color: #e8491d;
      animation: 
      secondaryImageOverlayIn 0.6s 0s cubic-bezier(.77,0,.175,1),
      secondaryImageOverlayOut2 0.6s 0.6s cubic-bezier(.77,0,.175,1);
      animation-fill-mode: both;
    }
}

@keyframes fadeIn {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }
@keyframes secondaryImageOverlayIn {
    0% {
      width: 0;
    }
    100% {
      width:  100%;
    }
  }
  @keyframes secondaryImageOverlayOut {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(102%);
    }
  }

  @keyframes secondaryImageOverlayOut2 {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(-102%);
    }
  }

</style>