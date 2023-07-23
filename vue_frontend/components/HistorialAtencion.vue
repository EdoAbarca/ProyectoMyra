<script>

import { mapState } from 'vuex'
import { mapMutations } from 'vuex'
import { mapGetters } from 'vuex'
import AsistenciaProf from './AsistenciaProf.vue'
import axios from 'axios'
import AsistenciaEnPaciente from './AsistenciaEnPaciente.vue'

export default {
  name:'HistorialAtencion',
  data() {
        return {
          datos:[]
        }
    },
  components: {
    AsistenciaProf,
    AsistenciaEnPaciente
},
  computed:{
    ...mapState('paciente',[
            'historialAtencion',     
        ]),
    }       
}

</script>

<template>
    <div class="contenedorHistoriaAtencion"  >
        <div class="barraDatos" id="barraDatosHistorial" >
          <h1 id="tituloEstado">Estado</h1>
          <h1 id="tituloFecha">Fecha</h1>
          <h1 id="tituloArea">Área</h1>
          <h1 id="tituloNombreProfesional">Profesional</h1>
          <h1 id="tituloRutProfesional">Rut</h1>
        
        </div>
        <div class ="ContenidoHistorial" :v-model="historialAtencion">
            <div>
                <AsistenciaEnPaciente v-for="(assist) in historialAtencion"
                    :key="assist.id"
                    :nombre="assist.nombreProfesional"
                    :rut="assist.rutProfesional"
                    :area ="assist.idArea_id"
                    :fecha="assist.fechaAsistencia"
                    :estado ="assist.estado"
                    :idProf = "assist.idProfesional_id"
    
                />
            </div>   
        </div>

    </div>
</template>

<style>
#tituloEstado{
    position: relative;
    display: flex;
    width: 15%;
    height: 100%;
    min-width: 120px;
    justify-content: center;
    align-items: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 13px;
    font-weight: 600;
}
#tituloFecha{
  position: relative;
  display: flex;
  width: 10%;
  min-width: 85px;
  justify-content: center;
  align-items: center;
  font-family: Arial, Helvetica, sans-serif;
  font-size: 13px;
  font-weight: 600;
}
.contenedorHistoriaAtencion{
    background-color: white;
    position: absolute;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 82%;
    top: 0;
    border-radius: 12.5px;
}
.ContenidoHistorial{
    position: relative;
    height: 100%;
    overflow-y: scroll;

    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));

}
.barraDatos{
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
    height: 25px;
    background-color: #BBBBBB;
    color: white;
}
</style>