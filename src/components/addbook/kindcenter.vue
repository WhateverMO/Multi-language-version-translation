<template>
  <div class="box">
    <ul>
      <li>
        图书名字：<el-input
          v-model="bookname"
          placeholder="请输入图书名字"
        ></el-input>
      </li>
      <li>
        作品类型：<el-select
          v-model="bookclass"
          ref="bookclass"
          placeholder="请选择"
        >
          <el-option
            v-for="item in kind"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li>
        语言种类：<el-select
          v-model="booklang"
          ref="booklang"
          placeholder="请选择"
        >
          <el-option
            v-for="item in lang"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li>
        作品简介:
        <el-input
          type="textarea"
          :rows="4"
          :maxlength="40"
          placeholder="请输入内容"
          v-model="bookintro"
        >
        </el-input>
      </li>
      <li><el-button type="primary" @click="write">上传图书信息</el-button></li>
    </ul>
    <ul>
      <el-upload
        class="avatar-uploader"
        action="http://43.138.162.174/api/author/add_books_index"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload"
      >
        <img v-if="imageUrl" :src="imageUrl" class="avatar" />
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
      <li class="cover">
        <el-button type="primary">上传图书封面</el-button>
      </li>
    </ul>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
export default {
  data() {
    return {
      kind: [
        {
          value: "1",
          label: "小说",
        },
        {
          value: "2",
          label: "传记",
        },
        {
          value: "3",
          label: "历史",
        },
        {
          value: "4",
          label: "科幻",
        },
        {
          value: "5",
          label: "奇幻",
        },
        {
          value: "6",
          label: "悬疑",
        },
        {
          value: "7",
          label: "推理",
        },
        {
          value: "8",
          label: "恐怖",
        },
        {
          value: "9",
          label: "浪漫",
        },
        {
          value: "10",
          label: "青春",
        },
        {
          value: "11",
          label: "散文",
        },
        {
          value: "12",
          label: "哲学",
        },
      ],
      lang: [
        {
          value: "1",
          label: "中文",
        },
        {
          value: "2",
          label: "英语",
        },
        {
          value: "3",
          label: "西班牙语",
        },
        {
          value: "4",
          label: "法语",
        },
        {
          value: "5",
          label: "德语",
        },
        {
          value: "6",
          label: "意大利语",
        },
        {
          value: "7",
          label: "俄语",
        },
        {
          value: "8",
          label: "阿拉伯语",
        },
        {
          value: "9",
          label: "日语",
        },
        {
          value: "10",
          label: "韩语",
        },
        {
          value: "11",
          label: "葡萄牙语",
        },
      ],
      bookname: "",
      bookintro: "",
      bookclass: "",
      booklang: "",
      picture: new FormData(),
      imageUrl: "",
      newbookid: 0,
    };
  },
  methods: {
    write() {
      var data = {
        name: this.bookname,
        lang_id: this.$refs.booklang.selected.value,
        book_desc: this.bookintro,
        bc_id: this.$refs.bookclass.selected.value,
      };
      console.log(data);
      const path = "/api/author/add_books_index";
      request.post(path, qs.stringify(data)).then((res) => {
        if (res.data.code == 200) {
          alert("你的图书编号是" + res.data.book_id);
          this.newbookid = res.data.book_id;
          sessionStorage.setItem("newbookid", res.data.book_id);
        }
      });
    },
    handleAvatarSuccess(res, files) {
      this.imageUrl = URL.createObjectURL(files.raw);
      this.picture.append("file", files.raw, files.name);
      request
        .post("/api/author/add_books_cover/" + this.newbookid, this.picture)
        .then((res) => {
          alert(res.data.msg);
          this.$router.push("/write");
        });
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isJPG && isLt2M;
    },
  },
};
</script>

<style scoped>
.box {
  margin-left: 35vh;
  margin-top: 80px;
}
ul {
  margin-left: 100px;
  float: left;
}
ul li {
  margin-bottom: 30px;
}
.avatar-uploader {
  cursor: pointer;
  width: 278px;
  height: 278px;
  background-color: rgb(235, 252, 247);
  border: 1px dashed #7a7b7b;
}
.avatar-uploader:hover {
  border: 1px dashed #c93b28;
}
.avatar-uploader-icon {
  font-size: 48px;
  width: 278px;
  height: 278px;
  line-height: 278px;
  text-align: center;
}
.avatar {
  width: 278px;
  height: 278px;
  display: block;
}
.el-input {
  width: 150px;
}
.el-button {
  margin-left: 5vw;
  width: 200px;
}

.el-textarea {
  width: 250px;
}
.left {
  margin-bottom: 200px;
}
.cover {
  margin-top: 50px;
}
</style>
