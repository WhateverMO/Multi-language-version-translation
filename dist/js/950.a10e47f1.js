"use strict";(self["webpackChunkrtbooks"]=self["webpackChunkrtbooks"]||[]).push([[950],{1380:function(t,e,s){s.d(e,{Z:function(){return m}});var i=function(){var t=this,e=t._self._c;return e("div",[e("div",{staticClass:"center"},[t._m(0),e("div",{staticClass:"center2"},[e("h2",[t._v("读者登录")]),e("div",{staticClass:"el-icon-user"},[t._v(" 用户id:"),e("el-input",{attrs:{placeholder:"请输入你的用户名"},model:{value:t.user_id,callback:function(e){t.user_id=e},expression:"user_id"}})],1),e("div",{staticClass:"el-icon-key"},[t._v(" 密码 :"),e("el-input",{attrs:{placeholder:"请输入密码","show-password":""},model:{value:t.password,callback:function(e){t.password=e},expression:"password"}})],1),e("el-button",{attrs:{type:"primary",plain:""},on:{click:t.login}},[t._v("立即登录")]),e("div",{staticClass:"register"},[t._v(" 没有账号，"),e("span",{staticClass:"enroll",on:{click:t.enroll}},[t._v("点击注册")])])],1)])])},r=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"center1"},[e("img",{attrs:{src:s(3205)}})])}],n=s(5410),a=s.n(n),o=(s(6265),s(8291)),l={name:"logincenter",data(){return{password:"",user_id:""}},methods:{enroll(){this.$router.push("/regester")},async login(){var t={user_id:this.user_id,password:this.password};const e="/api/user/login";await o.Z.post(e,a().stringify(t)).then((t=>{console.log(t),alert(t.data.msg),200==t.data.code&&this.$router.push("/reader")})),await o.Z.get("/api/user/information").then((t=>{sessionStorage.setItem("id",t.data.user_id),this.$store.commit("name",t.data.username),this.$store.commit("sex",t.data.user_gender),this.$store.commit("place",t.data.user_area),this.$store.commit("intro",t.data.user_describe),this.$store.commit("age",t.data.user_age),this.$store.commit("id",t.data.user_id),this.$store.commit("image",t.data.user_avatar),console.log(t.data)}))}}},u=l,d=s(1001),c=(0,d.Z)(u,i,r,!1,null,"85081eb8",null),m=c.exports},2749:function(t,e,s){s.d(e,{Z:function(){return u}});var i=function(){var t=this,e=t._self._c;return e("div",[e("el-menu",{staticClass:"el-menu",attrs:{mode:"horizontal"}},[e("el-submenu",{attrs:{index:"1"}},[e("template",{slot:"title"},[t._v("切换语言")]),e("el-menu-item",{attrs:{index:"2-1"}},[t._v("英语")]),e("el-menu-item",{attrs:{index:"2-2"}},[t._v("法语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("德语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("日语")])],2),e("el-menu-item",{attrs:{index:"0"},on:{click:t.re}},[t._v("rt-books")]),e("el-menu-item",{attrs:{index:"2"}},[t._v("玄幻")]),e("el-menu-item",{attrs:{index:"3"}},[t._v("都市")]),e("el-menu-item",{attrs:{index:"4"}},[t._v("仙侠")]),e("el-menu-item",{attrs:{index:"5"}},[t._v("历史")]),e("el-menu-item",{attrs:{index:"6"}},[t._v("悬疑")]),e("el-menu-item",{attrs:{index:"7"}},[t._v("推理")]),e("el-menu-item",{attrs:{index:"8"}},[t._v("言情")]),e("el-menu-item",{attrs:{index:"9"}},[t._v("更多")]),e("div",{staticClass:"search"},[e("el-input",{attrs:{placeholder:"请输入内容"},model:{value:t.input,callback:function(e){t.input=e},expression:"input"}}),e("el-button",{attrs:{type:"primary",plain:""}},[t._v("搜索")])],1)],1)],1)},r=[],n={name:"top",data(){return{input:""}},methods:{re(){this.$router.push("/")}}},a=n,o=s(1001),l=(0,o.Z)(a,i,r,!1,null,null,null),u=l.exports},6337:function(t,e,s){s.r(e),s.d(e,{default:function(){return m}});var i=function(){var t=this,e=t._self._c;return e("div",[e("top"),e("logincenter"),e("div",{staticClass:"bottoms"},[e("foot")],1)],1)},r=[],n=s(1380),a=s(7378),o=s(2749),l={components:{top:o.Z,foot:a.Z,logincenter:n.Z},data(){return{}},methods:{}},u=l,d=s(1001),c=(0,d.Z)(u,i,r,!1,null,"47febb1f",null),m=c.exports},3205:function(t,e,s){t.exports=s.p+"img/welcom.d466cbee.jpeg"}}]);
//# sourceMappingURL=950.a10e47f1.js.map