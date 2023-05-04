<script>
export default {

props: ['nombre','rut','area'],
data (){
    return{   
    }
}
}
</script>
<template>
    <li class="ProfesionalLista">
        <div class="ContenedorEtiquetaProfesional">
            <div class="EtiquetaProfesional">{{ area }}</div> 
            </div>
        <div class="ContenedorNombreProfesional">{{ nombre }}</div>
        <div class="ContenedorRutProfesional">Rut: {{ rut }}</div>
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

    font-size: 15px;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 500;
    cursor: pointer;
    transition: all 200ms linear;
}
.ContenedorEtiquetaProfesional{
    position: relative;
    width: 25%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    
}
.ContenedorNombreProfesional{
    position: relative;
    width: 50%;
    height: 100%;
    padding-top: 10px;
    left: 2%;
    justify-content: center;
    text-align: left;

    
}

.ContenedorRutProfesional{
    width: 25%;
    height: 100%;
    padding-top: 10px;
    justify-content: center;
    text-align: left;
}

.EtiquetaProfesional{
    
    text-align: center;
    position: relative;
    width: 80%;
    height: 25px;
    background-color: blueviolet;
    color: white;
    border-radius: 9px;

    font-size: 12px;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 600;
    line-height: 25px;
}
.ProfesionalLista:hover{
    background-color: #969696;
    color: #F3F3F3;
}

</style>