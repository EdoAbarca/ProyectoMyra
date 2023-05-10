<script>
import EtiquetaProfesional from './EtiquetaProfesional.vue';
import { mapState, mapMutations } from 'vuex'
import ProfesionalLista from './ProfesionalLista.vue';
export default {

props: ['nombre','rut','area'],
computed:{
    ...mapState(['profesional'])
},
methods:{
    ...mapMutations({
      elegir: 'profesional/elegir',
    }),

}
    
,
}
</script>
<template>
    <div class="ContenedorBaseDatos"  >
        <div id="tituloDatosP">Datos Profesional</div>
        <div class="Cont-Info-Basica">
            <div id="datosIzquierdaBasico">
                <h1 class="TextoContenido">Nombre: {{ nombre }}</h1>
                <h1 class="TextoContenido">Rut: {{ rut }}</h1>
                <h1 class="TextoContenido">Cargo: Cuidadora-40</h1>
            </div>
            <div id="datosDerechaBasico">
                <EtiquetaProfesional id="etiquetaEnDatos" :area="area"/>
            </div>
        </div>
        <div class="Cont-Coord">
            <div id="datosIzquierdaCoord">
                <h1 class="TextoContenido">Coordinador: Adriana Del Carmen  Hernandez</h1>
                
            </div>
            <div id="datosDerechaCoord">
                <h1 class="TextoContenido">Contrato: Tipo</h1>
            </div>
        </div>

    </div>
</template>
<style>
.ContenedorBaseDatos{
    position: relative;
    width: 100%;
    height: 100%;
    background-color: violet;
    display: flex;
    flex-direction: column;
    font-family: Arial, Helvetica, sans-serif;

    transition: all 200ms linear;

}
.TextoContenido{
    margin-top: 1%;
    margin-left: 20px;
    position: relative;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 13px;
    font-weight: 600;
    width: 100%;
}
#tituloDatosP{
    position: relative;
    text-align: center;
    width: 100%;
    height: 25px;
    border-radius: 12.5px 12.5px 0px 0px;

    background-color: #669098;
    color: white;
    padding-top: 5px;

    overflow: hidden;
    
}
.Cont-Info-Basica{
    position: relative;
    display: flex;
    width: 100%;
    height: 55%;
    flex-direction: row;
    background-color: #F4F4F4;
    
}
.Cont-Coord{
    color: #005D71;
    position: relative;
    display: flex;
    width: 100%;
    height: 20%;
    flex-direction: row;
    background-color: #DEEFF2;
    
}
#datosIzquierdaBasico{
    position: relative;
    display: flex;
    flex-direction: column;
    width: 70%;
    height: 100%;

    
}
#datosDerechaBasico{
    position: relative;
    display: flex;
    width: 30%;
    height: 100%;
}
#etiquetaEnDatos{
    top: 15px;
    right: -5px;
}

#datosIzquierdaCoord{
    position: relative;
    display: flex;
    flex-direction: column;
    width: 70%;
    height: auto;

    
}
#datosDerechaCoord{
    
    position: relative;
    display: flex;
    flex-direction: column;
    width: 30%;
    height: auto;
    align-items: center;
    justify-content: center;

    
}




</style>