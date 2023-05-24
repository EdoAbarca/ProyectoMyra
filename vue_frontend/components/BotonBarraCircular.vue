<template>
    <div id ="fondoBotonCircular">
        
        <NuxtLink class="btnCircular" to="/">
            <img class="home casa"  src="../static/home1.svg" alt="">
        </NuxtLink>
    </div>

</template>
<script>
</script>
<style>
#fondoBotonCircular{
    position: relative;
    background-color: #EEF7F9;
    margin-top: 2px;
    border-radius: 35px;
    width: 35px;
    height: 35px;
    z-index: -1;
}
.btnCircular {
  overflow: hidden;
  position: relative;
  display: flex;
  width: 100%;
  height: 100%;
  border-radius: 40px;
  border:none;
  transition: 0.3s;
  z-index: 2;
  background-color: #EEF7F9;
  transition: all 200ms linear;
  
  

}

.btnCircular:hover {
  background-color: #48ABBF;
  color: white;
}
.home{
    position:relative;
    left: -10px;
    top:-10px;
    width: 55px;
    height: 55px;
    z-index: 1;
    cursor: pointer;


}
.casa:hover{
    content: url("../static/home2.svg");
}


</style>

