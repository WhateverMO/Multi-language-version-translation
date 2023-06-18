<template>
  <div>
    <div id="head" v-for="(item, index) in books" :key="index">
      <div id="headl"><img :src="item.cover_path" /></div>
      <div id="headr">
        <ul>
          <li>书名:《{{ item.book_name }}》</li>
          <li>作者:{{ item.author_name }}</li>
          <li class="intro">简介:{{ item.desc }}</li>
          <li>
            <el-button type="primary" plain @click="statread(item.book_id)"
              >点击阅读</el-button
            >
            <el-button type="primary" plain>关注作者</el-button>
            <el-button type="primary" @click="showdialog">加入书架</el-button>

            <el-dialog
              title="选择收藏夹"
              :visible.sync="dialogVisible"
              width="30%"
              :before-close="handleClose"
            >
              <span
                v-for="(item, index) in collect"
                :key="index"
                class="collects"
              >
                <el-radio v-model="radio" :label="item">{{
                  item
                }}</el-radio></span
              >

              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false"
                  >取 消 收 藏</el-button
                >
                <el-button type="primary" @click="collectbook"
                  >确 定 收 藏</el-button
                >
              </span>
            </el-dialog>
          </li>
        </ul>
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
      books: [{}],
      dialogVisible: false,
      collect: [],
      radio: "",
    };
  },
  methods: {
    statread(bookid) {
      sessionStorage.setItem("bookid", bookid);
      sessionStorage.setItem("bookno", 1);
      this.$router.push("/readbook");
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    showcollect() {
      request.get("/api/user/get_collection_lib").then((res) => {
        console.log(res.data);
        if (res.data.code == 200) {
          this.collect = res.data.collections;
        }
      });
    },
    showdialog() {
      this.dialogVisible = true;
      this.showcollect();
    },
    collectbook() {
      console.log(this.radio, typeof this.radio);
      this.dialogVisible = false;
      request
        .post("/api/user/collect/" + this.bookid + "/" + this.radio)
        .then((res) => {
          if (res.data.code == 200) {
            alert("收藏成功");
          } else {
            alert("已经在收藏夹了不要重复收藏哦");
          }
        });
    },
  },
  mounted() {
    var data = { book_name: sessionStorage.getItem("searchcontent") };
    request.post("/api/user/book/search", qs.stringify(data)).then((res) => {
      console.log(res.data);
      this.books = res.data.books;
    });
  },
  create() {},
};
</script>

<style>
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
  font-size: 15px;
}
#headl {
  width: 300px;
}
#headr {
  width: 500px;
  font-family: "Courier New", Courier, monospace;
  font-size: 15px;
}
#headr .el-button {
  width: 100px;
  height: 40px;
}
#head li {
  margin-top: 20px;
}
</style>