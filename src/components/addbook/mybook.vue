<template>
  <div>
    <div class="btitle">我的作品</div>
    <el-table :data="books" style="width: 75%">
      <el-table-column prop="book_name" label="图书名称" width="150">
      </el-table-column>
      <el-table-column prop="book_class" label="图书类型" width="100">
      </el-table-column>
      <el-table-column prop="desc" label="图书简介" width="150">
      </el-table-column>
      <el-table-column prop="lang" label="图书语言" width="100">
      </el-table-column>
      <el-table-column prop="is_original" label="译作或原创" width="100">
      </el-table-column>
      <el-table-column prop="follower_count" label="章节名" width="320">
        <template slot-scope="scope1">
          <el-select v-model="scope1.row.selectedValue" placeholder="请选择">
            <el-option
              v-for="(item, index) in scope1.row.content_title"
              :key="index"
              :value="item"
            >
            </el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="150">
        <template slot-scope="scope">
          <el-button @click="addcontent(scope.row)" type="text" size="small"
            >新增章节</el-button
          >
          <el-button @click="checkcontent(scope.row)" type="text" size="small"
            >修改章节</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <div class="zhan"></div>
  </div>
</template>
  
  <script>
import request from "@/request";
import router from "@/router";
export default {
  data() {
    return {
      books: [{}],
      key: "",
    };
  },
  methods: {
    addcontent(row) {
      console.log("w s add ");
      if (row.flag == 0) {
        sessionStorage.removeItem("contentno");
        sessionStorage.removeItem("checkno");
        sessionStorage.setItem("newbookid", row.book_id);
        router.push("/write");
      } else {
        sessionStorage.setItem("transbook", row.original_book_id);
        sessionStorage.setItem("newstanslate", row.book_id);
        sessionStorage.setItem("langid", row.lang_id);
        sessionStorage.setItem("contentno", row.content_title.length + 1);
        router.push("/translation");
      }
    },
    checkcontent(row) {
      console.log("w s xg ");
      var index = row.content_title.indexOf(row.selectedValue);
      if (row.flag == 0) {
        sessionStorage.setItem("newbookid", row.book_id);
        sessionStorage.setItem("checkno", index + 1);
        router.push("/write");
      } else {
        sessionStorage.setItem("checkstransno", 1);
        sessionStorage.setItem("transbook", row.original_book_id);
        sessionStorage.setItem("newstanslate", row.book_id);
        sessionStorage.setItem("langid", row.lang_id);
        sessionStorage.setItem("contentno", index + 1);
        router.push("/translation");
      }
    },
  },
  mounted() {
    request.get("/api/author/get_my_books").then((res) => {
      console.log(res.data);
      this.books = res.data.books;
    });
  },
};
</script > 
  
  <style scoped>
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

.btitle {
  text-align: center;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  font-size: 25px;
  font-weight: 1000px;
  margin-bottom: 20px;
  margin-top: 40px;
}
.block {
  margin-top: 20px;
}
.button {
  border: none;
}
.el-table {
  margin-left: 20vw;
}
</style>