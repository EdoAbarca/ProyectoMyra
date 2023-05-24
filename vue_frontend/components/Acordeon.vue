<script>

import {mapGetters} from 'vuex'
export default{
    data() {
        return {
        opcion: 'CATEGORIAS',
        idAnterior:"idbase"
    }},
	computed:{
		...mapGetters('profesional',[
            'getPagos',
        ])
	},
    methods:{
        acordeon(id){
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
    <div class="container">
        <div class="accordion">

			<div class="accordion-item">
                <button id="accordion-button-1" aria-expanded="false"  >
                    <span class="accordion-title">Sueldo Base </span>
					<span class="valorPago"> ${{getPagos.sueldoBase}}</span>  
                </button>
            </div>

			<div class="accordion-item">
                <button id="accordion-button-1" aria-expanded="false"  >
                    <span class="accordion-title">Gratificaciones </span>
					<span class="valorPago"> ${{getPagos.gratificaciones}}</span>  
                </button>
            </div>

			<div class="accordion-item">
                <button id="accordion-button-1" aria-expanded="false"  >
                    <span class="accordion-title">Horas Extras </span>
					<span class="valorPago"> $80000</span>  
                </button>
            </div>

			<div class="accordion-item">
                <button id="accordion-button-2" aria-expanded="false" @click="acordeon('accordion-button-2')" >
                    <span class="accordion-title">Extras Movilización </span>
					<span class="valorPago"> $80000</span>
                    <span class="icon" aria-hidden="true"></span>
                </button>
                <div class="accordion-content">
                    <p>Movilización <span class="valorPago"> $80000</span></p>
					<p>Colación <span class="valorPago"> $80000</span></p>
					<p>Viatico <span class="valorPago"> $80000</span></p>
                </div>
            </div>

			<div class="accordion-item">
                <button id="accordion-button-3" aria-expanded="false" @click="acordeon('accordion-button-3')" >
                    <span class="accordion-title">Bonos </span>
					<span class="valorPago"> $80000</span>
                    <span class="icon" aria-hidden="true"></span>
                </button>
                <div class="accordion-content">
                    <p>Bonos <span class="valorPago"> $80000</span></p>
					<p>Asignación Familiar <span class="valorPago"> $80000</span></p>
					<p>Aguinaldo <span class="valorPago"> $80000</span></p>
					<p>Vacaciones <span class="valorPago"> $80000</span></p>
					<p>B. Sala Cuna <span class="valorPago"> $80000</span></p>
                </div>
            </div>

			<div class="accordion-item">
                <button id="totalHaberes" aria-expanded="false"  >
                    <span class="accordion-title">Total Haberes </span>
					<span class="valorPago"> $80000</span>  
                </button>
            </div>

			<div class="accordion-item">
                <button id="totalImponible" aria-expanded="false"  >
                    <span class="accordion-title">Total Imponible </span>
					<span class="valorPago"> $80000</span>  
                </button>
            </div>

            <div class="accordion-item">
                <button id="accordion-button-4" aria-expanded="false" @click="acordeon('accordion-button-4')" >
                    <span class="accordion-title">Descuentos </span>
					<span class="valorPago"> ${{getPagos.descuentos}}</span>
                    <span class="icon" aria-hidden="true"></span>
                </button>
                <div class="accordion-content">
                    <p>AFP <span class="valorPago"> $80000</span></p>
					<p>ISAPRE <span class="valorPago"> $80000</span></p>
					<p>FONASA <span class="valorPago"> $80000</span></p>
					<p>Seguro de cesantia <span class="valorPago"> $80000</span></p>
					<p>Impuesto único <span class="valorPago"> $80000</span></p>
					<p>Cuenta Ahorro AFP <span class="valorPago"> $80000</span></p>
					<p>Descuentos CCAF <span class="valorPago"> $80000</span></p>
					<p>Anticipos <span class="valorPago"> $80000</span></p>
					<p>Descuentos <span class="valorPago"> $80000</span></p>
					<p>Ley 3% <span class="valorPago"> $80000</span></p>
                </div>
            </div>
        </div>
		<div id="totalLiquido"><p>Total Liquido <span class="valorPago"> $80000</span></p></div>

    </div>

</template>
<style>
@import url('https://fonts.googleapis.com/css?family=Hind:300,400&display=swap');
 * {
	 box-sizing: border-box;
}
 *::before, *::after {
	 box-sizing: border-box;
}

 .container {
    position: absolute;
    display: flex;
	width: 100%;
    height: 100%;
	font-family: Arial, Helvetica, sans-serif;
	flex-direction: column;

}
 .accordion .accordion-item {
	 border-bottom: 1px solid #e5e5e5;
}
 .accordion .accordion-item button[aria-expanded='true'] {
	 border-bottom: 1px solid #03b5d2;
}
 .accordion button {
	 display: flex;
	 position: relative;
     align-items: center;
	 
	 text-align: left;
	 width: 100%;
     height: 30px;
	
	 color: #7288a2;
	 font-size: 15px;
	 font-weight: 400;
	 border: none;
	 background: none; 
	 outline: none;
}
 .accordion button:hover, .accordion button:focus {
	 cursor: pointer;
	 color: #03b5d2;
}
 .accordion button:hover::after, .accordion button:focus::after {
	 cursor: pointer;
	 color: #03b5d2;
	 border: 1px solid #03b5d2;
}
 .accordion button .accordion-title {
	 padding: 1em 1.5em 1em 0;
	 padding-left: 3%;
}
 .accordion button .icon {
	 display: flex;
	 position: absolute;
	 right: 0;
	 width: 22px;
	 height: 22px;
	 border: 2px solid;
	 border: none;

}
 .accordion button .icon::before {
	 display: flex;
	 position: absolute;
	 content: '';
	 top: 9px;
	 left: 5px;
	 width: 10px;
	 height: 2px;
	 background: currentColor;
}
 .accordion button .icon::after {
	 display: flex;
	 position: absolute;
	 content: '';
	 top: 5px;
	 left: 9px;
	 width: 2px;
	 height: 10px;
	 background: currentColor;
}
 .accordion button[aria-expanded='true'] {
	 color: #03b5d2;
}
 .accordion button[aria-expanded='true'] .icon::after {
	 width: 0;
}
 .accordion button[aria-expanded='true'] + .accordion-content {
	 opacity: 1;
	 max-height: 100%;
	 transition: all 200ms linear;
	 will-change: opacity, max-height;
}
.accordion button[aria-expanded='true']+ .accordion-item{
	height: 100%;
}
 .accordion .accordion-content {
	 opacity: 0;
	 max-height: 0;
	 overflow: hidden;
	 transition: opacity 200ms linear, max-height 200ms linear;
	 will-change: opacity, max-height;
	 
}
 .accordion .accordion-content p {
	 font-size: 12px;
	 font-weight: 300;
	 margin-top: 2%;
	 margin-bottom: 2%;
	 padding-left: 3%;


}
 
.accordion{
    display: flex;
	position: relative;
    width: 100%;
	height: 90%;
    flex-direction: column;
	overflow-y: scroll;
}
.accordion-item{
	display: flex;
	position: relative;
    flex-direction: column;


}
.valorPago{
	position: absolute;
	right: 0%;
	width: 50%;

}
#totalLiquido{
	display: flex;
	background-color: #DEEFF2;
	position: absolute;
	width: 100%;
	height: 10%;
	bottom: 0%;
	align-items: center;
	font-weight: 600;
	color: #005D71;
	border-radius: 0px 0px 12.5px 12.5px;
}
#totalLiquido p{
	padding-left: 3%;
}
#totalLiquido .valorPago{
	padding-right: 2%;
}
</style>