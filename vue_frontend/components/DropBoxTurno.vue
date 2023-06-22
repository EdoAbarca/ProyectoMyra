<script>
import{mapMutations,mapActions} from 'vuex'
export default{
    data() {
    return {
      opcion: 'Turnos',
      idAnterior:"idbase",
    }
  },

  methods:{
    ...mapMutations({
        elegirCategoria: 'paciente/elegirCategoria'
    }),
    ...mapActions('paciente',[
            'fetchPacientes',
            'filtrarTurnos'       
        ]),
    filtro(valor){

      this.opcion = valor;
      if(valor === 0){
        valor = null;
        this.fetchPacientes();
      }
      this.elegirCategoria(valor);
      this.filtrarTurnos();


    }
  }
}

</script>

<template>
     

  	<form class="sec-center2">

            <input class="dropdown2" type="checkbox" id="dropdown2" name="dropdown2"/>
	  	   <label class="for-dropdown2" for="dropdown2">
          <h1 id="textoDropBox2">{{opcion}}</h1>
          <div class="uil2"></div></label>

	  
  		<div class="section-dropdown2"> 
            <div class="columna">
                <div class="contenedorEleccion2" id="item1">
                    <input  class="Radio-eleccion2" id="Todas2" type="radio" value="Turnos" v-model ="opcion" @click="filtro(0)"/>
                    <label  class="elementoSelect" for="Todas2">Todos</label>
                </div>

                <div class="contenedorEleccion2" id="item2">
                    <input  class="Radio-eleccion2" id="2" type="radio" value="2 Hrs" v-model ="opcion" @click="filtro(1)"/>
                    <label  class="elementoSelect" for="2">2 Hrs</label>
                </div>

                <div class="contenedorEleccion2" id="item3">
                    <input  class="Radio-eleccion2" id="4" type="radio" value="4 Hrs" v-model ="opcion" @click="filtro(2)"/>
                    <label  class="elementoSelect" for="4">4 Hrs</label>
                </div>

                <div class="contenedorEleccion2" id="item3">
                    <input  class="Radio-eleccion2" id="6" type="radio" value="6 Hrs" v-model ="opcion" @click="filtro(3)"/>
                    <label  class="elementoSelect" for="6">6 Hrs</label>
                </div>

                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="8" type="radio" value="8 Hrs" v-model ="opcion" @click="filtro(4)" />
                    <label  class="elementoSelect" for="8">8 Hrs</label>
                </div>
              
    
            </div>
            <div class="columna">
              
              
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="10" type="radio" value="10 Hrs" v-model ="opcion" @click="filtro(5)" />
                    <label  class="elementoSelect" for="10">10 Hrs</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="12" type="radio" value="12 Hrs" v-model ="opcion" @click="filtro(6)" />
                    <label  class="elementoSelect" for="12">12 Hrs</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="24" type="radio" value="24 Hrs" v-model ="opcion" @click="filtro(7)" />
                    <label  class="elementoSelect" for="24">24 Hrs</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="otro4" type="radio" value="otro4" v-model ="opcion" @click="filtro(8)" />
                    <label  class="elementoSelect" for="otro4">Otro</label>
                </div>
            </div>
          
  			
        </div>
  	</form>

</template>
<style>
.sec-center2 {
  position: relative;
  width: 35%;
  min-width: 200px;
  max-height: 30px;
  
  z-index: 200;
  box-sizing: border-box;
  border-radius: 0px 0px 8px 0px;
  background-color: #D9D9D9;
  color:#D9D9D9 ;
}

.contenedorEleccion2{
    color: #48ABBF;
    position: relative; 
    box-sizing: border-box;
    
    width: 99%;
    height: 30px;
    
    display: flex;

    transition: all 200ms linear;
    font-family: 'Roboto', sans-serif;
    font-weight: 600;
    font-size: 12px;
    vertical-align: middle;
    
    padding-left: 10px;
    margin: 2px 0;

    border-radius: 3px;

    
}
.contenedorEleccion2:hover {
  color: white;
  background-color: #48ABBF;
}

.columna{
    position: relative;
    display: flex;
    width: 100%;
    flex-direction: column;
    overflow: hidden;
    box-sizing: border-box;
}
.elementoSelect{
  display: flex;
    width: 100%;
    height: 100%;
    cursor: pointer;
    font-display: flex;
    align-items: center;
    vertical-align: middle;
}

.section-dropdown2{
  position: relative;
  width: 400px;
  height: 150px;
  top: 20px;
  box-sizing: border-box;

  background-color: white;
  border-radius: 4px;
  padding: 5px;
  box-shadow: 0 14px 35px 0 rgba(9,9,12,0.4);
  
  display: flex;
  flex-direction: row;
  z-index: 300;

  opacity: 0;
  pointer-events: none;
  transform: translateY(20px);
  transition: all 200ms linear;
  
}
[type="checkbox"]:checked,
[type="checkbox"]:not(:checked){
  position: relative;
  left: 0px;
  opacity: 0;
  pointer-events: none;
}

.dropdown2:checked ~ .section-dropdown2{
  opacity: 1;
  pointer-events: auto;
  transform: translateY(0);
}


.section-dropdown2:before {
  position: absolute;
  top: -20px;
  left: 0;
  width: 100%;
  content: '';
  display: block;
  z-index: 1;
  
}
.section-dropdown2:after {
  position: absolute;
  top: -7px;
  left: 30px;
  width: 0; 
  height: 0; 
  border-left: 8px solid transparent;
  border-right: 8px solid transparent; 
  border-bottom: 8px solid white;
  content: '';
  display: block;
  z-index: 2;
  transition: all 200ms linear;

  
}

.dropdown2:checked + .for-dropdown2,
.dropdown2:not(:checked) + .for-dropdown2{

  position: relative;
  width: 85%;
  border-radius: 4px;
  border: none;
  box-shadow: 0 12px 35px 0 rgba(255,235,167,.15);

  cursor: pointer;
  display: inline-block;


  
}
.dropdown2:checked + .for-dropdown2:before,
.dropdown2:not(:checked) + .for-dropdown2:before{
  position: fixed;
  top: 0;
  left: 0;
  content: '';
  width: 100%;
  height: 100%;
  z-index: -1;
  cursor: auto;
  pointer-events: none;
  
}
.dropdown2:checked + .for-dropdown2:before{
    pointer-events: auto;
}
.dropdown2:not(:checked) + .for-dropdown2 .uil2 {
  font-size: 24px;
  margin-left: 10px;
  transition: transform 200ms linear;
}
.dropdown2:checked + .for-dropdown2 .uil2 {
  transform: rotate(180deg);
  font-size: 24px;
  margin-left: 10px;
  transition: transform 200ms linear;
}

.for-dropdown2{

    position: relative;
    display: flex;
    height: 20px;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    
    background-color: white;

}
#textoDropBox2{
  top: 3px;
  left: 10px;
  position: relative;
  display: flex;
  font-size: 12px;
  align-items: center;  


}

.uil2{
    position: relative;
    left: 80%;
    bottom: 40%;
    z-index: 2001;
    width: 0; 
    height: 0; 
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 10px solid #D9D9D9;
}
.Radio-eleccion2{
    opacity: 0;
}
.dropdown2:hover + .for-dropdown2 .uil2 {
    
    transition: all 200ms linear;
    border-top: 10px solid #B9B8B8;
}

.dropdown2:checked:hover + .for-dropdown2:hover,
.dropdown2:not(:checked):hover + .for-dropdown2:hover{
    color: gray;
    transition: all 200ms linear;
}


</style>