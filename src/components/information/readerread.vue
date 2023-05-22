<template>
  <div>
    <div class="btitle">我的阅读记录</div>
    <table border="1" cellspacing="0">
      <tr class="title">
        <td class="name">作品名称</td>
        <td class="author">作者</td>
        <td class="intro">简介</td>
        <td class="no">阅读章节</td>
        <td class="time">阅读时间</td>
      </tr>
      <tr v-for="(items, i) in books" :key="i">
        <td v-for="(item, j) in items" :key="j">{{ item }}</td>
      </tr>
    </table>
    <div class="zhan"></div>
  </div>
</template>

<script>
import request from "@/request";
export default {
  data() {
    return {
      books: "",
    };
  },
  methods: {},
  mounted() {
    request.get("/api/user/read_history").then((res) => {
      this.books = res.data.books;
      console.log(res.data);
    }); //拿阅读记录
  },
};
</script > 

<style scoped>
h2 {
  text-align: center;
}
.read {
  width: 220px;
  height: 50px;
}
.c3 {
  margin-left: 300px;
}
.zhan {
  height: 100px;
}

table {
  width: 70vw;
  margin: 0 auto;
  color: #0e01019d;
  letter-spacing: 1px;
}
.intro {
  width: 550px;
}
.title {
  text-align: center;
}
td {
  padding: 5px;
}
.btitle {
  text-align: center;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  font-size: 25px;
  font-weight: 1000px;
  margin-bottom: 20px;
}
tr:hover {
  background-color: rgb(249, 246, 242);
}
</style>