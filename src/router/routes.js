
export default [
    {
        path: '/',
        component: () => import('@/pages/index/unsucess'),
    },
    {
        path: '/regester',
        component: () => import('@/pages/start/regester'),
    },
    {
        path: '/regestertranslate',
        component: () => import('@/pages/start/regestertranslate'),
    },
    {
        path: '/loginreader',
        component: () => import('@/pages/start/login'),
    },
    {
        path: '/loginauthor',
        component: () => import('@/pages/start/loginauthor'),
    },
    {
        path: '/checkpassword',
        component: () => import('@/pages/start/checkpassword'),
    },
    {
        path: '/checkpasswordauthor',
        component: () => import('@/pages/start/checkpasswordauthor'),
    },
    {
        path: '/reader',
        component: () => import('@/pages/index/reader'),
    },
    {
        path: '/author',
        component: () => import('@/pages/index/author'),
    },
    {
        path: '/authorinformation',
        component: () => import('@/pages/information/author'),
    },
    {
        path: '/checkinformationauthor',
        component: () => import('@/pages/information/checkinformationauthor'),
    },
    {
        path: '/readerinformation',
        component: () => import('@/pages/information/reader'),
    },
    {
        path: '/collect',
        component: () => import('@/pages/information/collect'),
    },
    {
        path: '/attention',
        component: () => import('@/pages/information/attention'),
    },
    {
        path: '/checkinformation',
        component: () => import('@/pages/information/checkinformation'),
    },
    {
        path: '/searchbook',
        component: () => import('@/pages/readbook/searchbook'),
    },
    {
        path: '/introbook',
        component: () => import('@/pages/readbook/introbook'),
    },
    {
        path: '/readbook',
        component: () => import('@/pages/readbook/readbook'),
    },

    {
        path: '/kind',
        component: () => import('@/pages/addbook/kind'),
    },
    {
        path: '/write',
        component: () => import('@/pages/addbook/write'),
    },
    {
        path: '/authorbook',
        component: () => import('@/pages/addbook/authorbook'),
    },
    {
        path: '/choose',
        component: () => import('@/pages/translate/choose'),
    },
    {
        path: '/compare',
        component: () => import('@/pages/translate/compare'),
    },
    {
        path: '/translation',
        component: () => import('@/pages/translate/translation'),
    },

]