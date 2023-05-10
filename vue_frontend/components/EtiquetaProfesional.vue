<script>
export default {
    props: ['area'],

    methods:{

        elegirColor(){
            console.log(this.area)
            let colorArea='#D9D9D9';
            switch(this.area){
                case 'ADMINISTRACION':
                    colorArea = "#FF8E85";
                    break
                case 'CUIDADOS':
                    colorArea = "#45CBDC";
                    break
                case 'FONOAUDIOLOGIA':
                    colorArea = "#FFA7B5";
                    break
                case 'KINESIOLOGIA':
                    colorArea = "#A994C0";
                    break
                case 'AUXILIARES':
                    colorArea = "#BEB5A6";
                    break
                default:
                    colorArea = "green"
            }
            return 'background-color: '+ colorArea+';'

            }

        }

    }
</script>
<template>
    <div class="EtiquetaProfesional" :style="elegirColor()">{{ area }}</div> 
</template>
<style>
.EtiquetaProfesional{
    
    text-align: center;
    position: relative;
    width: 80%;
    height: 25px;
    background-color: aquamarine;
    color: white;
    border-radius: 9px;
    font-size: 12px;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 600;
    line-height: 25px;
}
</style>