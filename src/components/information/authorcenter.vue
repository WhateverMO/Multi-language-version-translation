<template>
  <div class="all">
    <div id="l">
      <img src="@/assets/img/headimg.jpg" alt="" width="200px" height="200px" />
      <div class="intro">
        <span>我的粉丝</span><span>我的作品</span><span>我的关注</span>
      </div>
      <div class="num"><span>0</span><span>0</span><span>0</span></div>
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
export default {
  data() {
    return {};
  },
  methods: {
    check() {
      this.$router.push("/checkinformationauthor");
    },
  },
};
</script>

<style scoped>
.all {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  height: 50vh;
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
.num span {
  padding-left: 20px;
  padding-right: 50px;
}
</style>