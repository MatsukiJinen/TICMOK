
require('./bootstrap');

window.Vue = require('vue');


import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import locale from 'element-ui/lib/locale/lang/ja'
import Storage from 'vue-web-storage';  
import VueCarousel from 'vue-carousel';

Vue.use(VueCarousel);
Vue.use(ElementUI, { locale })
Vue.use(Storage)

Vue.component('main-component', require('./components/MainComponent.vue'));
Vue.component('random-component', require('./components/RandomComponent.vue'));
Vue.component('selectable-component', require('./components/SelectableComponent.vue'));

const app = new Vue({
    el: '#app'
});