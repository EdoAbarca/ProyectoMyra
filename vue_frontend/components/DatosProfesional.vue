<script>
import DatosBasicosProf from "./DatosBasicosProf.vue";
import Estadistica from "./Estadistica.vue";
import BotonObtener from "./BotonObtener.vue";
import HistorialAsistenciaProf from "./HistorialAsistenciaProf.vue";

import Acordeon from "./Acordeon.vue";
import { mapState, mapGetters, mapMutations } from "vuex";
import * as XLSX from "xlsx";

export default {
  components: {
    DatosBasicosProf,
    Estadistica,
    BotonObtener,
    Acordeon,
    HistorialAsistenciaProf,
  },
  computed: {
    ...mapState("profesional", ["dataProfesional"]),
    ...mapGetters("profesional", [
      "getDatosBasicos",
      "getEstadisticas",
      "getMostrar",
    ]),
  },
  methods: {
    ocultar(id) {
      const box = document.getElementById(id);
      const itemToggle = box.getAttribute("aria-expanded");
      if (itemToggle == "false") {
        box.setAttribute("aria-expanded", "true");
      } else {
        box.setAttribute("aria-expanded", "false");
      }
    },
    cambiar(id) {
      if (id === "remuneraciones") {
        document.getElementById("remuneraciones").style.zIndex = "100";
        document.getElementById("remuneraciones").style.opacity = "1";
        document.getElementById("btCambioDerecha").style.backgroundColor =
          "#669098";
        document.getElementById("asistencias").style.zIndex = "0";
        document.getElementById("asistencias").style.opacity = "0";
        document.getElementById("btCambioIzquierda").style.backgroundColor =
          "#5AB3C6";
      } else {
        document.getElementById("remuneraciones").style.zIndex = "0";
        document.getElementById("remuneraciones").style.opacity = "0";
        document.getElementById("asistencias").style.zIndex = "100";
        document.getElementById("asistencias").style.opacity = "1";

        document.getElementById("btCambioDerecha").style.backgroundColor =
          "#5AB3C6";
        document.getElementById("btCambioIzquierda").style.backgroundColor =
          "#669098";
      }
    },
    //FUNCION PARA EXPORTAR EXCEL
    async getReportHandler() {
      try {
        const res = await this.$axios.get("/reporte_profesional/1"); //El "1" debe ser el ID del profesional, a recuperar desde la vista de muestra de datos
        let data = res.data;

        // Create a new workbook
        const workbook = XLSX.utils.book_new();

        // Create a worksheet and add the data to it
        const worksheet = XLSX.utils.json_to_sheet(data.data);
        XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");

        // Generate the Excel file
        const excelBuffer = XLSX.write(workbook, {
          bookType: "xlsx",
          type: "array",
        });

        // Convert the Excel buffer to a Blob
        const blob = new Blob([excelBuffer], {
          type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        });

        // Create a URL object from the Blob
        const url = window.URL.createObjectURL(blob);

        // Create a temporary link element and set its properties
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "reportePrueba.xlsx");

        // Simulate a click on the link to initiate the file download
        link.click();

        // Clean up the URL object
        window.URL.revokeObjectURL(url);
      } catch (e) {
        console.log("Error: ", e);
      }
    },
  },
};
</script>
<template>
  <div class="ContenedorDatosP">
    <transition appear name="fade">
      <div class="contEfecto" v-if="getMostrar === true">
        <div class="DatosBasicos">
          <DatosBasicosProf
            :nombre="dataProfesional.nombre"
            :rut="dataProfesional.rut"
            :area="dataProfesional.idArea_id"
            :centro="dataProfesional.idCentro_id"
            :coordinador="dataProfesional.nombreCoordinador"
            :contrato="dataProfesional.tipoContrato"
            :idCoord="dataProfesional.idCoordinador_id"
          />
        </div>
        <div class="EstadisticasProfesional">
          <Estadistica
            tipo="Inasistencias"
            :valor="dataProfesional.inasistencias"
          />

          <Estadistica
            tipo="Horas totales"
            :valor="dataProfesional.horasTotales"
          />
          <Estadistica
            tipo="Horas Extra"
            :valor="dataProfesional.horasExtras"
          />
          <Estadistica tipo="Vacaciones" :valor="dataProfesional.vacaciones" />
          <Estadistica tipo="Licencias" :valor="dataProfesional.licencia" />
        </div>
        <div class="DatosCambiantes">
          <div class="BotonesCambio">
            <div
              class="BtnDerecha"
              id="btCambioDerecha"
              @click="cambiar('remuneraciones')"
            >
              Remuneración
            </div>
            <div
              class="BtnIzquierda"
              id="btCambioIzquierda"
              @click="cambiar('asistencias')"
            >
              Asistencias
            </div>
          </div>
          <div class="Informacion">
            <Acordeon id="remuneraciones" />
            <HistorialAsistenciaProf id="asistencias" />
          </div>
        </div>
        <div class="BtnObtenerReporte">
          <BotonObtener />
        </div>
      </div>
    </transition>
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

.ContenedorDatosP {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 95%;
}
.contEfecto {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}
.DatosBasicos {
  position: relative;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 20%;
}
.EstadisticasProfesional {
  position: relative;
  display: flex;
  width: 100%;
  height: 15%;
  flex-direction: row;
  justify-content: center;
}
.DatosCambiantes {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 55%;
  justify-content: center;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.15));
}
.BotonesCambio {
  display: flex;
  position: relative;
  left: 25%;
  width: 50%;
  height: 8%;
  font-size: 14px;
  font-weight: 500;
  font-family: Arial, Helvetica, sans-serif;
  z-index: -1;
  background-color: #5ab3c6;
  border-radius: 12.5px 12.5px 0 0;
}

.BtnDerecha,
.BtnIzquierda {
  position: relative;
  display: flex;
  width: 50%;
  height: 100%;
  justify-content: center;
  align-items: center;
  color: white;

  border-radius: 12.5px 12.5px 0px 0px;
  transition: all 200ms linear;
  cursor: pointer;
  background-color: #669098;
}

.BtnIzquierda {
  border-radius: 12.5px 12.5px 0px 0px;
  background-color: #5ab3c6;
}

.Informacion {
  position: relative;
  display: flex;
  height: 100%;
  left: 3%;
  width: 93%;
  justify-content: center;
  transition: all 200ms linear;
}
.BtnObtenerReporte {
  position: relative;
  display: flex;
  width: 100%;
  bottom: 0;
  height: 10%;
  justify-content: center;
  align-items: center;
}
#remuneraciones {
  width: 100%;
  height: 100%;
  z-index: 100;
  opacity: 1;
  transition: all 250ms linear;
}
#asistencias {
  width: 100%;
  height: 100%;
  opacity: 0;
  z-index: -100;
  transition: all 250ms linear;
}
</style>