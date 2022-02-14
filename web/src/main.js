import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// globally import element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.use(router)

// using element-plus
app.use(ElementPlus)
app.mount('#app')
