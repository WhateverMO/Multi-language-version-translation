<template>
  <div v-if="this.flag">
    <div class="btitle">我的阅读记录</div>
    <table border="1" cellspacing="0">
      <tr class="title">
        <td class="name">作品名称</td>
        <td class="author">作者</td>
        <td class="intro">简介</td>
        <td class="no">阅读章节</td>
        <td class="time">阅读时间</td>
      </tr>
      <tr v-for="(items, i) in showbook" :key="i">
        <td v-for="(item, j) in items" :key="j">{{ item }}</td>
      </tr>
    </table>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentpage"
        :page-sizes="[5, 10]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="this.books.length"
      >
      </el-pagination>
    </div>
    <div class="zhan"></div>
  </div>
</template>

<script>
import request from "@/request";
export default {
  data() {
    return {
      books: [[]],
      flag: false,
      showbook: [[]],
      pagenum: 5,
      currentpage: 1,
    };
  },
  methods: {
    handleSizeChange(val) {
      this.pagenum = val;
      this.showbook = this.books.slice(0, val);
      this.currentpage = 1;
    },
    handleCurrentChange(val) {
      this.currentpage = val;
      var start = this.pagenum * (val - 1);
      var end = this.pagenum * val;
      console.log(start, end);
      if (end <= this.books.length) {
        this.showbook = this.books.slice(start, end);
      } else {
        this.showbook = this.books.slice(start, this.books.length);
        console.log(this.showbook);
      }
    },
  },
  mounted() {
    request.get("/api/user/read_history").then((res) => {
      console.log(res.data);
      if (this.books.length != 0) {
        this.flag = true;
        this.books = res.data.books;
        if (res.data.books.length >= 5) {
          this.showbook = res.data.books.slice(0, 5);
        } else {
          this.showbook = res.data.books;
        }
        console.log(this.showbook);
        console.log(this.books);
      }
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
.block {
  margin-left: 28vw;
  margin-top: 20px;
}
</style>