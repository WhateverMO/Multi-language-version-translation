"use strict";(self["webpackChunkrtbooks"]=self["webpackChunkrtbooks"]||[]).push([[870],{2749:function(t,e,s){s.d(e,{Z:function(){return u}});var i=function(){var t=this,e=t._self._c;return e("div",[e("el-menu",{staticClass:"el-menu",attrs:{mode:"horizontal"}},[e("el-submenu",{attrs:{index:"1"}},[e("template",{slot:"title"},[t._v("切换语言")]),e("el-menu-item",{attrs:{index:"2-1"}},[t._v("英语")]),e("el-menu-item",{attrs:{index:"2-2"}},[t._v("法语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("德语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("日语")])],2),e("el-menu-item",{attrs:{index:"0"},on:{click:t.re}},[t._v("rt-books")]),e("el-menu-item",{attrs:{index:"2"}},[t._v("玄幻")]),e("el-menu-item",{attrs:{index:"3"}},[t._v("都市")]),e("el-menu-item",{attrs:{index:"4"}},[t._v("仙侠")]),e("el-menu-item",{attrs:{index:"5"}},[t._v("历史")]),e("el-menu-item",{attrs:{index:"6"}},[t._v("悬疑")]),e("el-menu-item",{attrs:{index:"7"}},[t._v("推理")]),e("el-menu-item",{attrs:{index:"8"}},[t._v("言情")]),e("el-menu-item",{attrs:{index:"9"}},[t._v("更多")]),e("div",{staticClass:"search"},[e("el-input",{attrs:{placeholder:"请输入内容"},model:{value:t.input,callback:function(e){t.input=e},expression:"input"}}),e("el-button",{attrs:{type:"primary",plain:""}},[t._v("搜索")])],1)],1)],1)},r=[],a={name:"top",data(){return{input:""}},methods:{re(){this.$router.push("/")}}},n=a,o=s(1001),l=(0,o.Z)(n,i,r,!1,null,null,null),u=l.exports},2212:function(t,e,s){s.r(e),s.d(e,{default:function(){return b}});var i=function(){var t=this,e=t._self._c;return e("div",[e("top"),e("logincenter"),e("foot")],1)},r=[],a=function(){var t=this,e=t._self._c;return e("div",[e("div",{staticClass:"center"},[t._m(0),e("div",{staticClass:"center2"},[e("h2",[t._v("作者登录")]),e("div",{staticClass:"el-icon-user"},[t._v(" 用户id:"),e("el-input",{attrs:{placeholder:"请输入你的用户名"},model:{value:t.user_id,callback:function(e){t.user_id=e},expression:"user_id"}})],1),e("div",{staticClass:"el-icon-key"},[t._v(" 密码 :"),e("el-input",{attrs:{placeholder:"请输入密码","show-password":""},model:{value:t.password,callback:function(e){t.password=e},expression:"password"}})],1),e("el-button",{attrs:{type:"primary",plain:""},on:{click:t.login}},[t._v("立即登录")]),e("div",{staticClass:"register"},[t._v(" 没有账号，"),e("span",{staticClass:"enroll",on:{click:t.enroll}},[t._v("点击注册")])])],1)])])},n=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"center1"},[e("img",{attrs:{src:s(3205)}})])}],o=s(5410),l=s.n(o),u=s(8291),d={name:"logincenter",data(){return{password:"",user_id:""}},methods:{enroll(){this.$router.push("/regestertranslate")},async login(){var t={author_id:this.user_id,password:this.password};const e="/api/author/login";await u.Z.post(e,l().stringify(t)).then((t=>{alert(t.data.msg),200==t.data.code&&(this.$router.push("/author"),sessionStorage.setItem("id",this.user_id),this.$store.commit("id",this.user_id))})),await u.Z.get("/api/author/information").then((t=>{this.$store.commit("name",t.data.author_name),this.$store.commit("age",t.data.author_age),this.$store.commit("sex",t.data.author_gender),this.$store.commit("place",t.data.author_area),this.$store.commit("intro",t.data.author_describe)}))}}},c=d,m=s(1001),p=(0,m.Z)(c,a,n,!1,null,"0066091e",null),h=p.exports,_=s(7378),v=s(2749),f={components:{top:v.Z,foot:_.Z,logincenter:h},data(){return{}},methods:{}},x=f,g=(0,m.Z)(x,i,r,!1,null,"bea7081c",null),b=g.exports},3205:function(t,e,s){t.exports=s.p+"img/welcom.d466cbee.jpeg"}}]);
//# sourceMappingURL=870.ce518be1.js.map