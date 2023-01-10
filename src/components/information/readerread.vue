<template>
  <div>
    <h2>我的阅读记录</h2>
    <div class="c3">
      <div class="name">
        <div class="title">作品名称</div>
        <div v-for="book in books" class="read">
          {{ book[0] }}
        </div>
      </div>
      <div class="author">
        <div class="title">作者</div>
        <div v-for="book in books" class="read">
          {{ book[1] }}
        </div>
      </div>
      <!-- <div class="intro">
        <div class="title">简介</div>
        <div v-for="book in books" class="read">
          {{ book[2] }}
        </div>
      </div> -->
      <div class="no">
        <div class="title">阅读章节</div>
        <div v-for="book in books" class="read">
          {{ book[3] }}
        </div>
      </div>
      <div class="time">
        <div class="title">阅读时间</div>
        <div v-for="book in books" class="read">
          {{ book[4] }}
        </div>
      </div>
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
  methods: {},
  mounted() {
    axios.get("http://localhost:5000/api/user/read_history").then((res) => {
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
.name,
.author,
.no,
.intro,
.time {
  display: inline-block;
}
.read {
  width: 220px;
  height: 50px;
}
.c3 {
  margin-left: 300px;
}
</style>