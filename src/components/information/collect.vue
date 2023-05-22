<template>
  <div class="all">
    <div class="collect">我的收藏</div>
    <div v-for="book in books">
      <li v-for="item in book">{{ item }}</li>
      <el-button type="primary" plain @click="cancel(book[0])"
        >取消收藏</el-button
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      books: "",
    };
  },
  methods: {
    cancel(x) {
      axios
        .post("http://192.168.111.142:8080/api/user/del_collect/" + x)
        .then((res) => {
          alert(res.data.msg);
        }); //拿阅读记录
      axios
        .get("http://192.168.111.142:8080/api/user/get_collection")
        .then((res) => {
          this.books = res.data.collect_books;
          this.$forceUpdate();
        }); //拿阅读记录
    },
  },
  mounted() {
    axios
      .get("http://192.168.111.142:8080/api/user/get_collection")
      .then((res) => {
        this.books = res.data.collect_books;
      }); //拿阅读记录
  },
};
</script>

<style scoped>
li {
  width: 600px;
  margin-left: 400px;
  margin-bottom: 20px;
}
.collect {
  display: flex;
  justify-content: center;
}
.all {
}
button {
  margin-left: 500px;
}
</style>