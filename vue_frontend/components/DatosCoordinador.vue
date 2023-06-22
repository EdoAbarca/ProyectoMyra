<script>
import DatosBasicosCoord from './DatosBasicosCoord.vue'
import Estadistica  from './Estadistica.vue'
import BotonObtener from './BotonObtener.vue'
import HistorialAsistenciaProf from './HistorialAsistenciaProf.vue'

import { mapState,mapGetters, mapMutations } from 'vuex'
import HistorialAtencion from './HistorialAtencion.vue'

export default {
  components: {
    DatosBasicosCoord,
    Estadistica,
    BotonObtener,
    HistorialAsistenciaProf,
    HistorialAtencion
},
    computed:{
        ...mapState('coordinador',[
            'dataCoordinador',
            'mostrar'       
        ]),
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
            <div class="contEfecto" v-if="mostrar == true">
                <div class="DatosBasicos">
                    <DatosBasicosCoord
                    :nombre="dataCoordinador.nombre"
                    :rut="dataCoordinador.rut"
                    :area="'area'"
                    :centro="dataCoordinador.idCentro_id"
                    />
                </div>
                <div class="EstadisticasProfesional">
                    <Estadistica tipo="Despidos totales" :valor="0"/>
                    <Estadistica tipo="Inasistencias de Profesionales" :valor="3"/>
                    <Estadistica tipo="Profesionales Mensuales" :valor="5"/>
                </div>
                <div class="DatosCambiantes">
                    <div class="BotonesCambio">
                        <div class="BtnDerecha" id="btCambioDerecha" @click="cambiar('remuneraciones')"> Profesionales a Cargo</div>
                        <div class="BtnIzquierda" id="btCambioIzquierda" @click="cambiar('asistencias')">Pacientes a Cargo</div>
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