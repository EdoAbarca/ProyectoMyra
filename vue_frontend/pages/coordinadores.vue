<script>
import BarraNav from "../components/BarraNav.vue";
import ContenidoLista from "../components/ContenidoLista.vue";
import BuscadorProfesionales from "../components/BuscadorProfesionales.vue";
import DatosProfesional from "../components/DatosProfesional.vue";

import DatosCoordinador from "../components/DatosCoordinador.vue";
export default {

  data() {
    return {
      fechaReporte: "24-06-2021",
    };
  },
  components: {
    BarraNav,
    DatosCoordinador
},
};
</script>

<template>
  <div class="ContenedorPrincipal">
    <div class="Navegacion">
      <BarraNav />
    </div>
    <div class="Contenedores">
      <div class="ContenedorGris">
        <div class="fondoGris" >
          <BuscadorProfesionales :page="'coordinadores'" />
          <ContenidoLista :page="'coordinadores'" />
        </div>
        
      </div>
      <div class="Separador"></div>
      <div class="ContenedorGris">
        <div class="fondoGris" >
          <DatosCoordinador />
        </div>
        
      </div>
    </div>
  </div>
</template>


<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: content-box;
}
.ContenedorPrincipal {
  position: absolute;
  width: 100%;
  height: 100%;
  min-width: 1024px;
  min-height: 100%;

  display: flex;
  flex-direction: column;
}
.Navegacion {
  position: relative;
  width: 100%;
  height: 60px;

  z-index: 10;
}
.Contenedores {

  overflow: hidden;
  box-sizing: border-box;
  position: relative;
  width: 100%;
  height: 100%;

  margin-top: 0px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}
.Separador {
  position: relative;
  width: 3%;
  height: 100%;
}
.ContenedorGris {
  display: flex;
  flex-direction: column;
  position: relative;
  width: 46%;
  min-width: 600px;
  height: 100%;
  background-color: #F7F7F7;
  justify-content: center;
}
.fondoGris{
  margin-top: 4%;
  width: 100%;
  height: 100%;
}
</style>
