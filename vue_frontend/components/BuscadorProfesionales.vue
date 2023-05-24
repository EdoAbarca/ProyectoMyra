<script>
import DropBox from './DropBox.vue'
import {mapMutations} from 'vuex'

export default {
    data(){
        return{
            datoBuscado:null

        }
    },
    components: {
        DropBox
    },
    methods:{
        ...mapMutations({
            datoPorBuscar: 'profesional/datoPorBuscar'
        }),
        buscar(){
            if(this.datoBuscado ===''){
                this.datoPorBuscar(null)
            }
            else{
                this.datoPorBuscar(this.datoBuscado)
            }   
        }

    }
  }
</script>

<template>
    <div class="ContenedorBuscador">
        <div class="BarraBusqueda">
            <input type="search" placeholder="Ingresa el nombre" id="buscador" v-model="datoBuscado" @keyup.enter="buscar()"/>
            <div class="BotonBusqueda"><img class="lupa" src="../static/iconolupa.svg" alt=""></div>
        </div>
        <div class="BarraFiltro">
            <div class="FondoDrop"></div>
            <DropBox/>
        </div>
    </div>
</template>

<style>
.ContenedorBuscador{
    position: relative;
    display: flex;
    flex-direction: column;
    
    width: 100%;
    height: 80px;
    font-family: Arial, Helvetica, sans-serif;
    
}
.BarraBusqueda{
    position: relative;
    display: flex;
    width: 100%;
    height: 60%;

    border-radius: 16px 16px 16px 0px;
    background-color: #D9D9D9;;
    
    flex-direction: row;
    align-items: center;
    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));
}
.BotonBusqueda{
    position: relative;
    display: flex;
    width: 10%;
    height: 100%;

    align-items: center;
    justify-content: center;

}

.FondoDrop{
    position: absolute;
    background-color: #D9D9D9;
    width: 250px;
    height: 30px;
    border-radius: 0px 0px 15px 15px;
    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));
}
.lupa{
    width: 30px;
    height: 30px;
    position: relative;
}
#buscador{
    position: relative;
    display: flex;
    border-radius: 20px;
    margin-left: 2%;
    padding-left: 2%;
    padding-right: 2%;
    border: none;

    width: 100%;
    height: 50%;
    background-color: #f5f5f5;
    color: #919191;
    transition: all 200ms linear;
    outline: none;
}
#buscador:focus, #buscador:hover{
    background-color: white;
}
#buscador::placeholder{
    font-weight: 600;
    color: #B9B8B8;
}

</style>