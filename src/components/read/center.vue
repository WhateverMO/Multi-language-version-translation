<template>
  <div class="bc">
    <div class="all">
      <div id="head">
        <div id="headl"><img src="@/assets/book/book_13.jpg" /></div>
        <div id="headr">
          <ul>
            <li>书名:《{{ bookname }}》</li>
            <li>作者:{{ bookauthor }}</li>
            <li class="intro">简介:{{ bookintro }}</li>
            <li>
              <el-button type="primary" plain @click="read">点击阅读</el-button>
              <el-button type="primary" plain>加入书架</el-button>
              <el-button type="primary" plain>投票互动</el-button>
            </li>
          </ul>
        </div>
      </div>

      <div class="center">
        <div href="#" class="title">目录</div>
        <div class="content">
          <li v-for="(item, index) in list" :key="index">
            {{ item }}
          </li>
        </div>
      </div>

      <div class="comment">
        <div class="title">粉丝互动</div>
        <el-table :data="tableData" border style="width: 80%">
          <el-table-column prop="user" label="用户" width="180">
          </el-table-column>
          <el-table-column prop="comment" label="评论"> </el-table-column>
        </el-table>
        <el-input
          type="textarea"
          :rows="2"
          placeholder="发表你的评论"
          v-model="textarea"
          class="sendtext"
        >
        </el-input>
        <el-button type="primary" plain class="send">点击发送</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  data() {
    return {
      tableData: [
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
      ],
      textarea: "",
      bookname: "",
      bookauthor: "",
      list: "[]",
      bookintro: "",
      bookid: "",
    };
  },
  methods: {
    read() {
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
      axios
        .post(
          "http://localhost:5000/api/user/read_book/start_read/" +
            this.bookid +
            "/" +
            1,
          qs.stringify(data)
        )
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("read", res.data);
          }, 1000);
          this.$router.push("/readbook");
        });
    },
  },
  mounted() {
    this.$bus.$on("introduce", (intro) => {
      this.bookauthor = intro.author_name;
      this.bookintro = intro.book_describe;
      this.bookname = intro.book_name;
      this.list = intro.content_list;
    });
    this.$bus.$on("bookid", (id) => {
      this.bookid = id;
      this.$store.commit("bookid", id);
    });
  },
};
</script>

<style scoped>
.bc {
  background: url(../../assets/img/5.jpg);
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
  width: 90vw;
  margin: 0 auto;
}
.all {
  margin: 0 auto;
  padding-top: 50px;
}
.intro {
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 6;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
}
img {
  width: 200px;
  height: 200px;
}
#head {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  margin-top: 40px;
}
#headl {
  width: 300px;
}
#headr {
  width: 500px;
}
#headr .el-button {
  width: 100px;
  height: 40px;
}
#head li {
  margin-top: 20px;
}
.title {
  letter-spacing: 20px;
  font-size: 25px;
  margin-bottom: 20px;
  margin-top: 20px;
  font-family: "Times New Roman", Times, serif;
  margin-left: 10px;
  text-shadow: #fc0 1px 0 10px;
}

.content li:nth-child(odd) {
  margin-left: 150px;
}

.content li {
  display: inline-flex;
  width: 400px;
  margin-bottom: 20px;
}
.comment {
  margin-bottom: 60px;
  opacity: 0.8;
}
.sendtext {
  margin-top: 20px;
  width: 600px;
  margin-left: 150px;
}
.send {
  height: 52px;
  margin-left: 5px;
}
.el-table {
  text-align: center;
  margin: 0 auto;
  font-size: 15px;
  letter-spacing: 2px;
}
</style>