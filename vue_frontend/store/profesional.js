export const state = () => ({
    datosProfesional:{
        nombre: "",
        rut: "",
        area:"",
        cargo:'',
        contrato:'',
        coordinador:''
    },
    pagoProfesional:{
        sueldoBase:"",
        gratificaciones: "",
        horasExtra:"",
        extraMovilizacion:"",
        movilizacion:"",
        colacion:"",
        viatico:"",
        bonosTotales:"",
        bonos:"",
        asignacion:"",
        vacaciones:"",
        salaCuna:"",
        totalHaberes:"",
        totalImponible:"",
        descuentosTotales:"",
        afp:"",
        isapre:"",
        fonasa:"",
        
        seguroCesantia:"",
        impuestoUnico:"",
        cuentaAFP:"",
        descuentosCCAF:"",
        anticipos:"",
        descuentos:"",
        ley3:"",
        totalLiquido:""


    },
    estProfesional:{
        inasistencias:"",
        horasTotales:"",
        horasExtra:"",
        diasLicencia:"",
        diasVacaciones:""
    },
    categoriaElegida: null,
    datoBuscadoProfesional: null,
    mostrar:false,
    idAnterior: false,
    profesionales:[
        { nombre: "Natalia Damaris Perello Contreras",
          rut:"19456957-5",
          area:"ADMINISTRACION",
          cargo:'Jefe de Area',
          contrato:'Normal',
          coordinador:'No aplica' //Centro de trabajo
        },
        { nombre: "Mariela Leonardo Tantarico",
          rut:"20345687-7",
          area:"CUIDADOS",
            cargo:'Cuidadora',
            contrato:'V2',
            coordinador:'Gonzalo Esteban Palacios'
        },
        { nombre: "Will Hermes Torrealba Alvarez",
          rut:"9234876-0",
          area:"CUIDADOS",
          cargo:'Cuidador',
            contrato:'V2',
            coordinador:'Gonzalo Esteban Palacios'
        },
        { nombre: "Angelina Elizabeth Cespedes Cortes",
          rut:"14987436-7",
          area:"KINESIOLOGIA",
          cargo:'Kinesiologa',
          contrato:'Normal',
          coordinador:'Jean David  Bustamante'
        }

      ],
    pagos:[
        { rut:'19456957-5',
        sueldoBase:"410.000",
        gratificaciones: "102.500",
        horasExtra:"0",
        extraMovilizacion:"25.000",
        movilizacion:"25.000",
        colacion:"0",
        viatico:"0",
        bonosTotales:"0",
        bonos:"0",
        asignacion:"0",
        salaCuna:"0",
        totalHaberes:"537.500",
        totalImponible:"512.500",
        descuentosTotales:"180.238",
        afp:"57.759",
        isapre:"0",
        fonasa:"35.875",
        seguroCesantia:"3.075",
        impuestoUnico:"0",
        cuentaAFP:"0",
        descuentosCCAF:"48.529",
        anticipos:"35.000",
        descuentos:"180.238",
        ley3:"0",
        totalLiquido:"357.262"
        },
        { rut:'20345687-7',
        sueldoBase:"1.148.958",
        gratificaciones: "162.292",
        horasExtra:"0",
        extraMovilizacion:"50.000",
        movilizacion:"20.000",
        colacion:"30.000",
        viatico:"0",
        bonosTotales:"0",
        bonos:"0",
        asignacion:"0",
        salaCuna:"0",
        totalHaberes:"1.361.250",
        totalImponible:"1.311.250",
        descuentosTotales:"464.241",
        afp:"147.778",
        isapre:"173.287",
        fonasa:"0",
        seguroCesantia:"7.868",
        impuestoUnico:"5.838",
        cuentaAFP:"0",
        descuentosCCAF:"0",
        anticipos:"100.000",
        descuentos:"464.241",
        ley3:"29.470",
        totalLiquido:"897.009"
        },
        { rut:'9234876-0',
        sueldoBase:"863.958",
        gratificaciones: "162.292",
        horasExtra:"0",
        extraMovilizacion:"150.000",
        movilizacion:"30.000",
        colacion:"20.000",
        viatico:"100.000",
        bonosTotales:"6.688",
        bonos:"0",
        asignacion:"6.688",
        salaCuna:"0",
        totalHaberes:"1.182.938",
        totalImponible:"1.026.250",
        descuentosTotales:"616.190",
        afp:"115.658",
        isapre:"269.518",
        fonasa:"0",
        seguroCesantia:"6.158",
        impuestoUnico:"0",
        cuentaAFP:"0",
        descuentosCCAF:"0",
        anticipos:"200.000",
        descuentos:"24.856",
        ley3:"0",
        totalLiquido:"566.748"
        },
        { rut:'14987436-7',
        sueldoBase:"440.000",
        gratificaciones: "121.000",
        horasExtra:"0",
        extraMovilizacion:"22.000",
        movilizacion:"11.000",
        colacion:"11.000",
        viatico:"0",
        bonosTotales:"44.000",
        bonos:"44.000",
        asignacion:"0",
        salaCuna:"0",
        totalHaberes:"627.000",
        totalImponible:"60.5000",
        descuentosTotales:"249.573",
        afp:"69.212",
        isapre:"0",
        fonasa:"42.350",
        seguroCesantia:"3.630",
        impuestoUnico:"0",
        cuentaAFP:"0",
        descuentosCCAF:"39.687",
        anticipos:"80.000",
        descuentos:"0",
        ley3:"14.694",
        totalLiquido:"377.427"
        }
    ],
    estadisticas:[
        { rut:'19456957-5',
            inasistencias:"0",
            horasTotales:"400",
            horasExtra:"35",
            diasLicencia:"7",
            diasVacaciones:"45"
        },
        { rut:'20345687-7',
            inasistencias:"3",
            horasTotales:"90",
            horasExtra:"56",
            diasLicencia:"7",
            diasVacaciones:"3"
        },
        { rut:'9234876-0',
            inasistencias:"0",
            horasTotales:"350",
            horasExtra:"78",
            diasLicencia:"0",
            diasVacaciones:"0"
        },
        { rut:'14987436-7',
            inasistencias:"1",
            horasTotales:"290",
            horasExtra:"35",
            diasLicencia:"15",
            diasVacaciones:"0"
        }
    ]


    
  })
