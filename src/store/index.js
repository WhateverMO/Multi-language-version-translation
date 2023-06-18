import Vue from 'vue'
import Vuex from "vuex";
//只有操作没有数据 数据通过服务器获得
const actions = {}
//修改操作state
const mutations = {
    //用户信息
    id(state, value) {
        state.id = value
    },
    name(state, value) {
        state.name = value
    },
    place(state, value) {
        state.place = value
    },
    age(state, value) {
        state.age = value
    },
    intro(state, value) {
        state.intro = value
    },
    sex(state, value) {
        state.sex = value
    },
    image(state, value) {
        state.image = value
    },
    //图书阅读的id
    bookid(state, value) {
        state.bookid = value
    },
    //创建图书
    createid(state, value) {
        state.createid = value
    },//建立新书
    firstbookid(state, value) {
        state.firstbookid = value
    },
    translatebookid(state, value) {
        state.translatebookid = value
    },

}
//数据信息
const state = {
    //用户信息
    id: '',
    age: '',
    name: '',
    place: '',
    intro: '',
    sex: '',
    image: '',
    //创建图书
    bookid: '',
    createid: "",
    //翻译
    firstbookid: '',
    translatebookid: '',


}
Vue.use(Vuex);
export default new Vuex.Store({
    actions,
    mutations,
    state
})
