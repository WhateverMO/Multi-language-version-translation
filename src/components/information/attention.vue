<template>
  <div>
    <div class="btitle">我关注的作者</div>
    <el-table :data="authors" style="width: 55%">
      <el-table-column prop="author_name" label="名称" width="150">
      </el-table-column>
      <el-table-column prop="age" label="年龄" width="120"> </el-table-column>
      <el-table-column prop="gender" label="性别" width="120">
      </el-table-column>
      <el-table-column prop="works_count" label="作品数" width="120">
      </el-table-column>
      <el-table-column prop="follower_count" label="粉丝数" width="120">
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small"
            >取消关注</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <div class="zhan"></div>
  </div>
</template>
  
  <script>
import request from "@/request";
export default {
  data() {
    return {
      authors: [{}],
    };
  },
  methods: {
    handleClick(row) {
      console.log(row);
      request
        .get("/api/user/remove_follow_author/" + row.author_id)
        .then((res) => {
          alert(res.data.msg);
          request.get("/api/user/get_followed_author").then((res) => {
            console.log(res.data);
            this.authors = res.data.authors;
          });
        });
    },
  },
  mounted() {
    request.get("/api/user/get_followed_author").then((res) => {
      console.log(res.data);
      this.authors = res.data.authors;
    });
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
  text-align: center;
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
.button {
  border: none;
}
.el-table {
  margin-left: 20vw;
}
</style>