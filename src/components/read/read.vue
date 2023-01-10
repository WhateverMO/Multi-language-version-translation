<template>
  <div id="c">
    <div id="c1">
      <ul>
        <li>{{ title }}</li>
      </ul>
    </div>
    <div id="c2">
      {{ content }}
    </div>
    <div id="c3">
      <ul>
        <li class="change">目录</li>
        <li @click="collect" class="change">收藏</li>
        <li class="change">点赞</li>
        <li class="change">分享</li>
      </ul>
    </div>
    <div id="c4">
      <ul>
        <li @click="head" class="change">上一章</li>
        <li @click="back" class="change">下一章</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  data() {
    return {
      content: "",
      title: "",
      bookid: "",
      contentno: "1",
    };
  },
  methods: {
    back() {
      let date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      let h = date.getHours();
      let m = date.getMinutes();
      let s = date.getSeconds();
      let time =
        year +
        "年" +
        month +
        "月" +
        day +
        "日" +
        h +
        "时" +
        m +
        "分" +
        s +
        "秒";
      var data = {
        user_id: sessionStorage.getItem("id"),
        time: time,
      };
      this.contentno = this.contentno * 1 + 1;
      axios
        .post(
          "http://localhost:5000/api/user/read_book/start_read/" +
            this.$store.state.bookid +
            "/" +
            this.contentno,
          qs.stringify(data)
        )
        .then((res) => {
          this.content = res.data.content_text;
          this.title = res.data.title;
        });
    },
    head() {
      let date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      let h = date.getHours();
      let m = date.getMinutes();
      let s = date.getSeconds();
      let time =
        year +
        "年" +
        month +
        "月" +
        day +
        "日" +
        h +
        "时" +
        m +
        "分" +
        s +
        "秒";
      var data = {
        user_id: sessionStorage.getItem("id"),
        time: time,
      };
      this.contentno = this.contentno * 1 - 1;
      axios
        .post(
          "http://localhost:5000/api/user/read_book/start_read/" +
            this.$store.state.bookid +
            "/" +
            this.contentno,
          qs.stringify(data)
        )
        .then((res) => {
          this.content = res.data.content_text;
          this.title = res.data.title;
        });
    },
    collect() {
      axios
        .post("http://localhost:5000/api/user/collect/" + this.$store.state.bookid)
        .then((res) => {
          alert(res.data.msg);
        });
    },
  },
  mounted() {
    this.$bus.$on("read", (read) => {
      this.content = read.content_text;
      this.title = read.title;
    });
  },
};
</script>

<style scoped>
#c1 {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 20px;
}
#c1 ul li {
  margin-bottom: 20px;
  margin-left: 50px;
}
#c2 {
  width: 800px;
  margin-left: 20vw;
  height: 80vh;
}
#c3 {
  position: fixed;
  top: 50vh;
  left: 15vw;
}
#c3 ul li {
  margin-bottom: 20px;
}
#c4 {
  position: fixed;
  top: 50vh;
  right: 15vw;
}
#c4 ul li {
  margin-bottom: 20px;
}
.change {
  cursor: pointer;
}
.change:hover {
  color: red;
}
</style>