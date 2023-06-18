<template>
  <div class="all">
    <div>
      <el-drawer
        title="作家的话"
        :visible.sync="drawer"
        :direction="direction"
        :before-close="Close"
      >
        <textarea
          name=""
          id=""
          cols="60"
          rows="35"
          placeholder="在此输入正文内容"
        ></textarea>
        <el-button
          @click="drawer = true"
          type="primary"
          style="margin-left: 16px"
        >
          保存
        </el-button>
      </el-drawer>
    </div>

    <div class="center">
      <div>
        章节：<el-input
          v-model="contentno"
          placeholder="请输入章节号"
        ></el-input>
      </div>
      <div>
        名称：<el-input v-model="title" placeholder="请输入章节名"></el-input>
      </div>
      <div>
        <textarea
          name=""
          id=""
          cols="120"
          rows="30"
          v-model="content"
          placeholder="在此输入正文"
        ></textarea>
      </div>
      <div class="choose">
        <el-button
          @click="drawer = true"
          type="primary"
          style="margin-left: 16px"
        >
          添加作家的话
        </el-button>
        <el-button type="primary" style="margin-left: 16px"> 保存 </el-button>
        <el-button type="primary" style="margin-left: 16px" @click="hand">
          发布
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";

import request from "@/request";
export default {
  data() {
    return {
      drawer: false,
      direction: "rtl",
      isCollapse: true,
      title: "",
      content: "",
      contentno: "",
      newbookid: "",
      flag: false,
    };
  },
  methods: {
    Close(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    hand() {
      var data = {
        content: this.content,
        title: this.title,
      };
      if (!this.flag) {
        request
          .post(
            "/api/author/addbooks/" + this.newbookid + "/" + this.contentno,
            qs.stringify(data)
          )
          .then((res) => {
            alert(res.data.msg);
            this.content = "";
            this.title = "";
            this.contentno = "";
          });
      } else {
        request
          .post(
            "/api/author/edit_my_books/" +
              this.newbookid +
              "/" +
              this.contentno,
            qs.stringify(data)
          )
          .then((res) => {
            alert(res.data.msg);
            sessionStorage.removeItem("checkno");
            this.content = "";
            this.title = "";
            this.contentno = "";
          });
      }
    },
  },
  mounted() {
    this.newbookid = sessionStorage.getItem("newbookid");
    this.contentno = sessionStorage.getItem("checkno");
    if (this.checkno != 0) {
      this.flag = true;
      request
        .get(
          "/api/author/get_my_books/" + this.newbookid + "/" + this.contentno
        )
        .then((res) => {
          console.log(res.data);
          this.content = res.data.content_text;
          this.title = res.data.title;
        });
    }
  },
};
</script>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.all {
  margin: auto;
}
.el-button {
  width: 200px;
}
.center {
  margin-left: 25vw;
  height: 700px;
  margin-top: 20px;
}
.center div {
  margin-bottom: 10px;
}
</style>