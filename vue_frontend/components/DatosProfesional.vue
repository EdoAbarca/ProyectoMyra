<script>
import DatosBasicosProf from './DatosBasicosProf.vue'
import Estadistica  from './Estadistica.vue'
import BotonObtener from './BotonObtener'

import Acordeon from './Acordeon.vue'
import { mapGetters, mapMutations } from 'vuex'

export default {
  components: {
    DatosBasicosProf,
    Estadistica,
    BotonObtener,
    Acordeon
    },
    computed:{
        ...mapGetters('profesional',[
            'getDatosBasicos',
            'getEstadisticas',
            'getMostrar'

        ])

    },
    methods:{
        ocultar(id){
            const box = document.getElementById(id);
            const itemToggle = box.getAttribute('aria-expanded');
            if (itemToggle == 'false') {
                box.setAttribute('aria-expanded', 'true');
            }
            else{
                box.setAttribute('aria-expanded', 'false');
            }

        }
    }
}
</script>
<template>
    <div class="ContenedorDatosP">
        <transition appear name="fade" >
            <div class="contEfecto" v-if="getMostrar===true">
                <div class="DatosBasicos">
                    <DatosBasicosProf 
                    :nombre="getDatosBasicos.nombre"
                    :rut="getDatosBasicos.rut"
                    :area="getDatosBasicos.area"
                    :cargo="getDatosBasicos.cargo"
                    :coordinador="getDatosBasicos.coordinador"
                    :contrato="getDatosBasicos.contrato"
                    />
                </div>
                <div class="EstadisticasProfesional">
                    <Estadistica tipo="Inasistencias" :valor="getEstadisticas.inasistencias"/>
                    
                    <Estadistica tipo="Horas totales" :valor="getEstadisticas.horasTotales"/>
                    <Estadistica tipo="Horas Extra" :valor="getEstadisticas.horasExtra"/>
                    <Estadistica tipo="Vacaciones" :valor="getEstadisticas.diasVacaciones"/>
                    <Estadistica tipo="Licencias" :valor="getEstadisticas.diasLicencia"/>
                </div>
                <div class="DatosCambiantes">
                    <div class="BotonesCambio">
                        <div class="BtnDerecha"> Remuneración</div>
                        <div class="BtnIzquierda">Asistencias</div>
                    </div>
                    <div class = "Informacion">
                        <Acordeon/>
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

.ContenedorDatosP{
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 95%;;

}
.contEfecto{
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;

}
.DatosBasicos{
    position: relative;
    display: flex;
    width: 100%;
    height: 20%;
    
}
.EstadisticasProfesional{

    position: relative;
    display: flex;
    width: 100%;
    height: 15%;
    flex-direction: row;
    justify-content: center;
}
.DatosCambiantes{
    position: relative;
    display: flex;
    background-color: #F9F9F9;
    width: 100%;
    height: 55%;
    flex-direction: column;
}
.BotonesCambio{
    display: flex;
    position: relative;
    
    width: 100%;
    height: 8%;
    font-size: 12px;
    font-family: Arial, Helvetica, sans-serif;
    

}
.BtnDerecha, .BtnIzquierda{
    position: relative;
    display: flex;
    width: 50%;
    height: 100%;
    justify-content: center;
    align-items: center;
    color: white;
    background-color: #669098;
    border-radius: 12.5px 0px 0px 0px;
    transition: all 200ms linear;
    cursor: pointer;
}

.BtnIzquierda{
    border-radius: 0px 12.5px 0px 0px;
}

.BtnDerecha:hover,.BtnIzquierda:hover{
    background-color: #52CBE2;
}



.Informacion{
    position: relative;
    display: flex;
    height: 100%;
    width: 100%;

    
}
.BtnObtenerReporte{
    position: relative;
    display: flex;
    width: 100%;
    bottom: 0;
    height: 10%;
    justify-content: center;
    align-items: center;

}


</style>