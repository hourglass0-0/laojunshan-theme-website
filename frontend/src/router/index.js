import {
    createRouter,
    createWebHistory
} from 'vue-router'
import InitialPage from '@/components/InitialPage.vue'
import LoginPage from '@/components/LoginPage.vue'
import RegPage from '@/components/RegPage.vue'
import HomePage from '@/components/HomePage.vue'
import ScenicPage from '@/components/ScenicPage.vue'
import GuidePage from '@/components/GuidePage.vue'
import BoardPage from '@/components/BoardPage.vue'
import ContactPage from '@/components/ContactPage.vue'

import ScenicIntroduction from '@/components/ScenicIntroduction.vue'
import ScenicHistory from '@/components/ScenicHistory.vue'
import ScenicEnvironment from '@/components/ScenicEnvironment.vue'
import MainAttraction from '@/components/MainAttraction.vue'
import NaturalResource from '@/components/NaturalResource.vue'
import TouristAttraction from '@/components/TouristAttraction.vue'
import HistoricalCulture from '@/components/HistoricalCulture.vue'



const routes = [{
        path: '/',
        component: InitialPage
    },
    {
        path: '/login',
        component: LoginPage
    },
    {
        path: '/reg',
        component: RegPage
    },
    {
        path: '/home',
        component: HomePage
    },
    {
        path: '/scenic',
        component: ScenicPage,
        children: [{
                path: 'introduction',
                component: ScenicIntroduction
            },
            {
                path: 'history',
                component: ScenicHistory
            },
            {
                path: 'environment',
                component: ScenicEnvironment
            },
            {
                path: 'scenic-spots',
                component: MainAttraction
            },
            {
                path: 'resources',
                component: NaturalResource
            },
            {
                path: 'honors',
                component: TouristAttraction
            },
            {
                path: 'culture',
                component: HistoricalCulture
            },
            {
                path: '',
                redirect: '/scenic/introduction'
            }
        ]
    },
    {
        path: '/guide',
        component: GuidePage
    },
    {
        path: '/board',
        component: BoardPage
    },
    {
        path: '/contact',
        component: ContactPage
    }
]

const router = new createRouter({
    history: createWebHistory(),
    routes
})

export default router