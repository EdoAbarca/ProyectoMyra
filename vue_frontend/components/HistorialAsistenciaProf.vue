<script>

import { mapState } from 'vuex'
import { mapMutations } from 'vuex'
import { mapGetters } from 'vuex'
import AsistenciaProf from './AsistenciaProf.vue'
import axios from 'axios'

export default {
  data() {
        return {
          datos:[]
        }
    },
  components: {
    AsistenciaProf
    },
  computed:{
    ...mapState('profesional',[
            'asistencias',     
        ]),
    }        
}
</script>

<template>
    <div class="contenedorHistoriaAsistencias">
        <div class="barraDatos" id="barraDatosHistorial">
          <h1 id="tituloEstado">Estado</h1>
          <h1 id="tituloFecha">Fecha</h1>
          <h1 id="tituloNombreProfesional">Paciente</h1>
          <h1 id="tituloRutProfesional">Rut</h1>
        
        </div>
        <div class ="ContenidoHistorial" :v-model="asistencias">
            <ul>
                <AsistenciaProf v-for="(assist) in asistencias"
                    :key="assist.id"
                    :nombrePaciente="assist.nombrePaciente"
                    :rutPaciente="assist.rutPaciente"
                    :estado ="assist.estado"
                    :fecha="assist.fechaAsistencia"
                    :idPac="assist.idPaciente_id"
                />
            </ul>   
        </div>

    </div>
</template>

<style>
.contenedorHistoriaAsistencias{
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 82%;
    top: 0;
    background-color: white;
    border-radius: 12.5px;
}
.ContenidoHistorial{
    position: relative;
    height: 100%;
    padding-left: 1%;
    overflow-y: scroll;    
}
#barraDatosHistorial{
  border-radius: 12.5px 12.5px 0 0;
}
</style>