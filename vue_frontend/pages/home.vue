<script>
import BarraNav from "../components/BarraNav.vue";
import { mapGetters } from "vuex";


export default {
  name: "Home",
  data() {
    return {
      fechaReporte: "24-06-2021",
    };
  },
  components: {
    BarraNav,
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
  },
/** 
  mounted: async function () {
    const res = await this.$axios.get('/profesional/');
    const data = res.data;
    console.log(res);
    console.log(data);
  },*/
  methods: {
    async logoutHandler() {
      try {
        await this.$axios.post('/logout');
        //await this.$auth.logout();
        localStorage.removeItem('user');
        console.log(localStorage.getItem('user'));
        this.$nuxt.refresh();
      } catch (e) {
        console.log(e.message);
      }
    },
    async isLoggedin(){
      return localStorage.getItem('user');
    },
  },
};
</script>

<template>
  <div class="ContenedorPrincipal">
    <div class="Navegacion">
      <BarraNav />
    </div>
    <div class="Contenedores">
      <div class="ContenedorGris" id="cont-home">
        <div class="ContenedorBtnImagenes">
          <NuxtLink class="BtnImg" id="btImgProfesionales" to="/profesionales">
            <img
              async
              class="imgB"
              id="imgProf"
              src="../static/profesionalImg.svg"
            />
            <div class="EtiquetaBotonImg">
              <h1 class="tituloBtnImg">Profesionales</h1>
            </div>
          </NuxtLink>
          <NuxtLink class="BtnImg" id="btImgPacientes" to="/pacientes">
            <img
              async
              class="imgB"
              id="imgPac"
              src="../static/pacientesImg2.svg"
            />
            <div class="EtiquetaBotonImg">
              <h1 class="tituloBtnImg">Pacientes</h1>
            </div>
          </NuxtLink>
          <NuxtLink class="BtnImg" id="btImgAlerta" to="/alertas">
            <img
              async
              class="imgB"
              id="imgAle"
              src="../static/alertasImg.svg"
            />
            <div class="EtiquetaBotonImg">
              <h1 class="tituloBtnImg">Alertas</h1>
            </div>
          </NuxtLink>
        </div>
        <div class="ContenedorBtnSubir">
          <div class="BtnSubir">Subir Reporte</div>
        </div>
        <v-btn v-if="isLoggedin" id="boton" @click="logoutHandler">Cerrar sesión</v-btn>
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

  margin-top: 1%;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.ContenedorGris {
  position: relative;
  width: 46%;
  height: 100%;
  background-color: #fcfcfc;
  justify-content: center;
}
.ContenedorBtnImagenes {
  position: relative;
  width: 80%;
  height: 70%;
  display: flex;
  justify-content: center;
  flex-direction: row;
}
#cont-home {
  position: relative;
  width: 94%;
  display: flex;

  flex-direction: column;
  align-items: center;
}

.BtnImg {
  position: relative;
  width: 26%;
  height: 100%;
  background-color: white;
  display: flex;
  margin-left: 2%;
  margin-right: 2%;
  border-radius: 20px;
  overflow: hidden;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));

  transition: all 200ms linear;
  cursor: pointer;
}
.imgB {
  position: relative;
  top: -2%;
  left: -20%;
  height: 110%;
  filter: opacity(0.8);
  transition: all 400ms linear;
}
.BtnImg:hover > .imgB {
  transform: translateX(-25%);
}

.BtnImg:hover > .EtiquetaBotonImg {
  background-color: rgba(64, 129, 142, 0.8);
}
.ContenedorBtnSubir {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80%;
  height: 20%;
}
.EtiquetaBotonImg {
  position: absolute;
  width: 100%;
  height: 20%;
  background-color: rgba(72, 171, 191, 0.8);
  z-index: 200;
  bottom: 0;
  justify-content: center;
  transition: all 400ms linear;
}

.tituloBtnImg {
  font-size: 25px;
  font-weight: 600;
  font-family: Arial, Helvetica, sans-serif;
  position: relative;
  top: 25%;
  text-align: center;
  color: white;
}
.BtnSubir {
  position: relative;
  width: 30%;
  height: 50%;
  background-color: #2db7b2;
  border-radius: 27px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 15px;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: 600;
}
.BtnSubir:hover {
  transition: all 200ms linear;
  background-color: #2d9894;
  cursor: pointer;
}

#boton {
  background-color: #48abbf;
  color: #ffffff;
  border-radius: 9px;
  margin-top: 3%;
}


</style>
