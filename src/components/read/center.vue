<template>
  <div class="bc">
    <div id="head">
      <div id="headl"><img :src="this.cover" /></div>
      <div id="headr">
        <ul>
          <li>书名:《{{ bookname }}》</li>
          <li>作者:{{ bookauthor }}</li>
          <li class="intro">简介:{{ bookintro }}</li>
          <li>
            <el-button type="primary" plain @click="statread"
              >点击阅读</el-button
            >
            <el-button type="primary" plain @click="attentionauthor()"
              >关注作者</el-button
            >
            <el-button type="primary" plain @click="showdialog"
              >加入书架</el-button
            >

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

    <div class="center">
      <div href="#" class="title">目录</div>
      <div class="content">
        <li v-for="(item, index) in list" :key="index" @click="read(index + 1)">
          {{ item }}
        </li>
      </div>
    </div>

    <div class="comment">
      <div class="title">粉丝互动</div>
      <el-table :data="tableData" border style="width: 80%">
        <el-table-column prop="user_name" label="用户" width="180">
        </el-table-column>
        <el-table-column prop="barrage" label="评论"> </el-table-column>
        <el-table-column prop="time" label="时间"> </el-table-column>
      </el-table>
      <el-input
        type="text"
        :rows="2"
        placeholder="发表你的评论"
        v-model="textarea"
        class="sendtext"
      >
      </el-input>
      <el-button type="primary" plain class="send" @click="send"
        >点击发送</el-button
      >
    </div>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
export default {
  data() {
    return {
      tableData: [{}],
      textarea: "",
      bookname: "",
      bookauthor: "",
      list: "[]",
      bookintro: "",
      bookid: "",
      cover: "",
      dialogVisible: false,
      collect: [],
      radio: "",
      author_id: 0,
    };
  },
  methods: {
    statread() {
      sessionStorage.setItem("bookno", 1);
      this.$router.push("/readbook");
    },
    read(bookno) {
      sessionStorage.setItem("bookno", bookno);
      this.$router.push("/readbook");
    },
    send() {
      var data = {
        barrage: this.textarea,
      };
      var bookid = sessionStorage.getItem("bookid");
      request
        .post("/api/user/read_book/introduce/" + bookid, qs.stringify(data))
        .then((res) => {
          if (res.data.code == 200) {
            alert("发送成功");
            this.textarea = "";
            request
              .get("/api/user/read_book/introduce/" + bookid)
              .then((res) => {
                this.bookauthor = res.data.author_name;
                this.bookintro = res.data.book_describe;
                this.bookname = res.data.book_name;
                this.list = res.data.content_list;
                this.cover = res.data.cover_path;
                this.tableData = res.data.barrages;
              });
          } else {
            alert("请登录后再发送评论哦~");
          }
        });
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
    attentionauthor() {
      request.get("/api/user/follow_author/" + this.author_id).then((res) => {
        console.log(res.data);
        alert(res.data.msg);
      });
    },
  },

  mounted() {
    this.bookid = sessionStorage.getItem("bookid");
    request.get("/api/user/read_book/introduce/" + this.bookid).then((res) => {
      console.log(res.data);
      this.bookauthor = res.data.author_name;
      this.bookintro = res.data.book_describe;
      this.bookname = res.data.book_name;
      this.list = res.data.content_list;
      this.cover = res.data.cover_path;
      this.tableData = res.data.barrages;
      this.author_id = res.data.author_id;
    });
  },
};
</script>

<style scoped>
.bc {
  margin-left: 10vw;
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
.title {
  letter-spacing: 20px;
  font-size: 25px;
  margin-bottom: 20px;
  margin-top: 20px;
  font-family: "Times New Roman", Times, serif;
  margin-left: 20px;
  color: crimson;
}
.content :hover {
  color: #2cdfe2;
  cursor: pointer;
}
.content li:nth-child(odd) {
  margin-left: 150px;
}

.content li {
  display: inline-flex;
  width: 400px;
  margin-bottom: 20px;
  font-size: 18px;
  font-family: "Courier New", Courier, monospace;
}

.comment {
  opacity: 0.8;
}
.sendtext {
  margin-top: 25px;
  margin-left: 200px;
  width: 600px;
  margin-left: 150px;
  margin-bottom: 50px;
}
.send {
  height: 42px;
  margin-left: 5px;
}
.el-table {
  text-align: center;
  margin: 0 auto;
  font-size: 15px;
  letter-spacing: 2px;
}
.collects {
  display: flex;
  margin-bottom: 20px;
}
</style>