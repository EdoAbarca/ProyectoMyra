<script>

export default {

props: ['tipo', 'valor'],
}
</script>
<template>
  <div class="ContenedorEstadistica">
    <div id="tituloEstadistica">{{tipo}}</div>
    <div id="estadisticaNumerica"> {{valor}}</div>
  </div>

</template>
<style>
.ContenedorEstadistica{
  width: 25%;
  background-color: aliceblue;
  
  display: flex;
  align-items: center;
  text-align: center;
  flex-direction: column;
  margin: 2%;
  border-radius: 9px;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  font-family: Arial, Helvetica, sans-serif;
  font-size: 12px;
}
#tituloEstadistica{
  position: relative;
  display: flex;
  background-color: #48ABBF;
  color: aliceblue;
  width: 100%;
  height: 45%;
  justify-content: center;
  border-radius: 9px 9px 0px 0px;
  align-items: center;
  
}
#estadisticaNumerica{
  position: relative;
  display: flex;
  width: 100%;
  height: 100%;
  color: #48ABBF;
  justify-content: center;
  align-items: center;

  font-family: Arial, Helvetica, sans-serif;
  font-size: 30px;
  font-weight: 600;
}
</style>
