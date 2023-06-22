<script>
import{mapMutations,mapActions} from 'vuex'
export default{
    data() {
    return {
      opcion: 'Áreas',
      idAnterior:"idbase",
    }
  },

  methods:{
    ...mapMutations({
        elegirCategoria: 'profesional/elegirCategoria'
    }),
    ...mapActions('profesional',[
            'fetchProfesionales',
            'filtrarArea'       
        ]),
    filtro(valor){

      this.opcion = valor;
      if(valor === 0){
        valor = null;
        this.fetchProfesionales();
      }
      this.elegirCategoria(valor);
      this.filtrarArea();


    }
  }
}

</script>

<template>
     

  	<form class="sec-center2">

            <input class="dropdown2" type="checkbox" id="dropdown2" name="dropdown2"/>
	  	   <label class="for-dropdown2" for="dropdown2">
          <h1 id="textoDropBox">{{opcion}}</h1>
          <div class="uil2"></div></label>

	  
  		<div class="section-dropdown2"> 
            <div class="columna">
                <div class="contenedorEleccion2" id="item1">
                    <input  class="Radio-eleccion2" id="Todas" type="radio" value="Áreas" v-model ="opcion" @click="filtro(0)"/>
                    <label  class="elementoSelect" for="Todas">Todos</label>
                </div>

                <div class="contenedorEleccion2" id="item2">
                    <input  class="Radio-eleccion2" id="Admins" type="radio" value="Administradores" v-model ="opcion" @click="filtro(1)"/>
                    <label  class="elementoSelect" for="Admins">Administradores</label>
                </div>

                <div class="contenedorEleccion2" id="item3">
                    <input  class="Radio-eleccion2" id="auxs" type="radio" value="Auxiliares" v-model ="opcion" @click="filtro(2)"/>
                    <label  class="elementoSelect" for="auxs">Auxiliares</label>
                </div>

                <div class="contenedorEleccion2" id="item3">
                    <input  class="Radio-eleccion2" id="coords" type="radio" value="Coordinadores" v-model ="opcion" @click="filtro(3)"/>
                    <label  class="elementoSelect" for="coords">Coordinadores</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="cuids" type="radio" value="Cuidadores" v-model ="opcion" @click="filtro(4)" />
                    <label  class="elementoSelect" for="cuids">Cuidadores</label>
                </div>
    
            </div>
            <div class="columna">
              
              <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="enfs" type="radio" value="Enfermeros" v-model ="opcion" @click="filtro(5)" />
                    <label  class="elementoSelect" for="enfs">Enfermeros</label>
                </div>
              <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="fonos" type="radio" value="Fonoadiólogos" v-model ="opcion" @click="filtro(6)" />
                    <label  class="elementoSelect" for="fonos">Fonoaudiólogos</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="kines" type="radio" value="Kinesiólogos" v-model ="opcion" @click="filtro(7)" />
                    <label  class="elementoSelect" for="kines">Kinesiólogos</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="meds" type="radio" value="Médicos" v-model ="opcion" @click="filtro(8)" />
                    <label  class="elementoSelect" for="meds">Médicos</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="nutris" type="radio" value="Nutricionistas" v-model ="opcion" @click="filtro(9)" />
                    <label  class="elementoSelect" for="nutris">Nutricionistas</label>
                </div>
                </div>
                <div class="columna">


                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="pods" type="radio" value="Podólogos" v-model ="opcion" @click="filtro(10)" />
                    <label  class="elementoSelect" for="pods">Podólogos</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="practs" type="radio" value="Practicantes" v-model ="opcion" @click="filtro(11)" />
                    <label  class="elementoSelect" for="practs">Practicantes</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="tenss" type="radio" value="TENS" v-model ="opcion" @click="filtro(12)" />
                    <label  class="elementoSelect" for="tenss">TENS</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="ters" type="radio" value="Terapeutas" v-model ="opcion" @click="filtro(13)" />
                    <label  class="elementoSelect" for="ters">Terapeutas</label>
                </div>
                <div class="contenedorEleccion2">
                    <input  class="Radio-eleccion2" id="otros" type="radio" value="Otros" v-model ="opcion" @click="filtro(14)" />
                    <label  class="elementoSelect" for="otros">Otros</label>
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
#textoDropBox{
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