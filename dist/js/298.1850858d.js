"use strict";(self["webpackChunkrtbooks"]=self["webpackChunkrtbooks"]||[]).push([[298],{3405:function(e,t,s){s.d(t,{Z:function(){return u}});var n=function(){var e=this,t=e._self._c;return t("div",[t("el-menu",{staticClass:"el-menu",attrs:{mode:"horizontal"}},[t("el-submenu",{attrs:{index:"1"}},[t("template",{slot:"title"},[e._v("切换语言")]),t("el-menu-item",{attrs:{index:"2-1"}},[e._v("英语")]),t("el-menu-item",{attrs:{index:"2-2"}},[e._v("法语")]),t("el-menu-item",{attrs:{index:"2-3"}},[e._v("德语")]),t("el-menu-item",{attrs:{index:"2-3"}},[e._v("日语")])],2),t("el-menu-item",{attrs:{index:"0"},on:{click:e.re}},[e._v("rt-books")]),t("el-menu-item",{attrs:{index:"2"}},[e._v("玄幻")]),t("el-menu-item",{attrs:{index:"3"}},[e._v("都市")]),t("el-menu-item",{attrs:{index:"4"}},[e._v("仙侠")]),t("el-menu-item",{attrs:{index:"5"}},[e._v("历史")]),t("el-menu-item",{attrs:{index:"6"}},[e._v("悬疑")]),t("el-menu-item",{attrs:{index:"7"}},[e._v("推理")]),t("el-menu-item",{attrs:{index:"8"}},[e._v("言情")]),t("el-menu-item",{attrs:{index:"9"}},[e._v("更多")]),t("el-menu-item",{attrs:{index:"10"},on:{click:e.back}},[e._v("退出登录")])],1)],1)},r=[],a=s(8291),i={name:"top",data(){return{input:""}},methods:{back(){const e="/api/user/logout";a.Z["delete"](e).then((e=>{alert(e.data.msg),200==e.data.code&&this.$router.push("/")}))},re(){this.$router.push("/reader")}}},o=i,l=s(1001),d=(0,l.Z)(o,n,r,!1,null,null,null),u=d.exports},4555:function(e,t,s){s.r(t),s.d(t,{default:function(){return k}});var n=function(){var e=this,t=e._self._c;return t("div",[t("top"),t("center"),t("foot")],1)},r=[],a=s(7378),i=s(3405),o=function(){var e=this,t=e._self._c;return t("div",{staticClass:"center"},[e._m(0),t("div",{staticClass:"center2"},[t("h2",[e._v("修改读者密码")]),t("div",{staticClass:"el-icon-user"},[e._v(" 用户账号 :"),t("el-input",{attrs:{placeholder:"请输入你的用户名账号"},model:{value:e.id,callback:function(t){e.id=t},expression:"id"}})],1),t("div",{staticClass:"el-icon-key"},[e._v(" 密码 :"),t("el-input",{attrs:{placeholder:"请输入密码","show-password":""},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}})],1),t("div",{staticClass:"el-icon-key"},[e._v(" 新密码 :"),t("el-input",{attrs:{placeholder:"请输入新的密码","show-password":""},model:{value:e.password2,callback:function(t){e.password2=t},expression:"password2"}})],1),t("el-button",{attrs:{type:"primary",plain:""},on:{click:e.check}},[e._v("立即修改")])],1)])},l=[function(){var e=this,t=e._self._c;return t("div",{staticClass:"center1"},[t("img",{attrs:{src:s(3205)}})])}],d=s(5410),u=s.n(d),c=s(8291),m={name:"checkpassword",data(){return{id:"",password:"",password2:""}},methods:{check(){var e={uid:this.id,password:this.password,new_password:this.password2};const t="/api/user/checkpassword";c.Z.post(t,u().stringify(e)).then((e=>{alert(e.data.msg),200==e.data.code&&this.$router.push("/")}))}}},p=m,v=s(1001),h=(0,v.Z)(p,o,l,!1,null,"2b6cf387",null),_=h.exports,f={components:{top:i.Z,foot:a.Z,center:_},data(){return{ishow:!1}},methods:{}},w=f,x=(0,v.Z)(w,n,r,!1,null,"d8b3f3dc",null),k=x.exports},3205:function(e,t,s){e.exports=s.p+"img/welcom.d466cbee.jpeg"}}]);
//# sourceMappingURL=298.1850858d.js.map