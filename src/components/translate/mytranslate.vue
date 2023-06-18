<template>
  <div class="all">
    <ul class="first">
      <li id="name">{{ title }}</li>
      <li id="content">
        <textarea rows="30" cols="70" @mouseup="getSelectedText">{{
          content
        }}</textarea>
        <el-button type="primary" @click="pre">上一章</el-button>
        <el-button type="primary" @click="next">下一章</el-button>
        <el-button type="primary" @click="robot">机器翻译</el-button>
      </li>
    </ul>
    <ul class="translate">
      <li>
        章节名字：<el-input
          v-model="translatetitle"
          placeholder="请输入翻译后的章节名字"
        ></el-input>
      </li>
      <li id="content">
        <textarea rows="30" cols="70" v-model="translatecontent"></textarea>
      </li>
      <li id="button">
        <el-button type="primary" @click="hand">上传作品</el-button>
        <el-button type="primary">保存作品</el-button>
      </li>
    </ul>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
export default {
  data() {
    return {
      content: "",
      title: "",
      contentno: "",
      translatetitle: "",
      translatecontent: "",
      selectedText: "",
      langid: "",
    };
  },
  mounted() {
    this.transbook = sessionStorage.getItem("transbook");
    this.newstanslate = sessionStorage.getItem("newstanslate");
    this.contentno = sessionStorage.getItem("contentno");
    this.langid = sessionStorage.getItem("langid");
    request
      .get(
        "/api/author/translate/" +
          this.transbook +
          "/" +
          this.newstanslate +
          "/" +
          this.contentno
      )
      .then((res) => {
        this.content = res.data.content;
        this.title = res.data.title;
      }); //获取对照翻译的内容
    console.log(sessionStorage.getItem("checkstransno"));
    if (sessionStorage.getItem("checkstransno")) {
      request
        .get(
          "/api/author/get_my_books/" + this.newstanslate + "/" + this.contentno
        )
        .then((res) => {
          console.log(res.data);
          this.translatecontent = res.data.content_text;
          this.translatetitle = res.data.title;
        }); //获取自己写过的内容
    }
  },
  methods: {
    hand() {
      var data = {
        text: this.translatecontent,
        title: this.translatetitle,
        contentnum: this.contentno,
      };
      const path =
        "/api/author/translate/" +
        this.transbook +
        "/" +
        this.newstanslate +
        "/" +
        this.contentno;
      request.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        this.translatetitle = "";
        this.translatecontent = "";
        this.next();
      }); //post提交新翻译的内容
    },
    getSelectedText() {
      var selection = window.getSelection();
      var selectedText = selection.toString();
      this.selectedText = selectedText;
    },
    robot() {
      this.getSelectedText();
      var data = {
        text: this.selectedText,
      };
      console.log(this.selectedText);
      request
        .post("/api/author/ai_translate/" + this.langid, qs.stringify(data))
        .then((res) => {
          console.log(res.data);
          if (res.data.code == 200) {
            alert(res.data.msg);
            this.translatecontent += res.data.trans_text;
          }
        });
    },
    pre() {
      this.contentno = parseInt(this.contentno) - 1;
      const path =
        "/api/author/translate/" +
        this.transbook +
        "/" +
        this.newstanslate +
        "/" +
        this.contentno;
      request.get(path).then((res) => {
        this.content = res.data.content;
        this.title = res.data.title;
        sessionStorage.setItem("contentno", this.contentno);
      }); //post提交新翻译的内容
    },
    next() {
      this.contentno = parseInt(this.contentno) + 1;
      const path =
        "/api/author/translate/" +
        this.transbook +
        "/" +
        this.newstanslate +
        "/" +
        this.contentno;
      request.get(path).then((res) => {
        this.content = res.data.content;
        this.title = res.data.title;
        sessionStorage.setItem("contentno", this.contentno);
      }); //post提交新翻译的内容
    },
  },
};
</script>

<style scoped>
.all {
  display: flex;
  margin-top: 2vh;
}
textarea {
  background-color: transparent;
  padding: 20px;
  letter-spacing: 2px;
  font-size: 15px;
  width: 35vw;
}
#name {
  margin-left: 10vw;
  margin-bottom: 20px;
  font-size: 20px;
  margin-top: 10px;
}
.el-button {
  margin-top: 10px;
  margin-left: 80px;
  margin-bottom: 20px;
}
.first {
  margin-left: 10vw;
}
.translate {
  margin-right: 5vw;
}
.translate li {
  margin-bottom: 10px;
}
</style>