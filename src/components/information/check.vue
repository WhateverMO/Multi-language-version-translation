<template>
  <div class="all">
    <ul>
      <el-upload
        class="avatar-uploader"
        action="http://43.138.162.174/api/user/information/modification/update_avatar"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload"
      >
        <img v-if="imageUrl" :src="imageUrl" class="avatar" />
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
    </ul>

    <ul>
      <li>
        用户名：<el-input
          v-model="input"
          placeholder="请输入新的用户名"
        ></el-input>
      </li>
      <li>
        性别： <el-radio v-model="radio" label="男">男</el-radio>
        <el-radio v-model="radio" label="女">女</el-radio>
      </li>
      <li>
        年龄：<el-select v-model="old" ref="old" placeholder="请选择你的年龄">
          <el-option
            v-for="item in age"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li>
        地区：<el-select
          v-model="place"
          ref="place"
          placeholder="请选择你所在的地区"
        >
          <el-option
            v-for="item in area"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li>
        个人介绍:<el-input
          type="textarea"
          :rows="3"
          placeholder="请输入介绍内容"
          v-model="textarea"
        >
        </el-input>
      </li>
      <li><el-button type="primary" @click="checkinfo">点击修改</el-button></li>
    </ul>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
import store from "@/store";
export default {
  data() {
    return {
      age: [
        {
          value: "选项1",
          label: "18",
        },
        {
          value: "选项2",
          label: "19",
        },
        {
          value: "选项3",
          label: "20",
        },
        {
          value: "选项4",
          label: "21",
        },
        {
          value: "选项5",
          label: "22",
        },
      ],
      area: [
        {
          value: "选项1",
          label: "重庆",
        },
        {
          value: "选项2",
          label: "四川",
        },
        {
          value: "选项3",
          label: "云南",
        },
        {
          value: "选项4",
          label: "湖南",
        },
        {
          value: "选项5",
          label: "北京",
        },
      ],
      radio: store.state.sex,
      input: store.state.name,
      textarea: store.state.intro,
      old: store.state.age,
      place: store.state.place,
      imageUrl: store.state.image,
      formData: "",
    };
  },

  methods: {
    handleAvatarSuccess(res, files) {
      this.imageUrl = URL.createObjectURL(files.raw);
      var formData = new FormData();
      formData.append("file", files.raw, files.name);
      const path = "/api/user/information/modification/update_avatar";
      request.post(path, formData).then((res) => {
        if (res.data.code == 200) {
          alert(res.data.msg);
        }
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
    checkinfo() {
      var data = {
        username: this.input,
        gender: this.radio,
        area: this.$refs.place.selected.label,
        user_describe: this.textarea,
        user_age: this.$refs.old.selected.label,
      };
      const path = "/api/user/information/modification";
      request.post(path, qs.stringify(data)).then((res) => {
        console.log(res.data);
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$store.commit("name", res.data.username);
          this.$store.commit("sex", res.data.user_gender);
          this.$store.commit("place", res.data.user_area);
          this.$store.commit("intro", res.data.user_describe);
          this.$store.commit("age", res.data.user_age);
          this.$router.push("/readerinformation");
        }
      });
    },
  },
};
</script>

<style scoped>
.all {
  display: flex;
  justify-content: center;
}
ul {
  margin-top: 50px;
  margin-left: 50px;
}
ul li {
  margin-bottom: 30px;
}
.el-input {
  width: 250px;
}
.el-button {
  margin-left: 5vw;
}
.el-textarea {
  width: 250px;
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
</style>
