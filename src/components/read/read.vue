<template>
  <div id="c">
    <div class="content">
      <div id="c1">
        <ul>
          <li>{{ title }}</li>
        </ul>
      </div>
      <div id="c2">
        {{ content }}
      </div>
    </div>
    <div class="zhan"></div>
    <div id="c3">
      <ul>
        <li class="change" @click="intro">目录</li>
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
import qs from "qs";
import request from "@/request";
import router from "@/router";
export default {
  data() {
    return {
      content: "",
      title: "",
      bookid: "",
      contentno: "1",
      bookno: "",
      maxbookno: "",
    };
  },
  methods: {
    back() {
      sessionStorage.setItem("bookno", parseInt(this.bookno) + 1);
      this.bookno = parseInt(this.bookno) + 1;
      let date = new Date();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      let h = date.getHours();
      let m = date.getMinutes();
      let time = month + "月" + day + "日" + h + "时" + m + "分";
      var data = {
        user_id: sessionStorage.getItem("id"),
        time: time,
      };
      request
        .post(
          "/api/user/read_book/start_read/" + this.bookid + "/" + this.bookno,
          qs.stringify(data)
        )
        .then((res) => {
          if (res.data.code != 4001) {
            this.content = res.data.content_text;
            this.title = res.data.title;
          } else {
            alert(res.data.msg);
          }
        });
    },
    head() {
      if (this.bookno != 1) {
        sessionStorage.setItem("bookno", parseInt(this.bookno) - 1);
        this.bookno = parseInt(this.bookno) - 1;
        let date = new Date();
        let month = date.getMonth() + 1;
        let day = date.getDate();
        let h = date.getHours();
        let m = date.getMinutes();
        let time = month + "月" + day + "日" + h + "时" + m + "分";
        var data = {
          user_id: sessionStorage.getItem("id"),
          time: time,
        };
        request
          .post(
            "/api/user/read_book/start_read/" + this.bookid + "/" + this.bookno,
            qs.stringify(data)
          )
          .then((res) => {
            this.content = res.data.content_text;
            this.title = res.data.title;
          });
      } else {
        alert("当前是第一章节，前面没有内容了");
      }
    },
    collect() {
      request
        .post(
          "http://localhost:5000/api/user/collect/" + this.$store.state.bookid
        )
        .then((res) => {
          alert(res.data.msg);
        });
    },
    intro() {
      this.$router.push("/introbook");
    },
  },
  mounted() {
    this.bookid = sessionStorage.getItem("bookid");
    this.bookno = sessionStorage.getItem("bookno");
    this.maxbookno = sessionStorage.getItem("maxbookno");
    let date = new Date();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    let h = date.getHours();
    let m = date.getMinutes();
    let time = month + "月" + day + "日" + h + "时" + m + "分";
    var data = {
      user_id: sessionStorage.getItem("id"),
      time: time,
    };
    request
      .post(
        "/api/user/read_book/start_read/" + this.bookid + "/" + this.bookno,
        qs.stringify(data)
      )
      .then((res) => {
        console.log(data);
        this.content = res.data.content_text;
        this.title = res.data.title;
      });
  },
};
</script>

<style scoped>
#c {
  /* background: url(../../assets/img/5.jpg); */
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
  width: 90vw;
  margin: 0 auto;
}
.content {
  width: 55vw;
  margin: 20px auto;
  border: 1px solid black;
  background-color: rgb(240, 230, 216);
  padding: 40px;
  font-family: "Courier New", Courier, monospace;
  font-size: 20px;
  letter-spacing: 5px;
}
.zhan {
  height: 50px;
}
#c1 {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 20px;
}
#c1 ul li {
  margin-bottom: 20px;
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