export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Puerto para nuxt app
  /* 
  server: {
    port:8080,
  },*/

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'vue_frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/vuetify'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    '@nuxtjs/auth'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: "http://localhost:8000",
    browserBaseURL: "http://localhost:8000",
    proxy: false,
  },
  
    proxy: {
      '/signup/': 'http://localhost:8000/api',
      '/signin/': 'http://localhost:8000/api',
      '/signout': 'http://localhost:8000/api',
      '/cargar_excel': 'http://localhost:8000/api',
      '/profesional/': 'http://localhost:8000/api'
    },
  
  auth: {
    strategies: {
      local: {
        token: {
          property: 'access_token',
          required: false,
          type: 'Bearer'
        },
        user: {
          property: false, // <--- Default "user"
          autoFetch: true
        },
        endpoints: {
          login: { url: '/api/signin/', method: 'post', propertyName:'data.user'},
          user: { url: '/user', method: 'get' },
          logout: { url: '/signout', method: 'post' }
        },
      }
    }
  },
  /* 
  redirect:{
    login:'/login',
  },*/

/* 
  router: {
    middleware: ['auth']
  },*/

// Build Configuration: https://go.nuxtjs.dev/config-build
build: {
}
}
