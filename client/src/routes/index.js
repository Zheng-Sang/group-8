import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login'
import Home from '../components/Home'
import Recommendation from '../components/Recommendation'
import SeatSelection from '../components/SeatSelection'
import Summary from '../components/Summary'


Vue.use(Router)

export default new Router({
  routes: [
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
        path: '/recommendation',
        name: 'Recommendation',
        component: Recommendation
    },
    {
        path: '/seatSelection',
        name: 'SeatSelection',
        component: SeatSelection
    },
    {
        path: '/summary',
        name: 'Summary',
        component: Summary
    },
  ]
})