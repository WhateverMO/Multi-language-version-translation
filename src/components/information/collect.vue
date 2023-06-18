<template>
  <div class="all">
    <div class="list">
      <ul class="title">
        我的收藏夹
      </ul>
      <ul
        v-for="(name, index) in collectname"
        :key="index"
        @click="collectbook(name)"
      >
        <li>
          {{ name }}
          <i class="el-icon-delete" @click="delecollectname(name)"></i>
        </li>
      </ul>
      <ul>
        <el-button type="text" @click="buider">创建收藏夹</el-button>
      </ul>
    </div>
    <div class="content">
      <ul class="title">
        我收藏的图书
      </ul>
      <ul
        v-for="(item, index) in this.collectbooks"
        :key="index"
        @click="collectbook(item.book_id)"
      >
        <li>
          {{ item.book_name }}___{{ item.desc }}
          <i class="el-icon-delete" @click="delecollectbook(item.book_id)"></i>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import request from "@/request";
import qs from "qs";
export default {
  data() {
    return {
      books: "",
      collectname: [],
      collectbooks: [],
    };
  },
  methods: {
    //创建图书收藏夹
    buider() {
      this.$prompt("请输入要创建的收藏夹名字", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          var data = {
            libname: value,
          };
          request
            .post("/api/user/create_collection", qs.stringify(data))
            .then((res) => {
              if (res.data.code == 200) {
                this.$message({
                  type: "success",
                  message: "收藏夹创建成功",
                });
                this.getnewcollect();
              }
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入",
          });
        });
    },
    //获取收藏夹图书内容
    collectbook(name) {
      request.get("/api/user/get_collection/" + name).then((res) => {
        if (res.data.code == 200) {
          sessionStorage.setItem("collectname", name);
          this.collectbooks = res.data.collection_book_list;
          console.log(this.collectbooks);
        }
      });
    },
    //删除收藏夹
    delecollectname(name) {
      request.delete("/api/user/dele_collection/" + name).then((res) => {
        console.log(res.data);
        if (res.data.code == 200) {
          alert("删除收藏夹成功");
          this.getnewcollect();
        }
      });
    },
    //获取所有收藏夹的名字
    getnewcollect() {
      request.get("/api/user/get_collection_lib").then((res) => {
        console.log(res.data);
        this.collectname = res.data.collections;
      }); //获取所有收藏夹名字
    },
    //删除收藏夹里的图书
    delecollectbook(id) {
      var collectname = sessionStorage.getItem("collectname");
      request
        .delete("/api/user/del_collect/" + id + "/" + collectname)
        .then((res) => {
          console.log(res.data);
          if (res.data.code == 200) {
            alert("删除收藏图书成功");
            this.collectbook(collectname);
          }
        });
    },
  },
  mounted() {
    request.get("/api/user/get_collection_lib").then((res) => {
      this.collectname = res.data.collections;
      request
        .get("/api/user/get_collection/" + res.data.collections[0])
        .then((res) => {
          this.collectbooks = res.data.collection_book_list;
        });
    }); //获取所有收藏夹名字
    console.log(this.collectname);
  },
};
</script>

<style scoped>
li {
  padding: 20px;
  font-family: "Times New Roman", Times, serif;
  font-size: 20px;
}
li:hover .el-icon-delete {
  display: inline-block;
}
li:hover {
  cursor: pointer;
  background-color: rgb(243, 240, 235);
  color: red;
}
.list {
  margin-left: 20vw;
  margin-top: 10vh;
  float: left;
}
.title {
  letter-spacing: 20px;
  font-size: 25px;
  margin-bottom: 20px;
  margin-top: 20px;
  font-family: "Times New Roman", Times, serif;
  margin-left: 20px;
  color: rgb(17, 155, 206);
}
.content {
  float: left;
  margin-left: 10vw;
  margin-top: 10vh;
}
.el-icon-delete {
  display: none;
}
</style>