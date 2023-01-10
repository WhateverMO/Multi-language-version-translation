<template>
  <div>
    <div id="searchbook">
      <el-input
        v-model="input"
        placeholder="请输入你要翻译图书的名字"
      ></el-input>
      <el-button type="primary" plain>搜索</el-button>
    </div>
    <div id="translatebook">
      <div id="kind">
        <ul>
          <li><a href="#">玄幻</a></li>
          <li><a href="#">奇幻</a></li>
        </ul>
        <ul>
          <li><a href="#">武侠</a></li>
          <li><a href="#">仙侠</a></li>
        </ul>
        <ul>
          <li><a href="#">都市</a></li>
          <li><a href="#">现实</a></li>
        </ul>
        <ul>
          <li><a href="#">军事</a></li>
          <li><a href="#">历史</a></li>
        </ul>
        <ul>
          <li><a href="#">游戏</a></li>
          <li><a href="#">体育</a></li>
        </ul>
        <ul>
          <li><a href="#">科幻</a></li>
          <li><a href="#">悬疑</a></li>
        </ul>
      </div>
      <div id="book">
        <li>
          <img
            src="@/assets/book/book_7.jpg"
            height="300px"
            width="200px"
            alt=""
            @click="bookone"
          />
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_13.jpg"
              height="300px"
              width="200px"
              alt=""
              @click="booktwe"
          /></a>
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_8.jpg"
              height="300px"
              width="200px"
              alt=""
              @click="bookthree"
          /></a>
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_6.jpg"
              height="300px"
              width="200px"
              alt=""
              @click="bookfour"
          /></a>
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_4.jpg"
              height="300px"
              width="200px"
              alt=""
          /></a>
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_1.jpg"
              height="300px"
              width="200px"
              alt=""
          /></a>
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_2.jpg"
              height="300px"
              width="200px"
              alt=""
          /></a>
        </li>
        <li>
          <a href="#"
            ><img
              src="@/assets/book/book_10.jpg"
              height="300px"
              width="200px"
              alt=""
          /></a>
        </li>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      bookid: "",
    };
  },
  methods: {
    bookone() {
      axios
        .get("http://localhost:5000/api/author/translate_option/" + 6)
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("first", res.data);
            this.$store.commit("firstbookid", 6);
          }, 1000);
          this.$router.push("/compare");
        });
    },
    booktwe() {
      axios
        .get("http://localhost:5000/api/author/translate_option/" + 7)
        .then((res) => {
          console.log(res.data);
          setTimeout(() => {
            this.$bus.$emit("first", res.data);
            this.$store.commit("firstbookid", 7);
          }, 1000);
          this.$router.push("/compare");
        });
    },
    bookthree() {
      axios
        .get("http://localhost:5000/api/author/translate_option/" + 8)
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("first", res.data);
            this.$nextTick(function () {
              this.$store.commit("firstbookid", 8);
            });
          }, 1000);
          this.$router.push("/compare");
        });
    },
    bookfour() {
      axios
        .get("http://localhost:5000/api/author/translate_option/" + 9)
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("first", res.data);
            this.$store.commit("firstbookid", 9);
          }, 1000);
          this.$router.push("/compare");
        });
    },
  },
};
</script>

<style scoped>
#searchbook {
  margin-left: 40vw;
  margin-top: 5vh;
}
#kind ul {
  display: inline-block;
  margin-left: 10vw;
}
#kind ul li {
  margin-bottom: 10vh;
}
#kind {
  margin-right: 10vw;
  margin-left: 10vw;
  margin-top: 10vh;
}
#book {
  margin-left: 15vw;
}
#book li {
  margin-right: 10vh;
  margin-bottom: 10vh;
  display: inline-block;
}
img:hover {
  cursor: pointer;
}
</style>