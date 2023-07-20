<script>
//import { mapState, mapGetters } from 'vuex'
import { mapMutations,mapActions } from 'vuex'
import EtiquetaProfesional from './EtiquetaProfesional.vue';

export default {

    props: ['nombre','rut','area','centro', 'id'],
    components:{
        EtiquetaProfesional
    },
    computed:{
    },
    methods:{
        ...mapMutations({
            mostrar: 'profesional/mostrar',
        }),
        ...mapActions('profesional',[
            'fetchProfesional'       
        ]), 
    }
}
</script>
<template>
    <li tabindex="0" class="ProfesionalLista" @click="fetchProfesional(id),mostrar(rut)">
        <div class="ContenedorEtiquetaProfesional">
            <EtiquetaProfesional id="etiquetaCentro" :area="null" :centro="centro"/>
            <EtiquetaProfesional id="etiquetaArea" :area="area" :centro="null"/>
        </div>
        <div class="ContenedorNombreProfesional">{{ nombre }}</div>
        <div class="ContenedorRutProfesional">{{ rut }}</div>
    </li>

</template>

<style>
.ProfesionalLista{
    margin-top: 5px;
    
    position: relative;
    width: 99%;
    height: 40px;
    display: flex;
    flex-direction: row;
    background-color: #F3F3F3;
    border-radius: 7px;
    text-align: center;
    overflow: hidden;

    font-family: Arial, Helvetica, sans-serif;
    font-weight: 500;
    cursor: pointer;
    transition: all 200ms linear;
    color: #253C41;
}
.ContenedorEtiquetaProfesional{
    position: relative;
    min-width: 220px;
    margin-left: 2%;
    width: 32%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.ContenedorNombreProfesional{
    position: relative;
    display: flex;
    width: 45%;
    min-width: 150px;
    height: 100%;
    margin-left: 10px;

    align-items: center;
    text-align: left;
    z-index: 100;
    font-size: 14px;
    

    
}

.ContenedorRutProfesional{
    width: 15%;
    height: 100%;
    min-width: 50px;
    left: -3%;
    display: flex;
    align-items: center;
    text-align: left;
    font-size: 14px;
    z-index: 200;
}
.ProfesionalLista:hover{
    background-color: #E7E7E7;
    color: #48ABBF;
}
.ProfesionalLista:focus{
    background-color: #E7E7E7;
    color: #48ABBF;
    
}

</style>