export const getters = {

    getCategoria(state){
        return state.categoriaElegida
    },
    getDatoBuscado(state){
        return state.datoBuscadoProfesional
    },
    getMostrar(state){
        return state.mostrar
    },
    getPagos(state){
        console.log(state.pagoProfesional);
        return state.pagoProfesional
    },
    getEstadisticas(state){
        return state.estProfesional
    },
    getDatosBasicos(state){
        return state.datosProfesional
    },
    getProfesionales(state){
        return state.profesionales
    },
    getDatosProfesionales(state){
        
    
        if(state.categoriaElegida === null && state.datoBuscadoProfesional===null){
            return state.profesionales
        }

        if(state.categoriaElegida != null){
            return state.profesionales.filter(profesionales => profesionales.area === state.categoriaElegida);
        }
        if(state.datoBuscadoProfesional!=null){
            const nombres = state.profesionales.filter(profesionales => profesionales.nombre.toLowerCase().search(state.datoBuscadoProfesional.toLowerCase())!=-1);
            const ruts = state.profesionales.filter(profesionales => profesionales.rut.toLowerCase().search(state.datoBuscadoProfesional.toLowerCase())!=-1);
          
            const resultado = nombres.concat(ruts);
            
            return resultado
        }
        return null;
        
    }
}
export const mutations = {
    mostrar(state,id){
        const idAnterior = state.idAnterior
        

        if(idAnterior != id){
            state.mostrar = true
        }
        else{
            state.mostrar = true;
            state.idAnterior = id;
        }
 
    },
    elegirCategoria(state,categoriaSeleccionada){
        state.categoriaElegida = categoriaSeleccionada;
    },
    datoPorBuscar(state,dato){
        state.datoBuscadoProfesional = dato;
    },
    recuperarDatos(state,rut){
        const datosBasicos = state.profesionales.find(profesionales => profesionales.rut === rut);
        const datosEstadisitcos = state.estadisticas.find(estadisticas => estadisticas.rut === rut);
        const datosPagos = state.pagos.find(pagos => pagos.rut === rut);
        console.log(datosBasicos)

        //console.log(datosBasicos);
        state.datosProfesional.nombre = datosBasicos.nombre;
        state.datosProfesional.rut = datosBasicos.rut;
        state.datosProfesional.area = datosBasicos.area;
        state.datosProfesional.cargo = datosBasicos.cargo;
        state.datosProfesional.contrato = datosBasicos.contrato;
        state.datosProfesional.coordinador = datosBasicos.coordinador;

        console.log(state.datosProfesional);


        state.estProfesional.inasistencias = datosEstadisitcos.inasistencias;
        state.estProfesional.horasExtra = datosEstadisitcos.horasExtra;
        state.estProfesional.horasTotales = datosEstadisitcos.horasTotales;
        state.estProfesional.diasLicencia = datosEstadisitcos.diasLicencia;
        state.estProfesional.diasVacaciones = datosEstadisitcos.diasVacaciones;

        state.pagoProfesional.sueldoBase = datosPagos.sueldoBase;
        state.pagoProfesional.horasExtra= datosPagos.horasExtra;
        state.pagoProfesional.extraMovilizacion=datosPagos.extraMovilizacion;
        state.pagoProfesional.movilizacion= datosPagos.movilizacion;
        state.pagoProfesional.colacion=datosPagos.colacion;
        state.pagoProfesional.viatico= datosPagos.viatico;
        state.pagoProfesional.bonosTotales = datosPagos.bonosTotales;
        state.pagoProfesional.bonos=datosPagos.bonos;
        state.pagoProfesional.asignacion=datosPagos.asignacion;
        state.pagoProfesional.vacaciones=datosPagos.vacaciones;
        state.pagoProfesional.salaCuna=datosPagos.salaCuna;
        state.pagoProfesional.totalHaberes=datosPagos.totalHaberes;
        state.pagoProfesional.totalImponible=datosPagos.totalImponible;
        state.pagoProfesional.descuentosTotales=datosPagos.descuentosTotales;
        state.pagoProfesional.afp=datosPagos.afp;
        state.pagoProfesional.isapre=datosPagos.isapre;
        state.pagoProfesional.fonasa=datosPagos.fonasa;
        
        state.pagoProfesional.seguroCesantia=datosPagos.seguroCesantia;
        state.pagoProfesional.impuestoUnico=datosPagos.impuestoUnico;
        state.pagoProfesional.cuentaAFP=datosPagos.cuentaAFP;
        state.pagoProfesional.descuentosCCAF=datosPagos.descuentosCCAF;
        state.pagoProfesional.anticipos=datosPagos.anticipos;
        state.pagoProfesional.descuentos=datosPagos.descuentos;
        state.pagoProfesional.ley3=datosPagos.ley3;
        state.pagoProfesional.totalLiquido=datosPagos.totalLiquido;

    }
      
  }
