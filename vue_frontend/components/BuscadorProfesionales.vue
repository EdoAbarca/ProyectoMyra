<script>
import DropBox from './DropBox.vue'

export default {
  components: {
    DropBox
    }
  }
</script>

<template>
    <div class="ContenedorBuscador">
        <div class="BarraBusqueda">
            <input type="search" placeholder="Ingresa el nombre" id="buscador" />
            <div class="BotonBusqueda">
                <img class="lupa"  src="../static/iconolupa.svg" alt="">
            </div>
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

    border-radius: 16px 16px 16px 0px;
    position: relative;
    width: 100%;
    height: 60%;
    background-color: #D9D9D9;;
    display: flex;
    flex-direction: row;
    align-items: center;
    filter: drop-shadow(0px 1px 1px rgba(0, 0, 0, 0.1));
}
.BotonBusqueda{
    position: relative;
    width: 10%;
    height: 100%;
    display: flex;
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
    border-radius: 20px;
    margin-left: 2%;
    padding-left: 2%;
    padding-right: 2%;
    border: none;
    position: relative;
    width: 100%;
    height: 50%;
    background-color: #f5f5f5;
    color: #919191;
    outline-color: #919191;
    outline-width: 5px;
    outline-offset: 1px;
    transition: all 200ms linear;
}
#buscador:focus, #buscador:hover{
    background-color: white;
}

</style>