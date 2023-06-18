<template>
  <div>
    <div id="c3" v-if="show">
      <h2>我的作品</h2>
      <el-table :data="books" border style="width: 80%">
        <el-table-column prop="book_name" label="书名" width="180">
        </el-table-column>
        <el-table-column prop="desc" label="简介"> </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import request from "@/request";
export default {
  data() {
    return {
      books: [{}],
      show: false,
    };
  },
  methods: {},
  created() {
    request.get("/api/author/get_my_books").then((res) => {
      if (res.data.code == 200) {
        this.books = res.data.books;
        this.show = true;
      }
    });
  },
};
</script > 

<style scoped>
#c3 h2 {
  margin-left: 30vw;
  margin-bottom: 20px;
}

#c3 {
  margin-left: 45vh;
}
</style>