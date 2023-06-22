<script>
import BarraNav from "../components/BarraNav.vue";
import ContenidoLista from "../components/ContenidoLista.vue";
import BuscadorProfesionales from "../components/BuscadorProfesionales.vue";
import DatosProfesional from "../components/DatosProfesional.vue";

export default {
  head() {
    return {
      title: "Vista profesionales - Rotativa Myra",
    };
  },
  middleware: "auth",
  data() {
    return {
      fechaReporte: "24-06-2021",
    };
  },
  components: {
    BarraNav,
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
        <BuscadorProfesionales />
        <ContenidoLista />
      </div>
      <div class="Separador"></div>
      <div class="ContenedorGris">
        <DatosProfesional />
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

  margin-top: 1%;
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
  position: relative;
  width: 46%;
  height: 100%;
  background-color: #fcfcfc;
  justify-content: center;
}
</style>
