<script>
import BotonBarra from "./BotonBarra.vue";
import BotonBarraCircular from "./BotonBarraCircular.vue";

export default {
  data() {
    return {
      fechaReporte: "24-06-2021",
    };
  },
  components: {
    BotonBarra,
    BotonBarraCircular,
  },
};
</script>

<template>
  <nav class="BarraNavegacion">
    <div id="barraAzul"></div>
    <nav id="barraGris">
      <div id="botonesNavegacion">
        <BotonBarraCircular id="bHome" />
      </div>
      <div id="botonesGenerales">
        <BotonBarra
          id="bProfesionales"
          tipo="Profesionales"
          link="/profesionales"
        />
        <BotonBarra id="bPacientes" tipo="Pacientes" link="/pacientes" />
        <BotonBarra
          id="bCoordinadores"
          tipo="Coordinadores"
          link="/coordinadores"
        />
        <BotonBarra id="bAlertas" tipo="Alertas" />
      </div>
      <div id="ultimoReporte">Último Reporte: {{ fechaReporte }}</div>
    </nav>
  </nav>
</template>

<style>
/*----------------------BARRAS DE NAVEGACIÓN---------------------- */
.BarraNavegacion {
  position: absolute;
  width: 100%;
  height: 60px;
  left: 0px;
  top: 0px;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  font-family: Arial, Helvetica, sans-serif;
}
#barraAzul {
  position: absolute;
  width: 100%;
  height: 20px;
  left: 0px;
  top: 0px;
  background: #005d71;
  z-index: -2;
}
#barraGris {
  position: absolute;
  width: 100%;
  height: 40px;
  left: 0px;
  top: 20px;
  z-index: -1;
  background: #eef7f9;
  display: flex;
  flex-direction: row;
  align-items: center;
}

/*----------------------CONTENEDORES DE BOTONES---------------------- */
#botonesNavegacion {
  position: relative;
  background-color: #eef7f9;
  height: 100%;
  width: 25%;
  z-index: 4;
  align-items: center;
}

#botonesGenerales {
  position: absolute;
  background-color: #48abbf;
  border-radius: 0px 0px 30px 30px;
  left: 25%;
  height: 100%;
  width: 50%;
  z-index: 4;
}
#ultimoReporte {
  display: flex;
  align-items: center;
  text-align: center;
  position: absolute;
  justify-content: center;
  width: 25%;
  height: 100%;
  right: 0px;
  z-index: 4;

  font-weight: 700;
  font-size: small;
  color: #005d71;
}

/*----------------------BOTONES GENERALES---------------------- */
#bProfesionales {
  width: 25%;
  height: 100%;
  z-index: 10;
}
#bPacientes {
  width: 25%;
  height: 100%;
  left: 25%;
  z-index: 10;
}
#bCoordinadores {
  width: 25%;
  height: 100%;
  left: 50%;
  z-index: 10;
}
#bAlertas {
  width: 25%;
  height: 100%;
  right: 0%;
  z-index: 10;
}
#bHome {
  margin-left: 85%;
  margin-top: 3px;
  width: 35px;
  height: 35px;
}
</style>
  