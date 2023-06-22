<script>
import DatosBasicosPaci from './DatosBasicosPaci.vue'
import Estadistica  from './Estadistica.vue'
import BotonObtener from './BotonObtener.vue'
import HistorialAsistenciaProf from './HistorialAsistenciaProf.vue'

import { mapState,mapGetters, mapMutations } from 'vuex'
import HistorialAtencion from './HistorialAtencion.vue'

export default {
  components: {
    DatosBasicosPaci,
    Estadistica,
    BotonObtener,
    HistorialAsistenciaProf,
    HistorialAtencion
},
    computed:{
        ...mapState('paciente',[
            'dataPaciente',
            'mostrarPac'       
        ]),
        ...mapGetters('paciente',[
            'getmostrarPac'

        ])

    },
    methods:{
        cambiar(id){
            if(id ==='remuneraciones'){
                document.getElementById('remuneraciones').style.zIndex = '100';
                document.getElementById('remuneraciones').style.opacity = '1';
                document.getElementById('btCambioDerecha').style.backgroundColor = '#669098';
                document.getElementById('asistencias').style.zIndex = '0';
                document.getElementById('asistencias').style.opacity = '0';
                document.getElementById('btCambioIzquierda').style.backgroundColor = '#5AB3C6';
                
            }
            else{
                document.getElementById('remuneraciones').style.zIndex = '0';
                document.getElementById('remuneraciones').style.opacity = '0';
                document.getElementById('asistencias').style.zIndex = '100';
                document.getElementById('asistencias').style.opacity = '1';

                document.getElementById('btCambioDerecha').style.backgroundColor = '#5AB3C6';
                document.getElementById('btCambioIzquierda').style.backgroundColor = '#669098';

            }

        }
    }
}
</script>
<template>
    <div class="ContenedorDatosP">
        <transition appear name="fade" >
            <div class="contEfecto" v-if="getmostrarPac == true">
                <div class="DatosBasicos">
                    <DatosBasicosPaci
                    :nombre="dataPaciente.nombre"
                    :rut="dataPaciente.rut"
                    :turno="dataPaciente.idTipoTurno_id"
                    :cliente="dataPaciente.idCliente_id"
                    :coordinador="dataPaciente.coordinador"
                    :cuidado="'falta este dato'"
                    :region ="dataPaciente.region"
                    :zona = "dataPaciente.zona"
                    />
                </div>
                <div class="EstadisticasProfesional">
                    <Estadistica tipo="Profesionales Activos" :valor="0"/>
                    <Estadistica tipo="Profesionales Diarios" :valor="3"/>
                    <Estadistica tipo="Profesionales Mensuales" :valor="5"/>
                </div>
                <div class="DatosCambiantes">
                    <div class="BotonesCambio">
                        <div class="BtnDerecha" id="btCambioDerecha" @click="cambiar('remuneraciones')"> Profesionales Activos</div>
                        <div class="BtnIzquierda" id="btCambioIzquierda" @click="cambiar('asistencias')">Historial de Atención</div>
                    </div>
                    <div class = "Informacion">
                        <HistorialAtencion id="remuneraciones"/>
                        <HistorialAtencion id="asistencias"/>
                        
                    </div>
                </div>
                <div class="BtnObtenerReporte">
                <BotonObtener/>
            </div>
        </div>
        
        
    </transition>

    </div>
</template>

<style>

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0
}

</style>