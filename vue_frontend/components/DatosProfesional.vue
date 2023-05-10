<script>
import DatosBasicosProf from './DatosBasicosProf.vue'
import { mapGetters } from 'vuex'

export default {
  components: {
    DatosBasicosProf
    },
    computed:{
        ...mapGetters('profesional',[
            'getNombre',
            'getRut',
            'getArea'
        ])

    }
}
</script>
<template>
    <div class="ContenedorDatosP">
        <div class="DatosBasicos">
            <DatosBasicosProf 
            :nombre="getNombre"
            :rut="getRut"
            :area="getArea"
            />
        </div>
        <div class="EstadisticasProfesional">

        </div>
        <div class="DatosCambiantes">
            <div class="BotonesCambio"></div>
            <div class = "Informacion"></div>
        </div>

    </div>
</template>

<style>
.ContenedorDatosP{
    display: flex;
    flex-direction: column;
    background-color: aqua;
    width: 100%;
    height: 95%;;

}
.DatosBasicos{
    display: flex;
    width: 100%;
    height: 20%;
    
}
.EstadisticasProfesional{

    display: flex;
    background-color: lightcoral;
    width: 100%;
    height: 20%;
}
.DatosCambiantes{
    display: flex;
    background-color: lightgoldenrodyellow;
    width: 100%;
    height: 50%;
}
</style>