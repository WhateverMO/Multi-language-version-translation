"use strict";(self["webpackChunkrtbooks"]=self["webpackChunkrtbooks"]||[]).push([[671],{3405:function(t,e,o){o.d(e,{Z:function(){return d}});var s=function(){var t=this,e=t._self._c;return e("div",[e("el-menu",{staticClass:"el-menu",attrs:{mode:"horizontal"}},[e("el-submenu",{attrs:{index:"1"}},[e("template",{slot:"title"},[t._v("切换语言")]),e("el-menu-item",{attrs:{index:"2-1"}},[t._v("英语")]),e("el-menu-item",{attrs:{index:"2-2"}},[t._v("法语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("德语")]),e("el-menu-item",{attrs:{index:"2-3"}},[t._v("日语")])],2),e("el-menu-item",{attrs:{index:"0"},on:{click:t.re}},[t._v("rt-books")]),e("el-menu-item",{attrs:{index:"2"}},[t._v("玄幻")]),e("el-menu-item",{attrs:{index:"3"}},[t._v("都市")]),e("el-menu-item",{attrs:{index:"4"}},[t._v("仙侠")]),e("el-menu-item",{attrs:{index:"5"}},[t._v("历史")]),e("el-menu-item",{attrs:{index:"6"}},[t._v("悬疑")]),e("el-menu-item",{attrs:{index:"7"}},[t._v("推理")]),e("el-menu-item",{attrs:{index:"8"}},[t._v("言情")]),e("el-menu-item",{attrs:{index:"9"}},[t._v("更多")]),e("el-menu-item",{attrs:{index:"10"},on:{click:t.back}},[t._v("退出登录")])],1)],1)},n=[],i=o(8291),a={name:"top",data(){return{input:""}},methods:{back(){const t="/api/user/logout";i.Z["delete"](t).then((t=>{alert(t.data.msg),200==t.data.code&&this.$router.push("/")}))},re(){this.$router.push("/reader")}}},r=a,l=o(1001),c=(0,l.Z)(r,s,n,!1,null,null,null),d=c.exports},3255:function(t,e,o){o.r(e),o.d(e,{default:function(){return x}});var s=function(){var t=this,e=t._self._c;return e("div",[e("top"),e("center"),e("foot")],1)},n=[],i=o(7378),a=function(){var t=this,e=t._self._c;return e("div",{attrs:{id:"c"}},[e("div",{staticClass:"content"},[e("div",{attrs:{id:"c1"}},[e("ul",[e("li",[t._v(t._s(t.title))])])]),e("div",{attrs:{id:"c2"}},[t._v(" "+t._s(t.content)+" ")])]),e("div",{staticClass:"zhan"}),e("div",{attrs:{id:"c3"}},[e("ul",[e("li",{staticClass:"change",on:{click:t.intro}},[t._v("目录")]),e("li",{staticClass:"change",on:{click:t.collect}},[t._v("收藏")]),e("li",{staticClass:"change"},[t._v("点赞")]),e("li",{staticClass:"change"},[t._v("分享")])])]),e("div",{attrs:{id:"c4"}},[e("ul",[e("li",{staticClass:"change",on:{click:t.head}},[t._v("上一章")]),e("li",{staticClass:"change",on:{click:t.back}},[t._v("下一章")])])])])},r=[],l=o(5410),c=o.n(l),d=o(8291),u=(o(1333),{data(){return{content:"",title:"",bookid:"",contentno:"1",bookno:"",maxbookno:""}},methods:{back(){sessionStorage.setItem("bookno",parseInt(this.bookno)+1),this.bookno=parseInt(this.bookno)+1;let t=new Date,e=t.getMonth()+1,o=t.getDate(),s=t.getHours(),n=t.getMinutes(),i=e+"月"+o+"日"+s+"时"+n+"分";var a={user_id:sessionStorage.getItem("id"),time:i};d.Z.post("/api/user/read_book/start_read/"+this.bookid+"/"+this.bookno,c().stringify(a)).then((t=>{4001!=t.data.code?(this.content=t.data.content_text,this.title=t.data.title):alert(t.data.msg)}))},head(){if(1!=this.bookno){sessionStorage.setItem("bookno",parseInt(this.bookno)-1),this.bookno=parseInt(this.bookno)-1;let e=new Date,o=e.getMonth()+1,s=e.getDate(),n=e.getHours(),i=e.getMinutes(),a=o+"月"+s+"日"+n+"时"+i+"分";var t={user_id:sessionStorage.getItem("id"),time:a};d.Z.post("/api/user/read_book/start_read/"+this.bookid+"/"+this.bookno,c().stringify(t)).then((t=>{this.content=t.data.content_text,this.title=t.data.title}))}else alert("当前是第一章节，前面没有内容了")},collect(){d.Z.post("http://localhost:5000/api/user/collect/"+this.$store.state.bookid).then((t=>{alert(t.data.msg)}))},intro(){this.$router.push("/introbook")}},mounted(){this.bookid=sessionStorage.getItem("bookid"),this.bookno=sessionStorage.getItem("bookno"),this.maxbookno=sessionStorage.getItem("maxbookno");let t=new Date,e=t.getMonth()+1,o=t.getDate(),s=t.getHours(),n=t.getMinutes(),i=e+"月"+o+"日"+s+"时"+n+"分";var a={user_id:sessionStorage.getItem("id"),time:i};d.Z.post("/api/user/read_book/start_read/"+this.bookid+"/"+this.bookno,c().stringify(a)).then((t=>{console.log(a),this.content=t.data.content_text,this.title=t.data.title}))}}),h=u,m=o(1001),k=(0,m.Z)(h,a,r,!1,null,"71c6bf30",null),_=k.exports,b=o(3405),g={components:{top:b.Z,center:_,foot:i.Z}},v=g,p=(0,m.Z)(v,s,n,!1,null,null,null),x=p.exports}}]);
//# sourceMappingURL=671.c1b2d7c1.js.map