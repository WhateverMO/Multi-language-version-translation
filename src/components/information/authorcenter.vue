<template>
  <div class="all">
    <div id="l">
      <img :src="$store.state.image" alt="" width="200px" height="200px" />
      <div class="intro">
        <span>我的粉丝</span><span @click="mybooks">我的作品</span
        ><span>我的关注</span>
      </div>
      <div class="num">
        <span>{{ this.follower_count }}</span
        ><span>{{ this.works_count }}</span
        ><span>0</span>
      </div>
    </div>
    <div id="c">
      <div>
        用户名:<span>{{ $store.state.name }}</span>
      </div>
      <div>
        账号:<span>{{ $store.state.id }}</span>
      </div>
      <div>
        性别:<span>{{ $store.state.sex }}</span>
      </div>
      <div>
        年龄:<span>{{ $store.state.age }}</span>
      </div>
      <div>
        地区:<span>{{ $store.state.place }}</span>
      </div>
      <div>
        个人介绍: <span>{{ $store.state.intro }}</span>
      </div>
      <el-button type="primary" @click="check">修改个人信息</el-button>
    </div>
  </div>
</template>

<script>
import request from "@/request";
export default {
  data() {
    return {
      works_count: 0,
      follower_count: 0,
    };
  },
  methods: {
    check() {
      this.$router.push("/checkinformationauthor");
    },
    mybooks() {
      this.$router.push("/authorbook");
    },
  },
  mounted() {
    request.get("/api/author/information").then((res) => {
      this.follower_count = res.data.follower_count;
      this.works_count = res.data.works_count;
      this.$store.commit("name", res.data.author_name);
      this.$store.commit("sex", res.data.author_gender);
      this.$store.commit("place", res.data.author_area);
      this.$store.commit("intro", res.data.author_describe);
      this.$store.commit("age", res.data.author_age);
      this.$store.commit("id", res.data.author_id);
      this.$store.commit("image", res.data.author_avatar);
    }); //给session发请求拿作者信息
  },
};
</script>

<style scoped>
.all {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  height: 45vh;
}
.kind span {
  margin-right: 10px;
}
#c {
  margin-left: 100px;
}
#c div {
  margin-bottom: 20px;
}
#c span {
  margin-left: 10px;
}
img {
  border-radius: 50%;
  object-fit: cover;
}
.intro {
  margin-top: 20px;
}
.num {
  margin-top: 10px;
}
.intro span {
  margin-right: 10px;
}

.intro :hover {
  cursor: pointer;
  color: red;
}
.num span {
  padding-left: 20px;
  padding-right: 50px;
}
.el-button {
  width: 200px;
}
</style>