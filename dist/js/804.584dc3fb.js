"use strict";(self["webpackChunkrtbooks"]=self["webpackChunkrtbooks"]||[]).push([[804],{2389:function(t,e,s){s.d(e,{Z:function(){return d}});var n=function(){var t=this,e=t._self._c;return e("div",[e("el-menu",{staticClass:"el-menu",attrs:{mode:"horizontal"}},[e("el-submenu",{attrs:{index:"1"}},[e("template",{slot:"title"},[t._v("切换语言")]),e("el-menu-item",{attrs:{index:"2-1"}},[t._v("英语")]),e("el-menu-item",{attrs:{index:"2-2"}},[t._v("法语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("德语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("日语")])],2),e("el-menu-item",{attrs:{index:"0"},on:{click:t.re}},[t._v("rt-books")]),e("el-menu-item",{attrs:{index:"2"}},[t._v("玄幻")]),e("el-menu-item",{attrs:{index:"3"}},[t._v("都市")]),e("el-menu-item",{attrs:{index:"4"}},[t._v("仙侠")]),e("el-menu-item",{attrs:{index:"5"}},[t._v("历史")]),e("el-menu-item",{attrs:{index:"6"}},[t._v("悬疑")]),e("el-menu-item",{attrs:{index:"7"}},[t._v("推理")]),e("el-menu-item",{attrs:{index:"8"}},[t._v("言情")]),e("el-menu-item",{attrs:{index:"9"}},[t._v("更多")]),e("el-menu-item",{attrs:{index:"10"},on:{click:t.back}},[t._v("退出登录")])],1)],1)},a=[],r=(s(6265),s(8291)),i={name:"top",data(){return{input:""}},methods:{back(){const t="/api/author/logout";r.Z["delete"](t).then((t=>{alert(t.data.msg),200==t.data.code&&this.$router.push("/")}))},re(){this.$router.push("/author")}}},o=i,l=s(1001),u=(0,l.Z)(o,n,a,!1,null,null,null),d=u.exports},5370:function(t,e,s){s.r(e),s.d(e,{default:function(){return k}});var n=function(){var t=this,e=t._self._c;return e("div",[e("top"),e("center"),e("foot")],1)},a=[],r=s(7378),i=s(2389),o=function(){var t=this,e=t._self._c;return e("div",{staticClass:"center"},[t._m(0),e("div",{staticClass:"center2"},[e("h2",[t._v("修改作者密码")]),e("div",{staticClass:"el-icon-user"},[t._v(" 用户账号 :"),e("el-input",{attrs:{placeholder:"请输入你的用户名账号"},model:{value:t.id,callback:function(e){t.id=e},expression:"id"}})],1),e("div",{staticClass:"el-icon-key"},[t._v(" 密码 :"),e("el-input",{attrs:{placeholder:"请输入密码","show-password":""},model:{value:t.password,callback:function(e){t.password=e},expression:"password"}})],1),e("div",{staticClass:"el-icon-key"},[t._v(" 新密码 :"),e("el-input",{attrs:{placeholder:"请输入新的密码","show-password":""},model:{value:t.password2,callback:function(e){t.password2=e},expression:"password2"}})],1),e("el-button",{attrs:{type:"primary",plain:""},on:{click:t.check}},[t._v("立即修改")])],1)])},l=[function(){var t=this,e=t._self._c;return e("div",{staticClass:"center1"},[e("img",{attrs:{src:s(3205)}})])}],u=s(5410),d=s.n(u),c=s(8291),m={name:"checkpassword",data(){return{id:"",password:"",password2:""}},methods:{check(){var t={uid:this.id,password:this.password,new_password:this.password2};const e="/api/author/checkpassword";c.Z.post(e,d().stringify(t)).then((t=>{alert(t.data.msg),200==t.data.code&&this.$router.push("/")}))}}},p=m,v=s(1001),h=(0,v.Z)(p,o,l,!1,null,"ba19944a",null),_=h.exports,f={components:{top:i.Z,foot:r.Z,center:_},data(){return{ishow:!1}},methods:{}},w=f,x=(0,v.Z)(w,n,a,!1,null,"3f914528",null),k=x.exports},3205:function(t,e,s){t.exports=s.p+"img/welcom.d466cbee.jpeg"}}]);
//# sourceMappingURL=804.584dc3fb.js.map